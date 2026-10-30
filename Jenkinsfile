pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Getting Python Incident Tracker source code'
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t python-incident-cicd:1.0 .'
            }
        }

        stage('Load Image into Minikube') {
            steps {
                sh 'minikube image load python-incident-cicd:1.0'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
                sh 'kubectl rollout status deployment/python-incident-cicd'
            }
        }
    }
}
