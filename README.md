# German Traffic Sign Classification with CNN (GTSRB)

A deep learning project for German traffic sign recognition and classification using Convolutional Neural Networks (CNNs) implemented with TensorFlow/Keras.

The project is based on the German Traffic Sign Recognition Benchmark (GTSRB) dataset and was developed in the context of Computer Vision for Autonomous Driving.

The complete workflow was mainly implemented inside Jupyter Notebooks and includes:

- exploratory data analysis
- dataset visualization
- preprocessing and augmentation
- CNN training
- model evaluation
- confusion matrix generation
- prediction analysis

---

# Project Overview

This project focuses on image classification for autonomous driving applications.

The goal is to classify German traffic signs into 43 different categories using deep learning techniques.

The workflow includes:

- loading and visualizing the GTSRB dataset
- preprocessing traffic sign images
- training a CNN model
- evaluating classification accuracy
- generating confusion matrices
- comparing results with literature

The project achieved a test accuracy of:

```text
95.67%
```

which places the model close to results reported in literature benchmarks. :contentReference[oaicite:0]{index=0}

---

# Dataset

The project uses the:

## German Traffic Sign Recognition Benchmark (GTSRB)

Dataset link:

[GTSRB Dataset](https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/published-archive.html?utm_source=chatgpt.com)

The dataset contains:

- 51,838 traffic sign images
- 43 traffic sign classes
- training and test datasets

The dataset was created for traffic sign recognition research and autonomous driving applications. :contentReference[oaicite:2]{index=2}
---

# Dataset Notice

⚠️ The original GTSRB image dataset is not included in this repository because the dataset is too large for GitHub.

The notebook expects the training images to be located inside:

```text
Final_Training/Images
```

as referenced at the beginning of the data loading section in the notebook.

The datasets can be downloaded from the official RUB (Ruhr University Bochum) archive:

[GTSRB Official Dataset Archive (RUB)](https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/published-archive.html?utm_source=chatgpt.com)

The following datasets were used in this project:

- `GTSRB_Final_Training_Images.zip`
- `GTSRB_Final_Test_Images.zip`

After downloading, extract the datasets and place the folders in the project directory so that the notebook can correctly load the images.

---

# Features

- Traffic sign image classification
- Convolutional Neural Network (CNN)
- Exploratory Data Analysis (EDA)
- Data Augmentation
- Image normalization
- Accuracy and loss visualization
- Confusion matrix generation
- Prediction confidence analysis
- Literature comparison

---

# Project Structure

```text
.
├── classificationWithCNN - final.ipynb
├── functions.py
├── Bericht.pdf
├── Aufgabenstellung_v02.pdf
└── README.md
```

Additional dataset folders:

```text
110m_cultural/
images/
ne_110m_admin_0_countries/
shapefiles/
```

---

# Exploratory Data Analysis

The project includes extensive analysis and visualization of the dataset:

- class distribution analysis
- dataset imbalance investigation
- visualization of all 43 traffic sign classes
- training/validation split analysis

The analysis shows that some classes contain significantly fewer images than others, which may affect model generalization. :contentReference[oaicite:3]{index=3}

---

# Data Preprocessing

The preprocessing pipeline includes:

- image normalization (`1./255`)
- image rotation
- zoom augmentation
- shear transformations
- train/validation split
- batch processing

Implemented using:

```python
ImageDataGenerator
```

The preprocessing and graph plotting utilities are implemented inside:

```text
functions.py
```

:contentReference[oaicite:4]{index=4}

---

# CNN Architecture

The classifier is based on a Convolutional Neural Network.

## Architecture

- Conv2D (128 filters)
- MaxPooling2D

- Conv2D (256 filters)
- MaxPooling2D

- Conv2D (512 filters)
- MaxPooling2D

- Flatten
- Dense Layer (512 neurons)
- Softmax Output Layer (43 classes)

The model uses:

- ReLU activation
- Adam optimizer
- Categorical Crossentropy loss

The CNN architecture was specifically designed for traffic sign image classification. :contentReference[oaicite:5]{index=5}

---

# Training

The model was trained for:

```text
25 epochs
```

The training workflow includes:

- training accuracy tracking
- validation accuracy tracking
- loss visualization
- convergence analysis

The project demonstrates strong convergence between training and validation curves, indicating good generalization performance. :contentReference[oaicite:6]{index=6}

---

# Model Evaluation

The evaluation pipeline includes:

- prediction generation
- confidence analysis
- confusion matrix computation
- misclassification analysis

Final test accuracy:

```text
95.67%
```

The confusion matrix highlights misclassified traffic sign classes and class similarities. :contentReference[oaicite:7]{index=7}

---

# Comparison with Literature

The project compares the achieved results with benchmark literature results from GTSRB research.

The achieved accuracy is competitive with several traditional approaches and demonstrates strong CNN classification performance. :contentReference[oaicite:8]{index=8}

---

# Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook

---

# Concepts Explored

- Computer Vision
- Convolutional Neural Networks (CNN)
- Traffic Sign Recognition
- Image Classification
- Data Augmentation
- Deep Learning
- Autonomous Driving
- Confusion Matrix Analysis

---

# Author

Kalil Sacko

Master Student in Computer Science  
Hochschule Bochum

---

# Notes

- The project was developed in the context of Computer Vision for Autonomous Driving.
- Most of the workflow was implemented directly inside Jupyter Notebooks.
- The project includes both technical implementation and scientific analysis/reporting.
- The report compares the model performance with literature benchmarks from GTSRB-related research.
