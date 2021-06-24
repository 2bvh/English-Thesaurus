import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def get_definition(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        top_match = get_close_matches(w, data.keys())[0]
        yn = input("Did you mean %s? Enter Y/N " % top_match)
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Please try again"
        else:
            return "We didn't understand your response."
    else:
        return "That word doesn't exist."


word = input("Enter word: ")

output = get_definition(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
