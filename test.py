import os

import time
import re

def process_line(line):
    # Extract numbers from the line using regular expression
    numbers = re.findall(r'-?\d+', line)
    # Convert numbers to integers and sum them
    result = sum(map(int, numbers))
    # Return the result
    return str(result)

input_file_path = 'file.txt'
output_file_path = 'output_file.txt'

# Check if the input file exists, if not, create one
if not os.path.exists(input_file_path):
    with open(input_file_path, 'w') as file:
        file.write('0 0\n')

try:
    while True:
        # Open the input file for reading
        with open(input_file_path, 'r') as input_file:
            # Read the content of the input file
            input_content = input_file.read()
        
        # Process the content
        output_content = ""
        for line in input_content.splitlines():
            result = process_line(line)
            output_content += result + '\n'
        
        # Write the processed content to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(output_content)
        
        # Wait for some time before checking again
        time.sleep(1)  # Adjust the sleep time as needed
except KeyboardInterrupt:
    pass
