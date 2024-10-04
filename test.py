from Config import SETTINGS
import subprocess
import os
from time import sleep

# Train the model for the current iteration
for setting in SETTINGS:
    if SETTINGS[setting]:
        model_file_path = os.path.join(setting, "Modelfile")
        print(model_file_path)
        result = subprocess.run(["ollama", "create", "ObsidianFormattingExpert", "-f", model_file_path], capture_output=True, text=True)
        sleep(2)
        print(result.returncode)

