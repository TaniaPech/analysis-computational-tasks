import numpy as np
import mne

from config import FS,TMIN,TMAX


def preprocess(raw):

    raw.set_eeg_reference("average")

    raw.filter(
        l_freq=4,
        h_freq=30
    )

    return raw


def create_epochs(raw,responses):

    appearance = responses.iloc[:,1]-3

    diffs = np.diff(appearance)

    valid = diffs>=2

    appearance = appearance.iloc[:-1][valid]

    samples = (appearance*FS).astype(int)

    events = np.column_stack((
        samples,
        np.zeros(len(samples),dtype=int),
        np.ones(len(samples),dtype=int)
    ))

    epochs = mne.Epochs(
        raw,
        events,
        event_id=1,
        tmin=TMIN,
        tmax=TMAX,
        preload=True
    )

    return epochs