pipeline {
    agent any

    environment {
        VENV = '.venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Python') {
            steps {
                sh 'python3 -m venv "$VENV"'
                sh '"$VENV/bin/python" -m pip install --upgrade pip'
                sh '"$VENV/bin/pip" install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '"$VENV/bin/python" -m pytest -v'
            }
        }

        stage('Restart service') {
            steps {
                sh 'sudo systemctl restart flask-github-repository.service'
                sh 'sudo systemctl is-active --quiet flask-github-repository.service'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'test-results.xml', allowEmptyArchive: true
        }
    }
}