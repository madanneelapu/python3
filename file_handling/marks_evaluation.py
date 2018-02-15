# display how many students passed. 50 is the passing mark.
# marks are comma separated
try:
    with open("marks.txt", "r") as f:
        count = 0
        for line in f.readlines():
            if len(line.strip()) == 0:
                continue

            marks = line.split(",")
            for m in marks:
                try:
                    if int(m) < 50:
                        break
                except:
                    break

            else:
                count += 1

        print("No. of students passed: ", count)

except Exception as ex:
    print("Error: ", ex)
