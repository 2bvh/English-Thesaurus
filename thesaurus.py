import json

data = json.load(open("data.json"))


def return_definition(word):
    return data[word]
