from flask import Flask, render_template
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    rss_feed_url = "https://static.cricinfo.com/rss/livescores.xml"
    try:
        response = requests.get(rss_feed_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        root = ET.fromstring(response.content)
        
        scores = []
        for item in root.findall('.//item'):
            title = item.find('title').text if item.find('title') is not None else 'N/A'
            link = item.find('link').text if item.find('link') is not None else '#'
            description = item.find('description').text if item.find('description') is not None else 'N/A'
            scores.append({'title': title, 'link': link, 'description': description})
            
        return render_template('index.html', scores=scores)
    except requests.exceptions.RequestException as e:
        return f"Error fetching RSS feed: {e}", 500
    except ET.ParseError as e:
        return f"Error parsing RSS feed: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
