# inet_4031_adduser_script

## Program Description
This program will help users automate the process of adding in users to a system. For example, needing to add more than 10 or 20 new users to a system will take a long time. This program (more so a scrpit) written in Python will automate all of the users onto the system without having to input one by one manually. Commands that user would use to add a new user would be manually typing in adduser (username). Doing this would bring the user into more steps such as group, password, and so on. While in the script/program, this is all automated as there are lines in the code that can interact with the Python interpreter allowing for command line commands to be put in without the need of manual user input. 

## Program User Operation
This program focuses on automating for adding users to a system. It takes in file that contains the information and then goes through it line by line to make sure that all information is input correctly into the system. Once this is finished, the user can access directories to double check if the users were added successfully. Read comments on program to get a deeper dive into the program workings.

## Input File Format
Explain the format of the input file. What is the purpose of each field in a line. Explain what the user needs to do if they want to skip a line in the input file. Expalin what the user needs to do if they do not want a new user added to any groups.

The input file format must be a text file. This is because it allows for the program to read the file itself. Any other would be invalid as the program is not designed to read in files different from text files. In the file, there must be 5 fields. These 5 fields are first name, last name, group, password, and the naming of the user. Without these 5 valid fields, the line will be considered invalid. If one wants to remove or not include a line in the file, put a # symbol before everything. The program will then skip it. For a user to not be added to groups, use the - symbol to replace the group field. 

## Command Excuction
Explain how the user runs the code. Remind the user they may need to set the Python file to be executable. ./create-users.py < createusers.input
To run this code, user must make sure to set it up as an executable. If already done so, proceed. IF not, to do this, one would need to run a chmod command that turns it from a read and write file to also an executable file (-x). Once this is all done, use the command ./(filename).py < (filename).input to run the program. 

## "Dry Run"
When user chooses dry run, this runs the code without actually executing all of the operating system commands listed in the Python code chunk. This only gives a small simulation as to what is happening if you did not dry run. Only dry run to test out code and double check that everything is working as intended. 
