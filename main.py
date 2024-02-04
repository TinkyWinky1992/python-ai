from __future__ import annotations
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def training(Roberto_ai: ChatBot):
    trainer = ListTrainer(Roberto_ai)
    trainer.train([
        "Hello, Dr. Roberto Rosemario. I've been experiencing persistent headaches lately, and I'm a bit worried "
        "about it. ",
        "Hello there! I'm sorry to hear about your headaches. Let's see how we can help. Would you like to schedule "
        "an appointment at our hospital? ",
        "Yes, please. I think it's best to get it checked out.",
        "Absolutely. I'll go ahead and make an appointment for you. Based on your description, it seems like it might "
        "be important to get this checked soon. I'll note it down and provide you with a report letter. "
    ])
    trainer.train([
        "what is your name?",
        "my name is Roberto but you can call me Doctor Roberto."
        "how can you help me?",
        "I can help you by, answer about your medical questions, or making your appointment. or talking your some joke."

    ])
    trainer.train([
        "tell me some joke?",
        "lalalallalalalalalalal"
    ])


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
        if user_input == "Quit":
            break

        try:
            Roberto_res = response(user_input, Roberto)
            print(Roberto_res)
        except(KeyboardInterrupt, EOFError, SystemExit):
            break


if __name__ == "__main__":
    conversation()
