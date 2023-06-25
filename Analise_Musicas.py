import pandas as pd
import numpy as np
from textblob import TextBlob
import nltk
import streamlit as st

st.title("Análise de Sentimento de Músicas")

nltk.download('punkt')

def resolve_everything_for_carlos(text):
  word_list = TextBlob(text).words
  values = [TextBlob(word).polarity for word in word_list]
  pol = sum(values)/len(values)
  if pol >= 0.2:
    return "Positivo"
  elif (pol > -0.2 and pol < 0.2):
    return "Neutro"
  else:
    return "Negativo"

texto = st.text_input("Digite sua Música em ingles:")
if st.button("Analisar Sentimento"):
    sentimento = resolve_everything_for_carlos(texto)
    st.write(f"Texto: {texto}")
    st.write(f"Sentimento: {sentimento}")