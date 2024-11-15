# Diamond Price Prediction

## Project Overview
This project is focused on predicting the price of diamonds based on various features such as carat, cut, color, clarity, and other physical characteristics. By applying machine learning techniques, we aim to build a predictive model that accurately estimates diamond prices, assisting in valuation and decision-making for buyers and sellers.


## Dataset
The dataset used in this project contains various features related to diamond quality and characteristics, which impact the diamond's market price. The main columns include:

- `carat`: Weight of the diamond
- `cut`: Quality of the diamond cut (Fair, Good, Very Good, Premium, Ideal)
- `color`: Diamond color grading (D through J, where D is the best)
- `clarity`: Clarity grading (IF, VVS1, VVS2, VS1, VS2, SI1, SI2)
- `depth`: Total depth percentage
- `table`: Width of the top of the diamond
- `x`, `y`, `z`: Dimensions of the diamond (length, width, depth)

## Project Steps

### 1. Data Preprocessing
- **Cleaning**: Handle any missing or erroneous data.
- **Feature Encoding**: Transform categorical variables (`cut`, `color`, `clarity`) into numerical representations.
- **Scaling**: Standardize or normalize numerical features as needed.

### 2. Exploratory Data Analysis (EDA)
- **Visualization**: Explore relationships between features and target variable (price).
- **Statistical Analysis**: Identify key factors impacting diamond prices.

### 3. Feature Engineering
- **New Features**: Creation of derived features, if necessary.
- **Feature Selection**: Select features based on correlation analysis, feature importance, and domain knowledge.

### 4. Model Building
We tested several models to find the one that best predicts diamond prices:
- **Linear Regression**
- **Ridge Regression**
- **Lasso Regression**
- **ElasticNet Regression**

The best-performing model based on evaluation metrics was selected for deployment.

### 5. Model Evaluation
- **Metrics Used**: Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared score (R²).
- **Cross-Validation**: Evaluate model stability with cross-validation.

### 6. Experiment Tracking with MLflow
MLflow is used to track experiments, logging each model's parameters and performance metrics for easy comparison.
- Start the MLflow server:
  `mlflow ui`

### 7.DVC (Data Version Control) is used for versioning datasets and managing the model training pipeline.

  1.Initialize DVC:
    `dvc init`
  2.Add the dataset to DVC:
    `dvc add data/diamonds.csv`

  3.Create a pipeline in dvc.yaml to automate preprocessing, training, and evaluation steps.

  4.Run the pipeline:
    dvc repro

  5.Track the DVC pipeline file and other DVC changes in Git:
    `git add dvc.yaml data/diamonds.csv.dvc`
    `git commit -m "Add data and pipeline setup with DVC"`


Best Model: Linear Regression
Performance: Achieved a R² score of approximately 0.94 , indicating that our model accurately predicts diamond prices within a reasonable error margin.


# Installation
1.Clone the repository:
  `git clone https://github.com/BhaveshNikam09/Piamond_Price_Prediction.git`

2.Navigate to the project directory:
   `cd DiamondPricePrediction`

3.Install dependencies:
   `pip install -r requirements.txt`


# Usage
1.Run the DVC pipeline:
  `dvc repro`

2.Run the model training script:
  `python src\DiamondPricePrediction\pipelines\training_pipeline.py`

3.Start the web app for predictions:
   `python app.py`

## Open a web browser and go to http://localhost:5000 to access the model prediction interface.

