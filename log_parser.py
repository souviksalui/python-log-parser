import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ==========================================
# 1. SETUP: Regex Pattern Construction
# ==========================================
# Regex with Named Groups for precision extraction
log_pattern = re.compile(
    r'(?P<ip>[\d\.]+)'           # IP Address
    r'\s-\s-\s'                  # Separator
    r'\[(?P<timestamp>.*?)\]'    # Timestamp
    r'\s'                        # Space
    r'"(?P<method>\w+)\s(?P<path>.*?)\sHTTP/.*?"' # Method & Path
    r'\s'                        # Space
    r'(?P<status>\d+)'           # Status Code
    r'\s'                        # Space
    r'(?P<size>\d+)'             # Byte Size
)

def parse_log_file(file_path):
    """Reads a log file and returns a list of dictionaries."""
    parsed_data = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                match = log_pattern.search(line)
                if match:
                    parsed_data.append(match.groupdict())
    except FileNotFoundError:
        print(f"Error: File {file_path} not found. Please create it first.")
        return []
    return parsed_data

# ==========================================
# 2. TRANSFORMATION: Pandas Cleaning
# ==========================================
def process_data(data_list):
    if not data_list:
        return pd.DataFrame()

    df = pd.DataFrame(data_list)

    # Type Conversion
    df['status'] = df['status'].astype(int)
    df['size'] = df['size'].astype(int)

    # Convert Timestamp to DateTime object
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%b/%Y:%H:%M:%S %z')

    return df

# ==========================================
# 3. VISUALIZATION: Matplotlib Chart
# ==========================================
def visualize_status_counts(df):
    """Generates and saves a bar chart of HTTP status codes."""
    if df.empty:
        print("No data to visualize.")
        return

    status_counts = df['status'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))

    # Color coding: Green for success (2xx), Red for errors (4xx, 5xx), Orange for redirects
    colors = []
    for code in status_counts.index:
        str_code = str(code)
        if str_code.startswith('2'):
            colors.append('#2ecc71') # Green
        elif str_code.startswith('3'):
            colors.append('#f1c40f') # Orange
        elif str_code.startswith('4'):
            colors.append('#e74c3c') # Red
        elif str_code.startswith('5'):
            colors.append('#c0392b') # Dark Red
        else:
            colors.append('gray')

    bars = plt.bar(status_counts.index.astype(str), status_counts.values, color=colors, edgecolor='black', alpha=0.8)

    plt.bar_label(bars) # Add count labels on top of bars
    plt.title('Server Log Analysis: HTTP Status Codes', fontsize=16, fontweight='bold')
    plt.xlabel('HTTP Status Code', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.3)

    # Save the plot
    output_file = f'status_report{datetime.now().strftime("%Y%m%d%H%M%S")}.png'
    plt.savefig(output_file, dpi=300)
    print(f"✅ Visualization saved as '{output_file}'")

# ==========================================
# 4. EXECUTION MAIN BLOCK
# ==========================================
if __name__ == "__main__":
    input_file = "server_logs.txt"

    print(f"--- 1. Reading {input_file} ---")
    raw_data = parse_log_file(input_file)
    print(f"✅ Extracted {len(raw_data)} valid records.")

    print("\n--- 2. Processing Data ---")
    clean_df = process_data(raw_data)

    if not clean_df.empty:
        print(clean_df.head())
        print(f"\nDataFrame Shape: {clean_df.shape}")

        print("\n--- 3. Generating Visualization ---")
        visualize_status_counts(clean_df)

        # Save to CSV
        clean_df.to_csv(f"cleaned_logs{datetime.now().strftime('%Y%m%d%H%M%S')}.csv", index=False)
        print("✅ Data saved to 'cleaned_logs.csv'")
    else:
        print("No valid data found to process.")
