def chcek(key, word):
    print word
    print key
    if len(word) is 0:
        if key[0] in final_states:
            ok = 1
    else:
        for state in lafn[key]:
            if (state, word[0]) in lafn:
                check((state, word[0]), word[1:])
            if (state, '.') in lafn:
                check((state, '.'), word)

lafn = {}
f = open("LNFA.in", "r")
date_in = f.readlines()

states = date_in[1]
symbols = date_in[3]
init_state = date_in[4]
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
        
print lafn
for line in date_in[8+nr_transition +1:]:
    ok = 0
    word = line[:-1]
    print init_state
    print word[0]
    if (init_state, word[0]) in lafn:
        check((init_state, word[0]), word)
    if (init_state, '.') in lafn:
        print "here"
        check((init_state, '.'), word)
    if ok:
        print "DA"
    else:
        print "NU"