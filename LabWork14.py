# clearing the file in which we have to write (so that we can get only desired data
open('file2.txt', 'w').close()

# opening both files using with statement so that they can be closed automatically as well as exception handling is
# also there
with open('file1.txt', 'r') as inp_file, open('file2.txt', 'a') as out_file:
    # creating line count var so that we can know which line is currently read
    line_count = 0
    for line in inp_file:
        line_count += 1
        # checking for odd lines
        if line_count % 2 != 0:
            out_file.write(line)
