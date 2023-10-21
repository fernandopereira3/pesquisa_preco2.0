terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.22.0"
    }
  }
}

provider "aws" {
    profile = "default"
    region = "us-west-2"
}

resource "aws_instance" "servidor" {
    ami           =  "ami-0efcece6bed30fd98"
    instance_type = "t2.nano"
    key_name = aws_key_pair.ssh.key_name
    tags = {
        Name = "servidor"
     }
}

resource "aws_key_pair" "ssh" {
  key_name   = "ssh"
  public_key = file("python.pub")
}