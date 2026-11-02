
pipeline {
    agent any

    environment {
        HOME = '/home/premchand'
        KUBECONFIG = '/home/premchand/.kube/config'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Python Incident Tracker'
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image'
                sh 'docker build --progress=plain -t python-incident-cicd:1.0 .'
            }
        }

        stage('Load Image into Minikube') {
            steps {
                echo 'Loading image into Minikube'
                sh 'sg k8saccess -c "minikube image load python-incident-cicd:1.0"'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying application'
                sh 'sg k8saccess -c "kubectl apply -f deployment.yaml"'
                sh 'sg k8saccess -c "kubectl apply -f service.yaml"'
                sh 'sg k8saccess -c "kubectl rollout status deployment/python-incident-cicd --timeout=120s"'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'sg k8saccess -c "kubectl get pods"'
                sh 'sg k8saccess -c "kubectl get services"'
            }
        }
    }
}

