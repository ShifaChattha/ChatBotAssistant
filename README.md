# ChatBotAssistant
Modular chatbot component of the NARS system with a simple web interface and JSON-based knowledge.

##  Folder Structure

```
NARS-Chatbot/
├── app.py             # Main application file
├── knowledge.json     # Chatbot knowledge base
├── requirements.txt   # Python dependencies
├── templates/         # HTML templates for the web interface
├── static/            # CSS, JS, images
├── README.md          # Project overview and instructions
└── .gitignore         # Ignored files
````

##  Features

- Simple and modular chatbot interface
- Loads knowledge from a JSON file
- Supports basic conversational logic
- Ready to integrate into the main NARS system
- Easy to run locally or deploy


##  Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/NARS-Chatbot.git
cd NARS-Chatbot
````
2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:

```bash
python app.py
```

2. Open your browser and go to:

```
http://127.0.0.1:5000
```

3. Chat with the bot! 

## Customization

* Edit `knowledge.json` to add or modify chatbot responses.
* Add more HTML templates or static assets to enhance the interface.
* Extend `app.py` to include advanced logic or APIs.

##  Notes

* This chatbot is **modular**, meaning it can be integrated into the main NARS system.
* Only the chatbot component is pushed to GitHub—**no sensitive or unrelated files**.


