pipeline {
    agent { label 'master' } 
	options {
		disableConcurrentBuilds() // Disable concurent builds
	}
	stages {
		stage ('Preparation::Common') { // Common preparation for Build
			steps {
                checkout scm
                sh 'ls -al'
			}
		}
	}
}