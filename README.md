# ClimateScope: Visualizing Global Weather Trends and Extreme Events

## Project Objective
The objective of ClimateScope is to analyze and visually represent global weather patterns using the Global Weather Repository dataset. This project aims to uncover seasonal trends, regional variations, and extreme weather events through interactive and insightful visualizations. By leveraging daily-updated, worldwide weather data, the project will enable users to explore climate behavior over time, compare conditions across regions, and identify anomalies. The ultimate goal is to provide an accessible, data-driven platform that supports climate awareness, decision-making, and further research into global weather dynamics.

## Project Workflow
- **Data Acquisition**: Download the Global Weather Repository dataset from Kaggle.
- **Data Understanding & Exploration**: Inspect dataset structure, data types, and key variables.
- **Data Cleaning & Preprocessing**: Handle missing values, convert units, aggregate data.
- **Data Analysis**: Perform statistical analysis, identify patterns and extremes.
- **Data Visualization Design**: Select visualization types and design interactive dashboard.
- **Visualization Development**: Build static and interactive visualizations.
- **Insights Generation**: Highlight findings and trends.
- **Final Dashboard & Reporting**: Deploy dashboard and document insights.

## Architecture Diagram
[Text-based representation - not included in this text file; refer to project documentation for visual diagram]

## Tech Stack
1. **Programming Language**: Python 3 – for data processing and visualization.
2. **Data Handling**: pandas – clean and transform data; kaggle API – download dataset.
3. **Visualization**: Plotly – create interactive charts and maps; Streamlit – build interactive dashboard.
4. **Storage**: CSV / Parquet files – store raw and processed data locally.
5. **Optional Tools**: folium – for additional map visualizations; python-dotenv – manage API keys securely.

## Environment Setup Guide
1. Install VSCode, Python in your local.
2. Setup Git: Install Git from git-scm.com. Configure once in terminal: `git config --global user.name "Your Name"` and `git config --global user.email "your@email.com"`.
3. Create Your Own GitHub Repo: Go to GitHub → "New Repository" → Name it climatescope-project (or similar). Add mentor as collaborator.
4. Clone Repo to Your Computer: `git clone https://github.com/your-username/climatescope-project.git` and `cd climatescope-project`.
5. Install all dependencies: Create a Virtual Environment with `python -m venv venv`. Activate: Windows PowerShell: `.\venv\Scripts\Activate.ps1`. Install pandas, plotly, streamlit, folium, python-dotenv.
6. Create a New Branch for Your Work: `git checkout -b feature/<task>`.
7. Add Your Code & Commit: `git add .` and `git commit -m "Message"`.
8. Push Your Branch to GitHub: `git push origin feature/<task>`.
9. Open a Pull Request (PR): Go to GitHub → Compare & Pull Request.
10. Keep Main Updated: `git checkout main` and `git pull origin main`.
Rules for This Internship: Always work on a branch → never directly on main. Push code regularly. One Pull Request = one task per week.

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

## Milestone 2: Core Analysis & Visualization Design

### Tasks Completed
- **Statistical Analysis**: Performed comprehensive analysis including distributions, correlations, seasonal patterns, trends, and extreme weather events.
- **Extreme Events Identification**: Identified extreme heat (>=35.0°C), precipitation (>=0.8mm), and wind (>=29.5kph) events.
- **Regional Comparisons**: Compared average temperature and humidity across countries.
- **Visualization Types Selected**:
  - Choropleth maps for geographic patterns (temperature, humidity).
  - Line charts for time-series trends (seasonal patterns, country-specific temperature trends).
  - Scatterplots for correlations (temperature vs humidity).
  - Heatmaps for correlation matrices.
  - Bar charts for extreme event counts.
- **Interactive Dashboard Design**: Built a multi-tab Streamlit dashboard with filters for countries and interactive visualizations.

### Analytical Findings
- **Distributions**: Temperature is slightly left-skewed; precipitation and wind are highly right-skewed with outliers.
- **Correlations**: Strong negative correlation between temperature and humidity (-0.35); positive between temperature and UV index (0.48).
- **Seasonal Patterns**: Temperature peaks in July-August, humidity in October-December, precipitation varies with slight increase in summer.
- **Trends**: Sample countries show varying temperature trends (e.g., Afghanistan +1.06°C/month, Angola -0.45°C/month).
- **Extreme Events**: 4,907 extreme heat events, 4,905 extreme precipitation events, 4,958 extreme wind events.
- **Regional Variations**: Highest average temperatures in Saudi Arabia (45°C), lowest in various cold regions.

### Dashboard Layout (Wireframes Description)
- **Tab 1: Overview**: Choropleth maps for temperature and humidity, key metrics.
- **Tab 2: Data Insights**: Statistical summaries, distributions, regional comparisons, trends.
- **Tab 3: Distributions**: Histograms and box plots for key variables.
- **Tab 4: Time Series**: Seasonal averages, country-specific trends.
- **Tab 5: Correlations**: Correlation heatmap, scatter plots.
- **Tab 6: Extremes**: Maps and bar charts for extreme events.
- **Tab 7: Summary**: Key findings, methodology, data sample.
- **Sidebar Filters**: Multi-select for countries, month range slider, variable selector.

### Deliverables
- **Analysis Script**: `weather_analysis.py` with statistical computations.
- **Interactive Dashboard**: `app.py` (Streamlit app) with multiple visualizations.
- **Summary Document**: This README section with findings and design details.

### Success Criteria
- Statistical insights derived and documented.
- Interactive dashboard built with appropriate visualizations.
- Dashboard supports user exploration through filters and tabs.

### Next Steps
- Proceed to Milestone 3: Visualization Development & Interactivity.

## Milestone 3: Visualization Development & Interactivity

### Tasks Completed
- **Static and Interactive Visualizations**: Built all planned visualizations using Plotly and integrated into Streamlit.
- **Interactivity Features**: Added filters for countries, sliders for months, tabs for different views.
- **Aesthetics and UX**: Applied consistent color schemes, clear labels, and responsive design.
- **Insights Highlighting**: Integrated key findings directly into the dashboard tabs.

### Deliverables
- **Interactive Dashboard Prototype**: Fully functional Streamlit app with all major features implemented.

### Success Criteria
- All major visualizations integrated and interactive.
- Dashboard demonstrates key insights from the data.
- User experience is smooth with proper filtering and navigation.

### Next Steps
- Proceed to Milestone 4: Finalization, Testing & Reporting.

## Milestone 4: Finalization, Testing & Reporting

### Tasks Completed
- **Comprehensive Testing**: Dashboard tested for functionality, data accuracy, and user experience.
- **Bug Fixes**: Addressed deprecation warnings and optimized performance.
- **Documentation**: Updated README with full project details, methodology, and insights.
- **Final Report**: Comprehensive summary of findings, trends, and project process.

### Deliverables
- **Fully Tested Dashboard**: Stable interactive dashboard meeting all objectives.
- **Final Project Report**: Detailed documentation in README.md.

### Success Criteria
- Dashboard is robust, bug-free, and meets all defined objectives.
- Project report clearly articulates findings and the project process.

### Future Enhancements (Optional)
- Incorporate live API-based weather updates.
- Add predictive modeling for weather forecasting.
- Enable anomaly alerts for extreme events.
