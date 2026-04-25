# Python for Data Science - Semester 5 Project

This repository contains my Semester 5 Python for Data Science project work.

The project focuses on core data science workflows using Python:
- synthetic dataset generation
- data format conversion (XLSX -> CSV, CSV -> JSON)
- exploratory data analysis (EDA)
- basic data cleaning operations
- visualization in a terminal-driven app
- optional PostgreSQL/Neon data import

## Project Goals

- Practice real-world data preprocessing and transformation.
- Build reusable Python utilities for common data tasks.
- Perform EDA and basic visual analytics from the command line.
- Prepare and move data into a relational database environment.

## Tech Stack

- Python 3.9+
- pandas
- numpy
- matplotlib
- seaborn
- psycopg (for PostgreSQL/Neon import)

## Repository Structure

- `main.py`: Terminal Data Science Explorer (load data, EDA, cleaning, plotting)
- `Student_data_generator.py`: Generates `Student.csv` (10,000 rows, 50 columns)
- `Employee_data_generator.py`: Generates `Employee.csv` (10,000 rows, 50 columns)
- `xlsxTocsv.py`: Converts Excel data (`MID.xlsx`) to CSV (`data.csv`)
- `csvTojson.py`: Converts CSV data (`hospital_directory.csv`) to JSON (`hospital_data.json`)

Data/sample files in repository:
- `Student.csv`, `Employee.csv`
- `hospital_directory.csv`, `hospital_data.json`
- `data.csv`, `data.json`

## How to Run

### 1) Generate datasets

```bash
python Student_data_generator.py
python Employee_data_generator.py
```

### 2) Convert files

XLSX -> CSV:

```bash
python xlsxTocsv.py
```

CSV -> JSON:

```bash
python csvTojson.py
```

### 3) Run terminal EDA app

Interactive mode:

```bash
python main.py
```

Directly load a dataset on start:

```bash
python main.py Employee.csv
```

You can also open:
- `Student.csv`
- `data.csv`
- any compatible `.csv` or `.xlsx` file

## Features Implemented

### Data Generation
- Generates realistic synthetic student and employee datasets.
- Adds controlled missing values to support cleaning practice.
- Includes mixed data types (numeric, categorical, boolean, date-like text).

### Data Exploration (EDA)
- Dataset shape, column list, and head preview.
- Data types and missing-value summary.
- Numeric descriptive statistics.

### Data Cleaning
- Drop rows with missing values.
- Fill missing values:
  - numeric columns -> mean
  - categorical columns -> mode / fallback value
- Remove duplicate records.

### Visualization
- Histogram
- Boxplot
- Scatter plot
- Correlation heatmap

## Learning Outcomes

This project demonstrates practical understanding of:
- reading and writing datasets across formats
- preprocessing and handling missing data
- exploratory data analysis techniques
- visual interpretation of numeric relationships
- organizing Python scripts as modular data utilities

## Notes

- Some scripts include hardcoded example input/output file names; ensure those files exist before running.
- For `import_to_neon.py`, make sure your database connection details are correctly configured in your environment.

## Future Improvements

- Add `requirements.txt` for one-command dependency setup.
- Add logging and argument support to all utility scripts.
- Add unit tests for converters and generators.
- Containerize execution with Docker for reproducibility.

---
Created as part of Semester 5 coursework for the Python for Data Science subject.
