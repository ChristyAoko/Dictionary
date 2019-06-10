import json
from difflib import get_close_matches

data = json.load (open("data.json"))
#function to return meaning of word
def translate(w):
    #for case sensitivity
    w = w.lower()
    #to check if word exists or not
    if w in data:
        return data [w]
    #to check for data that starts in a capital letter
    elif w.title() in data:
        return data[w.title()]
    #to check for acronyms like UN
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches (w, data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query."
    else:
        return "The word doesn't exist. Please double check it."

print ('\n****WELCOME TO MY PYTHON DICTIONARY*****\n')
word = input ("Enter word: ")

output = translate(word)

if type(output) == list:
   for item in output:
    print (item)
else:
    print(output)
