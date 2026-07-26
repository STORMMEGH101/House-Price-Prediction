# 🏠 Bangalore House Price Prediction using Machine Learning

A Machine Learning web application that predicts the estimated price of residential properties in Bangalore based on user inputs such as location, total square footage, number of bedrooms (BHK), and bathrooms. The application is built with **Python**, **Scikit-learn**, and **Streamlit** to provide an interactive and user-friendly interface.

---

## 🚀 Features

- Predict house prices instantly using a trained Machine Learning model.
- Interactive Streamlit interface.
- Select property location from available locations.
- Enter total area, number of BHK, and bathrooms.
- Fast and accurate predictions using a trained regression model.
- Clean and responsive user interface.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data preprocessing and analysis |
| NumPy | Numerical computations |
| Scikit-learn | Machine Learning model training |
| Streamlit | Web application development |
| Pickle | Saving and loading the trained model |

---

## 📂 Project Structure

```
House-Price-Prediction/
│
├── app.py
├── artifacts/
│   ├── banglore_home_prices_model.pickle
│   └── columns.json
├── model/
│   ├── Bangalore_House_Data.csv
│   └── House_Price_Prediction.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Machine Learning Workflow

### 1. Data Collection
- Collected the Bangalore House Price dataset.

### 2. Data Preprocessing
- Removed unnecessary columns.
- Handled missing values.
- Converted range values (such as "2100-2850") into numerical values.
- Removed outliers using statistical methods.
- Standardized location names.

### 3. Feature Engineering
- Created the **price per square foot** feature.
- Applied **One-Hot Encoding** to convert location names into numerical features.

### 4. Model Training
- Split the dataset into training and testing sets.
- Trained a **Linear Regression** model.
- Evaluated the model using performance metrics.

### 5. Model Serialization
- Saved the trained model using **Pickle**.
- Saved feature columns in **columns.json** for deployment.

### 6. Deployment
- Built an interactive web application using **Streamlit**.
- Loaded the trained model and generated real-time predictions.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/STORMMEGH101/House-Price-Prediction.git
```

Navigate to the project folder:

```bash
cd House-Price-Prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

- Improve UI design.
- Add interactive charts and analytics.
- Deploy the application online using Streamlit Community Cloud.
- Improve prediction accuracy using advanced regression models.
- Add support for additional property features.
----------------------------------------------------------------------------------------------------------------
