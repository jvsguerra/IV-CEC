# KVFinderMD analysis for the IV CEC (Congresso de estudantes do CNPEM)

## System requirements

- [Anaconda](https://www.anaconda.com/) (v2022.10)

```bash
sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
./Anaconda3-2022.10-Linux-x86_64.sh
```

- [Python 3](https://www.python.org) (v3.9.0)

```bash
conda create -n jupyter python==3.9.6 notebook
conda activate jupyter
ipython kernel install --name jupyter --user
```

- [PyMOL](https://www.pymol.org) (v2.5.0)

```bash
conda install -c conda-forge pymol-open-source
```

## Python requirements

- [toml](https://pypi.org/project/toml) (v0.10.2): a Python library for parsing and creating TOML;

- [KVFinderMD](https://github.com/LBC-LNBio/KVFinderMD) (v0.2.1): a Python package for identifying and describing cavities throughout molecular dynamics simulations;

- [matplotlib](https://pypi.org/project/matplotlib/) (v3.6.1): a comprehensive library for creating static, animated, and interactive visualizations in Python;

- [MDAnalysis](https://pypi.org/project/MDAnalysis/) (v2.3.0):a Python library for the analysis of computer simulations of many-body systems at the molecular scale, spanning use cases from interactions of drugs with proteins to novel materials;

- [SERD](https://pypi.org/project/SERD/) (v0.1.2): a Python package to detect solvent-exposed residues of a target biomolecule;

- [nglview](https://pypi.org/project/nglview/) (v3.0.3): an IPython/Jupyter widget to interactively view molecular structures and trajectories.

```bash
pip install -r requirements.txt
```

## Analysis

- HIV-1 protease ([HIV-analysis.ipynb](https://github.com/jvsguerra/IV-CEC/blob/main/HIV-analysis.ipynb)): explore cavity alignment (grid, distance matrix and contact matrix) to group cavities throughtout the molecular dynamics trajectory;

- ALDH 1/2 ([ALDH-analysis.ipynb](https://github.com/jvsguerra/IV-CEC/blob/main/ALDH-analysis.ipynb)): explore the difference of the substrate binding site volume between ALDH1 and ALDH2.

## License

The software is licensed under the terms of the MIT License and is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the MIT License for more details.
