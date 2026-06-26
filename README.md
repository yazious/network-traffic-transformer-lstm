# Network Traffic Classification Using Transformer-Enhanced LSTM Models

## Overview

This project focuses on network traffic classification using deep learning techniques. Three different models were implemented and compared: LSTM, CNN-LSTM, and a Transformer-Enhanced LSTM model.

The goal of the project is to classify different types of network traffic and intrusion attacks using publicly available datasets. The experiments were carried out on two datasets and evaluated on three separate classification tasks.

---

## Models Used

The following models were implemented during the experiments.

| Model            | Description                                                     |
| ---------------- | --------------------------------------------------------------- |
| LSTM             | Basic LSTM model with dense layers                              |
| CNN-LSTM         | Convolutional layers followed by LSTM                           |
| Transformer-LSTM | LSTM combined with Multi-Head Attention and feed-forward layers |

---

## Datasets

| Dataset         | Classes                            | Samples |
| --------------- | ---------------------------------- | ------- |
| CIC-Darknet2020 | 4-class and 8-class classification | 103,121 |
| CICIDS2017      | 12 attack classes                  | 239,535 |

### Dataset Links

* https://www.kaggle.com/datasets/dhoogla/cicdarknet2020
* https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset

---

## Project Structure

```text
network-traffic-transformer-lstm/
│
├── README.md
├── requirements.txt
│
├── notebooks/
│   └── experiment.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── model.py
│   └── evaluate.py
│
├── dataset/
│   └── dataset_links.txt
│
├── results/
│   └── metrics.txt
│
├── figures/
│   ├── D1_4class_curves.png
│   ├── D1_8class_curves.png
│   ├── D2_cicids_curves.png
│   ├── dataset1_distribution.png
│   ├── dataset2_distribution.png
│   ├── task1_4class_confusion.png
│   ├── task1_4class_comparison.png
│   ├── task2_8class_confusion.png
│   ├── task2_8class_comparison.png
│   ├── task3_cicids_confusion.png
│   └── task3_cicids_comparison.png
│
└── report/
    └── final_report.pdf
```

---

## Installation

```bash
https://github.com/yazious/network-traffic-transformer-lstm.git

cd network-traffic-transformer-lstm

pip install -r requirements.txt
```

---

## Running the Project

1. Download the datasets using the provided links.
2. Place the dataset files inside the dataset folder.
3. Open the notebook in Google Colab or Jupyter Notebook.
4. Run all cells in sequence.

The individual source files can also be executed separately if required.

```bash
python src/preprocessing.py
python src/model.py
python src/train.py
python src/evaluate.py
```

---

## Results

### Task 1 — CIC-Darknet2020 (4-Class)

| Model            | Accuracy | Precision | Recall | F1-Score |
| ---------------- | -------- | --------- | ------ | -------- |
| LSTM             | 92.83%   | 92.78%    | 92.83% | 92.77%   |
| CNN-LSTM         | 94.31%   | 94.42%    | 94.31% | 94.32%   |
| Transformer-LSTM | 93.57%   | 93.66%    | 93.57% | 93.58%   |

### Task 2 — CIC-Darknet2020 (8-Class)

| Model            | Accuracy | Precision | Recall | F1-Score |
| ---------------- | -------- | --------- | ------ | -------- |
| LSTM             | 74.24%   | 74.38%    | 74.24% | 72.11%   |
| CNN-LSTM         | 79.04%   | 79.33%    | 79.04% | 77.98%   |
| Transformer-LSTM | 76.62%   | 76.37%    | 76.62% | 74.87%   |

### Task 3 — CICIDS2017 (12-Class)

| Model            | Accuracy | Precision | Recall | F1-Score |
| ---------------- | -------- | --------- | ------ | -------- |
| LSTM             | 98.48%   | 98.59%    | 98.48% | 98.37%   |
| CNN-LSTM         | 98.90%   | 99.05%    | 98.90% | 98.82%   |
| Transformer-LSTM | 98.81%   | 98.95%    | 98.81% | 98.72%   |

---

## Team Members

* M Ayaz          — 62795
* Areeba Shah     — 63745
* Hafiza Amna     — 63580

Course: Computer Networks
Instructor: Ms. Poma Panezai
Department of Software Engineering, BUITEMS

---


## Discussion

The results show that all three models perform well on network traffic classification tasks. CNN-LSTM achieved the highest accuracy in most experiments, while the Transformer-LSTM model produced comparable results across all datasets.

On the CICIDS2017 dataset, both deep learning models achieved accuracy above 98%, indicating that these approaches are effective for intrusion detection problems.

The attention mechanism used in the Transformer-LSTM model helped capture important feature relationships and produced stable performance on multi-class classification tasks.

---



## References

1. Pacheco, F., et al. Towards the Deployment of Machine Learning Solutions in Network Traffic Classification. IEEE Communications Surveys & Tutorials, 2018.

2. Liu, X., et al. TransECA-Net: A Transformer-Based Model for Encrypted Traffic Classification. Applied Sciences, 2025.

3. Azab, M., et al. Network Traffic Classification: Techniques, Datasets, and Challenges, 2024.

4. Zhang, J., et al. Robust Network Traffic Classification. IEEE/ACM Transactions on Networking.

5. CIC-Darknet2020 Dataset.

6. CICIDS2017 Dataset.
