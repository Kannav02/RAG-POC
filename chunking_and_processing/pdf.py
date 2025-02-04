import os
import json
# the idea here is, all the documents to be fed into the RAG would be of the type `Document` and the PyPDFLoader is one that is used to load PDF files, so we use all of these things
# RecursiveCharacterTextSplitter is again used chunking the text
from langchain.docstore.document import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


chunk_size:int = 4000
chunk_overlap:int = 400

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    length_function=len,
    is_separator_regex=False,
)

# Can still be customised to contain information about different meta_data like maybe even source or the url
def process_pdf(file_path:str) -> list[Document]:
    """
    Function to Process a PDF Document, and convert it to a document that can be used by a Vector DB or for langchain operations

    Args:
        - file_path:str -> the destination of the file that has to be converted which is either relative or absolute path
    
    Returns:
    A List Of Documents
    """
    loader = PyPDFLoader(file_path=file_path)
    document_pages = loader.load_and_split(text_splitter=text_splitter)
    return document_pages




