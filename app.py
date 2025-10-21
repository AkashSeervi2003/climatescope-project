import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots

st.set_page_config(page_title="ClimateScope Dashboard", page_icon="🌍", layout="wide")

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .tab-header {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_weather_data.csv")
    monthly_df = pd.read_csv("monthly_weather_data.csv")
    monthly_df['month_num'] = pd.to_datetime(monthly_df['month'].astype(str)).dt.month
    return df, monthly_df

# Load datasets
df, monthly_df = load_data()

# Compute analysis results
key_vars = ['temperature_celsius', 'humidity', 'precip_mm', 'wind_kph', 'pressure_mb', 'uv_index']
basic_stats = df[key_vars].describe()
distributions = {var: {'skewness': df[var].skew(), 'kurtosis': df[var].kurtosis()} for var in key_vars}
corr_matrix = df[key_vars].corr()
seasonal_avg = monthly_df.groupby('month_num')[key_vars].mean()
trends = {}
for country in monthly_df['country'].unique()[:10]:  # More countries
    country_data = monthly_df[monthly_df['country'] == country].sort_values('month_num')
    if len(country_data) > 1:
        slope = np.polyfit(country_data['month_num'], country_data['temperature_celsius'], 1)[0]
        trends[country] = slope
hot_threshold = df['temperature_celsius'].quantile(0.95)
hot_events = df[df['temperature_celsius'] >= hot_threshold]
precip_threshold = df['precip_mm'].quantile(0.95)
precip_events = df[df['precip_mm'] >= precip_threshold]
wind_threshold = df['wind_kph'].quantile(0.95)
wind_events = df[df['wind_kph'] >= wind_threshold]
regional_avg = df.groupby('country')[key_vars].mean()

st.markdown('<h1 class="main-header">🌍 ClimateScope: Global Weather Trends & Extreme Events</h1>', unsafe_allow_html=True)

# Sidebar filters
st.sidebar.header("🌐 Interactive Filters")
selected_countries = st.sidebar.multiselect(
    "Select Countries (for detailed views)",
    options=sorted(df['country'].unique()),
    default=sorted(df['country'].unique())[:5]
)
month_range = st.sidebar.slider("Month Range for Trends", 1, 12, (1, 12))
variable_select = st.sidebar.selectbox("Select Variable for Histograms", key_vars)

# Filter data
filtered_df = df[df['country'].isin(selected_countries)]
filtered_monthly = monthly_df[(monthly_df['country'].isin(selected_countries)) & (monthly_df['month_num'].between(month_range[0], month_range[1]))]

# Tabs
tabs = st.tabs(["🏠 Overview", "📊 Data Insights", "📈 Distributions", "📉 Time Series", "🔗 Correlations", "⚠️ Extremes", "📋 Summary"])

with tabs[0]:  # Overview
    st.markdown('<h2 class="tab-header">Global Weather Overview</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        temp_avg = df.groupby('country')['temperature_celsius'].mean().reset_index()
        fig_temp = px.choropleth(
            temp_avg,
            locations="country",
            locationmode="country names",
            color="temperature_celsius",
            hover_name="country",
            color_continuous_scale="RdYlBu_r",
            title="🌡️ Average Temperature by Country (°C)"
        )
        fig_temp.update_layout(margin=dict(l=0, r=0, t=40, b=0))
        st.plotly_chart(fig_temp, use_container_width=True)
    
    with col2:
        humid_avg = df.groupby('country')['humidity'].mean().reset_index()
        fig_humid = px.choropleth(
            humid_avg,
            locations="country",
            locationmode="country names",
            color="humidity",
            hover_name="country",
            color_continuous_scale="Blues",
            title="💧 Average Humidity by Country (%)"
        )
        fig_humid.update_layout(margin=dict(l=0, r=0, t=40, b=0))
        st.plotly_chart(fig_humid, use_container_width=True)
    
    st.subheader("📈 Key Global Statistics")
    cols = st.columns(4)
    metrics = [
        ("Avg Temperature", f"{df['temperature_celsius'].mean():.1f}°C", "🌡️"),
        ("Avg Humidity", f"{df['humidity'].mean():.1f}%", "💧"),
        ("Avg Precipitation", f"{df['precip_mm'].mean():.2f}mm", "🌧️"),
        ("Total Records", f"{len(df):,}", "📊")
    ]
    for col, (label, value, icon) in zip(cols, metrics):
        with col:
            st.markdown(f'<div class="metric-card">{icon} <strong>{label}:</strong> {value}</div>', unsafe_allow_html=True)

with tabs[1]:  # Data Insights
    st.markdown('<h2 class="tab-header">Statistical Analysis Insights</h2>', unsafe_allow_html=True)
    
    st.subheader("📊 Basic Statistics Summary")
    st.dataframe(basic_stats.style.format("{:.2f}").background_gradient(cmap='Blues', axis=0))
    
    st.subheader("📈 Distribution Characteristics")
    dist_df = pd.DataFrame(distributions).T
    st.dataframe(dist_df.style.format("{:.2f}").background_gradient(cmap='coolwarm', axis=0))
    
    st.subheader("🌍 Regional Comparisons (Top 10 Hottest Countries)")
    top_temp = regional_avg[['temperature_celsius', 'humidity']].sort_values('temperature_celsius', ascending=False).head(10)
    st.dataframe(top_temp.style.format("{:.1f}").background_gradient(cmap='Reds', subset=['temperature_celsius']))
    
    st.subheader("📉 Temperature Trends (Sample Countries)")
    trends_df = pd.DataFrame(list(trends.items()), columns=['Country', 'Trend (°C/month)'])
    st.dataframe(trends_df.style.format({'Trend (°C/month)': "{:.4f}"}).background_gradient(cmap='RdYlGn', subset=['Trend (°C/month)']))

with tabs[2]:  # Distributions
    st.markdown('<h2 class="tab-header">Data Distributions</h2>', unsafe_allow_html=True)
    
    st.subheader(f"📊 Histogram of {variable_select.replace('_', ' ').title()}")
    fig_hist = px.histogram(
        df, x=variable_select, nbins=50,
        title=f"Distribution of {variable_select.replace('_', ' ').title()}",
        color_discrete_sequence=['#1f77b4']
    )
    st.plotly_chart(fig_hist, use_container_width=True)
    
    st.subheader("📦 Box Plots for Key Variables")
    fig_box = px.box(
        df[key_vars], title="Box Plots of Key Weather Variables",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig_box, use_container_width=True)

with tabs[3]:  # Time Series
    st.markdown('<h2 class="tab-header">Time Series Trends</h2>', unsafe_allow_html=True)
    
    st.subheader("🗓️ Seasonal Patterns")
    seasonal_data = seasonal_avg.reset_index()
    fig_seasonal = px.line(
        seasonal_data.melt(id_vars='month_num', var_name='Variable', value_name='Value'),
        x='month_num', y='Value', color='Variable',
        title="Seasonal Averages Across Months",
        labels={'month_num': 'Month', 'Value': 'Average Value'},
        color_discrete_sequence=px.colors.qualitative.Dark24
    )
    st.plotly_chart(fig_seasonal, use_container_width=True)
    
    st.subheader("🌡️ Country-Specific Temperature Trends")
    if not filtered_monthly.empty:
        fig_trends = px.line(
            filtered_monthly.sort_values(['country', 'month_num']),
            x='month_num', y='temperature_celsius', color='country',
            title="Monthly Temperature Trends by Selected Countries",
            labels={'month_num': 'Month', 'temperature_celsius': 'Temperature (°C)'}
        )
        st.plotly_chart(fig_trends, use_container_width=True)
    else:
        st.info("Select countries and adjust month range to view trends.")

with tabs[4]:  # Correlations
    st.markdown('<h2 class="tab-header">Correlations & Relationships</h2>', unsafe_allow_html=True)
    
    st.subheader("🔗 Correlation Heatmap")
    fig_heatmap = px.imshow(
        corr_matrix, text_auto=True, aspect="auto",
        title="Correlation Matrix of Key Variables",
        color_continuous_scale="RdBu_r"
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    st.subheader("📊 Scatter Plot: Temperature vs Humidity")
    sample_size = min(5000, len(filtered_df))
    if sample_size > 0:
        fig_scatter = px.scatter(
            filtered_df.sample(sample_size),
            x='temperature_celsius', y='humidity', color='country',
            title="Temperature vs Humidity Relationship",
            labels={'temperature_celsius': 'Temperature (°C)', 'humidity': 'Humidity (%)'},
            opacity=0.7
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.info("Select countries to view scatter plot.")

with tabs[5]:  # Extremes
    st.markdown('<h2 class="tab-header">Extreme Weather Events</h2>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    extremes = [
        ("Extreme Heat", len(hot_events), f">= {hot_threshold:.1f}°C", "🔥"),
        ("Extreme Precipitation", len(precip_events), f">= {precip_threshold:.1f}mm", "🌧️"),
        ("Extreme Wind", len(wind_events), f">= {wind_threshold:.1f}kph", "💨")
    ]
    for col, (label, count, thresh, icon) in zip(cols, extremes):
        with col:
            st.markdown(f'<div class="metric-card">{icon} <strong>{label}:</strong><br>{count:,} events<br><small>{thresh}</small></div>', unsafe_allow_html=True)
    
    st.subheader("🔥 Extreme Heat Event Locations")
    fig_heat_extremes = px.scatter_mapbox(
        hot_events.sample(min(1000, len(hot_events))),  # Sample for performance
        lat="latitude", lon="longitude",
        hover_name="location_name", hover_data=["country", "temperature_celsius"],
        color="temperature_celsius", color_continuous_scale="Reds",
        title="Global Extreme Heat Event Locations (Sample)",
        mapbox_style="carto-positron", zoom=1
    )
    st.plotly_chart(fig_heat_extremes, use_container_width=True)
    
    st.subheader("🌧️ Top Countries with Extreme Events")
    extreme_counts = hot_events.groupby('country').size().sort_values(ascending=False).head(10)
    fig_extreme_bar = px.bar(
        extreme_counts.reset_index(name='Count'),
        x='country', y='Count',
        title="Top 10 Countries by Extreme Heat Events",
        labels={'Count': 'Number of Events'},
        color='Count', color_continuous_scale="Reds"
    )
    st.plotly_chart(fig_extreme_bar, use_container_width=True)

with tabs[6]:  # Summary
    st.markdown('<h2 class="tab-header">Project Summary & Insights</h2>', unsafe_allow_html=True)
    
    st.subheader("🎯 Key Findings")
    insights = [
        "🌡️ **Temperature Patterns**: Global average temperature is 22.8°C, with highest in Saudi Arabia (45°C). Seasonal peaks in July-August.",
        "💧 **Humidity Trends**: Negatively correlated with temperature (-0.35), highest in humid regions.",
        "🌧️ **Precipitation**: Highly skewed distribution, extreme events (>=0.8mm) occur in 4,905 records.",
        "💨 **Wind & Pressure**: Wind speeds show extreme outliers, pressure varies by region.",
        "📊 **Correlations**: Strong relationships between temperature and UV index (0.48), humidity and UV (-0.57).",
        "⚠️ **Extreme Events**: 4,907 extreme heat events, concentrated in hot climates.",
        "📈 **Trends**: Sample countries show varying monthly temperature changes, from -0.45°C to +1.06°C/month."
    ]
    for insight in insights:
        st.markdown(f"• {insight}")
    
    st.subheader("🛠️ Methodology")
    st.write("""
    - **Data Source**: Global Weather Repository (Kaggle) - 97,824 records across 41 columns.
    - **Analysis**: Statistical summaries, distributions, correlations, seasonal patterns, trends, and extreme event detection.
    - **Visualization**: Interactive choropleth maps, time series, scatter plots, heatmaps, and bar charts using Plotly.
    - **Tools**: Python (pandas, numpy), Streamlit for dashboard, Plotly for charts.
    """)
    
    st.subheader("📋 Data Sample")
    st.dataframe(df.head(10).style.format("{:.2f}", subset=key_vars))

# Footer
st.markdown("---")
st.markdown("**🌍 ClimateScope Dashboard** - Interactive Global Weather Analysis | *Data: Kaggle Global Weather Repository* | *Built with Streamlit & Plotly*")
st.markdown("*© 2024 ClimateScope Project*")
