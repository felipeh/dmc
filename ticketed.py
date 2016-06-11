def ticketedDMC(numWalkers=1000, numSteps=1000, dt=0.01):
    import numpy as np
    V = lambda x: x**2 / 2
    m = numWalkers
    x = np.zeros(m)
    t = np.random.rand(m)
    vals = []
    for i in range(numSteps):
        x1 = x + np.sqrt(dt) * np.random.randn(m)
        p  = np.exp(-dt*(V(x) + V(x1))/2)
        vals.append(np.mean(p))

        p  = p / np.mean(p)
        N  = np.floor(p + np.random.rand(m))
        N  = np.maximum(np.ones(m), N)
        N[p<t] = 0
        N = N.astype(int)
        newx = []
        newt = []
        for j in range(m):
            if N[j] > 0:
                newx.append(x1[j])
                newt.append(t[j] / p[j])
            for k in range(1,N[j]):
                newx.append(x1[j])
                newTicket = 1./p[j] + (1-1./p[j]) * np.random.rand()        
                newt.append(newTicket)
        
        assert len(newx) == np.sum(N)

        m = len(newx)
        ns.append(m)
        x = np.array(newx)
        t = np.array(newt)

    return -np.log(np.mean(vals[numSteps/2:numSteps])) / dt, m

if __name__ == "__main__":
    import numpy as np
    ests = []
    ns = []
    for i in range(20):
        E, m = ticketedDMC(1000,1000,0.01)
        ests.append(E)
        ns.append(m)
        print E, m

    print np.mean(ests), np.std(ests)
    print np.mean(ns), np.std(ns)
