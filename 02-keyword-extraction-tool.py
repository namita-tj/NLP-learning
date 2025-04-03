import spacy
from PyPDF2 import PDFReader
from wordcloud import WordCloud
import argparse

def keyword_extractor(article):
  nlp=spacy.load("en-core-web-md")
  reader=PDFReader(article)
  text=" ".join([page.extract_text() for page in reader.pages])
  doc=nlp(text)
  keywords=[token.text for token in doc if token.pos_ in ["NOUN","PROPN"]]
  print("Keywords (without duplicates):",set(keywords))

if __name__=="__main__":
  parser=argparse.ArgumentParser("Extract keywords from a PDF:")
  parser.add_argument("--pdf",type=str,required=True)
  args=parser.parse_args()
  keyword_extractor(args.pdf)
