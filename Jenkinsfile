pipeline {
    agent any

    tools {
        python 'Py'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'YOUR_GITHUB_REPO_URL'
            }
        }

        stage('Verify Tools') {
            steps {
                bat 'terraform -version'
                bat 'python --version'
                bat 'aws --version'
            }
        }

        stage('Run Python Trigger') {
            steps {
                bat 'py trigger.py'
            }
        }
    }

    post {
        success {
            echo 'Terraform Infrastructure Created Successfully'
        }

        failure {
            echo 'Pipeline Failed'
        }
    }
}