import numpy as np
import pandas as pd
import joblib
from transformers import pipeline
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
import torch

def create_classifier():
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    return classifier

def evaluate_text(model, text, labels):
    results = model(text, labels, multi_label=True)
    return results

model = joblib.load('zeroz-shot-bart.pk1')

text = ["The fire west of yellowstone has grown to be 50 square acres"]
labels = ["grateful", "political", "frustration", "sarcasm", "solution-focused", "informative or news-focused","fearful or panicked","blaming","seeking help or advice","fire-management-related"]

results = evaluate_text(model, text, labels)
print(results)