
# Utility to rename the column names in the RATER_S1 and RATER_2 tabs of Sofia's data

import pandas as pd


INPUT_FILE_CODER1 = '2_clean_data/coder1_clean_data.csv'
INPUT_FILE_CODER2 = '2_clean_data/coder2_clean_data.csv'
OUTPUT_FILE_INTEGRATED_VA = '3_integration/integrated_VA.csv'


def main():

    df1 = pd.read_csv(INPUT_FILE_CODER1, keep_default_na=False)
    df2 = pd.read_csv(INPUT_FILE_CODER2, keep_default_na=False)

    # STEP 1. Concatenate data frames to facilitate processing them
    df2 = df2.drop(df2.columns[0], axis=1)
    df = pd.concat([df1, df2], axis=1)

    # STEP 2. Generate data frame with new columns
    questions = ['1', '2', '3', '4', '5', '6']
    rubrics = ['1', '2', '3']
    texts = ['1', '2']
    languages = ['1', '2']
    coders = ['1', '2']

    col_names = ['Student']
    print('Processing...')
    # Generate columns of new data frame
    for t in texts:
        for r in rubrics:
            for q in questions:
                for l in languages:
                    for c in coders:
                        col_name = 'Q' + q + '_' + 'R' + r + '_' + 'T' + t + '_' + 'L' + l + '_' + 'C' + c
                        col_names.append(col_name)

    df_out = df[col_names]

    # Export to CSV
    print('Exporting to CSV...')
    df_out.to_csv(OUTPUT_FILE_INTEGRATED_VA, na_rep='NA', index=False, encoding='utf-8')
    print('Done.')


if __name__ == '__main__':
    main()