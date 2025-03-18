from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from llama import tokenizer
from llama import model


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)

def store_in_faiss(textes):
    vecteurs = embedding_model.encode(textes)
    index.add(np.array(vecteurs, dtype=np.float32))
    return index

documents = ["L'IA révolutionne le monde.", "Le machine learning est puissant.", "Llama 3.2 améliore la génération de texte."]

docstore = {str(i): doc for i, doc in enumerate(documents)}

vectorstore = FAISS(embedding_function=embedding_model.encode, index=index, docstore=docstore, index_to_docstore_id=str)

retriever = vectorstore.as_retriever()

def ask_ai(query):
    retrieved_docs = retriever.get_relevant_documents(query)
    context = " ".join([doc for doc in retrieved_docs])

    prompt = f"Contexte : {context}\nQuestion : {query}\nRéponse :"

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=150)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response

question = "Cest quoi l'IA ?" #Poser les questions ici.
response = ask_ai(question)
print(response)
