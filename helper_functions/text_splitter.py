from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import re

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

def label_section(text):
    if re.search(r'\b(eligibility|eligible|who can apply)\b', text, re.I):
        return "eligibility"
    elif re.search(r'\b(application|how to apply|steps)\b', text, re.I):
        return "application"
    elif re.search(r'\b(overview|introduction|objective|grant description)\b', text, re.I):
        return "description"
    else:
        return "general"