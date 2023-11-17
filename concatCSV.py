import pandas as pd
import glob

def concatenate_csv_files(input_path, output_path):
    all_files = glob.glob(input_path + "/*.csv")

    # List to store DataFrames
    dfs = []

    for file in all_files:
        # Read only the first 50 lines and select columns 3 and 4
        df = pd.read_csv(file)

        # Append the DataFrame to the list
        dfs.append(df)

    # Concatenate all DataFrames in the list
    result_df = pd.concat(dfs, ignore_index=True)

    # Write the result to a new CSV file
    result_df.to_csv(output_path, index=False)

if __name__ == '__main__':
    input_directory = '/home/starling/Desktop/data'  # Update with the actual path to your CSV files
    output_file = 'dataset.csv'

    concatenate_csv_files(input_directory, output_file)
