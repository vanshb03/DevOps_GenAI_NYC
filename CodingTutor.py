
import langchain
import openai
import tiktoken

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI



########
#Chunk up the RAG TD Chat GPT text file into 2500 character chunks
enc = tiktoken.get_encoding("cl100k_base")
def length_function(text: str) -> int:
    return len(enc.encode(text))

splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=2500, #try reducing the chunk size more significantly, then bumping up the k value (check out chatgpt)
    chunk_overlap=480,
    length_function=length_function,
)
file_path = 'RAGTDDCHATGPT.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()
chunks = splitter.split_text(text_content)

#gotta load these chunks into a vector db
########






EXPERIENCE_LEVEL_QUESTION = 'Rate your coding ability on a scale of 1 to 5'
print(EXPERIENCE_LEVEL_QUESTION)
experience_level = input()

experience_level

FRAMEWORKS_USED_QUESTIONS = 'Which coding languages have you used?'
print(FRAMEWORKS_USED_QUESTIONS)
frameworks_used = input()
frameworks_used

WHAT_TO_LEARN_QUESTIONS = "What would you like to learn?"
print(WHAT_TO_LEARN_QUESTIONS)
what_to_learn = input()
what_to_learn

CREATE_CONTEXT_PROMPT = f"""Summarize this student's coding experience level and learning goals using the following information: 
      The student's experience level on a scale of 0 to 5: {experience_level}
      The coding languages the student has used: {frameworks_used}
      The thing the student wants to learn: {what_to_learn}"""

import os
llm = ChatOpenAI(
    openai_api_key=os.environ["OPENAI_API_KEY"],
    model_name='gpt-4',
    temperature=0.0
)
context = llm.invoke(CREATE_CONTEXT_PROMPT)
context

jsonOutput = {"context": context}

PROMPT = f"""You are evaluating potential project ideas. Each idea has a hierarchy based on difficulty and applicability in the industry, rated on a scale from 1 to 5. Your goal is to organize these ideas in ascending order of difficulty and descending order of applicability: {context} Given their coding experience, what simple example project could the student build to learn the topic they want to learn? """

project = llm.invoke(str(PROMPT))
project



