/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Python Script') {
            steps {
                sh 'python -mainn.py'
            }
        }
    }
}
