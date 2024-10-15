import json
import boto3
from urllib.parse import unquote_plus

# Initialize AWS clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ProcessedWebData')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = unquote_plus(event['Records'][0]['s3']['object']['key'])
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
        data = json.loads(content)
        
        item = {
            'id': data['url'],
            'title': data['title'],
            'content_summary': data['content'][:200] + '...' if len(data['content']) > 200 else data['content'],
            'timestamp': data['timestamp']
        }
        
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully processed data from {data["url"]}')
        }
    except Exception as e:
        print(f"Error processing {key}: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error processing {key}: {str(e)}')
        }