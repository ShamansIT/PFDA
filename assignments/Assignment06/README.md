# Knock airport Weather
This project analyzes weather data from Knock Airport, focusing on temperature, wind speed, and other meteorological parameters. The analysis was performed in Jupyter Notebook, with focus on data analysis and visualization, including color gradients for better visual representation.

## Data Information
The data contains information on weather conditions with the following fields:
- **date**: Date and Time (UTC)
- **rain**: Precipitation Amount (mm)
- **temp**: Air Temperature (°C)
- **wetb**: Wet Bulb Temperature (°C)
- **dewpt**: Dew Point Temperature (°C)
- **rhum**: Relative Humidity (%)
- **vappr**: Vapour Pressure (hPa)
- **msl**: Mean Sea Level Pressure (hPa)
- **wdsp**: Mean Wind Speed (knots)
- **wddir**: Predominant Wind Direction (degrees)
- **ww**: Synop code for Present Weather
- **w**: Synop code for Past Weather
- **sun**: Sunshine duration (hours)
- **vis**: Visibility (m)
- **clht**: Cloud height (100's of feet) - 999 if none
- **clamt**: Cloud amount
- **ind**: Indicator

- **Station Name**: KNOCK AIRPORT
- **Station Height**: 201 M 
- **Latitude**:53.906  ,Longitude: -8.817

## Analysis and Visualization
The project is organized into several logical blocks, each containing data processing, calculations, or visualization of specific aspects of the weather data. Each plot is separated by blocks in the Jupyter Notebook for convenience.

### Key Steps of Analysis
#### Loading and Preparing Data:
- Import libraries.
- Load data from the .csv file.
- Convert the date column to datetime format for easier processing.

#### Temperature Visualization:
- **Temperature Over Time**: Plot of temperature over all dates, with color gradient representing temperature values (viridis color scheme).
- **Daily Mean Temperature**: Plot of the mean daily temperature, with color gradient for daily mean values (plasma color scheme).
- **Monthly Mean Temperature**: Plot of the monthly mean temperature with color gradient for average monthly values (inferno color scheme).

#### Wind Speed Over Time: 
Plot of wind speed with color gradient representing wind speed values (magma color scheme), including a 24-hour rolling mean line.
- **24-hour Rolling Mean Wind Speed**: Separate plot for the 24-hour rolling mean wind speed with a color gradient (Spectral color scheme).
- **Daily Max Wind Speed**: Plot of the daily maximum wind speed with a color gradient for daily maximum values (coolwarm color scheme).
- **Monthly Mean of Daily Max Wind Speed**: Plot of the monthly mean of daily maximum wind speeds with a color gradient for monthly mean values (cividis color scheme).

### Project Features
- **Handling Missing Values**: Missing data in key columns such as temp and wdsp is processed to ensure accurate calculations.
- **Grouping and Aggregation**: Data is grouped by day and month to calculate mean and maximum values.
- **Color Gradients**: All plots include a color gradient that reflects variable values for better visual comprehension.

## Results
- **Temperature Plots**: Complete visualizations for temperature, daily mean, and monthly mean temperature with color gradients.
- **Wind Speed Plots**: Plots for wind speed over time, a 24-hour rolling mean, as well as daily maximum and monthly mean of daily maximum wind speeds.

This project provides a detailed insight into the weather conditions at Knock Airport, particularly in terms of temperature and wind speed variations over the observed period.

## File Structure
- **hly4935.csv**: Input data from the weather station.
- **assignment_6_Weather.ipynb**: Jupyter Notebook with code and visualizations.
- **README.md**: Project description.

## Reason of adding this file in project
Although adding a Readme.md file was not in the requirements for the project, it was still decided to add it to the project for the following reasons:
- when importing data, a description of the data was found and I could not just throw this description away and wanted to leave it in the project
- the Readme.md file with only the description of the Data looked incomplete and illogical, so I decided to add the description of the program as it is usually done.
