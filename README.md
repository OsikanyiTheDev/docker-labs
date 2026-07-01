# 🐳 Docker Learning Labs (2–7)

A hands-on DevOps learning journey covering Docker fundamentals through advanced container deployment, including Compose, security, and AWS ECR deployment.

---

## 📌 Overview

This repository documents my step-by-step progress in learning Docker and container-based application deployment.

It includes:

* Building Docker images
* Managing persistent data with volumes
* Container networking
* Multi-container apps using Docker Compose
* Flask + MySQL full-stack container app
* Container security hardening
* AWS ECR image deployment

---

## 📚 Lab Progress

### ✅ Lab 2 — Building Docker Images

* Created custom Docker images using Dockerfile
* Learned layers, caching, and build context
* Ran Python applications inside containers

---

### ✅ Lab 3 — Volumes and Persistence

* Used Docker volumes for persistent storage
* Understood container data lifecycle
* Separated application and data storage

---

### ✅ Lab 4 — Docker Networking

* Created multiple containers communicating over Docker networks
* Understood bridge networking
* Container-to-container communication

---

### ✅ Lab 5 — Docker Compose (Multi-Container Apps)

* Built multi-service application using `docker-compose.yml`
* Connected Flask application with MySQL database
* Used service discovery (`db` hostname)
* Learned environment variables and dependencies

### 🧠 Stack Used:

* Flask (Python)
* MySQL 8
* Docker Compose

---

### ✅ Lab 6 — Container Security Hardening

* Understood container security principles:

  * Running non-root users inside containers
  * Minimizing image size
  * Reducing privileges
* Compared insecure vs secure container configurations

---

### ✅ Lab 7 — Private Registry & AWS ECR

* Created AWS ECR repository
* Built Docker images locally
* Tagged images for AWS ECR
* Pushed images to Amazon ECR

### 🚀 Commands Used:

```bash
aws ecr create-repository --repository-name my-flask-app

aws ecr get-login-password | docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-1.amazonaws.com

docker tag my-flask-app:latest <account>.dkr.ecr.us-east-1.amazonaws.com/my-flask-app:latest

docker push <account>.dkr.ecr.us-east-1.amazonaws.com/my-flask-app:latest
```

---

## 🧰 Technologies Used

* Docker
* Docker Compose
* Flask (Python)
* MySQL
* AWS ECR
* Linux (Ubuntu VM)
* Git & GitHub

---

## 📁 Project Structure

```
docker-labs/
│
├── docker-lab2/
├── docker-lab3/
├── docker-lab4/
├── docker-lab5-compose/
├── docker-lab6-security/
├── docker-lab7-ecr/
```

---

## 🎯 Key Skills Learned

* Containerization fundamentals
* Multi-container orchestration
* Database integration with apps
* Networking between containers
* Security best practices
* Cloud container registry (AWS ECR)
* CI/CD readiness foundation

---

## 🚀 How to Run (Example: Lab 5)

```bash
cd docker-lab5-compose

docker compose up --build
```

Then open:

```
http://localhost:5000
```

---

## 📦 Author

**Osikanyi Essandoh**
Cloud & DevOps Learner
Focused on Docker, AWS, Data Engineering & Financial Engineering

---

## 📌 Future Work

* Kubernetes (Lab 8+)
* AWS ECS Fargate deployment
* CI/CD pipelines with GitHub Actions
* Monitoring with Prometheus & Grafana
