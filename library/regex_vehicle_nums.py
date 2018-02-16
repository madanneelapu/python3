# Read a file with vehicle numbers and print valid vehicle numbers with regular expression
# sort them by serial number
import re


def extract_sl_no(vnum):
    m2 = re.search("^[a-zA-Z]{2}\s*\d{1,2}\s*[a-zA-Z]{1,2}\s*(\d{1,4})$", vnum)
    return int(m2.group(1))


valid_nums = set()
try:
    with open("vehicle_nums.txt", "r") as f:
        lines = f.readlines();
        for line in lines:
            line = line.strip("\n")
            # print(line)
            m1 = re.match("^[a-zA-Z]{2}\s*\d{1,2}\s*[a-zA-Z]{1,2}\s*\d{1,4}$", line)
            if (m1):
                print("Matched: ", line)
                valid_nums.add(line)

    print(valid_nums)

    for num in sorted(valid_nums, key=lambda l: extract_sl_no(l)):
        print(num)

except Exception as ex:
    print("error: ", ex)
