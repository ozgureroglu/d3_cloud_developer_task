# Cloud Developer Task

This repository folder contains the code for the task given for the Cloud Solutions Architect Role.

## Prerequisite: 

This projects assumes that 
- You have an AWS account and configured a profile for AWS CLI to access your account from command line.
- You already created an S3 bucket to be used for holding tfstate files



# Project Folders
There are 3 projects in this folder:

## InfraTF

This folder includes a Terraform project to setup an sample infrastructure to be used as the testing environment.
- It holds the terraform state on S3
- It will serve as the source of tfstate file that will be used.
- Includes various AWS resources to be generated


## LambdaTF

This folder includes the Terraform projects that will handle the deployment of the Lambda Function. The code for Lambda function will be developed in the 3rd folder below. 


## PythonLambdaFunction

This folder holds the python lambda function that will do the actual business.
