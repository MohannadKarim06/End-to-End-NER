import spacy

model_path = "model\spacy_model1"

NER_model = spacy.load(model_path)


def predict_entities(text):
    
    doc = NER_model(text)  
    
    entities = [
        {"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_}
        for ent in doc.ents
    ]
    return {"entities": entities}



