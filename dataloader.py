import os
import sys

from langchain.document_loaders import PyPDFLoader

#sys.path.append('../..') #define the File path
MODEL = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Access the API keys
 
TOGETHER_API_KEY=os.getenv("TOGETHER_API_KEY")
TOGETHER_API_SERVICE_URL = os.getenv("TOGETHER_API_SERVICE_URL")



loader = PyPDFLoader("docs/Shohel_Mahmud_Resume.pdf")
pages = loader.load()
print(len(pages))

page = pages[0]
#print(page)
#print(page.metadata)

#Load document from other datasources
""" from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader


from langchain_community.document_loaders import WebBaseLoader """

#loader = WebBaseLoader(
    #web_path = "https://www.espn.com/"
    # header_template = None,
    # verify_ssl = True,
    # proxies = None,
    # continue_on_failure = False,
    # autoset_encoding = True,
    # encoding = None,
    # web_paths = (),
    # requests_per_second = 2,
    # default_parser = "html.parser",
    # requests_kwargs = None,
    # raise_for_status = False,
    # bs_get_text_kwargs = None,
    # bs_kwargs = None,
    # session = None,
    # show_progress = True,
    # trust_env = False,
#clea)
#Lazy load
# from bs4 import BeautifulSoup
# docs = []
# for doc in loader.lazy_load():
#     docs.append(doc)
# print(docs[0].page_content[:100])
# print(docs[0].metadata)

#Async Loader
# docs = []
# async for doc in loader.alazy_load():
#     docs.append(doc)
# print(docs[0].page_content[:100])
# print(docs[0].metadata)


#Document Splitting into chunks

""" from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # chunk size (characters)
    chunk_overlap=200,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
) """
#all_splits = text_splitter.split_documents(pages)

""" print(f"Split blog post into {len(all_splits)} sub-documents.")
for splittext in all_splits:
    print(splittext) """

text1 = "hello I am software developer. How can I assist you today" 

from langchain_text_splitters import TokenTextSplitter

text_splitter = TokenTextSplitter(chunk_size=10, chunk_overlap=0)

texts = text_splitter.split_text(text1)
print(texts)

