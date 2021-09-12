import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def getDefinition(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #for cities
        return data[word.title()]
    elif word.upper() in data: #for words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        check=input("Did you mean %s instead?, Enter Y if yes, or N if no." % get_close_matches(word,data.keys())[0])
        if check=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif check=="N":
            return "The word doesn't exist in this dictionary."
        else:
            return "Invalid answer."
    else:
        return "The word doesn't exist in this dictionary."

word=input("Enter a word:")
output=getDefinition(word)

if(isinstance(output,str)):
    print(output)

else:
    for item in output:
        print(item)