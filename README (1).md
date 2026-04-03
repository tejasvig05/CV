# 🌾 Crop Recommendation System

A beginner-friendly Machine Learning project that recommends the most suitable crops to grow based on soil nutrients and local weather conditions — built with Python and scikit-learn.

---

## 📌 The Problem

Farmers in India and across the world often rely on guesswork or tradition to decide which crop to grow. Planting the wrong crop for the local soil and climate leads to poor yields, financial loss, and wasted resources. With basic soil test data and weather information, a data-driven recommendation can make a meaningful difference.

## 💡 The Solution

This project trains a **Random Forest classifier** on soil (N, P, K, pH) and weather (temperature, humidity, rainfall) data to predict which crop will thrive best. It supports **11 common crops** and gives the top 3 recommendations with confidence scores.

---

## 🗂️ Project Structure

```
crop-recommendation-system/
│
├── app.py                  # Interactive CLI — run this to get recommendations
├── requirements.txt        # Python dependencies
│
├── src/
│   └── model.py            # Dataset generation, model training, prediction logic
│
├── notebooks/
│   └── eda.py              # Exploratory Data Analysis — generates charts
│
├── data/
│   └── crop_data.csv       # Auto-generated dataset (created on first run)
│
└── reports/
    └── figures/            # EDA charts saved here
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/crop-recommendation-system.git
cd crop-recommendation-system
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### ▶️ Get a Crop Recommendation (main app)
```bash
python app.py
```
You will be prompted to enter:
| Input | Description | Example |
|---|---|---|
| N | Nitrogen content (kg/ha) | 90 |
| P | Phosphorus content (kg/ha) | 42 |
| K | Potassium content (kg/ha) | 43 |
| Temperature | In degrees Celsius | 20 |
| Humidity | In percentage | 82 |
| pH | Soil pH level | 6.5 |
| Rainfall | In mm | 200 |

The app prints the **top 3 recommended crops** with confidence scores, growing season, and a farming tip.

---

### 📊 Run Exploratory Data Analysis
```bash
python notebooks/eda.py
```
Saves 5 charts to `reports/figures/`:
- Crop distribution
- Feature distributions
- Average NPK per crop
- Correlation heatmap
- Rainfall & temperature boxplots

---

### 🧪 Train & Test the Model Directly
```bash
python src/model.py
```
Trains the model, prints accuracy and a classification report, then runs a sample prediction.

---

## 🌱 Supported Crops

| Crop | Season | Key Condition |
|---|---|---|
| Rice | Kharif | High humidity + rainfall |
| Wheat | Rabi | Cool & dry |
| Maize | Kharif | Moderate rainfall |
| Chickpea | Rabi | Drought-tolerant |
| Kidney Beans | Kharif | Well-drained soil |
| Pigeon Peas | Kharif | Semi-arid regions |
| Moth Beans | Kharif | Very drought-resistant |
| Mung Bean | Zaid | Short-duration crop |
| Black Gram | Kharif | Black cotton soil |
| Lentil | Rabi | Nitrogen-fixing |
| Cotton | Kharif | Deep black soil |

---

## 📈 Model Details

| Property | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Number of trees | 100 |
| Train/Test split | 80% / 20% |
| Features | N, P, K, Temperature, Humidity, pH, Rainfall |
| Typical accuracy | ~95–98% |

---

## 🧠 What I Learned

- How to frame a real-world problem as a classification task
- Data generation and exploratory data analysis with pandas & matplotlib
- Training and evaluating a Random Forest model with scikit-learn
- Saving and loading models with pickle
- Building a user-friendly CLI interface in Python

---

## 📄 License

MIT License — free to use, modify, and share.
