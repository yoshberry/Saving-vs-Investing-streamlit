
import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Saving vs Investing in Europe",
    page_icon="💶",
    layout="wide"
)


# Custom financial website theme
st.markdown("""
<style>
    
.stApp {
    background-color: #FAF9F4;
    background-image:
        radial-gradient(
            circle,
            transparent 0 22px,
            rgba(217, 180, 91, 0.13) 23px 25px,
            transparent 26px
        ),
        radial-gradient(
            circle,
            transparent 0 13px,
            rgba(23, 75, 53, 0.06) 14px 16px,
            transparent 17px
        );

    background-size: 220px 220px, 310px 310px;
    background-position: 0 0, 100px 120px;
    animation: moneyDrift 45s linear infinite;
}

@keyframes moneyDrift {
    from {
        background-position: 0 0, 100px 120px;
    }

    to {
        background-position: 220px 220px, -210px -190px;
    }
}


    h1, h2, h3 {
        color: #174B35;
    }

    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #D9B45B;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
    }

    [data-testid="stMetricLabel"] {
        color: #174B35;
        font-weight: 600;
    }

    [data-testid="stMetricValue"] {
        color: #174B35;
    }

    hr {
        border-color: #D9B45B;
    }
</style>
""", unsafe_allow_html=True)

# Floating currency coins background
st.html("""
<style>
    .money-floater-layer {
        position: fixed;
        inset: 0;
        overflow: hidden;
        pointer-events: none;
        z-index: 0;
    }

    .money-floater {
        position: absolute;
        bottom: -90px;
        width: 58px;
        height: 58px;
        border: 1.5px solid;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 27px;
        font-weight: 600;
        opacity: 0.15;
        box-sizing: border-box;
        animation: floatMoney 22s linear infinite;
    }

    .money-floater.euro {
        color: #B58B32;
        border-color: #D9B45B;
    }

    .money-floater.pound {
        color: #174B35;
        border-color: #174B35;
    }

    .money-floater:nth-child(1) {
        left: 8%;
        width: 66px;
        height: 66px;
        font-size: 31px;
        animation-duration: 23s;
    }

    .money-floater:nth-child(2) {
        left: 24%;
        width: 48px;
        height: 48px;
        font-size: 23px;
        animation-duration: 27s;
        animation-delay: 4s;
    }

    .money-floater:nth-child(3) {
        left: 43%;
        width: 74px;
        height: 74px;
        font-size: 35px;
        animation-duration: 25s;
        animation-delay: 2s;
    }

    .money-floater:nth-child(4) {
        left: 62%;
        width: 54px;
        height: 54px;
        font-size: 25px;
        animation-duration: 29s;
        animation-delay: 7s;
    }

    .money-floater:nth-child(5) {
        left: 79%;
        width: 68px;
        height: 68px;
        font-size: 32px;
        animation-duration: 24s;
        animation-delay: 3s;
    }

    .money-floater:nth-child(6) {
        left: 93%;
        width: 46px;
        height: 46px;
        font-size: 22px;
        animation-duration: 28s;
        animation-delay: 9s;
    }

    @keyframes floatMoney {
        0% {
            transform: translateY(0) rotate(0deg);
        }

        50% {
            transform: translateY(-55vh) rotate(18deg);
        }

        100% {
            transform: translateY(-115vh) rotate(-12deg);
        }
    }

    @media (prefers-reduced-motion: reduce) {
        .money-floater {
            animation: none;
        }
    }
</style>

<div class="money-floater-layer">
    <span class="money-floater euro">€</span>
    <span class="money-floater pound">£</span>
    <span class="money-floater euro">€</span>
    <span class="money-floater pound">£</span>
    <span class="money-floater euro">€</span>
    <span class="money-floater pound">£</span>
</div>
""")




# Sidebar navigation
st.sidebar.markdown(
    "## 💶 Money & Markets"
)

st.sidebar.caption(
    "A European financial analysis | 2006–2025"
)

st.sidebar.divider()

st.sidebar.markdown("### Explore the Analysis")

page = st.sidebar.radio(
    "Navigation",
    [
        "Project Overview",
        "Inflation Across Europe",
        "Savings vs Investment",
        "European Economies",
        "Brexit Analysis",
        "Conclusion"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()

st.sidebar.caption(
    "Data analysis project | 2006–2025"
)


# Load European inflation data
hicp_df = pd.read_csv("data/europe_hicp_monthly_2006_2025.csv.csv")

# Load savings and investment comparison data
real_value_df = pd.read_csv(
    "data/euro_area_real_value_comparison_2006_2025.csv"
)

# Load the integrated European economic dataset
europe_df = pd.read_csv(
    "data/europe_integrated_monthly_dataset.csv"
)


# Project introduction
if page == "Project Overview":

    # Homepage hero section
    st.html("""
    <div style="
        background: linear-gradient(120deg, #123D2B, #1B5A3D);
        padding: 28px 35px;
        border-radius: 16px;
        margin-bottom: 30px;
        border: 1px solid #D9B45B;
    ">

        <div style="
            color: #E2C16F;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 15px;
        ">
            EUROPEAN FINANCIAL ANALYSIS | 2006–2025
        </div>

        <h1 style="
            color: #FAF9F4;
            font-size: 30px;
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 18px;
        ">
            Saving vs Investing:<br>
            The Real Value of Money Over Time
        </h1>

        <p style="
            color: #F2EAD7;
            font-size: 15px;
            line-height: 1.7;
        ">
            Discover how savings, investments and inflation have shaped
            purchasing power across Europe over the past 20 years.
        </p>

        <p style="
            color: #F2EAD7;
            font-size: 15px;
            line-height: 1.7;
        ">
            A comparative analysis of 27 EU countries and the United Kingdom,
            using a €10,000 starting simulation.
        </p>

    </div>
    """)

    # Project overview section
    st.markdown("## Project at a Glance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Years Analysed", "20")

    with col2:
        st.metric("Countries Covered", "28")

    with col3:
        st.metric("Starting Amount", "€10,000")

    st.divider()

    st.subheader("Research Focus")

    st.write("""
    How have savings returns, investment performance and inflation
    affected the real purchasing power of money across Europe
    between 2006 and 2025?
    """)

    # Main project insight
    st.divider()
    st.subheader("The Real Value of €10,000")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Real Value of Savings",
            "€7,063.37",
            delta="-29.37%",
            delta_color="inverse"
        )

    with col2:
        st.metric(
            "Real Value of Investment",
            "€11,866.32",
            delta="+18.66%"
        )

    st.caption(
        "Values represent purchasing power in January 2006 euros. "
        "Investment performance is based on the EURO STOXX price index "
        "and excludes dividends."
    )

    # About this project
    st.divider()
    st.subheader("About This Project")

    st.write("""
    This project examines how savings, investments and inflation
    have influenced the purchasing power of money across Europe
    between 2006 and 2025.

    The analysis compares the EU27 countries with the United Kingdom,
    explores differences between European regions and investigates
    economic trends around the Brexit period.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🌍 Research Scope")
        st.write(
            "28 countries, covering 27 EU member states "
            "and the United Kingdom."
        )

    with col2:
        st.markdown("### 📊 Data Sources")
        st.write(
            "Eurostat, European Central Bank, Bank of England, "
            "World Bank and EURO STOXX."
        )

    with col3:
        st.markdown("### 🔎 Methodology")
        st.write(
            "Historical data analysis, inflation-adjusted simulations, "
            "regional comparisons and Brexit-period analysis."
        )

    st.info(
        "Important: The findings are descriptive, not proof of causation. "
        "The savings and investment comparisons also use different "
        "underlying data definitions."
    )


    st.subheader("Project Overview")

    st.write("""
    Explore how inflation, savings returns and investment performance
    have shaped the real value of money across European economies.

    The analysis covers EU27 countries and the United Kingdom
    between January 2006 and December 2025.
    """)

    # Key Financial Results
    st.divider()

    st.subheader("Key Financial Results")

    st.write("""
    The simulation starts with an initial investment of €10,000
    in January 2006 and compares the results by December 2025.
    """)

    # Display financial results using metric cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Final Savings Value",
            value="€10,722",
            delta="+7.22%"
        )

    with col2:
        st.metric(
            label="Final Investment Value",
            value="€18,013",
            delta="+80.13%"
        )

    with col3:
        st.metric(
            label="Real Savings Value",
            value="€7,063",
            delta="-29.37%"
        )

    with col4:
        st.metric(
            label="Real Investment Value",
            value="€11,866",
            delta="+18.66%"
        )

# Inflation Across Europe
if page == "Inflation Across Europe":

    st.subheader("Inflation Across Europe")

    st.write("""
    Explore how consumer prices have changed across European countries
    between January 2006 and December 2025.
    """)

    # Select a country
    country_codes = sorted(hicp_df["geo"].unique())

    selected_country = st.selectbox(
        "Select a country",
        country_codes,
        index=country_codes.index("DE")
    )


    # Select countries for comparison
    selected_countries = st.multiselect(
        "Compare inflation across countries",
        country_codes,
        default=["DE", "FR", "IT", "ES", "NL"]
    )

    # Filter the data for the selected country
    country_df = hicp_df[
        hicp_df["geo"] == selected_country
    ].copy()

    # Convert the monthly date column
    country_df["TIME_PERIOD"] = pd.to_datetime(
        country_df["TIME_PERIOD"],
        format="%Y-%m"
    )

    # Calculate year-on-year inflation
    country_df["Inflation_Rate"] = (
        country_df["OBS_VALUE"].pct_change(12) * 100
    )

    
    # Sort the data by date
    country_df = country_df.sort_values("TIME_PERIOD")

    # Calculate key inflation indicators
    latest_hicp = country_df["OBS_VALUE"].iloc[-1]

    average_inflation = country_df["Inflation_Rate"].mean()

    first_hicp = country_df["OBS_VALUE"].iloc[0]
    last_hicp = country_df["OBS_VALUE"].iloc[-1]

    total_price_increase = (
        (last_hicp / first_hicp) - 1
    ) * 100


    # Display inflation indicators
    st.divider()
    st.subheader("Inflation Indicators")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Latest HICP Index",
            value=f"{latest_hicp:.2f}"
        )

    with col2:
        st.metric(
            label="Average Annual Inflation",
            value=f"{average_inflation:.2f}%"
        )

    with col3:
        st.metric(
            label="Total Price Increase",
            value=f"{total_price_increase:.2f}%"
        )


    # Create the inflation index chart
    fig = px.line(
        country_df,
        x="TIME_PERIOD",
        y="OBS_VALUE",
        title=f"Consumer Price Index (HICP) – {selected_country}",
        labels={
            "TIME_PERIOD": "Year",
            "OBS_VALUE": "HICP Index"
        }
    )

    fig.update_layout(
        template="plotly_white",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)
        # UK data limitation
    if selected_country == "UK":
        st.info(
            "UK HICP observations in this dataset end in November 2020. "
            "Later months are not available in this source."
        )

    
    # Compare annual inflation across selected countries
    st.divider()
    st.subheader("Country Inflation Comparison")

    if selected_countries:

        comparison_df = hicp_df[
            hicp_df["geo"].isin(selected_countries)
        ].copy()

        comparison_df["TIME_PERIOD"] = pd.to_datetime(
            comparison_df["TIME_PERIOD"],
            format="%Y-%m"
        )

        comparison_df = comparison_df.sort_values(
            ["geo", "TIME_PERIOD"]
        )

        # Calculate year-on-year inflation for each country
        comparison_df["Inflation_Rate"] = (
            comparison_df.groupby("geo")["OBS_VALUE"]
            .pct_change(12) * 100
        )

        # Create the comparison chart
        comparison_fig = px.line(
            comparison_df,
            x="TIME_PERIOD",
            y="Inflation_Rate",
            color="geo",
            title="Annual Inflation Comparison Across Europe",
            labels={
                "TIME_PERIOD": "Year",
                "Inflation_Rate": "Inflation Rate (%)",
                "geo": "Country"
            }
        )

        comparison_fig.update_layout(
            template="plotly_white",
            hovermode="x unified"
        )

        st.plotly_chart(
            comparison_fig,
            use_container_width=True
            
        )

        

    else:
        st.info("Please select at least one country to compare.")



    # Prepare data for the European inflation heatmap
    heatmap_df = hicp_df.copy()

    heatmap_df["TIME_PERIOD"] = pd.to_datetime(
        heatmap_df["TIME_PERIOD"],
        format="%Y-%m"
    )

    heatmap_df = heatmap_df.sort_values(
        ["geo", "TIME_PERIOD"]
    )

    # Calculate year-on-year inflation for each country
    heatmap_df["Inflation_Rate"] = (
        heatmap_df.groupby("geo")["OBS_VALUE"]
        .pct_change(12) * 100
    )

    # Extract the calendar year
    heatmap_df["Year"] = heatmap_df["TIME_PERIOD"].dt.year

    # Calculate average annual inflation by country
    annual_heatmap_df = (
        heatmap_df.groupby(["geo", "Year"])["Inflation_Rate"]
        .mean()
        .reset_index()
    )

    # Arrange countries and years for the heatmap
    heatmap_pivot = annual_heatmap_df.pivot(
        index="geo",
        columns="Year",
        values="Inflation_Rate"
    )
    # Display the European inflation heatmap
    st.divider()
    st.subheader("European Inflation Heatmap")

    heatmap_fig = px.imshow(
        heatmap_pivot,
        labels={
            "x": "Year",
            "y": "Country",
            "color": "Average Annual Inflation (%)"
        },
        aspect="auto",
        color_continuous_scale="RdYlGn_r",
        title="Average Annual Inflation by Country (2007–2025)"
    )

    heatmap_fig.update_layout(
        template="plotly_white",
        height=750
    )

    st.plotly_chart(heatmap_fig, use_container_width=True)
    
    # Savings vs Investment
if page == "Savings vs Investment":

    st.subheader("Savings vs Investment")

    st.write("""
    Compare how savings and stock market investments performed
    over the period January 2006 to December 2025.

    The simulation starts with €10,000 and examines both nominal
    returns and the impact of inflation on purchasing power.
    """)
        # Prepare the monthly data
    real_value_df["month"] = pd.to_datetime(real_value_df["month"])

    real_value_df = real_value_df.sort_values("month")

    # Get the first and last real and nominal values
    final_savings = real_value_df["savings_value"].iloc[-1]
    final_investment = real_value_df["investment_value"].iloc[-1]

    final_real_savings = real_value_df["real_savings_value"].iloc[-1]
    final_real_investment = real_value_df["real_investment_value"].iloc[-1]
        # Display the final financial results
    st.divider()
    st.subheader("Final Financial Results")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Final Savings Value",
            value=f"€{final_savings:,.2f}"
        )

    with col2:
        st.metric(
            label="Final Investment Value",
            value=f"€{final_investment:,.2f}"
        )

    with col3:
        st.metric(
            label="Real Savings Value",
            value=f"€{final_real_savings:,.2f}"
        )

    with col4:
        st.metric(
            label="Real Investment Value",
            value=f"€{final_real_investment:,.2f}"
        )
    # Compare nominal and real financial performance
    st.divider()
    st.subheader("Savings vs Investment Performance")

    comparison_fig = px.line(
        real_value_df,
        x="month",
        y=[
            "savings_value",
            "investment_value",
            "real_savings_value",
            "real_investment_value"
        ],
        title="Nominal vs Real Value of €10,000 (2006–2025)",
        labels={
            "month": "Year",
            "value": "Portfolio Value (€)",
            "variable": "Financial Performance"
        }
    )

    comparison_fig.update_layout(
        template="plotly_white",
        hovermode="x unified",
        yaxis_title="Value (€)",
        legend_title="Financial Performance"
    )

    st.plotly_chart(comparison_fig, use_container_width=True)
    
# European Economies
if page == "European Economies":

    st.subheader("European Economies")

    st.write("""
    Explore how economic performance has changed across European
    countries between 2006 and 2025.

    This section uses GDP per capita adjusted for Purchasing Power
    Parity (PPP) to compare economic differences across Europe.
    """)

    # Group European countries by region
    country_regions = {
        "Northern Europe": ["DK", "EE", "FI", "IE", "LV", "LT", "SE"],
        "Southern Europe": ["CY", "GR", "IT", "MT", "PT", "ES"],
        "Western Europe": ["AT", "BE", "DE", "FR", "LU", "NL"],
        "Eastern Europe": ["BG", "HR", "CZ", "HU", "PL", "RO", "SK", "SI"]
    }

    # Prepare the GDP per capita data
    europe_df["year"] = pd.to_numeric(
        europe_df["year"],
        errors="coerce"
    )

    europe_df["GDP_per_capita_PPP"] = pd.to_numeric(
        europe_df["GDP_per_capita_PPP"],
        errors="coerce"
    )

    # Calculate annual GDP per capita for each country
    annual_gdp_df = (
        europe_df.groupby(["country_code", "year"])["GDP_per_capita_PPP"]
        .mean()
        .reset_index()
    )

    # Remove missing GDP observations
    annual_gdp_df = annual_gdp_df.dropna(
        subset=["GDP_per_capita_PPP"]
    )

    # Select countries for GDP comparison
    available_countries = sorted(annual_gdp_df["country_code"].unique())

    selected_gdp_countries = st.multiselect(
        "Select countries to compare",
        available_countries,
        default=["DE", "FR", "IT", "ES", "NL", "UK"]
    )

    # Create the individual country GDP comparison chart
    if selected_gdp_countries:

        filtered_gdp_df = annual_gdp_df[
            annual_gdp_df["country_code"].isin(selected_gdp_countries)
        ]

        gdp_fig = px.line(
            filtered_gdp_df,
            x="year",
            y="GDP_per_capita_PPP",
            color="country_code",
            title="GDP per Capita (PPP) Across European Countries (2006–2025)",
            labels={
                "year": "Year",
                "GDP_per_capita_PPP": "GDP per Capita (PPP)",
                "country_code": "Country"
            }
        )

        gdp_fig.update_layout(
            template="plotly_white",
            hovermode="x unified",
            yaxis_title="GDP per Capita (PPP)"
        )

        st.plotly_chart(
    gdp_fig,
    use_container_width=True,
    key="individual_gdp_chart"
)

    else:
        st.info("Please select at least one country to compare.")

    # Assign each country to its European region
    country_region_mapping = {
        country: region
        for region, countries in country_regions.items()
        for country in countries
    }

    annual_gdp_df["Region"] = annual_gdp_df["country_code"].map(
        country_region_mapping
    )

    # Calculate average GDP per capita by European region
    regional_gdp_df = (
        annual_gdp_df.groupby(["Region", "year"])["GDP_per_capita_PPP"]
        .mean()
        .reset_index()
    )

    # Create the regional GDP comparison chart
    st.divider()
    st.subheader("Economic Performance by European Region")

    regional_gdp_fig = px.bar(
    regional_gdp_df,
    x="year",
    y="GDP_per_capita_PPP",
    color="Region",
    barmode="group",
    title="Average GDP per Capita (PPP) by European Region (2006–2025)",
    labels={
        "year": "Year",
        "GDP_per_capita_PPP": "Average GDP per Capita (PPP)",
        "Region": "European Region"
    }
)

    regional_gdp_fig.update_layout(
        template="plotly_white",
        hovermode="x unified",
        yaxis_title="Average GDP per Capita (PPP)"
    )

    
    # Display the regional GDP chart
    st.plotly_chart(
    regional_gdp_fig,
    use_container_width=True,
    key="regional_gdp_chart"
)
     # Calculate GDP growth by European region
    regional_growth = (
        regional_gdp_df.sort_values("year")
        .groupby("Region")["GDP_per_capita_PPP"]
        .agg(
            first_value="first",
            last_value="last"
        )
        .reset_index()
    )

    regional_growth["Growth_Percentage"] = (
        (regional_growth["last_value"] / regional_growth["first_value"] - 1) * 100
    )

    # Display GDP growth indicators by region
    st.divider()
    st.subheader("GDP Growth Across European Regions (2006–2025)")

    col1, col2, col3, col4 = st.columns(4)

    region_order = [
        "Northern Europe",
        "Southern Europe",
        "Western Europe",
        "Eastern Europe"
    ]

    for col, region in zip(
        [col1, col2, col3, col4],
        region_order
    ):
        region_result = regional_growth[
            regional_growth["Region"] == region
        ]

        with col:
            if not region_result.empty:
                growth = region_result["Growth_Percentage"].iloc[0]

                st.metric(
                    label=region,
                    value=f"{growth:.2f}%",
                    delta="GDP per capita growth"
                )
            else:
                st.metric(
                    label=region,
                    value="N/A"
                )
        # Create a horizontal bar chart for regional GDP growth
    regional_growth_fig = px.bar(
        regional_growth,
        x="Growth_Percentage",
        y="Region",
        orientation="h",
        color="Region",
        text="Growth_Percentage",
        title="GDP per Capita Growth by European Region (2006–2025)",
        labels={
            "Growth_Percentage": "GDP Growth (%)",
            "Region": "European Region"
        }
    )

    regional_growth_fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    regional_growth_fig.update_layout(
        template="plotly_white",
        showlegend=False,
        xaxis_title="GDP Growth (%)",
        yaxis_title="European Region"
    )

    st.plotly_chart(
        regional_growth_fig,
        use_container_width=True,
        key="regional_growth_bar_chart"
    )       
    # Brexit Analysis
if page == "Brexit Analysis":

    st.subheader("Brexit Analysis")

    st.write("""
    Explore the economic differences between the United Kingdom
    and the EU27 before, during and after the Brexit transition.

    The analysis covers the period from 2006 to 2025.
    """)
    
    # Prepare annual GDP per capita data
    brexit_gdp_df = europe_df.copy()

    brexit_gdp_df["year"] = pd.to_numeric(
        brexit_gdp_df["year"],
        errors="coerce"
    )

    brexit_gdp_df["GDP_per_capita_PPP"] = pd.to_numeric(
        brexit_gdp_df["GDP_per_capita_PPP"],
        errors="coerce"
    )

    # Calculate annual GDP per capita for each country
    annual_brexit_gdp_df = (
        brexit_gdp_df.groupby(["country_code", "year"])["GDP_per_capita_PPP"]
        .mean()
        .reset_index()
    )

    # Calculate UK GDP per capita
    uk_gdp_df = annual_brexit_gdp_df[
        annual_brexit_gdp_df["country_code"] == "UK"
    ][["year", "GDP_per_capita_PPP"]].copy()

    uk_gdp_df["Group"] = "United Kingdom"

    # Calculate average EU27 GDP per capita
    eu27_gdp_df = annual_brexit_gdp_df[
        annual_brexit_gdp_df["country_code"] != "UK"
    ].groupby("year")["GDP_per_capita_PPP"].mean().reset_index()

    eu27_gdp_df["Group"] = "EU27 Average"

    # Combine UK and EU27 data
    brexit_comparison_df = pd.concat(
        [uk_gdp_df, eu27_gdp_df],
        ignore_index=True
    )

    # Create the GDP comparison chart
    st.divider()
    st.subheader("UK vs EU27 GDP per Capita (PPP)")

    brexit_gdp_fig = px.line(
        brexit_comparison_df,
        x="year",
        y="GDP_per_capita_PPP",
        color="Group",
        markers=True,
        title="UK vs EU27 Average GDP per Capita (PPP), 2006–2025",
        labels={
            "year": "Year",
            "GDP_per_capita_PPP": "GDP per Capita (PPP)",
            "Group": "Comparison"
        }
    )

    brexit_gdp_fig.update_layout(
        template="plotly_white",
        hovermode="x unified",
        yaxis_title="GDP per Capita (PPP)"
    )

    st.plotly_chart(
        brexit_gdp_fig,
        use_container_width=True,
        key="brexit_gdp_comparison"
    )
    
    # Define the Brexit periods
    brexit_periods = {
        "Pre-referendum (2006–2015)": (2006, 2015),
        "Referendum and transition (2016–2020)": (2016, 2020),
        "Post-transition (2021–2025)": (2021, 2025)
    }

    # Assign each year to a Brexit period
    brexit_comparison_df["Brexit_Period"] = brexit_comparison_df["year"].apply(
        lambda year: next(
            (
                period for period, (start, end) in brexit_periods.items()
                if start <= year <= end
            ),
            None
        )
    )

    # Calculate average GDP per capita by period
    period_gdp_df = (
        brexit_comparison_df.groupby(["Group", "Brexit_Period"])["GDP_per_capita_PPP"]
        .mean()
        .reset_index()
    )

    # Create the Brexit period comparison chart
    st.divider()
    st.subheader("UK vs EU27 GDP per Capita Across Brexit Periods")

    period_gdp_fig = px.bar(
        period_gdp_df,
        x="Brexit_Period",
        y="GDP_per_capita_PPP",
        color="Group",
        barmode="group",
                category_orders={
            "Brexit_Period": [                
                "Pre-referendum (2006–2015)",
                "Referendum and transition (2016–2020)",
                "Post-transition (2021–2025)"
            ]
        },
        title="Average GDP per Capita (PPP) Before, During and After Brexit",
        labels={
            "Brexit_Period": "Brexit Period",
            "GDP_per_capita_PPP": "Average GDP per Capita (PPP)",
            "Group": "Comparison"
        }
    )

    period_gdp_fig.update_layout(
        template="plotly_white",
        xaxis_title="Brexit Period",
        yaxis_title="Average GDP per Capita (PPP)",
        hovermode="x unified"
    )

    st.plotly_chart(
        period_gdp_fig,
        use_container_width=True,
        key="brexit_period_gdp_chart"
    )
    # Prepare GBP/EUR exchange-rate data
    exchange_rate_df = europe_df[
        ["month", "GBP_per_EUR"]
    ].copy()

    exchange_rate_df["month"] = pd.to_datetime(
        exchange_rate_df["month"],
        errors="coerce"
    )

    exchange_rate_df["GBP_per_EUR"] = pd.to_numeric(
        exchange_rate_df["GBP_per_EUR"],
        errors="coerce"
    )

    exchange_rate_df = exchange_rate_df.dropna(
        subset=["month", "GBP_per_EUR"]
    )

    
    # Remove duplicate monthly exchange-rate records
    exchange_rate_df = exchange_rate_df.drop_duplicates(
        subset=["month"]
    )

    # Sort exchange-rate data by month
    exchange_rate_df = exchange_rate_df.sort_values("month")

    # Create the GBP/EUR exchange-rate chart
    st.divider()
    st.subheader("British Pound vs Euro Exchange Rate")

    exchange_rate_fig = px.line(
        exchange_rate_df,
        x="month",
        y="GBP_per_EUR",
        title="GBP per EUR Exchange Rate (2006–2025)",
        labels={
            "month": "Year",
            "GBP_per_EUR": "GBP per EUR"
        }
    )

    exchange_rate_fig.update_layout(
        template="plotly_white",
        hovermode="x unified",
        yaxis_title="GBP per EUR"
    )

    st.plotly_chart(
        exchange_rate_fig,
        use_container_width=True,
        key="brexit_exchange_rate_chart"
    )

    # Real purchasing power comparison
    st.divider()
    st.subheader("The Real Purchasing Power Story")

    real_value_df["month"] = pd.to_datetime(
        real_value_df["month"]
    )

    real_value_fig = px.line(
        real_value_df,
        x="month",
        y=["real_savings_value", "real_investment_value"],
        title="Real Value of €10,000 After Inflation (2006–2025)",
        labels={
            "month": "Year",
            "value": "Real Value (€)",
            "variable": "Financial Approach"
        }
    )

    real_value_fig.update_layout(
        template="plotly_white",
        hovermode="x unified",
        yaxis_title="Real Value (€)",
        legend_title="Financial Approach"
    )

    st.plotly_chart(
        real_value_fig,
        use_container_width=True,
        key="brexit_real_purchasing_power"
    )
# Conclusion
if page == "Conclusion":

    st.subheader("Conclusion")
    # Key project findings
    st.divider()
    st.subheader("Key Findings")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Final Savings Value", "€10,722.09")
    col2.metric("Final Investment Value", "€18,012.89")
    col3.metric("Real Savings Value", "€7,063.37")
    col4.metric("Real Investment Value", "€11,866.32")

    st.divider()

    st.write("""
    This project explored how savings, investments and inflation
    affected the purchasing power of money across Europe between
    2006 and 2025.

    The results show that saving money provided a modest nominal
    return, but inflation significantly reduced its real value.
    Investing in the EURO STOXX price index produced a stronger
    result over the same period, although past performance does
    not guarantee future returns.

    The analysis also highlighted differences in inflation and
    economic performance across European regions, as well as
    changes in the UK's economic indicators around Brexit.

    Overall, the findings demonstrate why inflation-adjusted
    returns are important when evaluating the long-term value
    of savings and investments.
    """)
        # Key takeaways
    st.divider()
    st.subheader("Key Takeaways")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 💶 Inflation")
        st.write(
            "Inflation reduced the purchasing power of savings "
            "over the 20-year period."
        )

    with col2:
        st.markdown("### 📈 Investment Performance")
        st.write(
            "The EURO STOXX price index outperformed savings "
            "in this simulation, even after inflation."
        )

    with col3:
        st.markdown("### 🌍 European Economies")
        st.write(
            "Inflation and economic trends differed across regions. "
            "The UK comparison also requires careful interpretation "
            "because of data limitations."
        )


# Website footer
st.divider()

st.html("""
<div style="
    text-align: center;
    padding: 20px 0;
">

    <p style="color: #174B35; font-weight: 600;">
        Saving vs Investing: The Real Value of Money Over Time
    </p>

    <p style="color: #777777; font-size: 13px;">
        Built with Python | Pandas | Streamlit | Plotly
    </p>

    <p style="color: #777777; font-size: 12px;">
        European Financial Analysis | 2006–2025
    </p>

</div>
""")
        


