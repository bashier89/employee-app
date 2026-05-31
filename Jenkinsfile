pipeline {
   agent any

   stages {
     stage('Check Files') {
       steps {
	sh 'ls -la'
	}
      }
    
      stage('Build Docker Image'){
	steps {
	  sh 'docker build -t employee-app .'
       }
     }
   }
 }

