import re
import sys


def sorting(file1, file2):
	with open("original.txt") as f:
		emails = f.readlines()
		sorted_emails = emails.sort()

		with open(file1, "w") as f1:
			for line in emails:
				f1.write(line)

		with open(file2, "w") as f2:
			pattern = r"y"
			for line in emails:
				if re.match(pattern, line):
					f2.write(line)


if __name__ == "__main__":
	
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	sorting(file1, file2)
	