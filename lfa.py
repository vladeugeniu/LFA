


def check(transition_list, word):
    """
    This is a recursive function that check
    the transition for every symbol in word
    """
    
    for transition in transition_list:
        




lafn = {}
f = open("date.in", "r")
date_in = f.readlines()

symbols = date_in[0]
states = date_in[1]
final_states = date_in[2]

i = 0
for line in date_in[3:]:
    lafn[states[i]] = line.split()
    lafn[states[i]] = [x.strip for x in lafn[states[i]]
    i += 1

    

