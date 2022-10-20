This is the terraform project which will create the testing infrastructure.

- It will store its state to a predefined bucket and key ( *it is assumed that this is already manually created* ). 
- The tfstate file of this project will be used for testing the lambda function.
  - Lambda function is developed under the *PythonLambdaFunction* folder and deployed with the Terraform project under the *LambdaTF* folder.



- This TF project creates an application EC2 instances, an ALB to open them internet.

- For EC2 instances to be ssh accessible provide a pem in the this project folder with name **Keypair-01.pem**