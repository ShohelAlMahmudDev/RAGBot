import os
import sys

from langchain.document_loaders import PyPDFLoader

loaders = [
PyPDFLoader("docs/Shohel_Mahmud_Resume.pdf"),
PyPDFLoader("docs/Elabs.HR.Zeugnis.ShohelAlMahmud.EN.pdf"),
PyPDFLoader("docs/Elabs.HR.Zeugnis.ShohelAlMahmud.EN.pdf"),
PyPDFLoader("docs/Job Experience Certificates.pdf")
]

docs = []
for loader in loaders:   
    docs.extend(loader.load())

#print(len(pages))

#page = pages[0]
#print(page)
#print(page.metadata)


from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # chunk size (characters)
    chunk_overlap=100,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
)

splitted_text = text_splitter.split_documents(docs)
print(len(splitted_text))

from langchain.embeddings.
vectordb = Chroma.from_documents(
    documents=splits,
    embedding = embedding,
    persist_directory=persist_directory
)
