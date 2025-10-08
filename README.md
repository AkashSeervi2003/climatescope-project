# ClimateScope Project

## Overview
through interactive visualizations.

## Environment Setup Guide
1. Install VSCode,Python in your local
1. Setup Git
Install Git: git-scm.com
Configure once in terminal:
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
2. Create Your Own GitHub Repo
● Go to GitHub → “New Repository” → Name it climatescope-project (or similar).
● Add a README (optional).
● Each student create their own repo
●  Add mentor as a collaborator and submit links to weekly Pull Requests.
●  Instructions to Add Me as Collaborator
● 1. Go to your GitHub repo → Settings → Collaborators.
● 2. Click “Add people”.
● 3. Enter my GitHub username:
● 4. Give me Write access.
● 5. I’ll accept the invite to access your repo.
● Copy the repo link (HTTPS or SSH).
3. Clone Repo to Your Computer
git clone https://github.com/your-username/climatescope-project.git
cd climatescope-project
4.Install all dependencies
Create a Virtual Environment
python -m venv venv
# Activate:
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Linux/Mac:
source venv/bin/activate
Install pandas,plotly,streamlit,folium,python-dotenv
5. Create a New Branch for Your Work
git checkout -b feature/step1-data-cleaning
Branch naming rule:
● Use feature/<task> (e.g., feature/data-exploration,
feature/visualizations).
6. Add Your Code & Commit
git add .
git commit -m "Added initial data cleaning script"
7. Push Your Branch to GitHub
git push origin feature/step1-data-cleaning
8. Open a Pull Request (PR)
● Go to GitHub → Your repo → You’ll see “Compare & Pull Request.”
● Add a short description of what you did.
● Submit the PR (your mentor will review).
9. Keep Main Updated
When mentor merges your branch, update your local main:
git checkout main
git pull origin main
10. Start Next Task
Repeat Steps 5 → 9 for each new task.
Rules for This Internship
● Always work on a branch → never directly on main.
● Push code regularly (don’t wait till deadline).
● One Pull Request = one task per week.

## Milestone 1: Data Preparation & Initial Analysis

### Tasks Completed
- **Dataset Download**: The Global Weather Repository dataset has been downloaded from Kaggle and is available as `GlobalWeatherRepository.csv`.
- **Project Environment Setup**: Python environment is set up with required packages: pandas, streamlit, plotly.
- **Dataset Inspection**:
  - Shape: 97,824 rows, 41 columns
  - Key variables: temperature_celsius, humidity, precip_mm, wind_kph, pressure_mb, uv_index, air_quality_PM2.5, etc.
  - Data types: Mostly float64, int64 for numeric; object for categorical (country, location_name, condition_text, etc.)
  - Missing values: 0 (dataset is complete)
  - Coverage: Worldwide, with data for various countries and locations.
- **Data Cleaning & Preprocessing**:
  - Converted `last_updated` to datetime format.
  - No missing values to handle.
  - Units are consistent (metric: Celsius, kph, mm, etc.).
  - No normalization required at this stage.
- **Aggregation**:
  - Created monthly averages from daily data, grouped by country and month.
  - Aggregated variables: temperature_celsius, humidity, precip_mm, wind_kph, pressure_mb, uv_index.
  - Result: 3,358 rows of monthly data.

### Deliverables
- **Cleaned Dataset**: `cleaned_weather_data.csv` (daily data, cleaned)
- **Aggregated Dataset**: `monthly_weather_data.csv` (monthly averages)
- **Summary Document**: This README section outlines data schema, key variables, and data quality.

### Data Schema
- **country**: object (Country name)
- **location_name**: object (City/location name)
- **latitude**: float64
- **longitude**: float64
- **timezone**: object
- **last_updated_epoch**: int64 (Unix timestamp)
- **last_updated**: datetime (Parsed date)
- **temperature_celsius**: float64
- **temperature_fahrenheit**: float64
- **condition_text**: object (Weather condition)
- **wind_mph**: float64
- **wind_kph**: float64
- **wind_degree**: int64
- **wind_direction**: object
- **pressure_mb**: float64
- **pressure_in**: float64
- **precip_mm**: float64
- **precip_in**: float64
- **humidity**: int64
- **cloud**: int64
- **feels_like_celsius**: float64
- **feels_like_fahrenheit**: float64
- **visibility_km**: float64
- **visibility_miles**: float64
- **uv_index**: float64
- **gust_mph**: float64
- **gust_kph**: float64
- **air_quality_Carbon_Monoxide**: float64
- **air_quality_Ozone**: float64
- **air_quality_Nitrogen_dioxide**: float64
- **air_quality_Sulphur_dioxide**: float64
- **air_quality_PM2.5**: float64
- **air_quality_PM10**: float64
- **air_quality_us-epa-index**: int64
- **air_quality_gb-defra-index**: int64
- **sunrise**: object
- **sunset**: object
- **moonrise**: object
- **moonset**: object
- **moon_phase**: object
- **moon_illumination**: int64

### Data Quality Issues
- No missing values detected.
- Data appears consistent and ready for analysis.
- Anomalies: None identified in initial inspection.

### Next Steps
- Proceed to Milestone 2: Core Analysis & Visualization Design.
