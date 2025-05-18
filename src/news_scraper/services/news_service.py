"""
News service module for fetching and processing news data.
"""
import requests
from src.news_scraper.config import NEWS_API_URL, NEWS_API_PARAMS

class NewsService:
    @staticmethod
    def get_top_news():
        """
        Fetch top news from the News API.
        
        Returns:
            list: List of news articles with their details.
        """
        response = requests.get(NEWS_API_URL, params=NEWS_API_PARAMS)
        data = response.json()

        if response.status_code != 200:
            print("Error:", data.get("message", "Unknown error"))
            return []

        articles = data["articles"]
        return [
            {
                "title": article["title"],
                "source": article["source"]["name"],
                "published_at": article["publishedAt"],
                "description": article["description"],
                "url": article["url"],
                "image_url": article["urlToImage"],
            }
            for article in articles
        ] 