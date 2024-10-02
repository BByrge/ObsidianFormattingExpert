import requests
import json

# API for ObsidianFormattingExpert

ENDPOINT = 'http://localhost:11434/api/generate'
HEADERS = {
    'Content-Type': 'application/json'
}

def format_content(content: str) -> str:
    # Process the content
    data = {
        'model': 'ObsidianFormattingExpert',
        'prompt': content,
        'stream': False,
    }
    response = requests.post(url=ENDPOINT, headers=HEADERS, data=json.dumps(data))
    if response.status_code == 200:
        data = json.loads(response.text)
        actual_response = data["response"]
        print(actual_response)
    else:
        print(f"Error: {response.status_code}, {response.text}")
    
    return actual_response

def main():
    content = "This is a test"
    format_content(content)
    print("Done. If you see this message, and you aren't testing, something went wrong.")

if __name__ == "__main__":
    main()