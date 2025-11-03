pipeline {
    agent any

    environment {
        IMAGE_NAME = "pranav9752/gradient"
    }

    stages {
        
        stage('Checkout Code') {
            steps {
                git branch: 'b1',
                    url: 'https://github.com/pranav1468/ML-OPS.git',
                    credentialsId: 'github-creds'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t gradient ."
            }
        }

        stage('Run Container Test') {
            steps {
                sh "docker run --rm gradient"
            }
        }

        stage('Login & Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh """
                    echo $PASS | docker login -u $USER --password-stdin
                    docker tag gradient $IMAGE_NAME:jenkins
                    docker push $IMAGE_NAME:jenkins
                    """
                }
            }
        }
    }
}
