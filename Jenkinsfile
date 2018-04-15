pipeline {
    agent { label 'master' } 
	options {
		disableConcurrentBuilds() 
	}
	stages {
		stage ('Build artifact') { 
			steps {
                checkout scm
                sh 'sudo su; aws cloudformation package --template-file ./SAM_telebot.yml --s3-bucket telebotlabda --output-template-file package-template.yml'
			}
		}
        stage ('Deploy::DEV') { 
			steps {
                sh 'sudo su; aws cloudformation deploy --template-file ./package-template.yml --stack-name LabdaFirstDeploy --capabilities CAPABILITY_IAM --parameters  Stage=dev'
			}
		}
        stage ('Deploy::Stage') { 
			steps {
                sh 'sudo su; aws cloudformation deploy --template-file ./package-template.yml --stack-name LabdaFirstDeploy --capabilities CAPABILITY_IAM --parameters  Stage=stage'
			}
		}
        stage ('Deploy::Prod') { 
            input {
                message "Should we deploy to prod"
                ok "Yes, we should."
                submitter "God`s will"
            }
			steps {
                sh 'sudo su; aws cloudformation deploy --template-file ./package-template.yml --stack-name LabdaFirstDeploy --capabilities CAPABILITY_IAM --parameters  Stage=prod'
			}
		}
	}
}