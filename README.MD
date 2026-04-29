# ACEest DevOps Assignment

**Submitted by:** Sai Ganesh T
**Roll No:** 2025ht66021

---

## 📌 Project Overview

This project demonstrates a complete DevOps pipeline for a Flask-based fitness management application. It includes version control, automated testing, CI/CD pipeline, containerization, Kubernetes deployment, and code quality analysis using SonarQube.

---

## ⚙️ Technologies Used

* Python (Flask)
* Git & GitHub
* Pytest
* Jenkins
* Docker
* Docker Hub
* Kubernetes (Minikube)
* SonarQube

---

## 🚀 Application Setup

Run locally:

```bash
python app.py
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🔄 CI/CD Pipeline

* Jenkins pulls code from GitHub
* Installs dependencies
* Runs automated tests
* Builds Docker image

---

## 🐳 Docker

Build image:

```bash
docker build -t aceest-app .
```

Push to Docker Hub:

```bash
docker push oceanbuffalo/aceest-app:v1
```

Docker Hub Repository:
https://hub.docker.com/r/oceanbuffalo/aceest-app

---

## ☸️ Kubernetes Deployment

```bash
kubectl apply -f deployment.yaml
kubectl expose deployment aceest-app --type=NodePort --port=5000
minikube service aceest-app
```

---

## 🔁 Deployment Strategies

* Rolling Update implemented using Kubernetes
* Rollback supported using:

```bash
kubectl rollout undo deployment aceest-app
```

---

## 🔍 SonarQube Code Quality Analysis

This project integrates **SonarQube** for static code analysis to ensure code quality and maintainability.

### 🚀 Setup (Docker)

```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts
```

Access SonarQube:
http://localhost:9000

---

### 🔐 Token Generation

* Login to SonarQube
* Go to: `My Account → Security`
* Generate a **Project Analysis Token**

---

### ▶️ Run Scan

```bash
docker run --rm -v "%cd%:/usr/src" sonarsource/sonar-scanner-cli \
-Dsonar.projectKey=aceest-devops \
-Dsonar.projectName=ACEest \
-Dsonar.sources=. \
-Dsonar.inclusions=app.py \
-Dsonar.exclusions=**/.git/**,**/__pycache__/**,**/.pytest_cache/** \
-Dsonar.host.url=http://host.docker.internal:9000 \
-Dsonar.login=<YOUR_TOKEN>
```

---

### 📊 Analysis Scope

* File analyzed: `app.py`
* Language: Python

---

### ✅ Outcome

* Static code analysis executed successfully
* Code quality metrics evaluated
* Issues (if any) identified

---

### 📸 Evidence

Screenshot of SonarQube dashboard is included in submission.

---

## 📊 Key Outcomes

* Automated CI/CD pipeline
* Containerized application
* Kubernetes deployment
* Code quality analysis using SonarQube

---

## ⚠️ Challenges Faced

* Jenkins environment path issues
* Docker access configuration
* Kubernetes setup and deployment
* SonarQube scan optimization

---

## ✅ Conclusion

This project successfully demonstrates a real-world DevOps pipeline integrating development, testing, containerization, deployment, and code quality analysis. It highlights how automation improves reliability, scalability, and efficiency.

---
