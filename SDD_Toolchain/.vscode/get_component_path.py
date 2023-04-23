import os
import csv
import argparse

# Define the argument parser
parser = argparse.ArgumentParser(description="Collect paths of each folder in a nested folder structure and store in a CSV file.")
parser.add_argument("--input_dir", help="the path to the top-level folder of the nested structure")
parser.add_argument("--output_dir", help="the path to the output directory")
args = parser.parse_args()

# Define a function to collect folder paths and write to a CSV file
def collect_folder_paths(input_dir, output_dir):
    # Define a list to store the paths of each folder
    folder_paths = []
    
    # Use os.walk to iterate through the nested folder structure
    for root, dirs, _ in os.walk(input_dir):
        # Iterate through each directory in the current level
        for dir_name in dirs:
            # Construct the full path of the current directory
            dir_path = os.path.join(root, dir_name)
            # Add the path to the list
            folder_paths.append(dir_path)

    # Create the output directory if it doesn't already exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the path to the output CSV file
    output_file = os.path.join(output_dir, "componentlist.csv")

    # Use the csv module to write the folder paths to the output file
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        for path in folder_paths:
            writer.writerow([path])

# Call the function to collect folder paths and write to the CSV file
collect_folder_paths(args.input_dir, args.output_dir)

