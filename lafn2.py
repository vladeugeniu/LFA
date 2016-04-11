def check(key, word):
   # print key
   # print word
    global ok
    if len(word) is 1:
        if (key[0],word[0]) in lafn and bool(set(lafn[key[0],word[0]]) & set(final_states)):
            ok = 1
    else:
        for state in lafn[key]:
            if (state, word[0]) in lafn:
                check((state, word[0]), word[1:])
            if (state, '.') in lafn:
                check((state, '.'), word)

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
        
for line in date_in[8+nr_transition +1:]:
    ok = 0
    word = line[:-1]
    #print (init_state, word[0])
    
    if (init_state, word[0]) in lafn:
        check((init_state, word[0]), word[1:])
    if (init_state, '.') in lafn:
        #print "cu punct"
        check((init_state, '.'), word)
        
    if ok:
        g.write("DA\n")
    else:
        g.write("NU\n")
