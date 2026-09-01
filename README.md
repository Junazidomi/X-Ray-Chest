# X-RAY Chest Prediction

## Description
## Objectives
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

     <img src="" width="350"/>
   - Normal Prediction 2
   - Pneumonia Prediction 1
   - Pneumonia Prediction 2
   - Pneumonia Prediction 3
     
     
   - Pneumonia Prediction
## Evaluation
