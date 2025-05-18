# News Scraper

A Python application that fetches top news headlines and sends them via email in a beautifully formatted HTML template.

## Features

- Fetches top news headlines from News API
- Creates beautiful HTML email templates
- Sends formatted news via email
- Configurable settings

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

## Configuration

Edit `src/news_scraper/config.py` to configure:
- News API settings
- Email settings
- Default recipient email

## Usage

Run the application using the entry point script:
```bash
python run.py
```

## Project Structure

```
.
├── run.py              # Entry point script
├── setup.py           # Package setup file
├── requirements.txt   # Project dependencies
└── src/
    └── news_scraper/
        ├── __init__.py
        ├── config.py
        └── services/
            ├── news_service.py
            ├── email_service.py
            └── template_service.py
```

## License

MIT License
