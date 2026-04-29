pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/TSG46/aceest-devops-v2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install flask pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t aceest-app .'
            }
        }
    }
}