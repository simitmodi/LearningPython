import pandas as pd

def xlsx_to_csv(input_path, output_path):
    # Load the Excel file
    df = pd.read_excel(input_path)

    # Export to CSV without the index column
    df.to_csv(output_path, index=False)

    print(f"Conversion complete! CSV saved at: {output_path}")

# Example usage
xlsx_to_csv("MID.xlsx", "data.csv")
