import json
from difflib import get_close_matches

with open('data.json') as f:
    data = json.load(f)

def find_definition(word):
    if word in data:
        return data[word]
    else:
        match = get_close_matches(word, data.keys(), 1, 0.6)
        if match == []:
            return 'That is not a real word. Please double check!'
        else:
            print(f'Did you mean {match[0]}?')
            answer = input('Type Y or N: ')
            if answer.lower() == 'y':
                return data[match[0]]
            elif answer.lower() == 'n':
                return 'Please check your word an try again then...'

word = input("What word would you like to know the defintion for?\n").lower()

result = find_definition(word)
if type(result) == list:
    j = 1
    for definition in result:
        print(f'{j}. {definition}')
        j += 1
else:
    print(result)
