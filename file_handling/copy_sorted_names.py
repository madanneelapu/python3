# write data to files
try:
    with open("names.txt", "r") as sf:
        with open("sorted_names.txt", "w") as tf:  # opening file in write mode
            lines = set()
            for line in sf.readlines():
                lines.add(line)

            tf.writelines(sorted(lines))  # sorting and writing data to file

except OSError as ex:
    print("Sorry! Error: ", ex)
