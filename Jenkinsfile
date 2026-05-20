pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                git 'https://github.com/kapilkhurana89/terraform-pyhton-pipline.git'
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'py trigger.py'
            }
        }

    }
}