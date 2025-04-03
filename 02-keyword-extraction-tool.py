import spacy

nlp=spacy.load("en-core-web-md")
text="Apple Inc. plans to open a new store in Paris next year. The store will sell iPhones and MacBooks."
doc=nlp(text)
keywords=[token.text for token in doc if token.pos_ in ["NOUN","PROPN"]]
print("Keywords (without duplicates):",set(keywords))
