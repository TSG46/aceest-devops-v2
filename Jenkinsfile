pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\Sai Ganesh\\AppData\\Local\\Python\\bin\\python.exe"
    }

    stages {

        stage('Clone Code') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/TSG46/aceest-devops-v2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat '"%PYTHON%" -m pip install flask pytest'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                bat '"%PYTHON%" -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t aceest-app .'
            }
        }
    }
}