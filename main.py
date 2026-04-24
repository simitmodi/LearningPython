# terminal_data_science_app.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
import argparse

class TerminalDataScienceApp:

    def __init__(self):
        self.df = None
        self.filename = ""
        print("\n--- Terminal Data Science Explorer ---")
        print("Topics Covered: Data Loading, Cleaning, EDA, Visualization\n")

    def load_data(self, file_path):
        """Load data from a CSV or Excel file."""
        try:
            ext = os.path.splitext(file_path)[1].lower()
            if ext in ['.xlsx', '.xls']:
                self.df = pd.read_excel(file_path)
            elif ext == '.csv':
                self.df = pd.read_csv(file_path)
            else:
                print(f"Error: Unsupported file extension '{ext}'. Use CSV or Excel.")
                return False
            self.filename = os.path.basename(file_path)
            print(f"✅ Successfully loaded '{self.filename}' (Shape: {self.df.shape})")
            return True
        except FileNotFoundError:
            print(f"❌ Error: File '{file_path}' not found.")
            return False
        except pd.errors.EmptyDataError:
            print(f"❌ Error: File '{file_path}' is empty.")
            return False
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            return False

    def show_basic_info(self):
        """Display basic information about the dataset."""
        if self.df is None:
            print("❌ No dataset loaded. Please load data first.")
            return

        print("\n--- Dataset Information ---")
        print(f"Filename: {self.filename}")
        print(f"Shape: {self.df.shape}")
        print("\nColumn Names:")
        for i, col in enumerate(self.df.columns):
            print(f"  {i+1}. {col}")
        print("\nFirst 5 rows:")
        print(self.df.head().to_string())

    def show_eda(self):
        """Perform and display Exploratory Data Analysis."""
        if self.df is None:
            print("❌ No dataset loaded. Please load data first.")
            return

        print("\n--- Exploratory Data Analysis (EDA) ---")
        print("\nDataset Info:")
        self.df.info()

        print("\nDescriptive Statistics (Numeric Columns):")
        numeric_df = self.df.select_dtypes(include=[np.number])
        if not numeric_df.empty:
            print(numeric_df.describe())
        else:
            print("No numeric columns found for descriptive statistics.")

        print("\nMissing Values:")
        missing = self.df.isnull().sum()
        if missing.any():
            print(missing[missing > 0].to_string())
        else:
            print("No missing values found.")

        print("\nData Types:")
        print(self.df.dtypes.to_string())

    def show_data_cleaning_menu(self):
        """Provide options for basic data cleaning."""
        if self.df is None:
            print("❌ No dataset loaded. Please load data first.")
            return

        while True:
            print("\n--- Data Cleaning ---")
            print("1. Drop rows with any missing values")
            print("2. Fill missing values (mean for numeric, mode for categorical)")
            print("3. Remove duplicate rows")
            print("4. Back to Main Menu")
            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                initial_shape = self.df.shape
                self.df.dropna(inplace=True)
                print(f"✅ Dropped rows with missing values. Shape changed from {initial_shape} to {self.df.shape}")
            elif choice == '2':
                initial_missing = self.df.isnull().sum().sum()
                for col in self.df.columns:
                    if self.df[col].dtype in ['object', 'category']:
                        # Fill with mode (first mode if multiple exist)
                        mode_val = self.df[col].mode()
                        if not mode_val.empty:
                            self.df[col].fillna(mode_val[0], inplace=True)
                        else:
                            # If no mode, fill with a placeholder
                            self.df[col].fillna('Unknown', inplace=True)
                    else:
                        # Fill numeric with mean
                        self.df[col].fillna(self.df[col].mean(), inplace=True)
                final_missing = self.df.isnull().sum().sum()
                print(f"✅ Filled missing values. Total missing values reduced from {initial_missing} to {final_missing}.")
            elif choice == '3':
                initial_shape = self.df.shape
                self.df.drop_duplicates(inplace=True)
                print(f"✅ Removed duplicate rows. Shape changed from {initial_shape} to {self.df.shape}")
            elif choice == '4':
                break
            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

    def show_visualization_menu(self):
        """Provide options for data visualization."""
        if self.df is None:
            print("❌ No dataset loaded. Please load data first.")
            return

        numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        all_cols = self.df.columns.tolist()

        if not numeric_cols:
            print("❌ No numeric columns found for visualization.")
            return

        while True:
            print("\n--- Data Visualization ---")
            print("1. Histogram (for a single numeric column)")
            print("2. Boxplot (for a single numeric column)")
            print("3. Scatter Plot (two numeric columns)")
            print("4. Correlation Heatmap (all numeric columns)")
            print("5. Back to Main Menu")
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                print(f"Available numeric columns: {numeric_cols}")
                col = input("Enter the column name for histogram: ").strip()
                if col in numeric_cols:
                    self._plot_histogram(col)
                else:
                    print(f"❌ Column '{col}' not found or not numeric.")
            elif choice == '2':
                print(f"Available numeric columns: {numeric_cols}")
                col = input("Enter the column name for boxplot: ").strip()
                if col in numeric_cols:
                    self._plot_boxplot(col)
                else:
                    print(f"❌ Column '{col}' not found or not numeric.")
            elif choice == '3':
                print(f"Available numeric columns: {numeric_cols}")
                col1 = input("Enter the X-axis column name: ").strip()
                col2 = input("Enter the Y-axis column name: ").strip()
                if col1 in numeric_cols and col2 in numeric_cols:
                    self._plot_scatter(col1, col2)
                else:
                    print(f"❌ One or both columns '{col1}', '{col2}' not found or not numeric.")
            elif choice == '4':
                if len(numeric_cols) < 2:
                    print("❌ Need at least 2 numeric columns for a correlation heatmap.")
                else:
                    self._plot_correlation_heatmap()
            elif choice == '5':
                break
            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, 4, or 5.")

    def _plot_histogram(self, col):
        """Helper function to plot a histogram."""
        try:
            plt.figure(figsize=(8, 6))
            plt.hist(self.df[col].dropna(), bins=30, edgecolor='black')
            plt.title(f'Histogram of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"❌ Error plotting histogram: {e}")

    def _plot_boxplot(self, col):
        """Helper function to plot a boxplot."""
        try:
            plt.figure(figsize=(6, 8))
            plt.boxplot(self.df[col].dropna())
            plt.title(f'Boxplot of {col}')
            plt.ylabel(col)
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"❌ Error plotting boxplot: {e}")

    def _plot_scatter(self, col1, col2):
        """Helper function to plot a scatter plot."""
        try:
            plt.figure(figsize=(8, 6))
            plt.scatter(self.df[col1], self.df[col2], alpha=0.6)
            plt.title(f'Scatter Plot: {col1} vs {col2}')
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"❌ Error plotting scatter plot: {e}")

    def _plot_correlation_heatmap(self):
        """Helper function to plot a correlation heatmap."""
        try:
            numeric_df = self.df.select_dtypes(include=[np.number])
            corr_matrix = numeric_df.corr()
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', center=0)
            plt.title('Correlation Heatmap')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"❌ Error plotting correlation heatmap: {e}")

    def run(self):
        """Main loop to run the terminal application."""
        parser = argparse.ArgumentParser(description='Terminal Data Science Explorer')
        parser.add_argument('file', nargs='?', help='Path to the CSV or Excel file to load')
        args = parser.parse_args()

        if args.file:
            if not self.load_data(args.file):
                sys.exit(1) # Exit if file loading fails

        while True:
            print("\n--- Main Menu ---")
            print("1. Load Data File")
            print("2. Show Basic Dataset Info")
            print("3. Perform EDA")
            print("4. Data Cleaning")
            print("5. Data Visualization")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                file_path = input("Enter the path to your CSV or Excel file: ").strip()
                self.load_data(file_path)
            elif choice == '2':
                self.show_basic_info()
            elif choice == '3':
                self.show_eda()
            elif choice == '4':
                self.show_data_cleaning_menu()
            elif choice == '5':
                self.show_visualization_menu()
            elif choice == '6':
                print("👋 Exiting Terminal Data Science Explorer. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    app = TerminalDataScienceApp()
    app.run()