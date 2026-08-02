import numpy as np

from scipy.stats import ttest_ind


def compare_groups(all_coh,all_sex):

    male = all_coh[all_sex=="Male"]

    female = all_coh[all_sex=="Female"]

    tvals,pvals = ttest_ind(
        male,
        female,
        axis=0,
        equal_var=False
    )

    return male,female,tvals,pvals