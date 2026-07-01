# 🚀 Docker Lab 7 — Private Registry & AWS ECR

## 📌 Overview
This project demonstrates how to:
- Build a Docker image
- Create an AWS ECR repository
- Tag Docker images for AWS
- Push images to a private registry

---

## 🏗️ Tech Stack
- Docker
- Flask (Python)
- AWS ECR
- AWS CLI

---

## ⚙️ Steps Performed

### 1. Build Docker Image
```bash
docker build -t my-flask-app .


### 2. Create ECR Repository
aws ecr create-repository --repository-name my-flask-app

### 3. Tag Image
docker tag my-flask-app:latest <account_id>.dkr.ecr.us-east-1.amazonaws.com/my-flask-app:latest

### 4. Push Image to AWS
docker push <account_id>.dkr.ecr.us-east-1.amazonaws.com/my-flask-app:latest

