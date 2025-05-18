"""
Main script for the news scraper application.
"""
from src.news_scraper.services.news_service import NewsService
from src.news_scraper.services.email_service import EmailService
from src.news_scraper.services.template_service import TemplateService
from src.news_scraper.config import DEFAULT_RECIPIENT

def main():
    """
    Main function to fetch news and send email.
    """
    # Get news
    news_service = NewsService()
    news = news_service.get_top_news()
    
    # Create email content
    template_service = TemplateService()
    news_blocks = template_service.create_news_blocks(news)
    html_content = template_service.create_html(news_blocks)
    
    # Send email
    email_service = EmailService()
    subject = "Daily Top News - Your Latest Headlines"
    
    if email_service.send_email(DEFAULT_RECIPIENT, subject, html_content):
        print("Email sent successfully!")
    else:
        print("Failed to send email.")

if __name__ == "__main__":
    main()