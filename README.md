# 🫀 Heart Disease Risk Predictor

A clean, interactive web app that uses Machine Learning to estimate the risk of heart disease based on everyday clinical health metrics.

🔗 **Live App:** [Try the Heart Disease Predictor here!](https://heart-disease-predictor-ndkjnszjecbvsz5gggpa2a.streamlit.app/)


## 💡 About The Project

I built this project to bridge the gap between Machine Learning models and simple, usable tools. Instead of leaving a trained model buried in a Google Colab notebook, I turned it into a full end-to-end web app using **Streamlit** and **Scikit-Learn**.

Anyone can plug in patient health values—like cholesterol, blood pressure, or max heart rate—and get an instant, easy-to-understand risk assessment.

---

## ✨ Key Features

* **Instant Risk Assessment:** Evaluates 13 key clinical parameters in real-time.
* **Simple & Intuitive UI:** Built with Streamlit so anyone can test scenarios without needing technical knowledge.
* **Lightweight & Fast:** Runs on a trained Random Forest model hosted seamlessly on Streamlit Cloud.

---

## 🛠️ Tech Stack & Tools

* **Language:** Python 3
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Frontend / Framework:** Streamlit
* **Deployment:** Streamlit Cloud & GitHub

---

## 📊 Parameters Used

The app takes the following inputs to make its prediction:

* **Basic Info:** Age, Sex
* **Vitals & Labs:** Resting BP, Serum Cholesterol, Fasting Blood Sugar
* **Cardiac Indicators:** Chest Pain Type, Max Heart Rate, Exercise-Induced Angina, ST Depression, Slope, Major Vessels, and Thalassemia status.

---

## 💻 Running Locally

Want to test or modify the code on your own machine?

```bash
git clone [https://github.com/abdul-pk268/heart-disease-predictor.git](https://github.com/abdul-pk268/heart-disease-predictor.git) && cd heart-disease-predictor && pip install -r requirements.txt && streamlit run app.py
