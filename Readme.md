Obsidian Markdown Enhancer
# Welcome to the Obsidian Markdown Enhancer!

This tool uses an AI model to improve the formatting and readability of your Obsidian Markdown files. It focuses on enhancing definitions and creating internal links between your notes. The bots name is ObsidianFormattingExpert and is a custom llama3.2.

## Features

- **Better Formatting:** Cleans up your notes for improved readability.
- **Definition Callouts:** Highlights definitions using callout blocks.
- **Automatic Wikilinks:** Creates links between notes based on titles and headers.

## How It Works

1. **Input:** Provide raw text from your Obsidian Markdown files.
2. **Processing:** The AI model enhances the formatting and fixes mistakes.
3. **Output:** Receive improved Markdown files with better structure and links.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/obsidian-markdown-enhancer.git
```

### Install Requirements

Run ollama
```bash
ollama serve
```
Train the model
```bash
ollama create ObsidianFormattingExpert -f Modelfile
```

Run the model
```bash
ollama run ObsidianFormattingExpert
```

Stop ollama
```bash
systemctl stop ollama
```


### Run the Enhancer

```bash
python enhance.py
```

### Enjoy Improved Notes

Your enhanced notes will be saved in the output folder.

## Useful links
https://github.com/ollama/ollama
https://github.com/ollama/ollama/blob/main/docs/api.md#list-local-models
https://dev.to/jayantaadhikary/using-the-ollama-api-to-run-llms-and-generate-responses-locally-18b7


## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.
