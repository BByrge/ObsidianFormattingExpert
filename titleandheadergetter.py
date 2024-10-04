import os
from Config import VAULT_PATH as TARGET_DIRECTORY

def get_file_names_and_headers(directory):
    file_headers = {}
    for root, dirs, files in os.walk(directory):
        # Skip directories named "attachments". This is where Obsidian stores images and shit.
        dirs[:] = [d for d in dirs if d.lower() != 'attachments']
        
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        headers = [line.strip().lstrip('#').strip() for line in file if line.startswith('#')]
                        note_title = os.path.splitext(file_name)[0]  # Remove file extension
                        file_headers[note_title] = headers
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return file_headers

def insert_into_modelfile(file_headers, modelfile_path, insert_line=30):
    with open(modelfile_path, 'r') as file:
        lines = file.readlines()
    
    for note_title, headers in file_headers.items():
        lines[insert_line:insert_line] = [f"{note_title}: {header}\n" for header in headers]
    
    with open(modelfile_path, 'w') as file:
        file.writelines(lines)

# Entry point
def keywords(target_directory, modelfile_path='/WIKILINKS_FORMATTING/Modelfile'):
    
    file_headers = get_file_names_and_headers(target_directory)
    insert_into_modelfile(file_headers, modelfile_path)

# Used to make Modelfile without running the whole program
def main():
    MODELFILE_PATH = r'/WIKILINKS_FORMATTING/Modelfile'
    keywords(TARGET_DIRECTORY, MODELFILE_PATH)

if __name__ == "__main__":
    main()
