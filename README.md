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

1. A. Azab, M. Khasawneh, S. Alrabaee, K.-K. R. Choo, and M. Sarsour, "Network Traffic Classification: Techniques, Datasets, and Challenges," *Digital Communications and Networks*, vol. 10, pp. 676–692, 2024.

2. F. Pacheco, E. Exposito, M. Gineste, C. Baudoin, and J. Aguilar, "Towards the Deployment of Machine Learning Solutions in Network Traffic Classification: A Systematic Survey," *IEEE Communications Surveys & Tutorials*, vol. 21, no. 2, pp. 1988–2014, 2019. DOI: 10.1109/COMST.2018.2883147

3. J. Zhao, X. Jing, Z. Yan, and W. Pedrycz, "Network Traffic Classification for Data Fusion: A Survey," *Information Fusion*, vol. 72, pp. 22–47, 2021.

4. J. Zhang, X. Chen, Y. Xiang, W. Zhou, and J. Wu, "Robust Network Traffic Classification," *IEEE/ACM Transactions on Networking*, vol. 23, no. 4, pp. 1257–1270, 2015. DOI: 10.1109/TNET.2014.2320577

5. Z. Liu, Y. Xie, Y. Luo, Y. Wang, and X. Ji, "TransECA-Net: A Transformer-Based Model for Encrypted Traffic Classification," *Applied Sciences*, vol. 15, no. 6, p. 2977, 2025. DOI: 10.3390/app15062977

6. N. Mandela, Sonia, N. Mistry, and A. Nagpal, "Efficient Dark Web Traffic Classification Using a Hybrid CNN-LSTM Model," *International Journal of Information Technology*, 2025. DOI: 10.1007/s41870-025-02427-x

7. I. Sharafaldin, A. H. Lashkari, and A. A. Ghorbani, "Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization," in *Proceedings of the 4th International Conference on Information Systems Security and Privacy (ICISSP)*, 2018, pp. 108–116.

8. H. Afifi et al., "Machine Learning with Computer Networks: Techniques, Datasets, and Models," *IEEE Access*, vol. 12, pp. 54673–54703, 2024. DOI: 10.1109/ACCESS.2024.3384460

9. N. Bayat, W. Jackson, and D. Liu, "Deep Learning for Network Traffic Classification," *arXiv preprint arXiv:2106.12693*, 2021.

10. A. Vaswani et al., "Attention Is All You Need," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 30, 2017.

11. S. Hochreiter and J. Schmidhuber, "Long Short-Term Memory," *Neural Computation*, vol. 9, no. 8, pp. 1735–1780, 1997.

12. M. Lopez-Martin, B. Carro, A. Sanchez-Esguevillas, and J. Lloret, "Network Traffic Classifier with Convolutional and Recurrent Neural Networks for Internet of Things," *IEEE Access*, vol. 5, pp. 18042–18050, 2017.

13. M. Lotfollahi, M. Jafari Siavoshani, R. Shirali Hossein Zade, and M. Saberian, "Deep Packet: A Novel Approach for Encrypted Traffic Classification Using Deep Learning," *Soft Computing*, vol. 24, no. 3, pp. 1999–2012, 2020.

14. H. Yao, C. Liu, P. Zhang, S. Wu, C. Jiang, and S. Yu, "Identification of Encrypted Traffic Through Attention Mechanism Based Long Short-Term Memory," *IEEE Transactions on Big Data*, 2019.

15. A. H. Lashkari, G. Kaur, and A. Rahali, "DIDarknet: A Contemporary Approach to Detect and Characterize the Darknet Traffic Using Deep Image Learning," in *Proceedings of the 10th International Conference on Communication and Network Security*, Tokyo, Japan, Nov. 2020.

16. X. Lin, G. Xiong, G. Gou, Z. Li, J. Shi, and J. Yu, "ET-BERT: A Contextualized Datagram Representation with Pre-training Transformers for Encrypted Traffic Classification," in *Proceedings of the ACM Web Conference (WWW)*, 2022, pp. 633–642.

17. Z. Liu et al., "Spatial-Temporal Feature with Dual-Attention Mechanism for Encrypted Malicious Traffic Detection," *Security and Communication Networks*, 2023.

18. J. H. Kalwar and S. Bhatti, "Deep Learning Approaches for Network Traffic Classification in the Internet of Things (IoT): A Survey," *arXiv preprint arXiv:2402.00920*, 2024.

19. R. Vinayakumar, M. Alazab, K. P. Soman, P. Poornachandran, A. Al-Nemrat, and S. Venkatraman, "Deep Learning Approach for Intelligent Intrusion Detection System," *IEEE Access*, vol. 7, pp. 41525–41550, 2019.

20. C. Yin, Y. Zhu, J. Fei, and X. He, "A Deep Learning Approach for Intrusion Detection Using Recurrent Neural Networks," *IEEE Access*, vol. 5, pp. 21954–21961, 2017.
