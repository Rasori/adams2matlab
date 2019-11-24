# Author Waltteri Koskinen
# 24.11.2019

import csv
import sys


def divider(filename):
    appendix = 0

    try:
        with open(filename, newline='\r\n') as input_file:
            reader = csv.reader(input_file, delimiter='\t')
            while True:
                empty_row = True
                while True:
                    row = next(reader)
                    if any(row) and row[0] == ' Result ID':
                        row = next(reader)
                        dataname = row[0]  # Used in file naming
                        break
                output_filename = dataname + '.csv'

                with open(output_filename, 'w', newline='\n') as output_file:
                    writer = csv.writer(output_file, delimiter='\t')
                    start = False
                    for row in reader:
                        if any(row) and row[0] == '0.000000e+00':
                            start = True
                        if any(row) and start:
                            writer.writerow(row)
                        if not any(row) and not empty_row:
                            break
                        empty_row = any(row)
                    appendix += 1

    except StopIteration:
        print(appendix, 'file(s) created')
        return 'File run till end'

    except OSError as e:
        print('Error occurred ')
        return False, e


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(divider(sys.argv[1]))

    else:
        print("Usage: adams2matlab.py INPUTFILENAME")
        print("-------------------------------------------------------")
        print("(Required) INPUTFILENAME - Your .tab file")



