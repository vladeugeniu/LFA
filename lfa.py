lafn = {}

f = open("date.in", "r")
date_in = f.readlines()

symbols = date_in[0]
states = date_in[1]
final_states = date_in[2]

for state in states:
    lafn[state] = []

i = 0
for line in date_in[3:]:
    lafn[states[i]] = line.split()
    i += 1
    
    

