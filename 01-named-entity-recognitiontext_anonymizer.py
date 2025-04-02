import spacy
import argparse

def anonymize_text(text, model="en_core_web_lg"):
    nlp = spacy.load(model)
    doc = nlp(text)
    
    replacements = {
        "PERSON": "[REDACTED NAME]",
        "ORG": "[REDACTED ORGANIZATION]",
        "GPE": "[REDACTED LOCATION]",
        "DATE": "[REDACTED DATE]",
        "EMAIL": "[REDACTED EMAIL]",
        "PHONE": "[REDACTED PHONE]"
    }
    
    anonymized_tokens = []
    for token in doc:
        for ent in doc.ents:
            if token.idx >= ent.start_char and token.idx < ent.end_char:
                replacement = replacements.get(ent.label_, f"[REDACTED {ent.label_}]")
                if token.i == ent.start:
                    anonymized_tokens.append(replacement)
                break
        else:
            anonymized_tokens.append(token.text)
    
    return " ".join(anonymized_tokens).replace(" .", ".").replace(" ,", ",")

def main():
    parser = argparse.ArgumentParser(description="Anonymize text using spaCy NER")
    parser.add_argument("input", help="Input text to anonymize")
    parser.add_argument("--model", default="en_core_web_lg", help="spaCy model to use")
    args = parser.parse_args()
    
    anonymized = anonymize_text(args.input, args.model)
    print("Anonymized text:")
    print(anonymized)

if __name__ == "__main__":
    main()
