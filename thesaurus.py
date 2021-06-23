import json

data = json.load(open("data.json"))


def get_definition(w):
    if w in data:
        return data[w]
    else:
        return "That word doesn't exist."


word = input("Enter word: ")

print(get_definition(word))
