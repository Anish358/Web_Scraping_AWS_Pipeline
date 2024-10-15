# AWS Setup Guide for Web Scraping and Analysis Pipeline

This guide provides step-by-step instructions for setting up the required AWS services for our Web Scraping and Analysis Pipeline.

## Prerequisites

- An AWS account
- AWS CLI installed and configured on your local machine
- Basic understanding of AWS services (S3, Lambda, DynamoDB)

## 1. Create an S3 Bucket

1. Go to the AWS S3 console
2. Click "Create bucket"
3. Choose a unique name for your bucket (e.g., "web-scraping-raw-data-v0 ")
4. Select the region closest to you
5. Leave other settings as default
6. Click "Create bucket"

## 2. Create a DynamoDB Table

1. Go to the AWS DynamoDB console
2. Click "Create table"
3. Set table name to "ProcessedWebData"
4. Set partition key to "id" (String)
5. Leave other settings as default
6. Click "Create"

## 3. Create a Lambda Function

1. Go to the AWS Lambda console
2. Click "Create function"
3. Choose "Author from scratch"
4. Set function name to "ProcessWebScrapedData"
5. Choose Python 3.9 as the runtime
6. Under "Permissions", choose "Create a new role with basic Lambda permissions"
7. Click "Create function"
8. In the "Code" tab, replace the default code with the content of your `lambda_function.py`
9. Click "Deploy" to save your changes

## 4. Configure Lambda Function

1. In the Lambda function page, go to the "Configuration" tab
2. Click on "General configuration" and edit
3. Increase the timeout to 1 minute (or more if needed)
4. Increase the memory if needed (start with 256MB and adjust as necessary)
5. Save your changes

## 5. Set Up IAM Permissions

1. Go to the IAM console
2. Find the role created for your Lambda function (it should start with "ProcessWebScrapedData-")
3. Click on the role name
4. Click "Add permissions" then "Create inline policy"
5. Go to the JSON tab and paste the following policy (replace with your actual values):

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::your-bucket-name/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem"
            ],
            "Resource": "arn:aws:dynamodb:your-region:your-account-id:table/ProcessedWebData"
        }
    ]
}
```

6. Review and create the policy

## 6. Set Up S3 Trigger for Lambda

1. Go back to your S3 bucket
2. Go to the "Properties" tab
3. Scroll down to "Event notifications" and click "Create event notification"
4. Configure as follows:
   - Name: "TriggerLambdaOnUpload"
   - Event types: Check "All object create events"
   - Destination: Choose "Lambda function"
   - Lambda function: Select "ProcessWebScrapedData"
5. Save your changes

## 7. Test the Setup

1. Upload a JSON file to your S3 bucket with the following structure:
   ```json
   {
     "url": "https://example.com",
     "title": "Example Page",
     "content": "This is the content of the page.",
     "timestamp": "2023-05-20T12:00:00Z"
   }
   ```
2. Check your DynamoDB table to see if the data was processed and stored

## Troubleshooting

- If the Lambda function isn't triggered, check the S3 event notification setup
- If the Lambda function is triggered but fails, check the CloudWatch logs for error messages
- Ensure your IAM permissions are set up correctly

## Security Considerations

- Always follow the principle of least privilege when setting up IAM permissions
- Consider encrypting your S3 bucket and DynamoDB table for sensitive data
- Regularly review and rotate your AWS access keys

## Cleanup

To avoid unnecessary AWS charges, remember to delete these resources when you're done:
1. S3 bucket
2. DynamoDB table
3. Lambda function
4. IAM role created for the Lambda function

## Using with Docker

When running the web scraper in a Docker container, ensure that the container has access to your AWS credentials. You can do this by mounting your AWS credentials file:

```bash
docker run -it --rm \
  -v ~/.aws:/root/.aws:ro \
  -e AWS_PROFILE=default \
  your-docker-image-name
```

Remember to never commit your AWS credentials to version control. Always use environment variables or mount the credentials file at runtime.