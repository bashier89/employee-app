pipeline {
   agent any

   stages {
     stage('Check Files') {
       steps {
	sh 'ls -la'
	}
      }
    
      stage('Check Python Files'){
	steps {
	  sh 'cat app.py'
	  sh 'cat requirements.txt'
       }
     }
      stage('Basic Validation'){
	steps {
	   sh 'test -f Dockerfile'
           sh 'test -f docker-compose.yml'
           sh 'echo "Basic validation passed"'
         }
       }
   }
 }

