# 📊 API Data Extraction and CSV Export (Python)

## 📌 Overview
This project demonstrates how to fetch data from a REST API using Python and store it in a structured CSV format for further analysis. It specifically extracts post titles from the JSONPlaceholder API.

## 📂 Project Structure
```
api-data-extraction-project/
│
├── main.py              # Main execution script
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── output/               # Directory for exported data
    └── titles.csv        # Extracted data in CSV format
```

## 🚀 Features
- Fetch data from a public REST API
- Robust error handling for HTTP requests
- Automatic directory creation for output
- Clean CSV formatting with headers

## 🛠️ Technologies Used
- Python 3
- `requests` library
- `csv` & `os` modules

## 📡 API Used
[JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts)

## 🔧 Installation & Usage
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the script:**
   ```bash
   python main.py
   ```
3. **View the results:**
   Check the `output/titles.csv` file.
