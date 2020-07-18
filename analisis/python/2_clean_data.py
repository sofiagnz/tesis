
# Data cleaning and standardization

import pandas as pd


INPUT_FILE_CODER1 = '1_new_column_names/coder1_cols_renamed.csv'
INPUT_FILE_CODER2 = '1_new_column_names/coder2_cols_renamed.csv'
OUTPUT_FILE_RATER1 = '2_clean_data/coder1_clean_data.csv'
OUTPUT_FILE_RATER2 = '2_clean_data/coder2_clean_data.csv'

# Transformation to int
def clean_value(value):
    value = str(value)
    value = value.strip()
    # Custom decision for values of rubric (decision taken by Sofia on Nov 17, 2019)
    # T-N -> T
    # N-T - N
    # T? NA -> NA
    if value == 'T-N': value = 'T'
    elif value == 'N-T': value = 'N'
    elif value == 'T? NA': value = 'T'

    # Conversion to numbers
    if value == 'N': value = '1'
    elif value == 'P': value = '2'
    elif value == 'T': value = '3'

    if value == 'NA':
        return value
    else:
        return int(float(value))


def main():
    df1_in = pd.read_csv(INPUT_FILE_CODER1, keep_default_na=False)
    df2_in = pd.read_csv(INPUT_FILE_CODER2, keep_default_na=False)

    coder = 0
    while coder < 1 or coder > 2:
        try:
            coder = int(input("Please enter the coder identifier (1 or 2): "))
        except ValueError:
            print('Invalid coder')

    if coder == 1:
        df_in = df1_in
        output_file = OUTPUT_FILE_RATER1
    else:
        df_in = df2_in
        output_file = OUTPUT_FILE_RATER2

    print('Processing...')
    df_in = df_in.applymap(clean_value)

    # Export to CSV
    print('Exporting to CSV...')
    df_in.to_csv(output_file, na_rep='NA', index=False, encoding='utf-8')
    print('Done.')


if __name__ == '__main__':
    main()
