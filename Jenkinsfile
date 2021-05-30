pipeline {
    agent any
    stages {
        stage('git') {
          steps{
            
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Venkateshsandupatla/Brain_stroke_prediction-MlOps.git']]])
          }  
        }
        stage("Dockerbuildandpush"){
            steps{
                script{
                  withDockerRegistry([credentialsId: "Docker", url: "https://index.docker.io/v1/"]) {
                  image = docker.build("venkateshsandupatla/Brain-strokepred-mlops", "Docker")
                  image.push()    
                  }  
                }
            }
        }
        stage("kuberneteslaunchpods"){
            steps{
                script{
                    kubernetesDeploy(
                    configs: 'k8sfiles/deployment.yml',
                    kubeconfigId: 'k8s',
                    enableConfigSubstitution: true
                    )           
                }
            }
        }
    }
}
