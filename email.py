"""
This module sorts all emails from your "input_file" and
additionally chooses emails starting with desired character.
"""

import re
import sys


def sorting(input_file, outputfile1, outputfile2, char):
    with open(input_file) as f:
        emails = f.readlines()
        emails.sort()

    with open(outputfile1, "w") as f1:
            for line in emails:
                f1.write(line)

    with open(outputfile2, "w") as f2:
            pattern = char
            for line in emails:
                if re.match(pattern, line):
                    f2.write(line)


if __name__ == "__main__":

    try:
        input_file = sys.argv[1]
        outputfile1 = sys.argv[2]         
        outputfile2 = sys.argv[3]
        char = sys.argv[4]
        sorting(input_file, outputfile1, outputfile2, char)
    except:
        print("""ERROR! Please enter correct command!
        Example: "python email.py origin.txt output1.txt output2.txt k" where:
        origin.txt - file with all your emails,
        output1.txt - new output file with sorted emails,
        output2.txt k - new output file with emails starting with k character.""")