# 🩺 Heart Failure Detection using Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Framework-Flask-green?logo=flask" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter" />
  <img src="https://img.shields.io/badge/ML-Classification-yellow?logo=scikitlearn" />
</p>

## 📖 Overview
This project is a **Machine Learning-based system** for predicting the likelihood of **heart failure**.  
It uses patient health records and applies different ML models to provide early diagnosis support.

🚀 The final application is deployed using **Flask** with a simple **web interface**.

---

## ✨ Features
- ✅ Data preprocessing (cleaning, null-value handling, encoding, scaling)  
- ✅ Multiple ML models trained & compared  
- ✅ Best accuracy achieved: **86% with Decision Tree**  
- ✅ Saved model (`ml_model.pkl`) for real-time predictions  
- ✅ Flask-based web app with interactive UI  

---

## 📂 Project Structure
Heart_Failure_Detection/  
│  
├── data/   
│ ├── heart_failure.csv # Raw dataset  
│ ├── cleaned_data.csv # Preprocessed dataset  
│  
├── notebooks/ # Model building & analysis  
│ ├── Logistic_Regression.ipynb  
│ ├── SVM.ipynb  
│ ├── KNN.ipynb  
│ ├── DecisionTree.ipynb  
│ ├── Random_Forest.ipynb  
│ ├── Ada_Boost.ipynb  
│  
├── models/  
│ └── ml_model.pkl # Saved trained model  
│  
├── app/  
│ ├── app.py # Flask backend  
│ ├── templates/  
│ │ └── index.html # Frontend UI  
│  
├── requirements.txt # Dependencies  
└── README.md # Documentation  


---

## ⚙️ Installation & Usage

```bash
# Clone this repository
git clone https://github.com/D-Neeraja/Heart_Failure_Detection.git
cd Heart_Failure_Detection

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app/app.py
```

🔗 Open the app in browser at: http://127.0.0.1:5000/

📊 Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 82%      |
| SVM                 | 84%      |
| KNN                 | 83%      |
| Decision Tree       | **86%**  |
| Random Forest       | 85%      |
| AdaBoost            | 84%      |

🚀 Future Improvements

🔹 Implement PCA for dimensionality reduction
🔹 Try XGBoost / LightGBM for boosting
🔹 Deploy on Streamlit / FastAPI for better UI
🔹 Cloud deployment (Heroku, AWS, etc.)

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

📌 Author

👩‍💻 **Neeraja D**  
[LinkedIn](https://www.linkedin.com/in/neerajadakkata) | [GitHub](https://github.com/D-Neeraja)

