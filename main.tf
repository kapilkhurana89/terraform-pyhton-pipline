provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "myserver" {
  ami           = "ami-01e8f03e3711eff18"
  instance_type = "t2.micro"
  key_name      = "ForSSH"

  tags = {
    Name = "PythonTerraformServer"
  }
}