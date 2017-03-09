import numpy as np

def ICs_2comp_nomasses(IC, mlist, nChains):
    K = len(IC[0])
    theta = [ IC[0] for i in range(nChains) ]
    gamma = [ IC[1] for i in range(nChains) ]
    xl = [ IC[2] for i in range(nChains) ]
    xu = [ IC[3] for i in range(nChains) ]

    ICs = []
    for i in range(nChains):
        ICs.append({ "theta": theta[i], "gamma": gamma[i], "xl": xl[i], "xu": xu[i], "log_mass": mlist })
    return ICs


def ICs_2comp_withmasses(IC, nChains):
    K = len(IC[0])
    theta = [ IC[0] for i in range(nChains) ]
    gamma = [ IC[1] for i in range(nChains) ]
    xl = [ IC[2] for i in range(nChains) ]
    xu = [ IC[3] for i in range(nChains) ]

    ICs = []
    for i in range(nChains):
        ICs.append({ "theta": theta[i], "gamma": gamma[i], "xl": xl[i], "xu": xu[i] })
    return ICs
