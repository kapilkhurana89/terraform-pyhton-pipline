pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('aws-creds')
        AWS_SECRET_ACCESS_KEY = credentials('aws-creds')
        AWS_DEFAULT_REGION    = 'ap-south-1'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/kapilkhurana89/terraform-pyhton-pipline.git'
            }
        }

        stage('Run Python') {
            steps {
                bat '"C:\\Users\\kapil\\AppData\\Local\\Python\\bin\\python.exe" trigger.py'
            }
        }
    }
}