from transcribe import whisperData
import os
import asyncio

# Folder to read files from
folder_path = r"C:\audio"

# Output file to write the filenames
output_file = "transcript.txt"

# Get list of files in the folder
file_list = os.listdir(folder_path)

# Write each file name to the output file
with open(output_file, "w", encoding="utf-8") as f:
    for count, file_name in enumerate(file_list, start=1):
        transcript = asyncio.run(whisperData(file_name))
        f.write(f"{count} - {transcript}\n")

print(f"File names written to {output_file}")
