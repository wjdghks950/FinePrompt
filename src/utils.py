import re
import random
import os
import json


def save_file(outputs, path):
    if not os.path.exists(path):
        with open(path, "w") as writer_obj:
            json.dump(outputs)
            writer_obj.close()
    else:
        with open(path, "r") as reader_obj:
            outputs = json.load(reader_obj)

    return outputs

# TODO: This file contains a bunch of functions related to the extraction of attributes from DROP and MuSiQue

def extract_numbers_from_text(text):
    pass

# TODO: This file also contains the evaluation scripts for both DROP and MuSiQue

def drop_evaluation(preds, gold):
    pass
    return em, f1

def musique_evaluation(preds, gold):
    pass
    return em, ans_f1, sup_f1


