# HSA13_hw26 AWS FastAPI Autoscaling Groups on AWS

This project demonstrates how to deploy a simple FastAPI application in Docker containers on AWS using Auto Scaling Groups managed by Terraform. The infrastructure includes a VPC, subnets, an Application Load Balancer (ALB), and an autoscaling group of EC2 instances running the FastAPI app.
Features

    FastAPI Application: A lightweight, async web app with a single endpoint (/) returning a "Hello World" message.
    Dockerized: The app runs inside a Docker container for portability and consistency.
    AWS Infrastructure: Managed via Terraform, including VPC, subnets, ALB, and Auto Scaling Groups.
    Autoscaling: Automatically scales the number of EC2 instances based on demand.

## Prerequisites

    Docker and Docker Compose for local testing.
    Terraform for infrastructure deployment.
    An AWS account with configured credentials (~/.aws/credentials).
    A Docker Hub account to push the container image.


##  Local Setup and Testing

### 1. Clone the repository:
    
```
git clone <repository-url>
cd <repository-directory>
```
### 2. Build and run locally with Docker Compose:

```

    docker-compose up --build
```
### 3. Test the app:
        Open your browser and go to http://localhost:8000.
        You should see: {"message": "Hello World from FastAPI in Docker on AWS!"}.

##  Deploying to AWS

    Build and push the Docker image:
    
```
docker build -t <your-dockerhub-username>/fastapi-app:latest .
docker push <your-dockerhub-username>/fastapi-app:latest
```
Update Terraform configuration:

    In terraform/main.tf, replace <your-dockerhub-username> in the user_data script with your Docker Hub username.
    Adjust variables in terraform/terraform.tfvars as needed (e.g., region, AMI ID, instance type).

Deploy the infrastructure:

```
    cd terraform
    terraform init
    terraform apply
```
    Access the app:
        After deployment, Terraform will output the ALB DNS name (e.g., web-alb-123456789.us-west-2.elb.amazonaws.com).
        Open this URL in your browser to access the FastAPI app.

##  Endpoints

    GET /: Returns a JSON response with a "Hello World" message.
        Example response: {"message": "Hello World from FastAPI in Docker on AWS!"}

##  Cleanup

To destroy the AWS infrastructure:
```
cd terraform
terraform destroy
```
##  Notes

    Ensure your AWS credentials have permissions to create VPCs, subnets, EC2 instances, ALBs, and Auto Scaling Groups.
    The default port for the FastAPI app is 8000, which is exposed via the ALB on port 80.

