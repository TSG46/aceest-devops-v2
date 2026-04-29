# ACEest DevOps Assignment

Submitted by Sai Ganesh T
Roll No: 2025ht66021

---

## 📌 Project Overview

This project demonstrates a complete DevOps pipeline for a Flask-based fitness management application. It includes version control, automated testing, CI/CD pipeline, containerization, and Kubernetes deployment.

---

## ⚙️ Technologies Used

* Python (Flask)
* Git & GitHub
* Pytest
* Jenkins
* Docker
* Docker Hub
* Kubernetes (Minikube)

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

## 📊 Key Outcomes

* Automated CI/CD pipeline
* Containerized application
* Kubernetes deployment
* Zero-downtime deployment strategy

---

## ⚠️ Challenges Faced

* Jenkins environment path issues
* Docker access from Jenkins
* Kubernetes setup and configuration

---

## ✅ Conclusion

The project successfully demonstrates a real-world DevOps pipeline with automation, testing, containerization, and deployment strategies.

---
