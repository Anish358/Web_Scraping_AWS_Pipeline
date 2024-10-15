import requests
from bs4 import BeautifulSoup
import json
import boto3
from datetime import datetime
import yaml

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

s3 = boto3.client('s3')
BUCKET_NAME = config['aws']['s3_bucket']

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find('h1').text.strip()
    content = ' '.join([p.text.strip() for p in soup.find_all('p')])
    
    return {
        'url': url,
        'title': title,
        'content': content,
        'timestamp': datetime.now().isoformat()
    }

def upload_to_s3(data, filename):
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=json.dumps(data),
        ContentType='application/json'
    )

def main():
    websites = config['scraping']['websites']
    
    for url in websites:
        try:
            data = scrape_website(url)
            filename = f"scraped_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            upload_to_s3(data, filename)
            print(f"Uploaded data from {url} to S3")
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")

if __name__ == "__main__":
    main()