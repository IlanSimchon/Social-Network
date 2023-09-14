import subprocess
import filecmp
import os

# Define the names of the student's and correct output files
student_output_file = "f1.txt"
correct_output_file = "f2.txt"

# Get the current working directory
current_directory = os.getcwd()

# Change to the directory containing main.py
os.chdir(current_directory)

# Run the main.py file and save its output to student_output_file
try:
    subprocess.run(["python3", "main.py"], stdout=open(student_output_file, "r+"), stderr=subprocess.PIPE, check=True, cwd=current_directory)
except subprocess.CalledProcessError as e:
    print(f"Error running main.py: {e.stderr.decode('utf-8')}")
    exit(1)

# Compare the student's output to the correct output
if filecmp.cmp(student_output_file, student_output_file, shallow=False):
    print("Output is correct. You passed the test successfully")
else:
    print("Output is incorrect. You are required to fix your code")
