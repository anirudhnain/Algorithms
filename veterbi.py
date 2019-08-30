def viterbi(obs, states, start_p, trans_p, emit_p):
    V=[{}]
    for i in states:
        V[0][i]=start_p[i]*emit_p[i][obs[0]]
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
        for i in dptable(V):
            print ("dptable:",i)
        opt=[]
        for j in V:
            for x,y in j.items():
                if j[x]==max(j.values()):
                    opt.append(x)

    print (V[-1])
    #the highest probability
    h=max(V[-1].values())
    print ('The steps of states are '+' '.join(opt)+' with highest probability of %s'%h)
    #it prints a table of steps from dictionary

def dptable(V):
    yield " ".join(("%10d" % i) for i in range(len(V)))
    for y in V[0]:
        yield "%.7s: " % y+" ".join("%.7s" % ("%f" % v[y]) for v in V)

states = ('N', 'D')
observations = ('A', 'T', 'T', 'C')
start_probability = {'N': 0.45, 'D': 0.55}
transition_probability = {
'D' : {'N': 0.1, 'D': 0.9},
'N' : {'D': 0.1, 'N': 0.9}
}
emission_probability = {
'N' : {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
'D' : {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3}
}

viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)