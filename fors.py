def process(a: int):
    print(a)

# Use **kwargs to cleanly accept any dynamic dictionary arguments
def fors(procs, frommm=0, intos=0, steeps=1):
    while frommm < intos:
        procs(frommm)
        frommm += steeps

_restarts = {'frommm': 0, 'intos': 10, 'steeps': 1}

# Explicitly unpack the dictionary using **
fors(process, **_restarts)