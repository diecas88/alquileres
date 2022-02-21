# fincaraiz 

By: diecas88.

Version: 0.1.0

analizar datos de los arrendamientos en la ciudad de Bucaramanga.

## Prerequisites

- [Anaconda](https://www.anaconda.com/download/) >=4.x
- Optional [Mamba](https://mamba.readthedocs.io/en/latest/)

## Create environment

```bash
conda env create -f environment.yml
activate fincaraiz
```

or 

```bash
mamba env create -f environment.yml
activate fincaraiz
```

## Project organization

    fincaraiz
        ├── data
        │   ├── docs         <- The final, canonical data sets for modeling.
        │   └── src          <- The original, immutable data dump.
        │   ├── processed                       <- The final, canonical data sets for modeling.
        │   └── raw                             <- The original, immutable data dump.
        │
        ├── notebooks                           <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                                           the creator's initials, and a short `-` delimited description, e.g.
        │                                           ``.
        │
        ├── .gitignore                          <- Files to ignore by `git`.
        │
        ├── environment.yml                     <- The requirements file for reproducing the analysis environment.
        │
        └── README.md                           <- The top-level README for developers using this project.

---
