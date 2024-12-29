# Data Analysis Covid19 Impact Taxi Project Research
![Data Analysis](https://www.mindinventory.com/blog/wp-content/uploads/2022/10/uber-like-app-cost.jpg)
**by Serhii Spitsyn**

## Description
The research date project of the impact of the Covid-19 epidemic on the trips of the New York City Taxi and Limousine Service (TLC) for the period 2015-2023.

## Project Stages

1. **Data Collection**: Gathering comprehensive datasets from NYC Taxi and Limousine Commission.
2. **Preprocessing**: Cleaning, formatting, and converting raw data for analysis.
3. **Exploratory Data Analysis (EDA)**: Generating visualizations and insights.
4. **Modeling and Predictions**: Building models to predict trends.
5. **Reporting and Documentation**: Summarizing findings and preparing this README.

## Project Scope and Data
The project's scope encompasses analyzing the effects of the Covid-19 epidemic on taxi trips within the New York City Taxi and Limousine Service (TLC) from 2015 to 2023. The dataset selected for analysis was chosen based on its accuracy and comprehensive data content. It includes data for each month throughout the specified period.

## Dataset Details
- Number of Data Files Processed: 328
- Total Data: 124 Gb

### Data Taxi dictionary

[Taxi Trip Records Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

### Describe Taxi data
Yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. The data used in the attached datasets were collected and provided to the NYC Taxi and Limousine Commission (TLC) by technology providers authorized under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP). The trip data was not created by the TLC, and TLC makes no representations as to the accuracy of these data.

For-Hire Vehicle (“FHV”) trip records include fields capturing the dispatching base license number and the pick-up date, time, and taxi zone location ID (shape file below). These records are generated from the FHV Trip Record submissions made by bases. Note: The TLC publishes base trip record data as submitted by the bases, and we cannot guarantee or confirm their accuracy or completeness. Therefore, this may not represent the total amount of trips dispatched by all TLC-licensed bases. The TLC performs routine reviews of the records and takes enforcement actions when necessary to ensure, to the extent possible, complete and accurate information.

### Yellow NYC Taxi Trip Records Dictionary
This document provides a data dictionary for the New York City Taxi Trip Records dataset, specifically focusing on the yellow taxi trips. The dataset is made available by the NYC Taxi and Limousine Commission (TLC).

### Data Yellow NYC Taxi Trip Records Fields
Field Name              | Description                                                                                           
------------------------|-------------------------------------------------------------------------------------------------------
VendorID                | A code indicating the TPEP provider that provided the record. 1= Creative Mobile Technologies, LLC; 2= VeriFone Inc.
tpep_pickup_datetime   | The date and time when the meter was engaged.
tpep_dropoff_datetime  | The date and time when the meter was disengaged.
Passenger_count         | The number of passengers in the vehicle. This is a driver-entered value.
Trip_distance           | The elapsed trip distance in miles reported by the taximeter.
PULocationID            | TLC Taxi Zone in which the taximeter was engaged.
DOLocationID            | TLC Taxi Zone in which the taximeter was disengaged.
RateCodeID              | The final rate code in effect at the end of the trip. 1= Standard rate, 2= JFK, 3= Newark, 4= Nassau or Westchester, 5= Negotiated fare, 6= Group ride.
Store_and_fwd_flag      | This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka “store and forward,” because the vehicle did not have a connection to the server. Y= store and forward trip, N= not a store and forward trip.
Payment_type            | A numeric code signifying how the passenger paid for the trip. 1= Credit card, 2= Cash, 3= No charge, 4= Dispute, 5= Unknown, 6= Voided trip.
Fare_amount             | The time-and-distance fare calculated by the meter.
Extra                   | Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges.
MTA_tax                 | $0.50 MTA tax that is automatically triggered based on the metered rate in use.
Improvement_surcharge   | $0.30 improvement surcharge assessed trips at the flag drop. The improvement surcharge began being levied in 2015.
Tip_amount              | Tip amount – This field is automatically populated for credit card tips. Cash tips are not included.
Tolls_amount            | Total amount of all tolls paid in trip.
Total_amount            | The total amount charged to passengers. Does not include cash tips.
Congestion_Surcharge    | Total amount collected in trip for NYS congestion surcharge.
Airport_fee             | $1.25 for pick up only at LaGuardia and John F. Kennedy Airports.

For more detailed information, refer to the [NYC Taxi Trip Records Yellow Data Dictionary PDF.](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)

### Green NYC Taxi Trip Records Dictionary
This document provides a data dictionary for the New York City Taxi Trip Records dataset, specifically focusing on the green taxi trips. The dataset is made available by the NYC Taxi and Limousine Commission (TLC).

### Data Green NYC Taxi Trip Records Fields
Field Name               | Description                                                                                          
------------------------|-----------------------------------------------------------------------------------------------------
VendorID                 | A code indicating the LPEP provider that provided the record. 1= Creative Mobile Technologies, LLC; 2= VeriFone Inc.
lpep_pickup_datetime    | The date and time when the meter was engaged.
lpep_dropoff_datetime   | The date and time when the meter was disengaged.
Passenger_count         | The number of passengers in the vehicle. This is a driver-entered value.
Trip_distance           | The elapsed trip distance in miles reported by the taximeter.
PULocationID            | TLC Taxi Zone in which the taximeter was engaged.
DOLocationID            | TLC Taxi Zone in which the taximeter was disengaged.
RateCodeID              | The final rate code in effect at the end of the trip. 1= Standard rate, 2= JFK, 3= Newark, 4= Nassau or Westchester, 5= Negotiated fare, 6= Group ride.
Store_and_fwd_flag      | This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka “store and forward,” because the vehicle did not have a connection to the server. Y= store and forward trip, N= not a store and forward trip.
Payment_type            | A numeric code signifying how the passenger paid for the trip. 1= Credit card, 2= Cash, 3= No charge, 4= Dispute, 5= Unknown, 6= Voided trip.
Fare_amount             | The time-and-distance fare calculated by the meter.
Extra                   | Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges.
MTA_tax                 | $0.50 MTA tax that is automatically triggered based on the metered rate in use.
Improvement_surcharge   | $0.30 improvement surcharge assessed on hailed trips at the flag drop. The improvement surcharge began being levied in 2015.
Tip_amount              | Tip amount – This field is automatically populated for credit card tips. Cash tips are not included.
Tolls_amount            | Total amount of all tolls paid in trip.
Total_amount            | The total amount charged to passengers. Does not include cash tips.
Trip_type               | A code indicating whether the trip was a street-hail or a dispatch that is automatically assigned based on the metered rate in use but can be altered by the driver. 1= Street-hail, 2= Dispatch.

For more detailed information, refer to the [NYC Taxi Trip Records Green Data Dictionary PDF.](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_green.pdf)

### FHV Trip Records
This document provides a data dictionary for the New York City Taxi Trip Records dataset, specifically focusing on the For-Hire Vehicle (FHV) trips. The dataset is made available by the NYC Taxi and Limousine Commission (TLC).

### Data FHV Trip Records Fields
Field Name                | Description                                                                                          
--------------------------|-------------------------------------------------------------------------------------------------------
dispatching_base_num      | TLC base license number of the base that dispatched the trip.
Pickup_date               | The date of the trip.
locationID                | TLC Taxi Zone in which the trip ended.
PUlocationID              | TLC Taxi Zone in which the trip began.

For more detailed information, refer to the [NYC Taxi Trip Records For-Hire Vehicle (FHV) Data Dictionary PDF.](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_fhv.pdf)

### Convector Problem
During the initial attempts to convert Parquet files to CSV format, numerous errors occurred due to invalid or incomplete data. The most common issues included:
- Invalid timestamps, such as those exceeding allowed ranges or having incorrect formats.
- Unexpected data structures causing processing failures.

To ensure successful conversion and minimize data loss, a new converter script with enhanced error handling was developed.

### Solution
The new script **`parquet_to_csv_convector_error_protection.py`** addresses these issues by:
- Cleaning problematic timestamps using the `clean_timestamps` function, which converts invalid dates to a valid format or marks them as `NaT` (Not a Time).
- Processing all columns in a Parquet file and saving the data as a DataFrame for CSV conversion.

### Key Functionalities
- **Timestamp Cleaning:** Automatically handles invalid values in columns with the "timestamp" type.
- **Flexible Conversion:** Supports all data types, including text, numeric, and timestamp columns.
- **Data Preservation:** Saves cleaned data into `output.csv` without losing structure or validity.

## Purpose of the Project
The primary goal of this project is to understand the impact of the Covid-19 pandemic on NYC's taxi services and provide actionable insights into usage patterns and their correlation with public health data.

## Methodology
The analysis was conducted in the following steps:
- **Data Integration**: Combining taxi and Covid-19 datasets.
- **Time Series Analysis**: Examining trends over time.
- **Geospatial Analysis**: Mapping trip data across NYC boroughs.
- **Statistical Modeling**: Identifying key correlations and predictive factors.

## Visialization
#### Taxi Trips vs COVID-19 Cases in NYC
![Taxi Trips vs COVID-19 Cases in NYC](https://raw.githubusercontent.com/ShamansIT/PFDA/refs/heads/main/project/Plot/Taxi%20Trips%20vs%20COVID-19%20Cases%20in%20NYC_visual_02.png)
#### Fare Amount, Extra Charges and Tips for Yellow Taxi
![Fare Amount, Extra Charges and Tips for Yellow Taxi](https://raw.githubusercontent.com/ShamansIT/PFDA/refs/heads/main/project/Plot/Fare%20Amount%2C%20Extra%20Charges%2C%20and%20Tips%20-%20Yellow%20Taxi.png)
#### Fare Amount, Extra Charges and Tips for Green Taxi
![Fare Amount, Extra Charges and Tips for Green Taxi](https://raw.githubusercontent.com/ShamansIT/PFDA/refs/heads/main/project/Plot/Fare%20Amount%2C%20Extra%20Charges%2C%20and%20Tips%20-%20Green%20Taxi.png)

## Conclusions
As can be concluded from the visualizations, there was a noticeable decline in demand for taxis at the beginning of the epidemic, coinciding with a significant outbreak of registered hospitalizations for Covid-19 in early 2022. 

The data also reveal a significant drop in tips at the onset of the epidemic. For Yellow Taxis, the tips volume gradually increased after the initial decline, demonstrating some recovery. In contrast, Green Taxis showed no positive trend in tip volume after the fall, indicating a potential disparity in recovery between the two services.

### Final Thoughts
This analysis highlights the resilience of NYC’s taxi system and the importance of data-driven decision-making for public transport policies during crises.

## Requirements
To complete the project, you must have:
- Python 3.8+
- Jupyter Notebook
- Seaborn
- Pandas
- Matplotlib

## Project Structure
project/
  - data_sort/                     # Directory containing raw and processed data
  - Plot/                          # Generated charts and graphs
  - data_exploration.ipynb         # Jupyter Notebook for analysis
  - parquet_to_csv_convector.py    # Script for converting .parquet to .csv
  - parquet_to_csv_convector_error_protection.py    # Script for converting .parquet to .csv
  - Readme.md                      # Project documentation

## Reference
- [TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [COVID-19 Daily Counts of Cases, Hospitalizations, and Deaths](https://data.cityofnewyork.us/Health/COVID-19-Daily-Counts-of-Cases-Hospitalizations-an/rc75-m7u3/about_data)
- [Comprehensive Literature Review on the Impacts of COVID-19 Pandemic on Public Road Transportation System: Challenges and Solutions](https://www.mdpi.com/2071-1050/14/15/9586)
- [Towards socially equitable public transport systems: The effect of COVID-19 on taxi trip behavior](https://www.sciencedirect.com/science/article/abs/pii/S2213624X24001603)
- [Seaborn: statistical data visualization](https://seaborn.pydata.org/)
- [Matplotlib Plot style](https://matplotlib.org/stable/plot_types/index)
- [Python Seaborn Tutorial](https://www.datacamp.com/tutorial/seaborn-python-tutorial)


### Contribution to the project
Contributions are welcome! You can help improve the project by opening an issue or creating a pull request.

## Contact Information
- <serhii.spitsyn.ie@gmail.com>
- [GitHub](https://github.com/ShamansIT)
