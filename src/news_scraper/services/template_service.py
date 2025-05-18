"""
Template service module for generating HTML content.
"""

class TemplateService:
    @staticmethod
    def create_news_blocks(news_list):
        rows = []
        for i in range(0, len(news_list), 2):
            news_pair = news_list[i:i+2]
            tds = ""
            for news in news_pair:
                tds += f'''
                <td width="50%" valign="top" style="padding: 10px;">
                    <a href="{news["url"]}" style="text-decoration: none; background-color: white; display: block; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                        <img src="{news["image_url"]}" alt="News Image" style="width: 100%; height: 200px; object-fit: cover; display: block;">
                        <div style="padding: 15px;">
                            <h2 style="margin: 0 0 10px; font-size: 18px; color: #2c3e50;">{news["title"]}</h2>
                            <p style="margin: 0 0 15px; color: #7f8c8d;">{news["description"]}</p>
                            <span style="font-weight: bold; color: #2c3e50;">{news["source"]}</span>
                            <p style="color: #95a5a6; margin-top: 10px; font-size: 12px;">{news["published_at"]}</p>
                        </div>
                    </a>
                </td>
                '''
            # If only one news block in this row, fill second cell with empty td
            if len(news_pair) == 1:
                tds += '<td width="50%" style="padding: 10px;"></td>'
            rows.append(f'<tr>{tds}</tr>')
        return '\n'.join(rows)

    @staticmethod
    def create_html(news_blocks):
        """
        Create the complete HTML email template with table layout (Gmail-compatible).

        Args:
            news_blocks (str): HTML table rows with news blocks

        Returns:
            str: Complete HTML email template
        """
        return f'''
        <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background-color: #f5f5f5; color: #333;">
            <center>
                <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f5f5f5">
                    <tr>
                        <td align="center" bgcolor="#2c3e50" style="padding: 20px; color: white;">
                            <h1 style="margin: 0; font-size: 28px;">Daily Top News</h1>
                            <p style="margin: 10px 0 0; font-size: 16px;">Your source for the latest headlines</p>
                        </td>
                    </tr>
                    <tr>
                        <td align="center">
                            <table width="80%" cellpadding="0" cellspacing="0" border="0" style="margin: 20px auto; min-width: 600px;">
                                {news_blocks}
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" bgcolor="#2c3e50" style="padding: 20px; color: white;">
                            <p style="margin: 0;">&copy; 2025 Daily Top News. All rights reserved.</p>
                        </td>
                    </tr>
                </table>
            </center>
        </body>
        '''
