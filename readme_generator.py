from pathlib import Path

file_names = ['intro.md', "vectordatabases/readme.md"]
output_file = Path('readme.md')

with output_file.open('w', encoding='utf-8') as outfile:
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())