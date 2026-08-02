import numpy as np
import mne_connectivity

from config import FS,FREQS,N_CYCLES


def compute_connectivity(epochs):

    con = mne_connectivity.spectral_connectivity_epochs(
        epochs,
        method="imcoh",
        mode="cwt_morlet",
        sfreq=FS,
        cwt_freqs=FREQS,
        cwt_n_cycles=N_CYCLES,
        fmin=4,
        fmax=30,
        tmin=-1
    )

    coh = con.get_data(output="dense")

    coh = np.clip(
        coh,
        -.999999,
        .999999
    )

    return np.arctanh(coh)