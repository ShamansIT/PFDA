"""
Converts Parquet files to a CSV file.

The files had an error related to the content of the files or incomplete data during the conversion.
The list of files for which this convector was used:
    fhv_tripdata_2017-06
    fhv_tripdata_2018-05
    fhv_tripdata_2018-06
    fhv_tripdata_2018-08

This script takes an input Parquet file and converts it to CSV format,
handling any problematic timestamps and writing the resulting CSV file to the specified output path.

Parameters:
- input_dir: str, the directory containing the input Parquet file.
- output_file: str, the path where the resulting CSV file will be saved.

Dependencies:
- path: a module providing paths to data directories.
- pyarrow (pa, pq): provides data manipulation capabilities for Apache Arrow and Parquet files.
- pandas (pd): provides data manipulation capabilities, including handling timestamps and writing CSV files.

Output name:
output.csv

Returns:
None

Author: Serhii Spitsyn
"""

import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
import path_manager as path

# Convert the PyArrow Table to a pandas DataFrame while handling problematic timestamps
def clean_timestamps(column):
    # Convert the column to a list of timestamps
    timestamps = column.to_pylist()
    cleaned_timestamps = []
    for ts in timestamps:
        try:
            # Convert to pandas Timestamp and set errors='coerce' to handle out of bounds
            cleaned_timestamps.append(pd.to_datetime(ts, errors='coerce'))
        except Exception as e:
            # In case of any exception, append NaT (Not a Time)
            cleaned_timestamps.append(pd.NaT)
    return cleaned_timestamps

parquet_file_path = path.input_dir

# Read the Parquet file into a PyArrow Table
table = pq.read_table(parquet_file_path)

# Create a dictionary to store cleaned columns
cleaned_columns = {}
for column_name, column_data in zip(table.column_names, table.columns):
    if pa.types.is_timestamp(column_data.type):
        # Clean the timestamps
        cleaned_columns[column_name] = clean_timestamps(column_data)
    else:
        # Directly convert non-timestamp columns to pandas Series
        cleaned_columns[column_name] = column_data.to_pandas()

# Create a pandas DataFrame from the cleaned columns
df = pd.DataFrame(cleaned_columns)

# Write the DataFrame to a CSV file
csv_file = 'output.csv'
df.to_csv(csv_file, index=False)
