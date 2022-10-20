import boto3
import json

s3 = boto3.resource('s3')


# --------------- Main handler ------------------
def lambda_handler(event, context):
      
    # Get the bucket key as inputs for the lambda
    bucket = event['bucket']
    key = event['key']
    
    # Get the name of the output section to extract. This is optional
    # and if no value is provided, lambda will print all output content
    output_name = event.get('output_name', None)
    
    content_object = s3.Object(bucket, key)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    
    # Check whether the output_name is given in the input
    if output_name == None:
        print(json_content['outputs'])
        outputs = json_content['outputs']
    else:
        print(json_content['outputs'][output_name])    
        outputs = json_content['outputs'][output_name]
    
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "Outputs": outputs
    }