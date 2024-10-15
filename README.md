# Web Scraping and Analysis Pipeline
[![AWS License](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Python License](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://aws.amazon.com/)
[![Docker License](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

This project implements an automated web scraping and analysis pipeline using Python, Docker, and AWS services.

## Technologies Used

- Python 3.9
- Docker
- AWS (S3, Lambda, DynamoDB)
- BeautifulSoup4 for web scraping
- Boto3 for AWS SDK

## Project Structure

- `src/`: Contains the main Python scripts
- `config/`: Configuration files
- `docs/`: Additional documentation
- `Dockerfile`: Instructions for building the Docker container
- `docker-compose.yml`: Docker Compose configuration

## 💡 Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/SanjayKParida/web-scraping-aws-pipeline.git
   cd web-scraping-aws-pipeline
   ```

2. Set up AWS credentials:
   - Follow the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) to set up your credentials

3. Configure AWS services:
   - Create an S3 bucket
   - Set up a DynamoDB table
   - Create a Lambda function
   - Configure S3 event to trigger Lambda
   (Detailed steps are in `docs/aws_setup.md`)

4. Update the `config/config.yaml` file with your AWS resource names and target websites.

## ⚡️ Usage with Docker

1. Build the Docker image:
   ```
   docker build -t web-scraper .
   ```

2. Run the Docker container:
   ```
   docker run -it --rm \
     -v ~/.aws:/root/.aws:ro \
     -e AWS_PROFILE=default \
     web-scraper
   ```

Alternatively, use Docker Compose:
```
docker-compose up
```

## 📟 Local Usage (without Docker)

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the scraper:
   ```
   python src/scraper.py
   ```

## ☎️ Contact

Sanjay Kumar Parida - kumarparidasanjay23@gmail.com
Project Link: [https://github.com/SanjayKParida/web-scraping-aws-pipeline](https://github.com/SanjayKParida/web-scraping-aws-pipeline)
