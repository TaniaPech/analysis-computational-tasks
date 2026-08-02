import numpy as np

from config import SUBLIST
from data_loader import load_subject
from preprocessing import preprocess, create_epochs
from connectivity import compute_connectivity
from statistics import compare_groups
from plotting import save_figure

all_coh=[]
all_sex=[]

for subject in SUBLIST:

    raw,responses,age,sex = load_subject(subject)

    raw = preprocess(raw)

    epochs = create_epochs(raw,responses)

    coh = compute_connectivity(epochs)

    all_coh.append(coh)
    all_sex.append(sex)

all_coh = np.asarray(all_coh)
all_sex = np.asarray(all_sex)

male,female,tvals,pvals = compare_groups(
    all_coh,
    all_sex
)

save_figure(
    all_coh.mean(axis=0),
    male.mean(axis=0),
    female.mean(axis=0),
    pvals
)