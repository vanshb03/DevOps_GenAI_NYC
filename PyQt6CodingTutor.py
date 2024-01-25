import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

import langchain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI

class ProjectEvaluatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Project Evaluator')

        self.experience_label = QLabel('Rate your coding ability on a scale of 1 to 5:')
        self.experience_input = QLineEdit()

        self.frameworks_label = QLabel('Which coding languages have you used?')
        self.frameworks_input = QLineEdit()

        self.learn_label = QLabel('What would you like to learn?')
        self.learn_input = QLineEdit()

        self.evaluate_button = QPushButton('Evaluate Project')
        self.evaluate_button.clicked.connect(self.evaluate_project)

        self.result_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.experience_label)
        layout.addWidget(self.experience_input)
        layout.addWidget(self.frameworks_label)
        layout.addWidget(self.frameworks_input)
        layout.addWidget(self.learn_label)
        layout.addWidget(self.learn_input)
        layout.addWidget(self.evaluate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def evaluate_project(self):
        experience_level = self.experience_input.text()
        frameworks_used = self.frameworks_input.text()
        what_to_learn = self.learn_input.text()

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

        self.result_label.setText(f"Project: {project}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProjectEvaluatorApp()
    window.show()
    sys.exit(app.exec())
