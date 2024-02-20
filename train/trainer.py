from __future__ import annotations
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
import utils
from tqdm import tqdm


def train_in_conversation(Roberto_ai: ChatBot, dialog):
    trainer = ChatterBotCorpusTrainer(Roberto_ai)
    utils.convert_dict_to_json(dialog)
    trainer.train("C:/Users/yuval/PycharmProjects/chat-ai/DataSets/conversation_in_action.json")


def training(Roberto_ai: ChatBot):
    trainer = ChatterBotCorpusTrainer(Roberto_ai)
    utils.convert_to_json_from_txt("C:/Users/yuval/PycharmProjects/chat-ai/DataSets/human_chat.txt")
    trainer.train("C:/Users/yuval/PycharmProjects/chat-ai/DataSets/human.json",
                  "C:/Users/yuval/PycharmProjects/chat-ai/DataSets/knowledgeExamples.json")
