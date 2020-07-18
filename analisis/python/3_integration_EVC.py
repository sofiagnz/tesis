
# Utility to rename the column names in the RATER_S1 and RATER_2 tabs of Sofia's data

import pandas as pd

INPUT_FILE_CODER1 = '2_clean_data/coder1_clean_data.csv'
INPUT_FILE_CODER2 = '2_clean_data/coder2_clean_data.csv'
OUTPUT_FILE_INTEGRATED_ORIGINAL_COLS = '3_integration/integrated_original_cols.csv'
OUTPUT_FILE_INTEGRATED_NEW_COLS = '3_integration/integrated_EVC.csv'


def main():

    df1 = pd.read_csv(INPUT_FILE_CODER1, keep_default_na=False)
    df2 = pd.read_csv(INPUT_FILE_CODER2, keep_default_na=False)

    # STEP 1. Concatenate data frames to facilitate processing them
    df2 = df2.drop(df2.columns[0], axis=1)
    df_in = pd.concat([df1, df2], axis=1)
    # Save to CSV (optional)
    # df_in.to_csv(OUTPUT_FILE_INTEGRATED_ORIGINAL_COLS, na_rep='NA', index=False, encoding='utf-8')

    # STEP 2. Generate data frame with new columns
    questions = ['1', '2', '3', '4', '5', '6']
    rubrics = ['1', '2', '3']
    texts = ['1', '2']
    language = ['1', '2']
    coder = ['1', '2']

    # new data frame
    columns = ['Student', 'Question', 'Rubric', 'Text', 'Language', 'Coder', 'Answer']
    df_out = pd.DataFrame(columns=columns)

    print('Processing...')
    for index, row in df_in.iterrows():
        count = 0
        for q in questions:
            for r in rubrics:
                for t in texts:
                    for l in language:
                        for c in coder:
                            original_col_name = 'Q' + q + '_' + 'R' + r + '_' + 'T' + t + '_' + 'L' + l + '_' + 'C' + c

                            answer = row[original_col_name]
                            student = int(float(row['Student']))

                            df_out = df_out.append(
                                {'Student': student, 'Question': q, 'Rubric': r, 'Text': t, 'Language': l, 'Coder': c,
                                 'Answer': answer},
                                ignore_index=True)

                            count = count + 1
                            # print (count)

    # Check unique values to see that there are no errors
    for col in df_out:
        print(df_out[col].unique())

    # Export to CSV
    print('Exporting to CSV...')
    df_out.to_csv(OUTPUT_FILE_INTEGRATED_NEW_COLS, na_rep='NA', index=False, encoding='utf-8')
    print('Done.')


if __name__ == '__main__':
    main()