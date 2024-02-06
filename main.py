from __future__ import annotations
import json
import io
from chatterbot import ChatBot, filters
from chatterbot.trainers import ChatterBotCorpusTrainer


def training(Roberto_ai: ChatBot):
    trainer = ChatterBotCorpusTrainer(Roberto_ai)
    trainer.train('chatterbot.corpus.english', "C:/Users/yuval/PycharmProjects/chat-ai/knowledgeExamples.json")

def init_bot() -> ChatBot:
    Roberto_ai = ChatBot('Roberto Rosemario')
    training(Roberto_ai)
    return Roberto_ai


def response(user_input, chat_ai) -> str | None:
    ai_input: str = chat_ai.get_response(user_input)
    if ai_input is not None:
        return ai_input
    return None


def conversation():
    Roberto: ChatBot = init_bot()
    while True:
        user_input: str = input("Type Something to Roberto: ")
        if user_input.lower() == "quit":
            break

        try:
            Roberto_res = response(user_input, Roberto)
            print(Roberto_res)
        except(KeyboardInterrupt, EOFError, SystemExit):
            break


if __name__ == "__main__":
    conversation()
