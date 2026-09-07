# X-RAY Chest Prediction

## Description

As technology advances quickly, the need for fast and efficient processes continues to grow, particularly in the healthcare sector. X-Ray prediction is an artificial intelligence-based feature designed to assist with analysis and prediction based on X-ray images. This system utilizes a CNN (Convolutional Neural Network) algorithm to recognize patterns and charateristics in radiographic images and classify them into two categories: normal lungs and lungs showing signs of pneumonia.

This feature aims to support the screening and analysis of X-ray images more quickly and efficiently. The prediction results serve as supporting information and are not intended to replace diagnoes or medical decisions made by healthcare professionals.

## Objectives

The objective of this project is
- Develop a CNN model to classify X-Ray Images of Pneumonia and Normal conditions.
- Perform data preprocessing and augmentation to make the model more powerful.
- Train the model with Tensorflow/Keras.
- Evaluate the model's performance using various evaluation metrics.
- Make predictions on new images that the model has never seen before
  
## Features

The feature of thsi project is:

- Dataset Preprocessing
- Data Augmentation
- CNN Image Classification
- Model Training
- Model Evaluation
- Accuracy and Loss Visualization
- Confusion Matrix
- Classification Report
- Prediction on a custom images
- Saved trained model (model.h5)
  
## Project Structure

The following is the project structure

```text
  X-Ray-Chest/
│
├── API/
│   └── kaggle.json
│
├── Model/
│   └── model.h5
│
├── Output/
│   ├── Accuracy Plot.png
|   ├── Loss Plot.png
│   ├── Confusion Matrix.png
│   ├── Normal Test 1.png
│   ├── Normal Test 2.png
│   ├── Pneumonia Test 1.png
│   ├── Pneumonia Test 2.png
|   └── Pneumonia Test 3.png
|
├── src/
│   ├── augmentated.py
│   ├── data_load.py
│   ├── model.py
│   ├── predictiion.py
│   └── train.py
│
├── Testing/
│   ├── Normal 1.jpeg
│   ├── Normal.jpeg
|   ├── Pneumonia 1.jpeg
|   ├── Pneumonia.jpeg
│   └── Pneumonia_2.jpeg
|
├── Notebook.ipynb
└──requirements.txt
```
## Installation

1. Clone Repository

   ```
      git clone https://github.com/Junazidomi/X-Ray-Chest.git
      cd X-Ray-Chest
   ```
   
2. Create Virtual Envirotment (Optional)

   Windows

   ```
      python -m venv venv
      venv\Scripts\activate
   ```

   Linux/MacOS

    ```
      python3 -m venv venv
      source venv/bin/activate
    ```
    
3. Install Dependencies

   ```
     pip install -r requirements.txt
   ```
   
4. Configure Kaggle API

   Download the kaggle.json from your Kaggle Account, then save it to the following folder:

   ```
     API/
     └── kaggle.json
   ```
   
5. Run The Notebook
   
   Open `Notebook.ipynb` using Jupyter Notebook, JupyterLab, or Visual Studio Code, then run all cells sequentially.

   The notebook will automatically:
    
    - Download the dataset from Kaggle.
    - Preprocess and augment the data.
    - Build and train the CNN model.
    - Evaluate the trained model.
   
## Model Architecture

The architecture model in this project is

```
                 Input (150×150×3)
                          │
                          ▼
                  Conv2D (32, 3×3)
                          │
                  Conv2D (32, 3×3)
                          │
                  BatchNormalization
                          │
                     MaxPooling2D
                          │
                     Dropout (0.3)
                          │
                          ▼
                  Conv2D (64, 5×5)
                          │
                  Conv2D (64, 5×5)
                          │
                  BatchNormalization
                          │
                    MaxPooling2D
                          │
                    Dropout (0.3)
                          │
                          ▼
                  Conv2D (128, 7×7)
                          │
                  Conv2D (128, 7×7)
                          │
                  BatchNormalization
                          │
                     MaxPooling2D
                          │
                     Dropout (0.3)
                          │
                          ▼
                       Flatten
                          │
                     Dense (256)
                          │
                    Dropout (0.3)
                          │
                     Dense (128)
                          │
                    Dropout (0.5)
                          │
                      Dense (1)
                          │
                       Sigmoid

```

### Training Configuration

|      Parameter      |         Value       |
|---------------------|---------------------|
| Activation Function | Relu, Softmax       |
| Optimizer           | RMSProp             |
| Loss Function       | Binary Crossentropy |
| Evaluation Metric   | Accuracy            |

## Result

Following  the training process, the model achieved the following performance:

### Training Process

|           Metric          |    Value    |
|---------------------------|-------------|
| Final Training Loss       |    0.1575   |
| Final Training Accuracy   |    0.9525   |
| Final Validation Loss     |    0.2471   |
| Final Validation Accuracy |    0.9057   |

### Model Evaluation

|    Dataset   |  Accuracy  |   Loss   |
|--------------|------------|----------|
| Training Set |   0.9628   | 0.0925   |
| Testing Set  |   0.9563   | 0.1047   |

### Classification Report

|    Class   |    precision    |    recall   |   f1-score   |
|------------|-----------------|-------------|--------------|
| NORMAL     |       0.93      |     0.98    |     0.96     |
| PNEUMONIA  |       0.98      |     0.93    |     0.96     |

## Metric Evaluation

Below is a visualization of the results:

1. Accuracy Plot

   <img src="https://raw.githubusercontent.com/Junazidomi/X-Ray-Chest/refs/heads/main/Output/Accuracy%20Plot.png" width="350"/>
   
2. Loss Plot

   <img src="https://raw.githubusercontent.com/Junazidomi/X-Ray-Chest/refs/heads/main/Output/Loss%20Plot.png" width="350"/>
   
3. Confusion Matrix

   <img src="https://raw.githubusercontent.com/Junazidomi/X-Ray-Chest/refs/heads/main/Output/Confusion%20Matrix.png" width="350"/>
5. Sample Predictions
   - Normal Prediction 1

     <img src="https://raw.githubusercontent.com/Junazidomi/X-Ray-Chest/refs/heads/main/Output/Normal_Prediction_1.png" width="350"/>
     
   - Normal Prediction 2

     <img src="https://raw.githubusercontent.com/Junazidomi/X-Ray-Chest/refs/heads/main/Output/Normal_Prediction_2.png" width="350"/>
     
   - Pneumonia Prediction 1

     <img src="https://raw.githubusercontent.com/Junazidomi/X-Ray-Chest/refs/heads/main/Output/Pneumonia_Prediction_1.png" width="350"/>
     
   - Pneumonia Prediction 2

     <img src="https://raw.githubusercontent.com/Junazidomi/X-Ray-Chest/refs/heads/main/Output/Pneumonia_Prediction_2.png" width="350"/>
     
   - Pneumonia Prediction 3

     <img src="https://raw.githubusercontent.com/Junazidomi/X-Ray-Chest/refs/heads/main/Output/Pneumonia_Prediction_3.png" width="350"/>
     
## Evaluation
