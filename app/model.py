import pickle
import spacy

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

model_path = r"model\spacy_model1"

NER_model = spacy.load(model_path)

nlp = spacy.load("en_core_web_sm")


def smart_capitalize(text):
    doc = nlp(text)  
    modified_tokens = []

    for token in doc:
        if token.pos_ in ["VERB", "AUX", "DET", "ADP", "CCONJ", "PRON", "SCONJ", "ADJ", "ADV"]:  
            modified_tokens.append(token.text.lower())  
        else:
            modified_tokens.append(token.text.capitalize())
    return " ".join(modified_tokens)


def predict_entities(text):
    """Predicts named entities while filtering out unwanted labels."""

    text = smart_capitalize(text)  
    doc = NER_model(text)  


    allowed_labels = {"PERSON", "ORG", "GPE", "DATE", "EVENT", "LOC", "PER", "MISC"}  # Exclude MISC and other unwanted labels

    entities = [
        {"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_}
        for ent in doc.ents if ent.label_ in allowed_labels
    ]

    return {"entities": entities}

text = "peter is dumb"

predict = predict_entities(text)

print(predict)



