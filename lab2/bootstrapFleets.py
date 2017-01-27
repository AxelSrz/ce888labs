import matplotlib

matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np


def boostrap(statistic_func, iterations, data):
    samples = np.random.choice(data, replace=True, size=[iterations, len(data)])
    # print samples.shape
    data_std = data.std()
    vals = []
    for sample in samples:
        sta = statistic_func(sample)
        # print sta
        vals.append(sta)
    b = np.array(vals)
    # print b
    lower, upper = np.percentile(b, [2.5, 97.5])
    return data_std, lower, upper


if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')
    # print df.columns

    data = df.values.T[1]
    boots = []
    boot = boostrap(np.std, 10000, data)

    print "--------------- Current set ---------------"

    print "Std: ",boot[0]
    print "Lower: ",boot[1]
    print "Upper: ",boot[2]

    data = df.values.T[3]
    data = data[~np.isnan(data)]
    boots = []
    boot = boostrap(np.std, 10000, data)

    print "--------------- New set ---------------"

    print "Std: ",boot[0]
    print "Lower: ",boot[1]
    print "Upper: ",boot[2]



# print ("Mean: %f")%(np.mean(data))
# print ("Var: %f")%(np.var(data))



