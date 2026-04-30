
import argparse
from agents.nlp_agent import parse_query
from agents.data_agent import process_data
from agents.report_agent import generate_report
import pandas as pd

def run(query, input_file, output_file):
    print("[1] Parsing query...")
    task = parse_query(query)
    print("Parsed Task:", task)

    print("[2] Loading data...")
    df = pd.read_excel(input_file)

    print("[3] Processing data...")
    result = process_data(df, task)

    print("[4] Generating report...")
    generate_report(result, output_file)

    print("✅ Report generated:", output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True)
    parser.add_argument("--input", type=str, default="data/demo.xlsx")
    parser.add_argument("--output", type=str, default="output/report.xlsx")

    args = parser.parse_args()
    run(args.query, args.input, args.output)
