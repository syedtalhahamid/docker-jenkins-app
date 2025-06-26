pipeline {
  agent any
  stages {
    stage('Clone') {
      steps {
        git 'https://github.com/your-org/student-feedback-microservice.git'
      }
    }
    stage('Build & Push Docker Images') {
      steps {
        dir('frontend-service') {
          sh 'docker build -t yourdockerhub/frontend-service .'
          sh 'docker push yourdockerhub/frontend-service'
        }
        dir('feedback-service') {
          sh 'docker build -t yourdockerhub/feedback-service .'
          sh 'docker push yourdockerhub/feedback-service'
        }
      }
    }
    stage('Deploy on EC2') {
      steps {
        sh 'ssh ec2-user@<ec2-ip> "cd /home/ec2-user/app && docker-compose pull && docker-compose up -d"'
      }
    }
  }
}
