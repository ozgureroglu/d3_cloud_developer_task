## Terrraform for Lambda
This is the terraform project which handles the deployment of the lambda function that will be used to deploy the .zip archive to AWS Lambda Service.

- Terraform gets the lambda functions .zip folder from the Lambda source folder, and it is hardcoded here, for now!!!
- For testing the deployed lambda a test event can be created in the following format ( or any trigger should send the event in this format ). Following were the ones I tested with. 

```
{
  "bucket": "tfbackend-oe",
  "key": "state/infra.tfstate",
  "output_name": "alb_id"
}
```