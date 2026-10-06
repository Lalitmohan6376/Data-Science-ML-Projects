# 🌊 Marine Microplastic Data Analysis

A Data Analytics and Exploratory Data Analysis (EDA) project focused on analyzing marine microplastic density using geographical and temporal information.

The project explores how microplastic density varies across different locations and sampling periods using the **SEA_MICRO.csv** dataset.

> 🚫 No Machine Learning model is used in this project. The focus is on Data Analysis, Feature Engineering, Data Visualization and Insight Generation.

---

# 🎯 Project Objectives

- 🔍 Explore the marine microplastic dataset
- 🧹 Inspect the dataset structure and data quality
- 📅 Extract useful features from the date column
- 🌍 Analyze geographical variation using latitude and longitude
- 📊 Understand the distribution of microplastic density
- 📈 Analyze temporal variation in microplastic density
- 💡 Generate meaningful insights from visualizations

---

# 📂 Dataset

The project uses:

`SEA_MICRO.csv`

The dataset contains approximately **2,000 observations** of marine microplastic measurements.

## 📋 Dataset Columns

| Column | Description |
|---|---|
| `Date` | Date of the microplastic observation |
| `Latitude` | Latitude of the sampling location |
| `Longitude` | Longitude of the sampling location |
| `Total_Pieces_L` | Total number of microplastic pieces per litre |
| `Normalized` | Normalized value associated with the observation |

---

# ⚙️ Feature Engineering

The original `Date` column was converted into datetime format and additional features were created:

| Feature | Description |
|---|---|
| `year` | Year extracted from the observation date |
| `month` | Month extracted from the observation date |
| `quarter` | Quarter of the year |
| `day_of_year` | Day number within the year |

These features help analyze temporal patterns in the dataset.

---

# 🛠️ Technologies & Libraries

- 🐍 **Python**
- 🐼 **Pandas** — Data loading, preprocessing and analysis
- 🔢 **NumPy** — Numerical operations
- 📊 **Matplotlib** — Data visualization

> All visualizations were created using **Matplotlib**. Seaborn was not used.

---

# 📊 Data Visualizations

Seven visualizations were created to understand the geographical, temporal and statistical characteristics of the dataset.

---

## 🌐 1. Latitude vs Microplastic Density

This visualization shows the variation in microplastic density across different latitude locations.

### Insights

- Microplastic density varies across different latitude locations.
- Some latitude regions show higher concentration values than others.
- There is no clear linear relationship between latitude and microplastic density.

---

## 🗺️ 2. Longitude vs Microplastic Density

This visualization shows how microplastic density changes across different longitude locations.

### Insights

- Microplastic density changes across different longitude locations.
- Some geographical locations show noticeably higher concentration values.
- There is no simple linear relationship between longitude and microplastic density.

---

## 📊 3. Monthly Average Microplastic Density

This visualization compares the average microplastic density across different months.

### Insights

- Average microplastic density varies across different months.
- Some months show higher average concentration than others.
- This indicates temporal variation in the observed microplastic density.

---

## 📈 4. Microplastic Density Distribution

A histogram is used to understand how microplastic density values are distributed.

### Insights

- Most observations fall within a lower-to-middle concentration range.
- A smaller number of observations show relatively high microplastic density.
- The dataset contains noticeable variation in concentration values.

---

## 📅 5. Microplastic Density Over Time

This visualization shows individual microplastic density observations across sampling dates.

### Insights

- Microplastic density varies across different sampling dates.
- Some dates show noticeably higher concentration values.
- The observations indicate temporal variation in microplastic density.

---

## 🌍 6. Geographical Distribution of Sampling Locations

This visualization shows the geographical distribution of the available sampling locations using latitude and longitude.

### Insights

- Sampling locations are distributed across different latitude and longitude regions.
- The dataset covers multiple geographical locations.
- The visualization provides an overview of the spatial coverage of the samples.

---

## 📊 7. Microplastic Density by Quarter

This visualization compares average microplastic density across the four quarters of the year.

### Insights

- Average microplastic density differs across the four quarters.
- Some quarters show higher average concentration than others.
- Quarterly comparison helps identify broad temporal variation in the dataset.

---

# 💡 Key Findings

The analysis shows that marine microplastic density varies across both **geographical locations and sampling periods**.

The latitude and longitude visualizations show spatial variation, while the monthly, quarterly and time-based visualizations show temporal variation.

The distribution analysis also shows that microplastic density is not evenly distributed, with some observations having considerably higher concentration values.

---

# ⚠️ Dataset Limitation

The dataset contains approximately 2,000 observations but has a limited number of meaningful input variables.

The available columns mainly contain:

- Date
- Latitude
- Longitude
- Microplastic density

Therefore, the project focuses on **Data Analytics and Visualization** rather than building a Machine Learning prediction model.

Additional environmental variables such as ocean temperature, currents, wind, chlorophyll concentration, depth and other oceanographic measurements could provide more useful information for predictive modeling.

---

# 📁 Project Structure

```text
Marine-Microplastic-Data-Analysis/
│
├── 📄 SEA_MICRO.csv
├── 📓 SEA_Microplastic_Analysis.ipynb
│
├── 🖼️ Visualizations/
│   ├── latitude_vs_microplastic.png
│   ├── longitude_vs_microplastic.png
│   ├── monthly_average_microplastic.png
│   ├── microplastic_density_distribution.png
│   ├── microplastic_density_over_time.png
│   ├── geographical_distribution.png
│   └── microplastic_density_by_quarter.png
│
└── 📄 README.md
