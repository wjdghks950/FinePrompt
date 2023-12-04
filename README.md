# FinePrompt: Unveiling the Role of Finetuned Inductive Bias on Compositional Reasoning in GPT-4
This repository contains the codes for the EMNLP 2023 Findings paper, [FinePrompt](https://openreview.net/forum?id=nmSvzxwfRZ&referrer=%5Bthe%20profile%20of%20Jeonghwan%20Kim%5D(%2Fprofile%3Fid%3D~Jeonghwan_Kim2)).
Our work deals with the idea of transferring task-specific inductive biases from finetuned models to prompts, as a way of improving GPT-4’s compositional reasoning capabilities.

## Setting Up the Environment
Since this work only deals with the effective prompting on GPT-4, our work requires the installation of the `openai` API.
```shell
pip install openai
```

## Evaluation using FinePrompt
```shell
python main.py --bias_type <bias_type_name> --dataset <dataset_name>
```
where `--bias_type` can be one of [`genbert`, `numnet`, `decomprc`, `quark`, `sae`, `qdgat`] and `--dataset` can be one of [`drop`, `musique`]

## Prompts
The set of base and in-context prompts are provided in the `prompts.py`.
