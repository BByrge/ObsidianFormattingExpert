import os
import subprocess
import ObsidianFormattingExpertAPI as api
import titleandheadergetter as thg
from Config import VAULT_PATH as TARGET_DIRECTORY, SETTINGS, TITLES_AND_HEADERS

def process_markdown_files(target_directory):
    for root, dirs, files in os.walk(target_directory):
        # Exclude directories named "attachments"
        dirs[:] = [d for d in dirs if d != 'attachments']
        
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)

                # Open the markdown file and read its content
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Send content to ObsidianFormattingExpert for processing
                updated_content = api.format_content(content)

                # Save the changes back to the file
                with open(filepath, 'w', encoding='utf-8') as file:
                    if updated_content:
                        file.write(updated_content)
                    else:
                        print(f"Error processing {filepath}")


if __name__ == "__main__":
    # Train the model for the current iteration
    for setting in SETTINGS:
        if SETTINGS[setting]:
            model_file_path = os.path.join(setting, "Modelfile")
            if setting == "WIKILINKS_FORMATTING" and TITLES_AND_HEADERS:
                # Run the titleandheadergetter.py keywords function
                thg.keywords(TARGET_DIRECTORY, model_file_path)
            result = subprocess.run(["ollama", "create", "ObsidianFormattingExpert", "-f", model_file_path])

            # Run the process_markdown_files function
            process_markdown_files(TARGET_DIRECTORY)
            # print(result.returncode)

    # Clear text after line 30 in the file at path WIKILINKS_FORMATTING/Modelfile
    # This clears the titles and headers from the file so it can be re-added in the next iteration
    modelfile_path = os.path.join("WIKILINKS_FORMATTING", "Modelfile")
    with open(modelfile_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) > 30:
            lines = lines[:30] + ['"""\nPARAMETER temperature 0.5\n']
        file.seek(0)
        file.writelines(lines)
        file.truncate()

