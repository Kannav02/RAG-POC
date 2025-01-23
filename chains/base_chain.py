from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_vertexai import ChatVertexAI
from typing import Union,Optional

# still have to work on the types for the same, maybe i will use postgres for schema rather than using FAISS, but lets see

class BaseChain:

    def __init__(self,model:Optional[Union[ChatGoogleGenerativeAI,ChatVertexAI]] = None,prompt_template:Optional[str]=None,vector_db=None):
        self.model = model
        if prompt_template:
            self.prompt_template = ChatPromptTemplate.from_template(prompt_template)

        self.vector_db = vector_db
        self.llm_chain = None
    
    def create_chain(self):
        self.llm_chainchain = self.prompt_template | self.model | StrOutputParser()
    
    def get_llm_chain(self):
        if self.llm_chain is None:
            self.create_chain()
        return self.llm_chain()
     