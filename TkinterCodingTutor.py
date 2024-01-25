import os
import tkinter as tk
from tkinter import Label, Entry, Button, Text, Scrollbar

import langchain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI

class ProjectEvaluatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Project Evaluator')

        self.experience_label = Label(root, text='Rate your coding ability on a scale of 1 to 5:')
        self.experience_input = Entry(root)

        self.frameworks_label = Label(root, text='Which coding languages have you used?')
        self.frameworks_input = Entry(root)

        self.learn_label = Label(root, text='What would you like to learn?')
        self.learn_input = Entry(root)

        self.evaluate_button = Button(root, text='Evaluate Project', command=self.evaluate_project)

        self.result_text = Text(root, wrap='word', height=10, width=50)
        self.result_scrollbar = Scrollbar(root, command=self.result_text.yview)
        self.result_text['yscrollcommand'] = self.result_scrollbar.set

        self.experience_label.pack()
        self.experience_input.pack()
        self.frameworks_label.pack()
        self.frameworks_input.pack()
        self.learn_label.pack()
        self.learn_input.pack()
        self.evaluate_button.pack()
        self.result_text.pack(side='left', padx=5)
        self.result_scrollbar.pack(side='right', fill='y')  # Corrected argument

    def evaluate_project(self):
        experience_level = self.experience_input.get()
        frameworks_used = self.frameworks_input.get()
        what_to_learn = self.learn_input.get()

        CREATE_CONTEXT_PROMPT = f"""Summarize this student's coding experience level and learning goals using the following information: 
              The student's experience level on a scale of 0 to 5: {experience_level}
              The coding languages the student has used: {frameworks_used}
              The thing the student wants to learn: {what_to_learn}"""

        llm = ChatOpenAI(
            openai_api_key=os.environ["OPENAI_API_KEY"],
            model_name='gpt-4',
            temperature=0.0
        )
        context = llm.invoke(CREATE_CONTEXT_PROMPT)

        PROMPT = f"""You are evaluating potential project ideas. Each idea has a hierarchy based on difficulty and applicability in the industry, rated on a scale from 1 to 5. Your goal is to organize these ideas in ascending order of difficulty and descending order of applicability: {context} Given their coding experience, what simple example project could the student build to learn the topic they want to learn? """

        project = llm.invoke(str(PROMPT))

        self.result_text.config(state='normal')  # Enable editing
        self.result_text.delete('1.0', 'end')  # Clear preavious content
        self.result_text.insert('1.0', f"{project}\n")  # Insert new content
        self.result_text.config(state='disabled')  # Disable editing

if __name__ == '__main__':
    root = tk.Tk()
    app = ProjectEvaluatorApp(root)
    root.mainloop()