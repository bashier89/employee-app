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
   }
 }

