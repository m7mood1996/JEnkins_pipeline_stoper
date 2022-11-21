/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Install pre-requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Python Script') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
