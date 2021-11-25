import json
import os
import sys

args = sys.argv[1:]
ocr_out_path = args[0]

# Read all observation files in directory
observation_filenames = os.listdir(ocr_out_path)
observations_contents = {filename[-9:-4]: json.load(open(f"{ocr_out_path}/{filename}"))
                         for filename in observation_filenames}

# Extract timing data from observation formats
timings = {image_name: observations_contents[image_name]['timings']
           for image_name in observations_contents}

# Calculate total timings by subtracting start and end times read from datetime format strings

# Export all timing data to single csv file
#  named after the folder where the observations came from



