pipeline {
   agent any

   stages {
     stage('Show Files') {
       steps {
	sh 'ls -la'
	}
      }
    
      stage('Build Docker Image'){
	steps {
	  sh 'docker build -t employee-app-ci .'
       }
     }
      stage('Verify Image'){
	steps {
	   sh 'docker images | grep employee-app-ci'
         }
       }
      stage('Deploy with Docker Compose'){
	steps {
	   sh 'docker compose up -d --build'
	}
   }
      stage('Verify Containers'){
	steps {
	   sh 'docker ps'
	}	
     }
   }
}

