# 🚦 Mumbai Traffic Congestion Prediction System

This project predicts traffic congestion levels in Mumbai using machine learning and visualizes routes and congestion zones on an interactive map. The solution supports urban planning teams, commuters, and traffic control systems with predictive insights.

---

## 🎯 Objectives
- Predict traffic congestion using ML models
- Identify peak congestion hours and high-risk locations
- Provide map-based route visualization with congestion markers
- Support smart city planning and route optimization

---

## 🧠 Tech Stack
| Component | Technology |
|----------|------------|
| Model Training | Python (Scikit-Learn, NumPy, Pandas) |
| Dashboard & API | Flask |
| Map Visualization | Leaflet.js, HTML |
| Notebook | Google Colab |
| Documentation | Research Report (PDF) |

---

## 🔬 Machine Learning Workflow
- Data preprocessing & feature engineering  
- Model training using **Random Forest, Gradient Boosting**
- Hyperparameter tuning for improved accuracy  
- Prediction of congestion level (Low, Medium, High)

✔ Achieved improved accuracy using **custom feature engineering** and boosted ensemble methods.

---

## 🗺 Interactive Visualization
The project includes a web application (Flask + Leaflet.js) to:
- Display routes on Mumbai map
- Highlight high congestion areas
- Provide congestion predictions for different routes

🔗 File: `map_with_routes.html`  
🔗 Flask Application: `app.py`

---

## 📁 Project Files
| File | Description |
|------|-------------|
| `Research_Project.ipynb` | ML model training notebook |
| `app.py` | Flask API & backend |
| `map_with_routes.html` | Front-end interactive traffic map |
| `Research_Report.pdf` | Full documentation & findings |

---

## 📌 How to Run the Project

### ▶️ Install Dependencies
- pip install flask pandas numpy scikit-learn
- python app.py
- http://127.0.0.1:5000/map
