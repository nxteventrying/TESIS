# Chaotic Time Series Generation, Analysis, and Forecasting

This repository contains my experimental workflows for generating, processing, and forecasting chaotic time series data.  
It includes scripts, processing notebooks, and exploratory feature extraction/forecasting methods, all inspired by recent research in chaos theory and deep learning.

---

## Repository Structure

- **GENESIS.py**  
  Main script for generating chaotic datasets.  
  This script supports multiple chaotic system configurations, simulating time series for downstream analysis.

- **Processing Notebooks**  
  Jupyter notebooks for:
  - Data cleaning and preprocessing.
  - Trial data exploration.
  - Applying dimensionality reduction (PCA, UMAP, t-SNE).

- **Forecasting Notebooks**  
  Experiments with:
  - Vanilla neural networks.
  - Convolutional neural networks (CNN).
  - Long Short-Term Memory networks (LSTM).  
  Currently tested on a single time series without scaling (baseline experiments).

- **Learning & Reference Notebooks**  
  Notebooks following exercises and concepts from *Time Series Forecasting* by Jason Brownlee, along with other exploratory scripts.

---

## Research References

This work is informed by the following articles:

1. Gilpin, W. (2021). *Chaos as an interpretable benchmark for forecasting and data-driven modelling*.  
   [DOI: 10.1038/s41567-021-01339-8](https://doi.org/10.1038/s41567-021-01339-8)

2. Villae, J., & Bruno, O. M. (2023). *Forecasting chaotic time series: Comparative performance of LSTM-based and Transformer-based neural networks*.  
   [arXiv:2301.09876](https://arxiv.org/abs/2301.09876)

3. Ali, S., et al. (2019). *Chaotic invariants for human action recognition*.  
   [DOI: 10.1109/CVPR.2019.00339](https://doi.org/10.1109/CVPR.2019.00339)

---

## Current Status

This is an **active research sandbox**, not a polished library.  
Expect:
- Scripts that could be refactored for clarity.
- Experimental notebooks with incomplete/inconclusive results.
- Rapidly changing structure as I clean and reorganize the codebase.

---

## License

[MIT License](LICENSE)
