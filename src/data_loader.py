import pandas as pd
import mne

from config import DATASET_PATH

metadata = pd.read_excel(
    DATASET_PATH/"extra_metadata.xlsx",
    sheet_name="Individual metadata",
    index_col=0
)


def load_subject(subject):

    raw = mne.io.read_raw_eeglab(
        DATASET_PATH
        / subject
        / "ses-1"
        / "eeg"
        / f"{subject}_ses-1_task-STEMSKILLS_eeg.set",
        preload=True
    )

    responses = pd.read_csv(
        DATASET_PATH
        / subject
        / "programming_responses.csv",
        index_col=0
    )

    age = metadata.loc[subject,"Age"]
    sex = metadata.loc[subject,"AAB Sex"]

    return raw,responses,age,sex