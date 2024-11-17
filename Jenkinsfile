pipeline {
    // agent { docker { image 'python-docker-3.12.6-alpine3.20:v6' } }
    agent any
    environment {
        MY_PASSWORD = credentials('af5bdc2b-124d-44ab-a094-d04b567261b9')
        // API_KEY="test"
        SONARQUBE_CREDS = credentials('SonarQubeBase64')

    }
    stages {
    
        stage('Display Password Unmasked') {
            steps {
                script {
                    sh '''
                    API_KEY=$(echo $MY_PASSWORD| cut -d':' -f2)

                    echo "Unmasked API_KEY is: $API_KEY" > /tmp/pss
                    '''
                }
            }
        }
        // stage('Extract API Key') {
        //     steps {
        //         script {
        //             // Define the string containing the API key
        //             def apiKeyString = $MY_PASSWORD
                    
        //             // Extract the API key using awk
        //             def extractedApiKey = sh(
        //                 script: "echo '${apiKeyString}' | awk -F':' '{print \$2}'",
        //                 returnStdout: true
        //             ).trim()
                    
        //             // Assign the extracted API key to an environment variable
        //             env.API_KEY = extractedApiKey
                    
        //             // Optionally, print the API key (Be cautious with sensitive data)
        //             echo "API Key extracted successfully."
        //         }
        //     }
        // }


        stage('Checkout') {
            steps {
                // Pull the source code from the repository (e.g., GitHub)
                sh 'git clone https://github.com/haynesdavis/qotd-python.git'
                sh 'git branch'
                sh 'git checkout jenkins-pipeline-test'
                sh 'git branch'
                sh 'echo "Unmasked API_KEY is: $env.API_KEY" > /tmp/pss2'
            }
        }


        stage('SCM Checkout') {
            steps{
            git branch: 'jenkins-pipeline-test', url: 'https://github.com/haynesdavis/qotd-python.git'
            sh 'git fetch --unshallow || true'
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONAR_SCANNER_HOME = tool 'SonarQubeScanner'
            }
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    sh """
                    ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                    -Dsonar.projectKey=SmpleApp \
                    -Dsonar.sources=. \
                    """
                }
            }
        }




                        // // run sonarqube test
                        // stage('Run Sonarqube') {
                        //     environment {
                        //         scannerHome = tool 'SonarQubeScanner';
                        //     }
                        //     steps {
                        //       withSonarQubeEnv(credentialsId: 'SonarQube', installationName: 'SonarQubeServer') {
                        //         sh "${scannerHome}/bin/sonar-scanner"
                        //       }
                        //     }
                        // }
                        // stage('Setup Python Environment and run app') {
                        //     steps {
                        //         // Set up Python and install dependencies
                        //         sh '''
                        //         pwd
                        //         cd qotd-python/
                        //         pwd
                        //         python3 -m venv venv
                        //         source venv/bin/activate
                        //         pip install --upgrade pip
                        //         pip install -r requirements.txt
                        //         gunicorn --bind 0.0.0.0:10000 app:app &
                        //         sleep 5
                        //         curl localhost:10000
                        //         '''
                        //     }
                        // }


        // stage('SonarQube Code Analysis') {
        //     steps {
        //         dir("${WORKSPACE}"){
        //         // Run SonarQube analysis for Python
        //         script {
        //             def scannerHome = tool name: 'SonarQubeScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
        //             withSonarQubeEnv('sonar') {
        //                 sh "${scannerHome}/bin/sonar-scanner \
        //                     -D sonar.projectVersion=1.0-SNAPSHOT \
        //                     -D sonar.qualityProfile="Sonar way" \
        //                     -D sonar.projectBaseDir=/var/lib/jenkins/workspace/Snyk-Testing/snyk-code-container-scan/appcode \
        //                     -D sonar.projectKey=sample-app \
        //                     -D sonar.sourceEncoding=UTF-8 \
        //                     -D sonar.language=python \
        //                     -D sonar.host.url=http://9.46.241.25:9000"
        //             }
        //         }
        //     }
        //     }
        // }

        // stage("SonarQube Quality Gate Check") {
        //     steps {
        //         script {
        //         def qualityGate = waitForQualityGate()
                    
        //             if (qualityGate.status != 'OK') {
        //                 echo "${qualityGate.status}"
        //                 error "Quality Gate failed: ${qualityGateStatus}"
        //             }
        //             else {
        //                 echo "${qualityGate.status}"
        //                 echo "SonarQube Quality Gates Passed"
        //             }
        //         }
        //     }
        // }


        stage('Code Optimisation') {
            steps {
                sh '''
                API_KEY=$(echo $MY_PASSWORD| cut -d':' -f2)
                export API_KEY
                echo "this is just a test comment added to amke sure there is a code change"

                python UC_optimise_code.py $SONARQUBE_CREDS
                '''
            }
        }


        stage('Test Case Generation') {
            steps {
                sh '''
                API_KEY=$(echo $MY_PASSWORD| cut -d':' -f2)
                export API_KEY
                python UC_test_cases.py
                '''
            }
        }

                        // stage('Check Prereqs for deployment') {
                        //     steps {
                        //         sh '''
                        //         API_KEY=$(echo $MY_PASSWORD| cut -d':' -f2)
                        //         export API_KEY
                        //         app_name="qotd-python"

                        //         PROMETHEUS_URL="http://9.30.96.66:9090"
                        //         QUERY='query=network_load{instance="9.46.241.25:10002", job="network_load"}'
                        //         result=$(curl -v -s -G "${PROMETHEUS_URL}/api/v1/query" --data-urlencode "${QUERY}")
                        //         echo $result
                        //         network_load=$(echo "$result" | jq -r '.data.result[0].value[1]')
                        //         echo "network_load is $network_load"
                        //         status=$(cat deployment_status.log)


                        //         deployment_prediction=$(python UC_pipeline_management.py $network_load $status)
                        //         echo "deployment_prediction is $deployment_prediction"
                        //         '''
                        //     }
                        // }


        // stage('Check Prereqs for deployment') {
        //     steps {
        //         script {
        //             // Execute the shell script and capture the deployment prediction
        //             def deployment_prediction = sh(
        //                 script: '''
        //                 # Extract API key
        //                 API_KEY=$(echo $MY_PASSWORD | cut -d':' -f2)
        //                 export API_KEY
                        
        //                 # App name and Prometheus query
        //                 app_name="qotd-python"
        //                 PROMETHEUS_URL="http://9.30.96.66:9090"
        //                 QUERY='query=network_load{instance="9.46.241.25:10002", job="network_load"}'

        //                 # Get network load from Prometheus
        //                 result=$(curl -s -G "${PROMETHEUS_URL}/api/v1/query" --data-urlencode "${QUERY}")
        //                 network_load=$(echo "$result" | jq -r '.data.result[0].value[1]')

        //                 # Read deployment status
        //                 status=$(cat UC_deployment_status.log)

        //                 # Call Python script to predict deployment outcome
        //                 deployment_prediction=$(python UC_pipeline_management.py "$network_load" "$status")
        //                 echo "$deployment_prediction"
        //                 ''',
        //                 returnStdout: true
        //             ).trim()

        //             echo "Deployment prediction is: ${deployment_prediction}"
        //             if (deployment_prediction == 'Failure') {
        //                 error("Stopping pipeline due to predicted deployment failure.")
        //             } else {
        //                 echo "Deployment prediction is successful. Proceeding with pipeline execution."
        //             }

        //         }
        //     }
        // }

        // stage('build') {
        //     steps {
        //         sh '''
        //         docker images
        //         app_name="qotd-python"
        //         latest_version=$(docker images --format "{{.Repository}}:{{.Tag}}" | grep '^qotd-python:v' | sort -V | tail -n 1)
        //         current_version=$(echo "$latest_version" | grep -oP '(?<=:v)[0-9]+')
        //         next_version=$((current_version + 1))
        //         sed -i "s/VERSION/$next_version/" app.py
        //         docker build -t "$app_name:v$next_version" .
        //         docker images
        //         '''
        //     }
        // }


        // stage('Deploy the sample app') {
        //     steps {
        //         sh '''
        //         app_name="qotd-python"
        //         API_KEY=$(echo $MY_PASSWORD| cut -d':' -f2)
        //         export API_KEY

        //         if docker ps --filter "name=qotd-python" --format "{{.Names}}" | grep -q "^qotd-python$"; then
        //             echo "Stopping the container qotd-python..."
        //             docker stop qotd-python
        //             echo "Container qotd-python stopped."
        //         else
        //             echo "Container qotd-python does not exist or is not running."
        //         fi

        //         if docker ps -a --filter "name=qotd-python" --format "{{.Names}}" | grep -q "^qotd-python$"; then
        //             echo "Removing the container qotd-python..."
        //             docker remove $app_name
        //             echo "Container qotd-python removed."
        //         else
        //             echo "Container qotd-python does not exist or is not running."
        //         fi

                
        //         latest_version=$(docker images --format "{{.Repository}}:{{.Tag}}" | grep '^qotd-python:v' | sort -V | tail -n 1)
        //         current_version=$(echo "$latest_version" | grep -oP '(?<=:v)[0-9]+')
        //         docker run -d --name $app_name -p 10000:10000 "$app_name:v$current_version"
        //         if docker ps --filter "name=$app_name" --filter "status=running" | grep -q "$app_name"; then
        //         echo "Container '$app_name' is running successfully."
        //         deployment_status="success"
        //         network_load=$(curl -s http://9.46.241.25:10002/metrics | cut -d' ' -f2)
        //         status="{deployment_status: $deployment_status, data: {network_load: $network_load}}"
        //         echo $status >> deployment_status.log
        //         else
        //         echo "Container '$app_name' is not running."
        //         fi

        //         '''
        //     }
        // }

        // stage('Rollback on failure') {
        //     steps {
        //         sh '''
        //         sleep 30
        //         app_name="qotd-python"

        //         app_response=$(curl -s localhost:10000)
        //         echo "app_response is - $app_response"
        //         PROMETHEUS_URL="http://9.30.96.66:9090"
        //         QUERY='query=cpu_load_state{instance="9.46.241.25:10001", job="cpu_load"}'
        //         result=$(curl -s -G "${PROMETHEUS_URL}/api/v1/query" --data-urlencode "${QUERY}")
        //         echo $result
        //         cpu_load=$(echo "$result" | jq -r '.data.result[0].value[1]')
        //         echo "value is $cpu_load"

        //         API_KEY=$(echo $MY_PASSWORD| cut -d':' -f2)
        //         export API_KEY
        //         app_running=$(python UC_rollback_deployment.py "${cpu_load}" "${app_response}" | sed -n '2p')

                
        //         if $app_running; then
        //             echo "App is healthy"
        //         else
        //             echo "App is not healthy, rolling back..."

        //             latest_version=$(docker images --format "{{.Repository}}:{{.Tag}}" | grep '^qotd-python:v' | sort -V | tail -n 1)
        //             current_version=$(echo "$latest_version" | grep -oP '(?<=:v)[0-9]+')
        //             prev_version=$((current_version - 1))

        //             if docker ps --filter "name=qotd-python" --format "{{.Names}}" | grep -q "^qotd-python$"; then
        //                 echo "Stopping the container qotd-python..."
        //                 docker stop qotd-python
        //                 echo "Container qotd-python stopped."
        //             else
        //                 echo "Container qotd-python does not exist or is not running."
        //             fi

        //             if docker ps -a --filter "name=qotd-python" --format "{{.Names}}" | grep -q "^qotd-python$"; then
        //                 echo "Removing the container qotd-python..."
        //                 docker remove $app_name
        //                 echo "Container qotd-python removed."
        //             else
        //                 echo "Container qotd-python does not exist or is not running."
        //             fi

        //             docker run -d --name $app_name -p 10000:10000 "$app_name:v$prev_version"
        //         fi
        //         sleep 10
        //         app_response=$(curl -s localhost:10000)
        //         echo $app_response

        //         '''
        //     }
        // }


    }
    post {
        always {
            // Cleanup workspace after the build, whether successful or failed
            cleanWs()
        }
    }
}