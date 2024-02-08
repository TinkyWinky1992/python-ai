from __future__ import annotations
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
import utils
from tqdm import tqdm


def train_with_custom_data(Roberto: ChatBot, custom_data):
    with tqdm(total=len(custom_data), desc='Training custom data') as pbar:
        for item in custom_data:
            # Extract relevant information from custom data
            question = item.get('question')
            answer = item.get('answer')

            # Create statement objects
            question_statement = Statement(text=question)
            answer_statement = Statement(text=answer)

            # Learn from the statement objects
            Roberto.learn_response(answer_statement, question_statement)
            pbar.update(1)  # Update progress bar


def training(Roberto_ai: ChatBot):
    trainer = ChatterBotCorpusTrainer(Roberto_ai)
    trainer.train('chatterbot.corpus.english', "C:/Users/yuval/PycharmProjects/chat-ai/knowledgeExamples.json")
    custom_data = utils.load_custom_data("C:/Users/yuval/PycharmProjects/chat-ai/new-data.json")
    train_with_custom_data(Roberto_ai, custom_data)
