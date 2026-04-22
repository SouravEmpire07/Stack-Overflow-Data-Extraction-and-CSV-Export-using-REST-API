import csv
import requests
import os

# API URL
API_URL = "https://jsonplaceholder.typicode.com/posts"
OUTPUT_DIR = "output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "titles.csv")

def fetch_data(url):
    """Fetch data from the REST API."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_to_csv(data, filepath):
    """Save the extracted titles to a CSV file."""
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    try:
        with open(filepath, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Header
            writer.writerow(["Post ID", "Title"])
            
            # Data rows
            for post in data:
                writer.writerow([post.get("id"), post.get("title")])
        print(f"Data successfully saved to {filepath}")
    except IOError as e:
        print(f"Error saving data to CSV: {e}")

def main():
    print("Starting data extraction...")
    data = fetch_data(API_URL)
    
    if data:
        save_to_csv(data, OUTPUT_FILE)
    else:
        print("No data extracted.")

if __name__ == "__main__":
    main()
