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
                    usernameVariable: 'pranav9752',
                    passwordVariable: 'Pranav@9752'
                )]) {
                    sh """
                    docker login -u $DOCKER_USER -p $DOCKER_PASS
                    docker tag gradient pranav9752/gradient:jenkins
                    docker push pranav9752/gradient:jenkins
                    """
                }
            }
        }
    }
}
