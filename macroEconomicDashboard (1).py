#Install FRED Api
!pip install fredapi

#Install Streamlit
!pip install streamlit

#import packages and modules
import fredapi as fa
import pandas as pd
fred = fa.Fred('f100ba61e4bd10d03095db8591149d4f')

##################################################
#Get Desired Metrics

#GDP (Quarterly)
gdp = fred.get_series('GDP')
gdpData = pd.DataFrame(gdp)
gdpData.index.name = 'Date'
gdpData.rename(columns={gdpData.columns[0]: 'Value'}, inplace=True)

#Government total expenditures (Quarterly)
governmentExpenditures = fred.get_series('W068RCQ027SBEA')
governmentExpendituresData = pd.DataFrame(governmentExpenditures)
governmentExpendituresData.index.name = 'Date'
governmentExpendituresData.rename(columns={governmentExpendituresData.columns[0]: 'Value'}, inplace=True)

#Personal Consumption Expenditures (Monthly)
personalConsumptionExpenditures = fred.get_series('PCE')
personalConsumptionExpendituresData = pd.DataFrame(personalConsumptionExpenditures)
personalConsumptionExpendituresData.index.name = 'Date'
personalConsumptionExpendituresData.rename(columns={personalConsumptionExpendituresData.columns[0]: 'Value'}, inplace=True)

#Unemployment Rate (Monthly)
unemploymentRate = fred.get_series('UNRATE')
unemploymentRateData = pd.DataFrame(unemploymentRate)
unemploymentRateData.index.name = 'Date'
unemploymentRateData.rename(columns={unemploymentRateData.columns[0]: 'Value'}, inplace=True)

#Consumer Price Index - Total All Items for the United States (Monthly)
consumerPriceIndex = fred.get_series('CPALTT01USM657N')
consumerPriceIndexData = pd.DataFrame(consumerPriceIndex)
consumerPriceIndexData.index.name = 'Date'
consumerPriceIndexData.rename(columns={consumerPriceIndexData.columns[0]: 'Value'}, inplace=True)

#Market Yield on U.S. Treasury Securities at 2-Year Constant Maturity (Daily)
twoYearTreasuryYield = fred.get_series('DGS2')
twoYearTreasuryYieldData = pd.DataFrame(twoYearTreasuryYield)
twoYearTreasuryYieldData.index.name = 'Date'
twoYearTreasuryYieldData.rename(columns={twoYearTreasuryYieldData.columns[0]: 'Value'}, inplace=True)

#Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity (Daily)
tenYearTreasuryYield = fred.get_series('DGS10')
tenYearTreasuryYieldData = pd.DataFrame(tenYearTreasuryYield)
tenYearTreasuryYieldData.index.name = 'Date'
tenYearTreasuryYieldData.rename(columns={tenYearTreasuryYieldData.columns[0]: 'Value'}, inplace=True)

#Federal Funds Effective Rate (Daily, 7-day)
fedFundsRate = fred.get_series('DFF')
fedFundsRateData = pd.DataFrame(fedFundsRate)
fedFundsRateData.index.name = 'Date'
fedFundsRateData.rename(columns={fedFundsRateData.columns[0]: 'Value'}, inplace=True)

# S&P 500 (Daily, Close)
sandp500 = fred.get_series('SP500')
sandp500Data = pd.DataFrame(sandp500)
sandp500Data.index.name = 'Date'
sandp500Data.rename(columns={sandp500Data.columns[0]: 'Value'}, inplace=True)

# NASDAQ Composite Index (Daily, Close)
nasdaq = fred.get_series('NASDAQCOM')
nasdaqData = pd.DataFrame(nasdaq)
nasdaqData.index.name = 'Date'
nasdaqData.rename(columns={nasdaqData.columns[0]: 'Value'}, inplace=True)

#Create Dashboard
import streamlit as st
import pandas as pd
import plotly.express as px

df_dict = {
    "GDP": gdpData,
    "Government Expenditures": governmentExpendituresData,
    "Personal Consumption Expenditures": personalConsumptionExpendituresData,
    "Unemployment Rate": unemploymentRateData,
    "Consumer Price Index": consumerPriceIndexData,
    "Two Year Treasury Yield": twoYearTreasuryYieldData,
    "Ten Year Treasury Yield": tenYearTreasuryYieldData,
    "Federal Funds Rate": fedFundsRateData,
    "S&P 500": sandp500Data,
    "NASDAQ": nasdaqData
}

# Streamlit App
st.title('Macroeconomic Data Dashboard')

# Dropdown to select the DataFrame
selected_df = st.selectbox("Select the Dataframe to View", list(df_dict.keys()))

# Show the selected dataframe
st.write(f"Displaying data for {selected_df}")
st.dataframe(df_dict[selected_df])


# Plotting
# Assuming each dataframe has a 'Date' column and a 'Value' column
st.write(f"Plotting data for {selected_df}")
fig = px.line(df_dict[selected_df], x='Value', y='Value', title=f"{selected_df} Over Time")
st.plotly_chart(fig)