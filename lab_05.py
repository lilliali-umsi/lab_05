# START LAB EXERCISE 05
print('Lab Exercise 05 \n')

# [IMPORTANT NOTE]
# The autograder in Gradescope will directly test functions and files instead of variables
# So even though the variables printed seems right, it's possible your code didn't pass all the test cases.

# In this lab, we use txt files. Be very careful that a line in txt files
# should contain a new line "\n" character at the end of this line.

# PROBLEM 1 (5 Points)
# Define a function named "concatenate_name_type".
# The function accepts two arguments - one is "file_name", the other is "file_type". Both two arguments are strings.
# For given arguments, the function should return "<file_name>.<file_type>"
# Pass two defined variables "file_name", "file_type" to the function, assign the result to "full_file_name"
# Print "full_file_name".

# BEGIN PROBLEM 1 SOLUTION
f_name = "file1"
f_type = "txt"

def concatenate_name_type(file_name, file_type):
    return f"{file_name}.{file_type}"

full_file_name = concatenate_name_type(f_name, f_type)
print(full_file_name)

# END PROBLEM 1 SOLUTION


# PROBLEM 2 (10 Points)
# Define a function named "write_into_file"
# The function accepts two arguments - one is "filename", the other is "file_content"
# "filename" is a string and "file_content" is a list of strings
# Open the file with "full_file_name", read all lines, store the last two lines into the variable "last_two_lines"
# Make sure that there is a new line character "\n" at the end of each line in "last_two_lines"
# Write "last_two_lines" into a new file called "file2.txt" using the function "write_into_file"
# Print "last_two_lines"

# BEGIN PROBLEM 2 SOLUTION

#def write_into_file(filename, file_content):
    #path = filename
    #file_handle = open(path)
    #lines = file_handle.readlines()
    #file_handle.close()
    #for line in lines[-2:]:
        #file_content.append(line)

#last_two_lines = []
#path = 'file2.txt'
#file_handle = open(path, 'w')
#write_into_file(full_file_name, last_two_lines)
#for line in last_two_lines:
    #file_handle.write(f"{line}")
#file_handle.close()
#print(last_two_lines)

def write_into_file(filename, file_content):
    file_open = open(filename, 'w')
    #for line in file_content:
    for line in file_content:
        file_open.write(f"{line}")
    file_open.close()

last_two_lines = []
file_handle = open(full_file_name)
file_content = file_handle.readlines()
print(file_content)
last_two_lines = file_content[1:]
filename = 'file2.txt'
write_into_file(filename,last_two_lines)
print(last_two_lines)

# END PROBLEM 2 SOLUTION


# PROBLEM 3 (10 Points)
# Finally, put all you've learned together.
# Open each file with file_name in "file_name_list" and "file_type",
# read all lines and store those unique lines into the variable "unique_lines".
# Make sure that there is a new line character "\n" at the end of each line in "unique_lines".
# Write "unique_lines" into a new file called "summary.txt" using the function "write_into_file".
# Print "unique_lines".

# BEGIN PROBLEM 3 SOLUTION
file_name_list = ["file1", "file2", "file3"]
file_type = "txt"
unique_lines = []
all_files = []
all_lines=[]
all_lines_string = []
unique_lines_list = []
for file in file_name_list:
    all_files.append(concatenate_name_type(file, file_type))
print(all_files)

for file in all_files:
    #print(file)
    file_opening = open(file, 'r')
    all_lines.append(file_opening.readlines())
    for line in all_lines:
        for x in line:
            all_lines_string.append(x.split(','))
print(all_lines_string)

for line in all_lines_string:
    if line not in unique_lines_list:
        unique_lines_list.append(line)
for line in unique_lines_list:
    for x in line:
        unique_lines.append(x)


#for line in unique_lines:
    #print(line)
    #file_opening.close()
write_into_file('summary.txt',unique_lines)
print(unique_lines)
# END PROBLEM 3 SOLUTION
#how can we check if a value already exists in unique_lines and only append it if it doesn't already exist
#you'll need for loops to iterate through file_name_list and the lines within each file
# END LAB EXERCISE
