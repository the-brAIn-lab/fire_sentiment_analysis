import joblib
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def pkl_model():

    model.save_pretrained("zero-shot-bart")
    tokenizer.save_pretrained("zero-shot-bart")

    model_name = "facebook/bart-large-mnli"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    pickle_model = joblib.dump(model, "zeroz-shot-bart.pk1")
    return model

pkl_model()

