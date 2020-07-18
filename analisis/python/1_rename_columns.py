
# Utility to rename the column names in the RATER_S1 and RATER_2 tabs

import sys
import re
from pandas import read_excel


INPUT_FILE = 'IntegracionPuntajes_Rater1_2_EVC_V1_fixedColNames.xlsx'
OUTPUT_FILE_RATER1 = '1_new_column_names/coder1_cols_renamed.csv'
OUTPUT_FILE_RATER2 = '1_new_column_names/coder2_cols_renamed.csv'
SHEET1_NAME = 'RATER_S1'
SHEET2_NAME = 'RATER_M2'


def main():

    coder = 0
    while coder < 1 or coder > 2:
        try:
            coder = int(input("Please enter the coder identifier (1 or 2): "))
        except ValueError:
            print('Invalid coder')

    if coder == 1:
        sheet_name = SHEET1_NAME
        output_file = OUTPUT_FILE_RATER1
    else:
        sheet_name = SHEET2_NAME
        output_file = OUTPUT_FILE_RATER2

    #print(sys.getfilesystemencoding())
    df = read_excel(INPUT_FILE, header=1, sheet_name=sheet_name, encoding='utf-8')
    #print(df.head())  # shows headers with top 5 rows

    #print(df.columns.tolist())
    print('Number of columns:', len(df.columns))

    # Keep the relevant rows
    df = df.head(45)

    # Remove empty columns
    df = df.dropna(axis=1, how='all')

    print('Number of columns after removing the empty ones:', len(df.columns))

    pattern1 = '(R1|R2)_(CR|PE)_(Q1|Q2|Q3|Q4|Q5|Q6)(Spa|Eng)_(RA|RE|RC)'
    pattern2 = '(CR|PE)_(R1|R2|R3|R4|R5|R6|P1|P2|P3|P4|P5|P6)(Spa|Eng)_(RA|RE|RC)'

    new_col_names = []
    for col_name in df.columns:
        text_in = question_in = language_in = rubric_in = None
        if col_name == 'NºEstudiante':
            new_col_names.append('Student')
        else:

            matches1 = re.findall(pattern1, col_name)

            if len(matches1) > 0:  # Pattern1 matched
                text_in = matches1[0][1]
                question_in = matches1[0][2]
                language_in = matches1[0][3]
                rubric_in = matches1[0][4]

            else:
                matches2 = re.findall(pattern2, col_name)
                if len(matches2) > 0:  # Pattern2 matched
                    text_in = matches2[0][0]
                    question_in = matches2[0][1].replace('R', 'Q').replace('P', 'Q')
                    language_in = matches2[0][2]
                    rubric_in = matches2[0][3]

                else:
                    print('Could not match!!', col_name)
                    sys.exit()

            question_out = question_in

            if rubric_in == 'RA': rubric_out = 'R1'
            elif rubric_in == 'RE': rubric_out = 'R2'
            else: rubric_out = 'R3'

            text_out = 'T1' if text_in == 'CR' else 'T2'
            language_out = 'L1' if language_in == 'Spa' else 'L2'
            coder_out = 'C1' if coder == 1 else 'C2'

            new_header = question_out + '_' + rubric_out + '_' + text_out + '_' + language_out + '_' + coder_out
            print(col_name + ' -> ' + new_header)
            new_col_names.append(new_header)

    df.columns = new_col_names

    # Save to CSV
    df.to_csv(output_file, na_rep='NA', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()