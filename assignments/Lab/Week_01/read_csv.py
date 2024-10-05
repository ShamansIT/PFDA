import csv
import requests

# Path to the CSV file
FILENAME = "data.csv"
DATADIR = "assignments\\Lab\\Week_01\\"

# 1. Reading and printing the CSV file
print("\nStep 1: Reading and printing the CSV file")
with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print(line)

# 2. Handling the header separately
print("\nStep 2: Handling the header separately")
with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if linecount == 0:
            print(f"Header: {line}\n-------------------")
        else:
            print(f"Data: {line}")
        linecount += 1

# 3. Calculating the average age
print("\nStep 3: Calculating the average age")
with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    total = 0
    count = 0
    for line in reader:
        if count > 0:  # Skip the header
            total += int(line[1])  # Age is in the second column
        count += 1
    print(f"Average age is {total / (count - 1)}")  # Subtract 1 to exclude the header

# 4. Using the quote parameter to automatically convert numeric values
print("\nStep 4: Using the quote parameter to convert numeric values")
with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        if count > 0:  # Skip the header
            total += line[1]  # Age is in the second column
        count += 1
    print(f"Average age is {total / (count - 1)}")

# 5. Reading the CSV as a dictionary and calculating the average age
print("\nStep 5: Reading CSV as dictionary and calculating average age")
with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        count += 1
    print(f"Average age is {total / count}")

# 6. Fetching and printing JSON data from the internet
print("\nStep 6: Fetching and printing JSON data from the internet")
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data)

# 7. Printing the current price in euros
print("\nStep 7: Printing the current price in Euros")
print(data['bpi']['EUR']['rate_float'])
