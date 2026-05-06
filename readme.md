# Titanic Survival Predictor

This is a simple Machine Learning web application built with Streamlit that predicts whether a passenger survived the Titanic disaster.

## Features

- Predict survival using:
  - Support Vector Classifier (SVC)
  - Random Forest
  - Decision Tree
- User-friendly Streamlit interface
- Real-time prediction

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- NumPy
- Pickle

## Files Required

Make sure the following files are in the same directory:

- `app.py`
- `svc_model.pkl`
- `rf_model.pkl`
- `dt_model.pkl`
- `scaler.pkl`

## Installation

1. Clone the repository or download the files.

2. Install the required libraries:

```bash
pip install streamlit scikit-learn numpy
```

## Run the Application

Use the following command in the terminal:

```bash
streamlit run app.py
```

## How to Use

1. Select a machine learning model.
2. Enter passenger details:
   - Passenger Class
   - Sex
   - Age
   - Fare
3. Click the **Predict** button.
4. The app will display whether the passenger survived or not.

## Example

Input:
- Passenger Class: 1
- Sex: Female
- Age: 30
- Fare: 100

Output:
- Survived

