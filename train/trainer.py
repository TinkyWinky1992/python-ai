from __future__ import annotations
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import utils
import json


def train_in_conversation(Roberto_ai: ChatBot, dialog):
    trainer = ChatterBotCorpusTrainer(Roberto_ai)

    utils.convert_dict_to_json(dialog)
    trainer.train("C:/Users/USER/projects/python-ai/DataSets/conversation_in_action.json")


def training(Roberto_ai: ChatBot):
    datas = [json.loads(open("C:/Users/USER/projects/python-ai/DataSets/welcoming.json", 'r').read()),
            ]
    custom_train(Roberto_ai, datas)

    trainer = ChatterBotCorpusTrainer(Roberto_ai)
    trainer.train("chatterbot.corpus.english.health")


def custom_train(Roberto_ai: ChatBot, datas):
    list = []
    for data in datas:
        for conversation_id, conversation_data in data.items():
            for index, line in conversation_data.items():
                list.append(line["Human 1"])
                list.append(line["Human 2"])

    trainer = ListTrainer(Roberto_ai)
    trainer.train(list)
