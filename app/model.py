import pickle
import spacy

model_path = r"C:\\dell\\End-to-End-NER\\model\\spacy_model1"

NER_model = spacy.load(model_path)

nlp = spacy.load("en_core_web_sm")

def smart_capitalize(text):
    """ Capitalizes only detected named entities to match the training format. """
    doc = nlp(text)  
    modified_tokens = []

    for token in doc:
        if token.pos_ in ["VERB", "AUX", "DET", "ADP", "CCONJ", "PRON", "SCONJ"]:  
            modified_tokens.append(token.text.lower())  
        else:
            modified_tokens.append(token.text.capitalize())
    return " ".join(modified_tokens)


def predict_entities(text):

    text = smart_capitalize(text)
    
    doc = NER_model(text)  
    
    entities = [
        {"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_}
        for ent in doc.ents
    ]
    return {"entities": entities}


