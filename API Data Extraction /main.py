import csv
import requests
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch data
response = requests.get(url)

# Check if request is successful
if response.status_code == 200:
    data = response.json()
else:
    print("Error fetching data:", response.status_code)
    exit()

# Ensure the output directory exists
output_dir = os.path.join(script_dir, "output")
os.makedirs(output_dir, exist_ok=True)

# Define the full path for the CSV file
output_file = os.path.join(output_dir, "titles.csv")

# Write data to CSV
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["Post ID", "Title"])
    
    # Data rows
    for post in data:
        writer.writerow([post["id"], post["title"]])

print(f"Data successfully saved to {output_file}")