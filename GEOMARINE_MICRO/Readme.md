# 🌊 GEOMARINE Micro — Marine Microplastic Data Analysis

A Data Analytics and Exploratory Data Analysis (EDA) project focused on understanding the geographical and temporal distribution of marine microplastic concentration using marine observation data.

## 🌍 About the Project

Microplastics are extremely small plastic particles that can be found in marine environments. Their concentration can vary depending on geographical location and sampling time.

The **GEOMARINE Micro** project explores marine microplastic observations using geographical coordinates, sampling dates, and concentration measurements.

The main purpose of this project is to transform raw environmental data into meaningful visualizations and insights.

This project was developed as a **Data Analyst / Data Analytics project** with a focus on:

- 📊 Exploratory Data Analysis
- 🌍 Geographical Data Analysis
- 📅 Temporal Data Analysis
- 📈 Data Visualization
- 💡 Insight Generation

> 🚫 No Machine Learning model is used in this project. The project focuses completely on Data Analysis and Visualization.

## 🎯 Project Objectives

- 🔍 Explore the GEOMARINE microplastic dataset
- 🧹 Inspect the dataset for missing values and duplicate records
- 📅 Analyze sampling dates
- 🌍 Analyze latitude and longitude information
- 📊 Understand the distribution of microplastic concentration
- 📈 Identify geographical and temporal patterns
- 💡 Generate meaningful insights from the data
- 📸 Create clear visualizations for data interpretation

## 📂 Dataset

The project uses the **GEOMARINE Microplastic Dataset**:

`GEOMARINE_MICRO.csv`

The dataset contains marine microplastic observations along with their geographical coordinates, sampling dates, and concentration measurements.

### 📋 Dataset Columns

| Column | Description |
|---|---|
| `Date` | Date associated with the microplastic observation |
| `Latitude` | Latitude of the sampling location |
| `Longitude` | Longitude of the sampling location |
| `MP_conc__particles_cubic_metre_` | Microplastic concentration measured in particles per cubic metre |
| `Normalized` | Normalized value associated with the microplastic observation |

### 🎯 Main Measurement

The primary variable analyzed in this project is:

`MP_conc__particles_cubic_metre_`

It represents the number of microplastic particles per cubic metre.

## 🛠️ Technologies & Libraries

The project was developed using Python and the following libraries:

- 🐍 **Python**
- 🐼 **Pandas** — Used for loading, cleaning, transforming and analyzing the dataset
- 🔢 **NumPy** — Used for numerical operations
- 📊 **Matplotlib** — Used for creating data visualizations
- 📈 **Seaborn** — Used for exploratory and statistical visualizations

## 🔎 Exploratory Data Analysis

The dataset was explored to understand its structure, quality and important patterns.

### 🧹 Data Inspection

The dataset was checked for:

- Missing values
- Duplicate records
- Number of rows and columns
- Column names
- Data types
- Basic statistical information

### 📅 Date Analysis

The `Date` column was converted into a proper datetime format to make temporal analysis easier.

### 🌍 Geographical Analysis

The `Latitude` and `Longitude` columns were used to understand the geographical distribution of the collected observations.

# 📊 Data Visualizations & Insights

## 🌐 1. Latitude vs Microplastic Concentration

This visualization shows how microplastic concentration varies across different latitude values.

### 💡 Insights

- Microplastic concentration varies across different latitude locations.
- Some latitude regions show noticeably higher concentration values.
- There is no simple linear relationship between latitude and concentration.

## 🗺️ 2. Longitude vs Microplastic Concentration

This visualization explores the relationship between longitude and microplastic concentration.

### 💡 Insights

- Microplastic concentration changes across different longitude locations.
- Some geographical locations show higher concentration values than others.
- This indicates spatial variation in the observed microplastic levels.

## 📅 3. Microplastic Concentration Over Time

This visualization shows how the observed microplastic concentration changes across different sampling dates.

### 💡 Insights

- Microplastic concentration varies across different sampling dates.
- Some observations show noticeably higher concentration values.
- The available data shows temporal variation in observed microplastic concentration.

## 📊 4. Microplastic Concentration Distribution

A histogram is used to understand how the concentration values are distributed across the dataset.

### 💡 Insights

- The observations are distributed across different concentration ranges.
- Most observations fall within a particular concentration range.
- Some observations have considerably higher concentration values.

## 🌍 5. Geographical Distribution of Sampling Locations

A latitude-longitude scatter plot is used to visualize where the available observations were collected.

### 💡 Insights

- The observations cover multiple geographical locations.
- The visualization provides an overview of the spatial coverage of the dataset.
- It helps understand how widely the available sampling locations are distributed.

# 💡 Key Findings

- 🌊 Microplastic concentration varies between different geographical locations.
- 📍 Some locations show noticeably higher concentrations than others.
- 📅 Microplastic concentration also changes across different sampling dates.
- 📊 The dataset contains observations across a range of concentration values.
- 🌍 Latitude and longitude provide useful information for understanding the spatial distribution of the samples.

# 📸 Project Visuals

Multiple visualization images were created as part of the analysis.

The visualizations include:

- 🌐 Latitude vs Microplastic Concentration
- 🗺️ Longitude vs Microplastic Concentration
- 📅 Microplastic Concentration Over Time
- 📊 Microplastic Concentration Distribution
- 🌍 Geographical Distribution of Sampling Locations

These visuals make the information in the raw dataset easier to understand and communicate.

# 📁 Project Structure

```text
GEOMARINE-Microplastic-Analysis/
│
├── 📄 GEOMARINE_MICRO.csv
├── 📓 GEOMARINE_Microplastic_Analysis.ipynb
│
├── 🖼️ Visualizations/
│   ├── latitude_vs_concentration.png
│   ├── longitude_vs_concentration.png
│   ├── concentration_over_time.png
│   ├── concentration_distribution.png
│   └── sampling_locations.png
│
└── 📄 README.md
