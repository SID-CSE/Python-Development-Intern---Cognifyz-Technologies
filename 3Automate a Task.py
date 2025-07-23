# Level 3 :Task 3
# Task: Automate a Task
'''
 Identify a repetitive task, such as data processing, file management, or report generation,
 and develop a script to automate it using Python. This task will showcase their problem-solving skills and
 familiarity with Python's automation capabilities.
'''

import os
import pandas as pd
from datetime import datetime

INPUT_FOLDER = "input_data"
OUTPUT_FOLDER = "processed_data"
REPORT_NAME = "summary_report.txt"
MERGED_FILE_NAME = "merged_cleaned.csv"

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def merge_csv_files(folder):
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    df_list = []
    for file in files:
        try:
            path = os.path.join(folder, file)
            df = pd.read_csv(path)
            df_list.append(df)
            print(f"Loaded: {file}")
        except Exception as e:
            print(f"Failed to load {file}: {e}")
    return pd.concat(df_list, ignore_index=True) if df_list else pd.DataFrame()

def clean_data(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df.drop_duplicates()

def generate_report(df, output_path):
    with open(output_path, "w") as f:
        f.write(f"Report generated on: {datetime.now()}\n")
        f.write(f"Total Rows: {len(df)}\n")
        f.write(f"Total Columns: {len(df.columns)}\n")
        f.write(f"Missing Values:\n{df.isnull().sum()}\n")
        f.write("\nColumn Names:\n" + ", ".join(df.columns))

def main():
    print("Scanning for CSV files...")
    merged_df = merge_csv_files(INPUT_FOLDER)
    if merged_df.empty:
        print("No CSV files found to process.")
        return
    cleaned_df = clean_data(merged_df)
    merged_output = os.path.join(OUTPUT_FOLDER, MERGED_FILE_NAME)
    report_output = os.path.join(OUTPUT_FOLDER, REPORT_NAME)
    cleaned_df.to_csv(merged_output, index=False)
    generate_report(cleaned_df, report_output)
    print(f"Automation Complete!\nCleaned Data: {merged_output}\nReport: {report_output}")

if __name__ == "__main__":
    main()