pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/kapilkhurana89/terraform-pyhton-pipline.git'
            }
        }

        stage('Run Python') {
            steps {
                bat 'python trigger.py'
            }
        }
    }
}