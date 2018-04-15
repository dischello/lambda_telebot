pipeline {
    agent { label 'master' } 
	options {
		disableConcurrentBuilds() 
	}
	stages {
		stage ('Build artifact') { 
			steps {
                checkout scm
                sh 'aws cloudformation package --template-file ./SAM_telebot.yml --s3-bucket telebotlabda --output-template-file package-template.yml'
			}
		}
        stage ('Deploy::DEV') { 
			steps {
                sh 'aws cloudformation deploy --template-file ./package-template.yml --stack-name DevEnv --parameter-overrides Stage=dev --capabilities CAPABILITY_IAM'
			}
		}
        stage ('Deploy::Stage') { 
			steps {
                sh 'aws cloudformation deploy --template-file ./package-template.yml --stack-name StageEnv --parameter-overrides Stage=stage --capabilities CAPABILITY_IAM'
			}
		}
        stage ('Deploy::Prod') { 
            input {
                message "Should we deploy to prod"
                ok "Yes, we should."
                submitter "God`s will"
            }
			steps {
                sh 'aws cloudformation deploy --template-file ./package-template.yml --stack-name ProdEnv --parameter-overrides Stage=prod --capabilities CAPABILITY_IAM'
			}
		}
	}
}