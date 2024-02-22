from __future__ import annotations
from chatterbot import ChatBot
import utils
from train import trainer


def init_bot() -> ChatBot:
    Roberto_ai = ChatBot('Roberto Rosemario',
                         database_uri='sqlite:///database.sqlite3',
                         logic_adapters=[
                             {

                                 'import_path': 'chatterbot.logic.BestMatch',
                                 "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",

                             }

                         ]
                         )

    trainer.training(Roberto_ai)
    return Roberto_ai


def response(user_input, chat_ai) -> str | None:
    ai_response = chat_ai.get_response(user_input)
    if ai_response is not None:
        return str(ai_response)
    return None


def conversation():
    conversation_list = {}
    counter = 1
    Roberto: ChatBot = init_bot()
    while True:
        print(conversation_list)
        text_user: str = "Human 1:"
        text_bot: str = "Human 2:"

        user_input: str = input("Type Something to Roberto: ")
        text_user += user_input
        if user_input.lower() == "quit":
            break

        try:
            # Display progress bar during conversation loop
            print("Processing input...")  # Static progress message
            Roberto_res = response(user_input, Roberto)

            text_bot += str(Roberto_res)
            dialog_lines = [text_bot, text_user]
            utils.creating_conversation_dict(conversation_list, dialog_lines, len(conversation_list))

            trainer.train_in_conversation(Roberto, conversation_list)

            print(Roberto_res)
        except(KeyboardInterrupt, EOFError, SystemExit):
            break


if __name__ == "__main__":
    conversation()
