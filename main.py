import os
import ObsidianFormattingExpertAPI as api
import titleandheadergetter as thg

TARGET_DIRECTORY = r'/home/bradley/Desktop/The vault/ObsidianOrganizerTest'
MODELFILE_PATH = r'/home/bradley/ObsidianOrganizer/ObsidianAIExpert/Modelfile'

def process_markdown_files(target_directory, modelfile_path):
    for root, dirs, files in os.walk(target_directory):
        # Exclude directories named "attachments"
        dirs[:] = [d for d in dirs if d != 'attachments']
        
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)

                # Open the markdown file and read its content
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Updates the model file with the headers and file names
                # This is used to train the model. Specifically for wikilinks.
                thg.get_file_names_and_headers(target_directory)

                # Send content to ObsidianFormattingExpert for processing
                updated_content = api.format_content(content)

                # Save the changes back to the file
                with open(filepath, 'w', encoding='utf-8') as file:
                    if updated_content:
                        file.write(updated_content)
                    else:
                        print(f"Error processing {filepath}")

# Call the function with the target directory
process_markdown_files(TARGET_DIRECTORY, MODELFILE_PATH)

