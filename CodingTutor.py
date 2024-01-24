from flask import Flask, render_template, request

import langchain
import openai
import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI

app = Flask(__name__)

EXPERIENCE_LEVEL_QUESTION = 'Rate your coding ability on a scale of 1 to 5'
FRAMEWORKS_USED_QUESTIONS = 'Which coding languages have you used?'
WHAT_TO_LEARN_QUESTIONS = "What would you like to learn?"

CREATE_CONTEXT_PROMPT = """Summarize this student's coding experience level and learning goals using the following information: 
    The student's experience level on a scale of 0 to 5: {}
    The coding languages the student has used: {}
    The thing the student wants to learn: {}"""

llm = ChatOpenAI(
    openai_api_key=os.environ["OPENAI_API_KEY"],
    model_name='gpt-4',
    temperature=0.0
)

PROMPT = """You are evaluating potential project ideas. Each idea has a hierarchy based on difficulty and applicability in the industry, rated on a scale from 1 to 5. Your goal is to organize these ideas in ascending order of difficulty and descending order of applicability: {}. Given their coding experience, what simple example project could the student build to learn the topic they want to learn?"""

@app.route('/')
def index():
    return render_template('index.html')  # Create an HTML template for your website

@app.route('/evaluate_project', methods=['POST'])
def evaluate_project():
    experience_level = request.form['experience_level']
    frameworks_used = request.form['frameworks_used']
    what_to_learn = request.form['what_to_learn']

    context = llm.invoke(CREATE_CONTEXT_PROMPT.format(experience_level, frameworks_used, what_to_learn))
    project = llm.invoke(PROMPT.format(context))

    return render_template('result.html', context=context, project=project)

if __name__ == '__main__':
    app.run(debug=True)