pipeline {
    agent any

    stages {
        stage('Scan code with Semgrep') {
            steps {
                sh '''#!/bin/bash
                python3 -m venv .venv
                source .venv/bin/activate
                pip3 install semgrep
                semgrep --config=auto --junit-xml -o logs/app-scan.xml app.py
                deactivate'''
                junit skipMarkingBuildUnstable: true, testResults: 'logs/app-scan.xml'
            }
        }
        stage('Removing current Docker container') {
            steps {
                sh 'docker stop $(docker container ls -q)'
            }
        }
        stage('Build Docker container') {
            steps {
                sh 'docker build -f Dockerfile -t app .'
            }
        }
        stage('Scan container with Trivy') {
            steps {
                sh 'curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl > html.tpl'
                sh 'mkdir -p logs'
                sh 'trivy image --ignore-unfixed --format template --template "@html.tpl" -o logs/app-scan.html app:latest'
                archiveArtifacts 'logs/app-scan.html'
                sh 'trivy image --ignore-unfixed --exit-code 1 --severity CRITICAL app:latest'
            }
        }
        stage('Run Docker container') {
            steps {
                sh 'docker run -d -p 5000:5000 app:latest'
            }
        }
    }
}