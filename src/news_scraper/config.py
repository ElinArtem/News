"""
Configuration settings for the news scraper.
"""

# News API Configuration
NEWS_API_KEY = "YOUR_API_KEY"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
NEWS_API_PARAMS = {
    "country": "us", # Change region of news
    "pageSize": 12, # Count of news
    "apiKey": NEWS_API_KEY,
}

# Email Configuration
EMAIL_CONFIG = {
    "sender_email": "YOUR_EMAIL", 
    "sender_password": "EMAIL_PASSWORD", # it's placed in dev mode in gmail
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 465,
}

# Default recipient email
DEFAULT_RECIPIENT = "EMAIL" 