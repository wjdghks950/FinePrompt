import os
import argparse
import openai
import json

from prompts import BASE_PROMPT_DICT
from utils import *
from tqdm import tqdm

# OpenAI query module
openai.api_key = "<YOUR OPENAI API KEY>"  # "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"

model = "gpt-4-1106-preview"

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

def generate_response(system_prompt, user_prompt, model, temp=0.0):
    # TODO: Construct few-shot samples here
    response, raw_response = openai_gpt_call(system_prompt, user_prompt, model, temp)
    return response, raw_response


if __name__ == "__main__":
    # TODO: Set up argparse here

    # TODO: Run the generate_response: (i) per task and (ii) per infusion type
    pass