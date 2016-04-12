def check(key, word):
    print key
    print word
    global ok
    if len(word) is 0:
        if key  in final_states:
           ok = 1
    else:
        if (key, word[0]) in lafn:
            for state in lafn[(key, word[0])]:
                check(state, word[1:])
        if (key, '.') in lafn:
            for state in lafn[(key, '.')]:
                check(state, word)

lafn = {}
f = open("LNFA.in", "r")
g = open("LNFA.out", "w")
date_in = f.readlines()

states = date_in[1]
symbols = date_in[3]
init_state = date_in[4][:-1]
final_states = date_in[6]
nr_transition = int(date_in[7])

for line in date_in[8:8+nr_transition]:
    line = line.split()
    key = (line[0], line[1])
    if key in lafn:
        lafn[key].append(line[2])
    else:
        lafn[key] = []
        lafn[key].append(line[2])
print states
print lafn        
for line in date_in[8+nr_transition +1:]:
    ok = 0
   
    word = line[:-1]
    
    #print (init_state, word[0])
   
   
    check(init_state, word)
 
        
    if ok:
        g.write("DA\n")
    else:
        g.write("NU\n")
