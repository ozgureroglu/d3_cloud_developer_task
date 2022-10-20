terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.3.0"

  backend "s3" {
    bucket = "tfbackend-oe"
    key    = "state/infra.tfstate"
    region = "eu-central-1"
  }
}

# Configure AWS provider:
provider "aws" {
  region  = "us-east-1"
}