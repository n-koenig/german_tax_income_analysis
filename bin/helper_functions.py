import pandas as pd

BASE_DIR = '/home/nils/Documents/Repositories/semester-10/rse/rse_24_individual_project/'


def process_source_data(input_path, output_path, quarterly):
    """
    Process the source data and save the processed data to a new file.
    """
    
    df = pd.read_csv(BASE_DIR + input_path, skiprows=7, skipfooter=4, delimiter=';', engine='python')
    
    df.iloc[11, 0] = 'Solidaritätszuschlag'
    df.iloc[12, 0] = 'Vermögensteuer'
    df.iloc[15, 0] = 'Getränkesteuer'
    df.set_index(df.columns[0], drop=True, inplace=True)
    df.index.rename('Tax name', inplace=True)

    if quarterly:
        col_names = [str(year) + '-q' + str(quarter) for year in range(1999, 2024) for quarter in range(1, 5)]
    else:
        col_names = [str(year) + '-' + str(month).zfill(2) for year in range(1999, 2025) for month in range(1, 13)]
    df.columns = col_names

    df = df.apply(pd.to_numeric, downcast='integer', errors='coerce')
    df = df.astype('Int64')

    if quarterly:
        df.to_csv(BASE_DIR + output_path)
    else:
        df.to_csv(BASE_DIR + output_path)

