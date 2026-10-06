# 🌊 SEA Micro — Microplastic Data Analysis

A data analysis project focused on understanding the **geographical and temporal distribution of marine microplastic pollution** using latitude, longitude, sampling dates, and microplastic density data.

This project was created as a **Data Analytics / Exploratory Data Analysis (EDA)** project. It focuses on extracting meaningful patterns and insights from the dataset through visualization rather than building a Machine Learning model.

---

## 🌍 About the Project

Microplastics are very small plastic particles found in marine environments. Their concentration can vary depending on **location and time**.

The goal of this project is to analyze marine microplastic data and understand:

* 📍 Where microplastic concentrations are higher or lower
* 🌐 How concentration varies across different geographical locations
* 📅 How microplastic density changes over time
* 📊 How the concentration values are distributed
* 🗺️ Where the available samples were collected
* 🔎 What patterns and variations can be observed in the dataset

The project uses **Exploratory Data Analysis (EDA)** and visualization to present these observations clearly.

---

## 🎯 Project Objectives

* 🔍 Explore the marine microplastic dataset
* 🧹 Check the dataset for missing values and duplicate records
* 📅 Extract useful information from the date
* 🌍 Analyze latitude and longitude information
* 📊 Understand the distribution of microplastic density
* 📈 Identify temporal and geographical patterns
* 💡 Generate meaningful insights from visualizations
* 📸 Create visual outputs for easier interpretation

---

## 📂 Dataset

The project uses the **SEA Microplastic Dataset**, containing information about marine microplastic observations.

### Dataset Columns

| Column       | Description                                        |
| ------------ | -------------------------------------------------- |
| `Date`       | Date when the observation/sample was recorded      |
| `Latitude`   | Latitude of the sampling location                  |
| `Longitude`  | Longitude of the sampling location                 |
| `Pieces_KM2` | Number of microplastic pieces per square kilometer |
| `month`      | Month extracted from the observation date          |
| `year`       | Year extracted from the observation date           |
| `day`        | Day extracted from the observation date            |
| `season`     | Season derived from the observation month          |

### 🎯 Main Variable

`Pieces_KM2` is the main measurement analyzed in this project.

It represents the estimated **number of microplastic pieces per square kilometer**.

---

## 🛠️ Technologies & Libraries

This project was created using Python and the following libraries:

* 🐍 **Python**
* 🐼 **Pandas** — Data loading, cleaning, transformation and analysis
* 🔢 **NumPy** — Numerical operations
* 📊 **Matplotlib** — Data visualization
* 📈 **Seaborn** — Statistical and exploratory visualization

> 🚫 No Machine Learning model was used in this project.
> The project focuses completely on **Data Analysis and Visualization**.

---

## 🔎 Data Analysis

The analysis includes:

### 🧹 Data Inspection

The dataset was inspected for:

* Missing values
* Duplicate records
* Dataset dimensions
* Column information
* Data types
* Basic statistical information

### 📅 Feature Extraction

The original `Date` column was converted into useful time-based features:

```text
month
year
day
season
```

This makes it easier to analyze the data from a temporal perspective.

---

# 📊 Visualizations

Several visualizations were created to understand the dataset.

### 🌐 1. Latitude vs Microplastic Density

Shows how microplastic concentration varies across different latitude values.

**Insight:**

* Microplastic density varies across different latitude locations.
* Some regions show noticeably higher concentrations.
* There is no simple linear relationship between latitude and density.

---

### 🗺️ 2. Longitude vs Microplastic Density

Shows the relationship between longitude and microplastic concentration.

**Insight:**

* Microplastic concentration changes across different longitude locations.
* Some locations contain considerably higher concentrations.
* This indicates that microplastic pollution is not evenly distributed geographically.

---

### 📅 3. Monthly Average Microplastic Density

Shows how the average microplastic density changes across different months.

**Insight:**

* Average density changes from month to month.
* Some months show higher microplastic concentrations.
* This indicates temporal variation in the observed microplastic levels.

---

### 📊 4. Microplastic Density Distribution

A histogram was used to understand how `Pieces_KM2` values are distributed.

**Insight:**

* Most observations are concentrated within a particular density range.
* A smaller number of observations have relatively high values.
* This shows variation in microplastic concentration across the collected samples.

---

### 🌍 5. Geographical Distribution of Sampling Locations

A latitude-longitude scatter plot was created to visualize the geographical coverage of the observations.

**Insight:**

* The observations are distributed across different geographical coordinates.
* The visualization shows the spatial coverage of the available samples.
* It provides a simple overview of where the data was collected.

---

## 💡 Key Insights

Through exploratory analysis, the project highlights that:

* 🌊 Microplastic concentration is **not uniformly distributed** across locations.
* 📍 Different geographical regions show different concentration levels.
* 📅 Microplastic density varies across the observed time periods.
* 📊 The dataset contains both common and relatively high-density observations.
* 🌍 Latitude and longitude provide useful information for understanding the spatial distribution of the collected samples.

---

## 📸 Project Visuals

The repository contains multiple visualization images generated during the analysis.

These visuals make it easier to understand the dataset without looking directly at the raw numerical values.

---

## 📁 Project Structure

```text
SEA-Microplastic-Data-Analysis/
│
├── 📄 SEA_MICRO.csv
├── 📓 SEA_Microplastic_Analysis.ipynb
│
├── 🖼️ Visualizations/
│   ├── latitude_vs_density.png
│   ├── longitude_vs_density.png
│   ├── monthly_density.png
│   ├── density_distribution.png
│   └── sampling_locations.png
│
└── 📄 README.md
```

---

## 👨‍💻 Project Type

**Data Analytics | Exploratory Data Analysis | Data Visualization**

This project demonstrates how raw environmental data can be explored, transformed, visualized, and interpreted to extract meaningful information.

---

## 🚀 Skills Demonstrated

* 🐍 Python Programming
* 🐼 Data Manipulation with Pandas
* 🔢 Numerical Analysis with NumPy
* 📊 Exploratory Data Analysis
* 📈 Data Visualization
* 🌍 Geospatial Data Exploration
* 📅 Date & Time Feature Extraction
* 💡 Data Interpretation
* 📝 Insight Generation

---

## 🌱 Conclusion

**SEA Micro** provides an exploratory view of marine microplastic distribution using geographical and temporal information.

The project demonstrates how **Data Analytics and Visualization** can be used to turn raw environmental observations into understandable patterns and insights.
