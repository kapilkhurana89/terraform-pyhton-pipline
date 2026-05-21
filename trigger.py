import os

terraform = r"C:\terraform\terraform.exe"

print("Initializing Terraform...")
os.system(f'"{terraform}" init')

print("Planning Terraform...")
os.system(f'"{terraform}" plan')

print("Applying Terraform...")
os.system(f'"{terraform}" apply -auto-approve')