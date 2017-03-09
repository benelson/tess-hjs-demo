import numpy as np
import re
from math import isnan

MJtoMsun = 0.000954265748
RJtoAU = 0.000477894503
RstarToAU = 0.00465047

def create_dict_from_file(filename):
    '''Creates a cleaned array from input file'''
    with open(filename) as f:
        array = f.read().splitlines()
    tmp = np.transpose([ list(map(float, [ j.strip() for j in i.split()] )) for i in array ])
    keys = ["per","mass","rad","x"]
    return dict(zip(keys, tmp))

def stan_output_to_posterior_samples_2comp(dic):
    return np.array([ dic['theta'].T[0], dic['theta'].T[1], dic['gamma'].T[0], dic['gamma'].T[1], dic['xl'].T[0], dic['xl'].T[1], dic['xu'] ]).T
