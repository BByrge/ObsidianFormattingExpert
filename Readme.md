Obsidian Markdown Enhancer
# Welcome to ObsidianFormattingExpert

Watch the tool in action- 

[In action](https://github.com/user-attachments/assets/724da12e-eb8f-4c38-a593-92d7498ba091)


ObsidianFormattingExpert is an AI-powered tool that enhances your Obsidian Markdown notes. It improves the formatting, formats definitions, and creates automatic wikilinks between notes.

## Disclaimer
Please backup your notes before using this tool. While the AI model is designed to enhance your notes, it may introduce errors or unwanted changes. Use at your own risk.

## Features

- **Better Formatting:** Cleans up your notes for improved readability.
- **Definition as Callouts:** Highlights definitions using callout blocks.
- **Automatic Wikilinks:** Creates links between notes based on titles and headers.

## How It Works

Leveraging the Ollama API, this tool runs a custom-trained AI model specifically designed to enhance Obsidian Markdown notes. The model aims to significantly improve the structure and readability of your content.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/BByrge/ObsidianFormattingExpert
```

### Install Dependencies

Download and install the Ollama - https://github.com/ollama/ollama

```bash
pip install -r requirements.txt
```

### Start the Ollama API

Run ollama
```bash
ollama serve
```

Stop ollama
```bash
systemctl stop ollama
```


### Configure the Tool

Edit the Config.py file to specify your vault path and settings.

### Run the Tool

```bash
python main.py
```

### Enjoy Improved Notes

Your enhanced notes will be saved in the output folder.

## Useful links
https://github.com/ollama/ollama
https://github.com/ollama/ollama/blob/main/docs/api.md#list-local-models
https://dev.to/jayantaadhikary/using-the-ollama-api-to-run-llms-and-generate-responses-locally-18b7


## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.
