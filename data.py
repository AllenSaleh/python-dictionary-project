import json
from difflib import get_close_matches
data = json.load(open('data.json'))
out = False
while (out==False):

    def filt(w):
        w = w.lower()
        if w in data:
            return data[w]
        elif w.title in data:
            return data[w.title()]
        elif w.upper() in data:
            return data[w.upper()]
        elif len(get_close_matches(w, data.keys())) > 0:
            yn = input('did you mena {} instead if yes prees Y if no N '.format(get_close_matches(w, data.keys())[0]))

            if yn == 'y':
                return data[get_close_matches(w, data.keys())[0]]
            elif yn == 'n':
                return 'this word does not excist! pleas double check'
        else:
            return 'we have not understand what you have enter'


    user = input("Enter ")
    output = filt(user)
    if type(output) == list:
        for i in output:
            print(i)
    else:
        print(output)
    ques = input('do you want to keep going ? Y/N')
    if ques.lower() == 'y':
      out =False
    elif ques.lower() == 'n':
      out=True

print ('Good Bey!')