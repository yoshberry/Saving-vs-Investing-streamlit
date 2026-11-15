# Saving vs Investing: The Real Value of Money Over Time

An interactive data analytics project exploring how savings returns, investment performance and inflation affected purchasing power across Europe between 2006 and 2025.

**[View the Live Interactive Dashboard](https://saving-vs-investing-europe.streamlit.app)**

## Project Overview

This project investigates how the value of money has changed over the past 20 years across the EU27 and the United Kingdom.

Using historical economic and financial data, it compares savings returns, investment performance and inflation to understand how different financial choices affect real purchasing power over time.

The analysis also explores differences between European economies and examines the UK's economic performance across the Brexit periods.

## Research Question

How have savings returns, investment performance and inflation affected real purchasing power across European economies over 2006–2025, and how does the UK compare with EU countries before and after Brexit?

## Project Scope

- **Geographical coverage:** EU27 countries and the United Kingdom
- **Historical period:** January 2006 – December 2025
- **Simulation currency:** EUR
- **Initial investment:** €10,000
- **Main comparisons:** Savings, investment performance, inflation and economic development

## Key Findings

The simulation highlights the difference between nominal returns and real purchasing power.

| Indicator | Final result |
|---|---:|
| Initial amount | €10,000 |
| Final savings value | €10,722.09 |
| Final investment value | €18,012.89 |
| Real savings value | €7,063.37 |
| Real investment value | €11,866.32 |

After adjusting for inflation:

- Savings experienced a cumulative real return of approximately **-29.37%**.
- The investment simulation achieved a cumulative real return of approximately **+18.66%**.
- The difference between the two real returns was approximately **48.03 percentage points**.

These results illustrate how inflation can reduce purchasing power even when the nominal value of savings increases.

## Interactive Dashboard

The Streamlit application contains six sections:

1. **Project Overview** – Research objectives, scope and key insights.
2. **Inflation Across Europe** – Country-level inflation trends and comparisons.
3. **Savings vs Investment** – Nominal and inflation-adjusted performance.
4. **European Economies** – GDP per capita and regional economic comparisons.
5. **Brexit Analysis** – UK and EU27 economic comparisons across Brexit periods.
6. **Conclusion** – Main findings and takeaways.

## Tools and Technologies

- Python
- Pandas
- Plotly
- Streamlit
- Jupyter Notebook
- Git and GitHub

## Data Sources

The analysis uses historical datasets from:

- Eurostat – Harmonised Index of Consumer Prices (HICP)
- European Central Bank (ECB) – Savings interest rates
- Bank of England – UK household savings rates
- World Bank – GDP per capita, purchasing power parity
- Historical EUR/GBP exchange-rate data
- EURO STOXX investment index data

## Methodology

The project combines data cleaning, exploratory data analysis, financial calculations and interactive visualisation.

The €10,000 simulation compares the development of savings and investment values over time. Results are also adjusted for inflation to estimate changes in purchasing power.

Brexit comparisons use three descriptive periods:

- Pre-referendum: 2006–2015
- Referendum and transition: 2016–2020
- Post-transition: 2021–2025

## Important Limitations

- The EURO STOXX price index excludes dividends, so it does not represent total investment returns.
- ECB Euro Area savings rates are aggregate figures, not individual country-level rates.
- UK and Euro Area savings-rate definitions are not identical.
- UK HICP data in the selected dataset ends in November 2020.
- GDP per capita PPP is used as an economic indicator, not as a direct measure of household wealth or disposable income.
- Brexit comparisons are descriptive and do not establish causation.

## Run the Project Locally

Clone the repository:

```bash
git clone https://github.com/yoshberry/Saving-vs-Investing-streamlit.git
```

Navigate into the project:

```bash
cd Saving-vs-Investing-streamlit
```

Create and activate a virtual environment, then install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Project Purpose

This project demonstrates how data analytics can be used to explore real-world financial and economic questions, transform historical datasets into meaningful insights, and communicate findings through interactive dashboards.

**Built with Python | Pandas | Plotly | Streamlit**
