## Sample Infrastructure with Terraform

This is the terraform project which will create the testing infrastructure. The lambda function will be processing the tfstate file of this project. That will include outputs of various objects including the ALB mentioned in the task question.

- It will store its state to a predefined bucket and key ( *it is assumed that this is already manually created* ). 
- The tfstate file of this project will be used for testing the lambda function.
  - Lambda function is developed under the *PythonLambdaFunction* folder and deployed with the Terraform project under the *LambdaTF* folder.

- This TF project creates EC2 instances, an ALB, necessary SG's etc to open them internet.

- For EC2 instances to be accessible by ssh, provide a pem in the this project folder with name ___Keypair-01.pem___