# Chaotic Time Series Generation & Forecasting

This repository contains code, scripts, and experiments for generating, processing, and forecasting chaotic time series.  
The work is inspired and guided by three main references:

1. **Gilpin, W. (2021)** – *Chaos as an interpretable benchmark for forecasting and data-driven modelling*

   DOI: https://doi.org/10.48550/arXiv.2110.05266
4. **Vllae, J. & Bruno, O. M. (2023)** – *Forecasting chaotic time series: Comparative performance of LSTM-based and Transformer-based neural networks*

   DOI: https://doi.org/10.1016/j.chaos.2025.116034
6. **Ali, S., et al. (2019)** – *Chaotic invariants for human action recognition*

   DOI: https://doi.org/10.1109/ICCV.2007.4409046

---

## Repository Structure

### Core Scripts
- **`genesis.py`**  
  A configurable chaotic time series generator built on a collection of helper functions and classes.  
  - **Purpose:** Generate synthetic datasets for forecasting and analysis.  
  - **Input:** JSON configuration specifying system type, parameters, sample length, etc.  
  - **Output:** Organized dataset folders with generated time series in `.csv` format.  
  - **Features:**  
    - Multiple chaotic systems (Lorenz, Rössler, and more)  
    - Batch generation from multiple configuration files  

- **`crawler.py`**  
  A dataset indexing tool to scan generated folders and collect metadata for further processing.  
  - **Purpose:** Automate the discovery of generated time series files.  
  - **Limitations:** Currently requires folder structure to be prepared manually before execution.  
  - **Output:** Indexed csv called id of file paths for loading into notebooks.

---

### Notebooks
#### experimentos- Workflow simulations*
Firsts iterations on the construction of genesis.py and helper functions
- **Refine and streamline the workflow and code structure**, figuring out how scripts should interact  

#### PG – *Playground Experiments*  
Exploratory notebooks where different ideas were tested, including:  
- Use of tsfresh for generic time series feature extraction (780+) and use of nolds for lyapunov exponent, correlation dimension and sampling entropy. 
- PCA, UMAP, and t-SNE for chaotic feature reduction
- Data Cleaning 
- Initial trials with vanilla neural networks, CNNs, and LSTMs for forecasting (on a single time series, without scaling)

#### EXODUS – *Tutorial Implementations*  
Notebooks created by following external tutorials, mainly from *Time Series Forecasting* by James Brownlee and other online resources.

#### Model-Specific Notebooks (VNN, CNN, LSTM)  
Dedicated forecasting experiments organized by architecture type.

---

## Workflow

```text
+---------------------+
|   config.json file  |
+----------+----------+
           |
           v
+---------------------+
|     GENESIS.py      |  --> Generates chaotic datasets (.csv)
+----------+----------+
           |
           v
+---------------------+
|     crawler.py      |  --> Index dataset files & metadata
+----------+----------+
           |
           v
+---------------------+
|   Jupyter Notebook  |  --> Processing, cleaning, scaling
+----------+----------+
           |
           v
+---------------------+
|  Forecasting Models |
| (VNN, CNN, LSTM...) |
+---------------------+
```
## Current Status

This is an **active research sandbox**, not a polished library.  
Expect:
- Scripts that could be refactored for clarity.
- Experimental notebooks with incomplete/inconclusive results.
- Rapidly changing structure as I clean and reorganize the codebase.

---

## License

[GLPv3](LICENSE)
