import subprocess


def run_command(command):
    result = subprocess.run(command,shell=True)

    if result.returncode != 0:
       print(f"Error running: {command}")
       exit(1)

print("Initializing Terraform...")
run_command("terraform init")

print("Planning Infrastructure...")
run_command("terraform plan")

print("Applying Infrastructure...")
run_command("terraform apply -auto-approve")

print("EC2 Instance Created Successfully")

    