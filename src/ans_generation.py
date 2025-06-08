from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.models import load_chat_model
import os

def generate_answer(transcript: str, query: str) -> str:
    try:
        prompt_temp=PromptTemplate(
            input_variables=['context', 'question'],
            template=open(os.path.join('prompts', 'template.txt')).read()
        )
        chain=prompt_temp|load_chat_model()|StrOutputParser()
        answer=chain.invoke({'context': transcript, 'question': query})
        return answer
    except Exception as e:
        return f"An error occurred while generating the answer: {str(e)}"