# python-log-parser
log-detective of api status code, built a robust Python ETL script to parse raw server logs (access.log) and transform them into a clean, analytical dataset.

# 🕵️ Log Detective: Python Regex Parser

## 📌 Overview
**Log Detective** is a Python-based data engineering mini-project designed to transform unstructured server logs into structured, analytical data. It utilizes advanced **Regular Expressions (Regex)** to parse raw text, **Pandas** for data cleaning and transformation and generates a **Pandas** bar chart to flag error spikes.

This project simulates a real-world ELT (Extract, Load, Transform) task where log files must be prepared for security auditing or traffic analysis.

By converting "200" and "404" strings into a color-coded chart, I turned a 1MB text file into a 5-second health check for any backend team. 📊

## 🚀 Features
- **Robust Parsing:** Uses Python `re` module with Named Capture Groups to handle complex log string formats.
- **Data Cleaning:** Automatically converts string timestamps to Python `datetime` objects and numeric fields to integers.
- **Error Handling:** Gracefully skips malformed or corrupted log lines without crashing.
- **Analysis Ready:** Outputs a clean Pandas DataFrame ready for visualization or SQL insertion.
- **Visualization Ready:** Displays a clean visualization of api status records.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:**
  - `pandas` (Data manipulation)
  - `re` (Pattern matching)
  - `datetime` (Time series handling)
  - `matplotlib` (api status analysis)

## 📋 Input vs. Output

### Raw Input (Unstructured Text)
'text
192.168.1.2 - - [04/Jan/2026:10:56:01 +0000] "POST /login HTTP/1.1" 401 532
Clean Output (Structured DataFrame)
| timestamp                 | ip          | method | path   | status | size |
| ------------------------- | ----------- | ------ | ------ | ------ | ---- |
| 2026-01-04 10:56:01+00:00 | 192.168.1.2 | POST   | /login | 401    | 532  |

## 💻 Usage
Clone the repository:

git clone https://github.com/souviksalui/python-log-parser.git

Install requirements:

pip install pandas
pip install matplotlib

Run the parser:

python log_parser.py

### 🧠 What I Learned
Leveraging Regex Named Groups (?P<name>...) greatly improves code readability compared to standard indexed groups.

Data type casting (converting "200" string to 200 integer) is a crucial, often overlooked step in preparing data for analysis.
