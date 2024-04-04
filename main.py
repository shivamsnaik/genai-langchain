
import os
from constants import gemini_api_key

# Langchain imports
from langchain_core.prompts import PromptTemplate 
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.schema import StrOutputParser
from langchain.schema.prompt_template import format_document

## Integrate our code GEMINI API
from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory

# Get the API keys and init gemini pro model
os.environ["GOOGLE_API_KEY"] = gemini_api_key    
llm = ChatGoogleGenerativeAI(model="gemini-pro", 
          safety_settings = {
              HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
              HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
              HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
          }
      )

results = llm.invoke("Hi")
print(results)
