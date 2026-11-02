pipeline {
    agent any

    environment {
        HOME = '/home/premchand'
        KUBECONFIG = '/home/premchand/.kube/config'
    }

    stages {
        stage('Checkout') {
            steps {
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
                sh 'sg k8saccess -c "minikube image load python-incident-cicd:1.0"'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'sg k8saccess -c "kubectl apply -f deployment.yaml"'
                sh 'sg k8saccess -c "kubectl apply -f service.yaml"'
                sh 'sg k8saccess -c "kubectl rollout status deployment/python-incident-cicd"'
            }
        }
    
