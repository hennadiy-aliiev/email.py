import re
import sys


def sorting(input_file, outputfile1, outputfile2):
    with open(input_file) as f:
        emails = f.readlines()
        emails.sort()

    with open(outputfile1, "w") as f1:
            for line in emails:
                f1.write(line)

    with open(outputfile2, "w") as f2:
            pattern = r"y"
            for line in emails:
                if re.match(pattern, line):
                    f2.write(line)


if __name__ == "__main__":

    input_file = sys.argv[1]
    outputfile1 = sys.argv[2]         
    outputfile2 = sys.argv[3]
    sorting(input_file, outputfile1, outputfile2)
