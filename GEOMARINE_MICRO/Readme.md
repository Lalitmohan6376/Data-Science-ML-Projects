# 🌊 GEOMARINE Micro — Marine Microplastic Data Analysis

A Data Analytics and Exploratory Data Analysis (EDA) project focused on analyzing marine microplastic concentration using geographical and temporal observation data.

The project uses the **GEOMARINE Microplastic Dataset** to explore how microplastic concentration varies across different locations and sampling dates.

The main focus of this project is **Data Analysis, Data Visualization and Insight Generation**.

> 🚫 No Machine Learning model is used in this project.

---

# 🎯 Project Objectives

The main objectives of this project are:

- 🔍 Understand the structure of the GEOMARINE microplastic dataset
- 🧹 Inspect the dataset and its data types
- 📅 Analyze microplastic observations over time
- 🌍 Analyze geographical variation using latitude and longitude
- 📊 Understand the distribution of microplastic concentration
- 🗺️ Visualize the geographical distribution of sampling locations
- 💡 Generate meaningful insights from the available data

---

# 📂 Dataset

The project uses the following dataset:

`GEOMARINE_MICRO.csv`

The dataset contains **85 observations** related to marine microplastic measurements.

Each observation contains information about the sampling date, geographical coordinates and measured microplastic concentration.

## 📋 Dataset Columns

| Column | Description |
|---|---|
| `Date` | Date associated with the microplastic observation |
| `Latitude` | Latitude of the sampling location |
| `Longitude` | Longitude of the sampling location |
| `MP_conc__particles_cubic_metre_` | Microplastic concentration measured in particles per cubic metre |
| `Normalized` | Normalized value associated with the observation |

---

# 🎯 Main Variable

The primary measurement analyzed in this project is:

`MP_conc__particles_cubic_metre_`

This represents the concentration of microplastic particles measured in **particles per cubic metre**.

---

# 🛠️ Technologies & Libraries

The project was developed using:

- 🐍 **Python**
- 🐼 **Pandas** — Used for data loading, cleaning and analysis
- 🔢 **NumPy** — Used for numerical operations
- 📊 **Matplotlib** — Used for creating all visualizations

> The visualizations in this project were created using **Matplotlib**.

---

# 🔎 Data Analysis

Before creating visualizations, the dataset was inspected to understand:

- Number of observations
- Number of columns
- Column names
- Data types
- Missing values
- Duplicate records
- Statistical characteristics of numerical variables

The `Date` column was converted into a proper datetime format to make temporal analysis easier.

---

# 📊 Data Visualizations

Five visualizations were created to understand the geographical distribution, temporal variation and overall distribution of marine microplastic concentration.

---

## 🌐 1. Latitude vs Microplastic Concentration

This graph shows the relationship between **Latitude** and **Microplastic Concentration**.

### 💡 Insights

- Microplastic concentration varies across different latitude locations.
- The concentration values are not evenly distributed across latitude.
- Some latitude regions contain noticeably higher concentration values than others.
- The points do not form a clear straight-line pattern.
- Therefore, latitude alone does not show a simple linear relationship with microplastic concentration.

### 📌 Interpretation

The graph indicates that geographical position represented by latitude may be associated with differences in observed microplastic concentration, but the relationship is not simply linear.

---

## 🗺️ 2. Longitude vs Microplastic Concentration

This graph shows how microplastic concentration changes across different **Longitude** values.

### 💡 Insights

- Microplastic concentration changes across different longitude locations.
- Some longitude regions contain higher concentration values than others.
- The observations are spread across different geographical positions.
- There is no clear simple linear relationship between longitude and concentration.
- This indicates spatial variation in the observed microplastic concentration.

### 📌 Interpretation

The concentration of microplastics is not uniform across the geographical area covered by the available observations.

---

## 📈 3. Microplastic Concentration Over Time

This graph shows the variation in microplastic concentration across the available **sampling dates**.

### 💡 Insights

- Microplastic concentration changes across different sampling dates.
- Some observations show relatively higher concentration values.
- Other observations show comparatively lower concentration values.
- The concentration does not remain constant throughout the observation period.
- This indicates temporal variation in the measured microplastic concentration.

### 📌 Interpretation

The available observations suggest that microplastic concentration can vary with sampling time.

However, because the dataset contains only **85 observations**, these variations should be interpreted as patterns in the available sample rather than a definitive long-term seasonal trend.

---

## 📊 4. Microplastic Concentration Distribution

This histogram shows the distribution of the measured microplastic concentration values.

### 💡 Insights

- The observations are spread across different concentration ranges.
- A larger portion of observations falls within the lower-to-middle concentration ranges.
- A smaller number of observations have relatively high concentration values.
- The presence of higher concentration observations shows that the dataset contains variation in microplastic pollution levels.
- The distribution is not perfectly uniform.

### 📌 Interpretation

Most observations occur within a particular concentration range, while some locations have considerably higher measured microplastic concentrations.

These higher values may represent locations with comparatively greater observed microplastic pollution.

---

## 🌍 5. Geographical Distribution of Sampling Locations

This graph shows the geographical distribution of the available sampling locations using **Longitude** and **Latitude**.

### 💡 Insights

- The sampling points are distributed across multiple geographical locations.
- The observations cover different latitude and longitude coordinates.
- The graph provides an overview of the spatial coverage of the dataset.
- Some areas contain observations closer together, while other areas have fewer observations.
- The available data therefore represents multiple geographical sampling locations rather than a single location.

### 📌 Interpretation

This visualization helps understand where the available marine microplastic samples were collected and provides a basic view of the spatial coverage of the dataset.

---

# 💡 Key Findings

Based on the five visualizations, the following observations were identified:

### 🌍 Geographical Variation

Microplastic concentration varies across different latitude and longitude locations.

This indicates that the observed microplastic concentration is **spatially variable** rather than evenly distributed.

### 📅 Temporal Variation

The concentration also changes across different sampling dates.

This suggests that the observed microplastic levels are not constant over time.

### 📊 Concentration Variation

The concentration distribution contains observations across different ranges, including some relatively high concentration values.

This shows that the dataset contains variation in the measured level of marine microplastic contamination.

### 🗺️ Spatial Coverage

The geographical distribution graph shows that the dataset contains samples from multiple geographical locations.

This allows basic spatial exploration of the available observations.

---

# ⚠️ Dataset Limitation

The GEOMARINE dataset contains only **85 observations**.

Therefore, the analysis is useful for **exploratory data analysis and visualization**, but the results should not be treated as a complete representation of global marine microplastic pollution.

The observed patterns describe the available dataset and may change if a larger and more geographically diverse dataset is used.

---

# 📸 Project Visualizations

The following visualizations were created as part of this project:

1. **Latitude vs Microplastic Concentration**
2. **Longitude vs Microplastic Concentration**
3. **Microplastic Concentration Distribution**
4. **Microplastic Concentration Over Time**
5. **Geographical Distribution of Sampling Locations**

These visualizations help convert the raw numerical data into an easier-to-understand graphical form.

---

# 📁 Project Structure

```text
GEOMARINE-Microplastic-Analysis/
│
├── 📄 GEOMARINE_MICRO.csv
├── 📓 GEOMARINE_Microplastic_Analysis.ipynb
│
├── 🖼️ Visualizations/
│   ├── Latitude vs Microplastic Concentration.png
│   ├── Longitude vs Microplastic Concentration.png
│   ├── Microplastic Concentration Distribution.png
│   ├── Microplastic Concentration Over Time.png
│   └── Geographical Distribution of Sampling Locations.png
│
└── 📄 README.md
