# Project Report
## Crop Recommendation System
### BYOP — Bring Your Own Project Submission

---

## 1. Problem Statement

Agriculture is the backbone of India's economy, supporting over 50% of its population. Yet many small and marginal farmers lack access to agronomic expertise when deciding which crop to sow each season. They often rely on what was grown the previous year, advice from neighbors, or instinct — without considering current soil health or local climate conditions.

Planting a crop ill-suited for the soil's nutrient profile or the region's rainfall pattern leads to:
- Low crop yield and financial loss
- Excessive use of fertilizers to compensate
- Soil degradation over time

**This project asks: Can a simple ML model, given basic soil and weather inputs, reliably suggest the best crop to grow?**

---

## 2. Why This Problem Matters

Soil testing is increasingly accessible (government schemes, private labs), but the gap lies in *interpreting* the results and translating them into a planting decision. A digital recommendation tool bridges this gap — it gives farmers (or agricultural extension workers) an objective, data-backed suggestion in seconds.

Even at a small scale — a student project used in a classroom demo, a mobile app for a village, or a dashboard for an NGO — the underlying idea has real social value.

---

## 3. Dataset

Since live soil-testing databases are not publicly available in a clean, labeled format for this scope, I generated a **synthetic dataset** based on published agronomic literature for 11 crops commonly grown in India.

Each crop was assigned a realistic range for:

| Feature | Description | Unit |
|---|---|---|
| N | Nitrogen content | kg/ha |
| P | Phosphorus content | kg/ha |
| K | Potassium content | kg/ha |
| Temperature | Average temperature | °C |
| Humidity | Relative humidity | % |
| pH | Soil acidity/alkalinity | 0–14 |
| Rainfall | Average annual rainfall | mm |

**Dataset size:** 2,200 samples (200 per crop), shuffled randomly.

The ranges were designed to be distinct enough per crop to make the classification learnable, while overlapping slightly to reflect real-world ambiguity.

---

## 4. Approach & Methodology

### Step 1 — Exploratory Data Analysis (EDA)
Before training any model, I visualized the dataset to understand:
- How many samples exist per crop (balanced distribution)
- The distribution shape of each feature (roughly uniform within ranges)
- Average N, P, K per crop (bar chart)
- Correlations between features (heatmap — mostly independent)
- Rainfall and temperature spread across crops (boxplots)

Key finding: NPK values are the most discriminating features between crops, followed by temperature and rainfall. pH and humidity add supplementary signal.

### Step 2 — Model Selection
For a beginner project, I chose **Random Forest** for several reasons:
- Works well with tabular data out-of-the-box
- Handles feature interactions without scaling
- Resistant to overfitting (ensemble of trees)
- Provides feature importance scores
- Easy to interpret

I did not use deep learning — the dataset size and task complexity don't justify it, and simpler models are easier to explain and debug.

### Step 3 — Training & Evaluation
- 80/20 train-test split with stratification (equal proportion of each crop in both sets)
- 100 decision trees in the forest
- Evaluated using accuracy, precision, recall, and F1-score per class

**Result:** The model achieves approximately **95–98% accuracy** on the test set, with high precision and recall across all 11 crops.

### Step 4 — Prediction Interface
I built an interactive CLI (`app.py`) that:
1. Auto-trains the model on first run (one-time setup)
2. Prompts the user to enter soil and weather values with input validation
3. Returns the top 3 recommended crops with confidence %, growing season, and a farming tip

---

## 5. Key Decisions

**Why synthetic data?**
Real labeled datasets combining soil NPK + GPS-linked weather + crop records are scarce and often proprietary. Synthetic data based on agronomic knowledge was a practical, transparent choice that still demonstrates the full ML pipeline.

**Why CLI over a web app?**
A command-line interface keeps the codebase simple and focused. The goal was to demonstrate the ML concepts cleanly, not to build a production product. Extending it to a Flask or Streamlit web app would be a natural next step.

**Why top 3 recommendations?**
Soil conditions in real life are never perfectly "ideal" for one crop. Giving 3 options with confidence scores respects this ambiguity and gives the farmer flexibility based on market conditions or preference.

---

## 6. Challenges Faced

| Challenge | How I Addressed It |
|---|---|
| No real-world labeled dataset available | Generated synthetic data from agronomic literature |
| Input validation in CLI | Used a while-loop with try/except to re-prompt invalid entries |
| Making EDA charts readable | Chose grouped bar charts for NPK comparison and boxplots for spread |
| Balancing simplicity vs. completeness | Kept model.py, app.py, and eda.py as separate files with clear responsibilities |

---

## 7. Results Summary

| Metric | Value |
|---|---|
| Model | Random Forest (100 trees) |
| Training samples | 1,760 (80%) |
| Test samples | 440 (20%) |
| Test Accuracy | ~96–98% |
| Crops supported | 11 |
| Prediction output | Top 3 crops + confidence |

---

## 8. What I Learned

- **Problem framing:** Translating a vague real-world issue ("farmers make uninformed decisions") into a concrete ML classification task.
- **EDA:** Visualizing data before modeling reveals patterns and anomalies early.
- **Random Forest:** How ensemble models build on weak learners to create a robust classifier.
- **scikit-learn pipeline:** fit → predict → evaluate → save → load.
- **Code organization:** Separating data logic (`model.py`), user interface (`app.py`), and analysis (`eda.py`) makes a project maintainable and readable.
- **Documentation:** Writing a clear README forces you to think about how others will use your code.

---

## 9. Future Improvements

- Replace synthetic data with real soil-test records from agricultural datasets (e.g., UCI, Kaggle)
- Add a Streamlit web interface for non-technical users
- Include fertilizer recommendation as a second output
- Support more crops and regional variations
- Add a map-based input to auto-fetch weather data by location

---

## 10. References

- Scikit-learn documentation: https://scikit-learn.org
- Indian agricultural crop profiles: ICAR (Indian Council of Agricultural Research)
- Soil nutrient guidelines: FAO Fertilizer and Plant Nutrition Bulletin
- Seaborn visualization library: https://seaborn.pydata.org
