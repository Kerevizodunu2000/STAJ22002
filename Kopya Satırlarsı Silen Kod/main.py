# Import necessary libraries
import pandas as pd

# Read the Excel file (update the file path to your actual Excel file)
file_path = 'deneme.xlsx'  # Replace with your file path
sheet_name = 'Sheet1'  # Update if your data is in a different sheet

# Load the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Find all duplicate rows based on all columns (entire row comparison)
duplicates = df[df.duplicated(keep=False)]

# Count the number of unique duplicate entries (by entire rows)
unique_duplicates = duplicates.drop_duplicates()
duplicate_count = unique_duplicates.shape[0]

# Count the distribution of duplicate occurrences (e.g., how many times each occurs)
duplicates_distribution = duplicates.groupby(list(duplicates.columns)).size().value_counts().sort_index()

# Calculate the total number of rows that will be removed when keeping only one instance of each duplicate
total_removals = len(duplicates) - duplicate_count

# Save the duplicates to a new Excel file
duplicates_file = 'duplicates_data.xlsx'
duplicates.to_excel(duplicates_file, index=False)
print(f"Duplicate entries saved to '{duplicates_file}'.")

# Generate the analysis report content
analysis_text = f"Number of unique duplicate entries (entire row matches): {duplicate_count}\n"
analysis_text += f"Distribution of duplicates (how many times each unique row appears):\n"
for count, freq in duplicates_distribution.items():
    analysis_text += f"  - {count} occurrence(s): {freq} unique rows\n"
analysis_text += f"Total number of rows that will be removed to clean the data: {total_removals}\n"

# Print the analysis in the console
print("\nDuplicate Analysis Report:")
print(analysis_text)

# Save the analysis report to a text file
analysis_file = 'duplicates_analysis.txt'
with open(analysis_file, 'w', encoding='utf-8') as file:
    file.write(analysis_text)
print(f"Duplicate analysis report saved to '{analysis_file}'.")

# Remove duplicates but keep only one instance of each (based on entire rows)
cleaned_df = df.drop_duplicates(keep='first')

# Save the cleaned DataFrame to a new Excel file
cleaned_file = 'cleaned_data.xlsx'
cleaned_df.to_excel(cleaned_file, index=False)
print(f"Cleaned data saved to '{cleaned_file}'.")
