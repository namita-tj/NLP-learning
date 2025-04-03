import spacy
from PyPDF2 import PdfReader
import argparse

def keyword_extractor():
  article=input("Enter path to the article : ").strip()
  nlp=spacy.load("en_core_web_md")
  try:
    reader=PdfReader(article)
    text=" ".join([page.extract_text() for page in reader.pages])
  except FileNotFoundError:
    print(f"File not found: {article}")
    return
  doc=nlp(text)
  keywords=[token.text for token in doc if token.pos_ in ["NOUN","PROPN"]]
  print("Keywords (without duplicates):",set(keywords))

if __name__=="__main__":
  keyword_extractor()
