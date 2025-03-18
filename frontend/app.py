import streamlit as st
import requests

st.title("🧠 IA Multi-Agent - Génération d’articles")

query = st.text_input("Entrez votre requête")
if st.button("Lancer l'analyse"):
    response = requests.get(f"http://localhost:8080/query/?query={query}")
    st.write(response.json()["response"])