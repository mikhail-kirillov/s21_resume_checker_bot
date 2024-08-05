# s21_resume_checker_bot

Telegram bot for resume checking using neural networks. This bot analyzes resumes uploaded in PDF format and provides recommendations for their improvement.

## Getting Started

To use this bot, you will need:

1. A Telegram bot token. Obtain it via [BotFather](https://t.me/botfather).
2. Access to the GigaChat API.

### Installation

To run the bot, follow these steps:

1. Clone the repository:

    `git clone https://github.com/mikhail-kirillov/s21_resume_checker_bot.git`

2. Navigate to the project directory:

    `cd s21_resume_checker_bot`

3. Install the dependencies:

    `pip install -r requirements.txt`

4. Create a `config.json` file with your settings. Example structure of the file:

    ```json
    {
      "auth": {
        "telegram": {
          "token": "YOUR_TELEGRAM_BOT_TOKEN"
        },
        "gigachat": [
          {
            "auth_data": "YOUR_GIGACHAT_AUTH_DATA"
          },
          {
            "scope": "YOUR_GIGACHAT_SCOPE"
          }
        ]
      }
    }
    ```

5. Start the bot:

    `python3 src/main.py`

## Features

- **Resume Analysis**: The bot analyzes uploaded resumes in PDF format and provides recommendations for improvement.
- **GigaChat Integration**: Uses GigaChat to generate suggestions for resume improvement.

## Development

### Project Structure

```bash
s21_resume_checker_bot/
├── src/
│   ├── main.py            # Application entry point
│   ├── parser.py          # Module for extracting text from PDF files
│   ├── handlers.py        # Telegram message handlers
│   ├── gigachat_api.py    # Integration with GigaChat API
│   └── just_messages.py   # Simple text responses
├── config.json            # Configuration file
└── requirements.txt       # Project dependencies
```

---

Date: 13-02-2024
