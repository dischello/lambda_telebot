pipeline {
	options {
		disableConcurrentBuilds() // Disable concurent builds
	}
	stages {
		stage ('Preparation::Common') { // Common preparation for Build
			agent { label 'master' } // This stage runs only on master due Jenkins Proxy Configuration
			steps {
                checkout scm
                sh 'ls -al'
			}
		}
	}
}