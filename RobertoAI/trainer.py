from __future__ import annotations
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
import utils
from tqdm import tqdm





def training(Roberto_ai: ChatBot):
    trainer = ChatterBotCorpusTrainer(Roberto_ai)
    trainer.train('chatterbot.corpus.english', "C:/Users/yuval/PycharmProjects/chat-ai/DataSets/knowledgeExamples.json")

