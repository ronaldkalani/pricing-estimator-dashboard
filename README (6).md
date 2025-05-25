
# 🧠 AI-Powered B2B Pricing & Estimating Dashboard

An interactive Streamlit dashboard for Pricing & Estimating Analysts to simulate, model, and optimize pricing decisions based on historical sales and profit data — tailored for RFPs and quoting tasks.

---

🚀 **Live Demo**  
👉 [Launch the App](https://pricing-estimator-dashboard25-ktykxk6stxahh48ywuobfu.streamlit.app/)

---

## 🎯 Goal

Build a data-driven pricing solution to:
- Recommend competitive quote prices
- Simulate margins for various customer order scenarios
- Empower sales and estimating teams with dynamic tools

---

## 👥 Intended Audience

- Pricing Analysts
- Sales & Business Development Teams
- Procurement/Finance Managers
- Executive Decision-Makers

---

## 🛠️ Strategy & Pipeline Steps

1. **Data Loading & Cleaning**
   - Load `Sample - Superstore.csv` using proper encoding
   - Engineer fields like `Estimated Cost` and `Profit Margin %`

2. **Analytics & Template Building**
   - Grouped pricing templates by Region, Category, Sub-Category
   - Custom quote estimator based on quantity and margin logic

3. **Predictive Modeling (Optional ML Layer)**
   - Regression model for profit prediction
   - Optimization insights using Random Forest or XGBoost

4. **Streamlit Dashboard**
   - Live filters for category, region, sub-category
   - KPI summaries: Avg. Sales, Cost, Margin
   - Quote simulation slider and visuals (bar & pie charts)

---

## ❗ Challenges Addressed

- Manual RFP pricing inefficiencies
- Regional margin uncertainty
- Lack of autonomous quoting tools for sales

---

## ❓ Problem Statement

> “How can we enable faster, data-informed pricing and quoting decisions in complex B2B environments with multi-product, multi-region sales pipelines?”

---

## 📦 Dataset

- **Source**: Kaggle / Tableau Superstore
- **File**: `Sample - Superstore.csv`
- **Fields**: Sales, Profit, Discount, Region, Sub-Category, Order Date

---

## 🤖 Machine Learning Predictions (Advanced Layer)

| Feature Input            | Model Output              |
|--------------------------|---------------------------|
| Region + Category        | Recommended Margin %      |
| Quantity + Discount      | Expected Profit           |
| Past RFP history         | Quote Success Likelihood  |

---

## 📈 Dashboard Features

- 💡 **Dynamic Quote Calculator**
- 📊 **Profitability Breakdown (Bar & Pie Charts)**
- 📁 **CSV Pricing Templates**
- 📉 **Category & Region Margin Analytics**

---

## 🔮 AGI Vision (Future Enhancement)

Integrate a self-learning AGI agent to:
- Adapt pricing based on win/loss feedback
- Simulate competitor behavior and client type
- Recommend margin bands and price anchoring strategies

---

## 🔗 References

- [Kaggle Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- [Streamlit Docs](https://docs.streamlit.io)
- [Job Role - DCM](https://www.dcmgroup.ca)

---

## 👨‍💼 Author

**Ronald Kalani**  
[LinkedIn](https://linkedin.com/in/ronald-kalani-1a465533)
