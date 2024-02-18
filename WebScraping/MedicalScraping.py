import wikipedia
def get_nih_content():
    text = wikipedia.summary("Doctor–patient relationship")
    print(text)

get_nih_content()