# validate name(incl spaces and dots) and DOB(yyyy-mm-dd,yyyy-m-d) using regular expression.

import re

valid_recs = []
try:
    with open("names_dobs.txt", "r") as f:
        lines = f.readlines();
        for line in lines:
            line = line.strip("\n")
            print(line)
            m1 = re.match("^[a-zA-Z]*\.?\s*[a-zA-Z]*\s*(\d{1,4}-\d{1,2}-\d{1,2})$", line)
            if (m1):
                print("Matched: ", line)
                print("dob:",m1.group(1))
                valid_recs.append(line)

    print(valid_recs)


except Exception as ex:
    print("error: ", ex)