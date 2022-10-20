This is the terraform project which will create the testing infrastructure.

### Prerequsities
- You should have an AWS account and configured your AWS CLI configuration at your own laptop.

- It will store its state to a predefined bucket and key. 
- The tfstate file of this project will be used for testing the lambda function which is developed under the lambda_app folder and deployed with the Terraform project under the LambdaTF folder.

- Credentials to access the S3 bucket are provided through AWS_PROFILE env variable, which is exported before running the terraform init command.

- This TF project creates an application EC2 instance, an ALB to open it internet.

- For EC2 instances to be ssh accessible provide a pem in the this project folder with name Keypair-01.pem