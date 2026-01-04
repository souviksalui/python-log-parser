# python-log-parser
log-detective of api status code, built a robust Python ETL script to parse raw server logs (access.log) and transform them into a clean, analytical dataset.

# 🕵️ Log Detective: Python Regex Parser

## 📌 Overview
**Log Detective** is a Python-based data engineering mini-project designed to transform unstructured server logs into structured, analytical data. It utilizes advanced **Regular Expressions (Regex)** to parse raw text and **Pandas** for data cleaning and transformation.

This project simulates a real-world ELT (Extract, Load, Transform) task where log files must be prepared for security auditing or traffic analysis.

## 🚀 Features
- **Robust Parsing:** Uses Python `re` module with Named Capture Groups to handle complex log string formats.
- **Data Cleaning:** Automatically converts string timestamps to Python `datetime` objects and numeric fields to integers.
- **Error Handling:** Gracefully skips malformed or corrupted log lines without crashing.
- **Analysis Ready:** Outputs a clean Pandas DataFrame ready for visualization or SQL insertion.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:**
  - `pandas` (Data manipulation)
  - `re` (Pattern matching)
  - `datetime` (Time series handling)

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

bash
git clone https://github.com/yourusername/log-detective.git
Install requirements:

bash
pip install pandas
pip install matplotlib

Run the parser:

bash
python log_parser.py

### 🧠 What I Learned
Leveraging Regex Named Groups (?P<name>...) greatly improves code readability compared to standard indexed groups.

Data type casting (converting "200" string to 200 integer) is a crucial, often overlooked step in preparing data for analysis.
