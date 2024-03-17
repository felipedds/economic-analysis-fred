## Predicting the Consumer Price Index For All Urban Consumers (CPI-U) using Economic Indicators

#### Description:

This project aims to predict the Consumer Price Index for All Urban Consumers (CPI-U) in the United States by leveraging various economic indicators. The CPI is a crucial measure of inflation, reflecting changes in the cost of living over time. By accurately forecasting CPI movements, policymakers, economists, and businesses can make informed decisions about monetary policy, budgeting, and investment strategies.

#### Data Sources: 
The project utilizes data from multiple sources, including:
- Unemployment Rate: A measure of the percentage of the total labor force that is unemployed but actively seeking employment.
- Labor Force Participation Rate: The proportion of the working-age population that is either employed or actively seeking employment.
- Treasury and Agency Securities: Data on the yields and performance of government and agency bonds, which reflect market sentiment and economic conditions.
All Commercial Banks Data: Information on various financial metrics and activities within the commercial banking sector, providing insights into lending practices and liquidity.

#### Objective:<br>
The primary goal is to build a robust predictive model capable of forecasting CPI movements based on changes in the selected economic indicators. The model's performance will be assessed using appropriate evaluation metrics, such as mean absolute error or root mean squared error, to ensure its reliability and effectiveness.

#### Modeling Approach:<br>
Machine learning algorithms, such as regression models, will be employed to analyze the relationships between the CPI and the economic indicators. Feature engineering, data preprocessing, and model evaluation will be key stages in developing accurate predictive models.

#### Implications:<br>
Accurate CPI predictions have significant implications for various stakeholders, including policymakers, investors, businesses, and consumers. Understanding future inflation trends can inform monetary policy decisions, asset allocation strategies, pricing decisions, and budget planning.

## Project Structure
```
economic-analysis-fred/
├── data/
│   ├── raw/                 # Raw data files
│   ├── processed/           # Processed data files
│   └── external/            # External datasets or data obtained from external sources
├── notebooks/               # Jupyter notebooks for data exploration, and analysis
├── src/                     # Source code
│   ├── data_preprocessing/  # Scripts or modules for data preprocessing
│   ├── feature_engineering/ # Scripts or modules for feature engineering
│   ├── modeling/            # Scripts or modules for modeling (machine learning models)
│   └── evaluation/          # Scripts for model evaluation and performance metrics
├── reports/                 # Reports generated(HTML, PDF) from analysis and modeling
├── models/                  # Saved models or model artifacts
├── environment.yml          # Conda environment file specifying dependencies
├── README.md                # README file describing the project and its components
└── requirements.txt         # Python dependencies file (alternative to environment.yml)
```

## Useful Links
Economic Data Analysis from FRED - Federal Reserve Economic Data Website: (https://fred.stlouisfed.org/).
Developer API: https://research.stlouisfed.org/docs/api/
