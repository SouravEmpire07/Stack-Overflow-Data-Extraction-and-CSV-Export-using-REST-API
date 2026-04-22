import csv
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

with open("titles.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title"])
    for post in data:
        writer.writerow([post["title"]])
        