import os
import argparse
import openai
import json

from prompts import BASE_PROMPT_DICT, construct_few_shot
from utils import *
from tqdm import tqdm

# OpenAI query module
openai.api_key = "<YOUR OPENAI API KEY>"  # "sk-xxxx"

def openai_gpt_call(system_prompt, user_prompt, model, temp=0.0):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = openai.ChatCompletion.create(
        model=model, 
        messages=messages
    )
    return response, response['choices'][0]['message']['content']

def preprocess_gpt_output(response, start_str="Answer:"):
    answer_start_idx = response.find(start_str) + len(start_str) if response.find(start_str) != -1 else 0
    prepro_response = response[answer_start_idx:]
    return prepro_response 

def generate_response(args, system_prompt, user_prompt, model, temp=0.0):

    response, raw_response = openai_gpt_call(system_prompt, user_prompt, model, temp)
    return response, raw_response


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--bias_type', type=str, default="genbert", help="[cot, selfask, genbert, numnet, decomprc, quark, sae, qdgat]")
    parser.add_argument('--dataset', type=str, default="drop", help="[drop, musique]")

    parser.add_argument('--output_dir', type=str, default="outputs", help="Path to outputs")
    parser.add_argument('--data_dir', type=str, default="data", help="Path to dataset and in-context sample data")
    parser.add_argument('--do_fewshot', action='store_true', help="Activate few-shot in-context learning for each prompt type")

    parser.add_argument('--model', type=str, default='gpt-4-1106-preview')
    parser.add_argument('--temp', type=float, default=0.0, help="model temperature")

    args = parser.parse_args()

    model = args.model
    temp = args.temp

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    # Load dataset
    data_path = os.path.join(args.data_dir, args.dataset)
    if os.path.exists(data_path):
        with open(data_path, "r") as reader_obj:
            dataset = json.load(reader_obj)
            reader_obj.close()

    # Load the in-context few-shot samples
    icl_sample_path = os.path.join(args.data_dir, args.dataset, "icl_samples")
    if os.path.exists(icl_sample_path):
        with open(icl_sample_path, "r") as reader_obj:
            icl_samples = json.load(reader_obj)
            reader_obj.close()
    
    # Run the generate_response: (i) per task and (ii) per infusion type
    system_prompt = BASE_PROMPT_DICT[f"base_{args.dataset}_base"] if args.bias_type[:4] == "base" else BASE_PROMPT_DICT[f"{args.bias_type}_prompt_base"]
    
    if args.do_fewshot:
        icl_sample_path = os.path.join(args.data_dir, args.dataset, "icl_samples")
        if os.path.exists(icl_sample_path):
            with open(icl_sample_path, "r") as reader_obj:
                icl_samples = json.load(reader_obj)
                icl_samples_prompt = construct_few_shot(icl_samples, args.bias_type, k=3)  # TODO: Construct few-shot samples here
                reader_obj.close()
    else:
        icl_samples_prompt = None
    
    for idx, data in enumerate(tqdm(dataset), desc=f"Evaluating FinePrompt on {args.dataset} for {args.bias_type}"):
        user_prompt = "Document:" + dataset["context"] + "Question:" + dataset["question"]
        response, raw_response = generate_response(system_prompt, user_prompt, model=model)
