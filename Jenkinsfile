pipeline {
    agent any

    environment {
        IMAGE_NAME = "gradient"
        DOCKER_REPO = "pranav9752/gradient"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'b1', url: 'https://github.com/pranav1468/ML-OPS.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Run Container for Testing') {
            steps {
                sh "docker run --name gradient_test --rm ${IMAGE_NAME}:latest"
            }
        }

        stage('Login & Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                        echo "Logging in to DockerHub..."
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin

                        docker tag ${IMAGE_NAME}:latest ${DOCKER_REPO}:jenkins
                        docker push ${DOCKER_REPO}:jenkins

                        echo "✅ Image pushed: ${DOCKER_REPO}:jenkins"
                    """
                }
            }
        }
    }
}
