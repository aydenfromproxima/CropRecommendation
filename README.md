#  Crop Recommendation System

A machine learning-based web application that recommends the most suitable crop to cultivate based on soil nutrients and environmental conditions. Built using Random Forest and deployed with Streamlit, this project focuses on both predictive accuracy and practical usability.

---

##  Overview

This system predicts the best crop to grow using key agricultural parameters such as soil composition, temperature, humidity, pH, and rainfall. Instead of returning a single rigid answer, the application provides the **top 3 recommended crops with confidence scores**, making it more aligned with real-world agricultural decision-making.

---

##  Key Features

* High accuracy multi-class classification model (~99%)
* Cross-validation to ensure generalization (no overfitting)
* Clean and intuitive user interface
* Top 3 crop recommendations instead of a single output
* Real-time predictions using trained ML model
* Structured input sections (Soil + Environment)

---

##  Dataset Information

The dataset contains agricultural data used to determine optimal crop conditions.

### Features:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH
* Rainfall

### Target:

* Crop label (multi-class classification with ~22 crops)

---

##  Machine Learning Model

* Algorithm: Random Forest Classifier
* Problem Type: Multi-class classification
* Evaluation:

  * Test Accuracy ≈ 99%
  * Cross-validation Accuracy ≈ 99%

### Why Random Forest?

* Handles non-linear relationships effectively
* Works well with tabular agricultural data
* Provides stable and consistent performance
* Requires minimal preprocessing

---

##  Prediction Logic

The model predicts probabilities for all crops and returns:

* Top 1 → Most suitable crop
* Top 2 → Alternative option
* Top 3 → Additional viable option

This approach reflects real-world farming decisions where multiple crops may be suitable under similar conditions.

---

##  User Interface Design

The interface is structured into two main sections:

###  Soil Nutrients

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)

###  Environmental Conditions

* Temperature
* Humidity
* pH
* Rainfall

Each input includes guidance to ensure accurate data entry.

---

##  Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Joblib

---

##  Deployment

The application is deployed using Streamlit Cloud and runs entirely in the browser, allowing users to interact with the model in real time.

---

## 💻 How to Run Locally

Follow these steps to run the project on your system:
 1. Clone the Repository
```
git clone https://github.com/aydenfromproxima/CropRecommendation.git
```
cd CropRecommendation

 2. Install Dependencies

Make sure Python is installed, then run:

pip install -r requirements.txt

 3. Ensure Model Files Exist

Make sure the following files are present in the project directory:

* crop_model.pkl
* label_encoder.pkl

If not, generate them by running:

python train_model.py

 4. Run the Streamlit App

streamlit run app.py

 5. Open in Browser

After running the command, Streamlit will provide a local URL.
Open it in your browser to use the application.

---

##  Future Improvements

* Add visualization of feature importance
* Integrate real-time weather API for automatic inputs
* Improve model with advanced algorithms (XGBoost, LightGBM)
* Add location-based recommendations
* Mobile-friendly UI improvements

---

##  Disclaimer

This application is intended for educational purposes only. Actual crop selection should consider additional real-world factors such as soil testing, regional climate, and expert agricultural advice.

---

##  Support

If you found this project useful, consider giving it a star and sharing it.
