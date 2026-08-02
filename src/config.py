from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_PATH = PROJECT_ROOT / "data" / "ds006803"
FIGURES_PATH = PROJECT_ROOT / "figures"

FIGURES_PATH.mkdir(parents=True, exist_ok=True)

FS = 250
TMIN = -1
TMAX = 2

FREQS = np.arange(4,30.1,0.1)
N_CYCLES = FREQS/2

CHANNELS = [
    "Fz","C3","Cz","C4",
    "Pz","PO7","Oz","PO8"
]

SUBLIST = ["sub-01c","sub-02c","sub-03c","sub-04c","sub-05c","sub-06c","sub-07c","sub-08c","sub-09c","sub-10c","sub-11c","sub-12c","sub-13c","sub-14c","sub-15c","sub-16c","sub-18c","sub-19c","sub-20c","sub-21c","sub-22c","sub-23c","sub-24c","sub-01e","sub-02e","sub-03e","sub-04e","sub-05e","sub-06e","sub-07e","sub-08e","sub-09e","sub-10e","sub-11e","sub-12e","sub-13e","sub-14e","sub-15e","sub-16e","sub-17e","sub-18e","sub-19e","sub-20e","sub-21e","sub-22e","sub-23e","sub-24e","sub-25e","sub-26e","sub-27e","sub-28e","sub-29e","sub-31e","sub-33e","sub-34e","sub-36e","sub-37e","sub-38e","sub-39e","sub-40e","sub-41e","sub-42e","sub-43e"]
