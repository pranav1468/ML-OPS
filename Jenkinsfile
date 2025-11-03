pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'b1', url: 'https://github.com/pranav1468/ML-OPS.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t gradient .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run gradient'
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                        echo "Logging into DockerHub..."
                        docker login -u $DOCKER_USER -p $DOCKER_PASS
                        docker tag gradient $DOCKER_USER/gradient:jenkins
                        docker push $DOCKER_USER/gradient:jenkins
                    """
                }
            }
        }
    }
}
