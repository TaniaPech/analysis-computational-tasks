# EEG Connectivity Analysis During Programming Tasks

This repository contains the computational pipeline used to analyze EEG functional connectivity during a programming task from the NeuroTechs Dataset for STEM Skills (OpenNeuro ds006803).

The analysis focuses on estimating functional connectivity using imaginary coherence (imCoh) in the theta, alpha, and beta frequency range, and comparing connectivity patterns between female and male groups.

---

## Repository Structure

```
analysis-computational-tasks/
│
├── data/
│   └── ds006803/          # Dataset (not included in this repository)
│
├── src/
│   ├── main.py            # Main analysis pipeline
│   ├── dataset.py         # Dataset loading functions
│   ├── preprocessing.py   # EEG preprocessing
│   ├── connectivity.py    # Connectivity estimation
│   ├── statistics.py      # Statistical analysis
│   └── plotting.py        # Visualization functions
│
├── figures/               # Generated figures
│
├── requirements.txt       # Python dependencies
└── README.md
```

---

## Dataset

The EEG recordings used in this project are part of:

**NeuroTechs Dataset for STEM Skills**  
OpenNeuro accession: ds006803

The dataset is not included in this repository.

After downloading, place the dataset inside:

```
data/ds006803/
```

The expected structure is:

```
data/
└── ds006803/
    ├── extra_metadata.xlsx
    ├── sub-01c/
    │   ├── programming_responses.csv
    │   └── ses-1/
    │       └── eeg/
    │           └── sub-01c_ses-1_task-STEMSKILLS_eeg.set
    └── ...
```

---

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Analysis

From the repository root:

```bash
python src/main.py
```

---

## Requirements

Python >= 3.10

Main dependencies:

- MNE
- MNE-connectivity
- NumPy
- Pandas
- SciPy
- Statsmodels
- Matplotlib