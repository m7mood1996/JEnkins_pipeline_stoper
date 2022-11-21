/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('check python version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Install pre-requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Python Script') {
            steps {
                sh 'python3 main.py'
            }
        }
    }
}
