"""
Configuration settings for the news scraper.
"""

# News API Configuration
NEWS_API_KEY = "bab148e8bdf845aebd074d90c80f4407"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
NEWS_API_PARAMS = {
    "country": "us",
    "pageSize": 12,
    "apiKey": NEWS_API_KEY,
}

# Email Configuration
EMAIL_CONFIG = {
    "sender_email": "dev.podshipnikoff@gmail.com",
    "sender_password": "ygyu oiik ntdc merv",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 465,
}

# Default recipient email
DEFAULT_RECIPIENT = "aaelin05@gmail.com" 