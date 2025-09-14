#!/usr/bin/env python3
from langchain_community.document_loaders import WebBaseLoader
import time, bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
import os

import ast

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100, chunk_overlap=50
)

embeddings = OllamaEmbeddings(model='mxbai-embed-large:latest')
vectorstore = ElasticsearchStore(
    embedding = embeddings,
    index_name="charlotte",
    es_url="http://localhost:9200",
    es_user="elastic",
    es_password="UKUFJRKz+rdmXZA_oEd-"
)

retriever = vectorstore.as_retriever()

def retrieve(query: str):
    """Retrieve information related to a query."""
    try:
        retrieved_docs = vectorstore.similarity_search(query, k=2)
        serialized = "\n\n".join(
        (f"Source: {doc.metadata}\n" f"Content: {doc.page_content}")
            for doc in retrieved_docs
        )
        return serialized, retrieved_docs
    except Exception as e:
        return "Exception: "+str(e)
        
def addToRag(content:str, metadata:dict):
    """
    Lets you store content to your vector store.
    You can add personal notes, info from web searches, or whatever else.
    Please remember to tag the source it came from in the metadata 
    as well as additional information that may be helpful to you later.
    args:
        -content: string with content to store
        -metadata: dictionary with 
         examples: 
         "{'source': 'news', 'url': 'https://jacobin.com/', 'type':'reference'}"
         "{'source': 'user input', 'type': 'memory'}"
    """
    try:
        document_to_store = Document(
            page_content=str(content),
            metadata=metadata,
        )

        doc_splits = text_splitter.split_documents([document_to_store])
    
        vectorstore.add_documents(documents=document_to_store, embedding = embeddings)
        return "Content added."
    except Exception as e:
        return "Exception: "+str(e)+"."
