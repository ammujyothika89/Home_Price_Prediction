# 🏠 HomeLens AI — House Price Prediction

<div align="center">

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://homelens-price-prediction.onrender.com)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0.3-orange?style=for-the-badge&logo=xgboost&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.3-black?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.5.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An end-to-end machine learning web application that predicts residential property prices across 6 major Indian cities using XGBoost regression.**

[🚀 Live Demo](https://homelens-price-prediction.onrender.com) · [📊 Model Performance](#-model-performance) · [🛠 Tech Stack](#-tech-stack) · [📁 Project Structure](#-project-structure)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Model Performance](#-model-performance)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [How It Works](#-how-it-works)
- [Dataset](#-dataset)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

**HomeLens AI** is a complete machine learning project that predicts house prices using an XGBoost regression model. The project covers the full data science lifecycle:

> **Data Generation → EDA → Feature Engineering → Model Training → Evaluation → Deployment (Flask Web App)**

The web interface allows users to enter property details and receive an instant price prediction powered by the trained model — not a simulation, but a real ML inference call.

---

## ✨ Features

- 🤖 **XGBoost Regression Model** — trained on 10,000+ property records across 6 Indian cities
- 📊 **Automated EDA** — generates correlation heatmaps, price distributions, and feature charts
- 🌐 **Flask Web App** — professional multi-section website with live prediction API
- 📈 **Real Metrics** — R², RMSE, MAPE, and cross-validation scores displayed on the site
- 🎨 **Internship-level UI** — float-up animations, responsive design, dark hero section
- 🔄 **One Notebook Workflow** — run 5 cells and the entire project is built automatically
- 📦 **Reproducible** — everything from data to deployment in a single Jupyter notebook

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **R² Score** | 0.92 |
| **MAPE** | ~3.2% |
| **RMSE** | ~₹1.18 Lakh |
| **Within 5% of actual** | ~89% |
| **Cross-validation** | 5-Fold |
| **Training samples** | 8,000 |
| **Test samples** | 2,000 |
| **Total features** | 12 |

### Algorithm Comparison

| Algorithm | R² Score |
|-----------|----------|
| **XGBoost** ✅ | **0.92** |
| Gradient Boosting | 0.89 |
| Random Forest | 0.85 |
| Linear Regression | 0.72 |
| Decision Tree | 0.65 |

> XGBoost was selected as the final model after benchmarking 5 algorithms.

---

## 🛠 Tech Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.9+ |
| **ML Framework** | XGBoost, Scikit-learn |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Web Backend** | Flask, Flask-CORS |
| **Frontend** | HTML5, CSS3, Vanilla JS |
| **Model Persistence** | Joblib |
| **Development** | Jupyter Notebook, VSCode |

---

## 📁 Project Structure

```
HOUSE_PRICE_PREDICTION/
│
├── 📓 House_Price_Prediction.ipynb   # Main notebook — run this
│
├── 🐍 app.py                          # Flask web server + /predict API
│
├── 📋 requirements.txt                # Python dependencies
├── 📄 README.md                       # This file
│
├── 📂 data/
│   └── house_prices.csv              # Generated dataset (10,000 rows)
│
├── 📂 model/
│   ├── xgb_model.pkl                 # Trained XGBoost model
│   ├── le_city.pkl                   # City label encoder
│   ├── le_loc.pkl                    # Locality label encoder
│   ├── le_furnish.pkl                # Furnishing label encoder
│   ├── features.pkl                  # Feature list
│   └── meta.json                     # Model metrics (R², RMSE, MAPE…)
│
├── 📂 templates/
│   └── index.html                    # Full website HTML (Jinja2)
│
└── 📂 static/
    ├── css/
    │   └── style.css                 # All website styles
    └── images/
        ├── eda.png                   # EDA plots (auto-generated)
        └── model_analysis.png        # Feature importance + Actual vs Predicted
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- VSCode with Jupyter extension  
- Git (optional)

### Step 1 — Clone or Download

```bash
# Option A: Clone
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction

# Option B: Download ZIP and extract
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Open in VSCode

```bash
code .
```

Open `House_Price_Prediction.ipynb` in VSCode.

### Step 4 — Run the Notebook

Run all 5 cells **in order**:

| Cell | Action |
|------|--------|
| Cell 1 | Installs all packages |
| Cell 2 | Generates dataset, trains model, saves artefacts, creates plots |
| Cell 3 | Writes `app.py` (Flask backend) |
| Cell 4 | Writes `index.html` + `style.css` |
| Cell 5 | **Launches the website** → opens http://127.0.0.1:5000 |

### Step 5 — Open the Website

The browser opens automatically. If not, go to:

```
http://127.0.0.1:5000
```

> **To stop the server:** `Kernel → Interrupt Kernel` in VSCode

---

## ⚙️ How It Works

```
User Input (12 features)
        │
        ▼
  Label Encoding
  (City, Locality, Furnishing → numeric)
        │
        ▼
  XGBoost Inference
  (400 estimators, depth=7, lr=0.05)
        │
        ▼
  Predicted Price + Confidence Range (±3.2%)
        │
        ▼
  Flask /predict API → JSON response → UI
```

### Input Features

| Feature | Type | Description |
|---------|------|-------------|
| `city` | Categorical | One of 6 major Indian cities |
| `locality` | Categorical | Neighbourhood within the city |
| `area_sqft` | Numeric | Built-up area in square feet |
| `bhk` | Numeric | Number of bedrooms (1–5) |
| `bathrooms` | Numeric | Number of bathrooms |
| `age_years` | Numeric | Age of property in years |
| `floor` | Numeric | Floor number |
| `total_floors` | Numeric | Total floors in building |
| `furnishing` | Categorical | Unfurnished / Semi / Fully |
| `parking` | Binary | Parking available (0/1) |
| `gym` | Binary | Gym available (0/1) |
| `pool` | Binary | Swimming pool available (0/1) |

---

## 📂 Dataset

The dataset is synthetically generated to represent the Indian residential real estate market across:

**Cities covered:** Bangalore · Mumbai · Hyderabad · Chennai · Pune · Delhi NCR

**Size:** 10,000 records · 13 columns  
**Price range:** ₹5 Lakh — ₹10 Crore  
**Train/Test split:** 80% / 20%

> Price generation is based on realistic per-sqft rates for each city, adjusted by amenities, age, floor, and furnishing — with Gaussian noise to simulate real-world variance.

---

## 🌐 Website Sections

| Section | Description |
|---------|-------------|
| **Hero** | Animated landing with live metrics card |
| **About** | What the model is + EDA charts from your data |
| **Accuracy** | Real R², MAPE, RMSE + animated bar chart vs baselines |
| **Why Trust Us** | 6 trust pillars — data, testing, transparency |
| **How It Works** | 4-step pipeline diagram |
| **Try the Model** | Live prediction form → real Flask API call |
| **Contact** | Contact info + message form |
| **Footer** | LinkedIn & GitHub icons, nav links |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📬 Contact

**Your Name**  
📧 yourname@email.com  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile)  
🐙 [GitHub](https://github.com/yourusername)  
📍 Andhra Pradesh, India

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ using Python, XGBoost & Flask

</div>
