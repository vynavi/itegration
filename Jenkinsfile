pipeline{
  agent any
  environment{
    PYTHON_PATH='C:\Users\vynub\AppData\Local\Programs\Python\Python313;C:\Users\vynub\AppData\Local\Programs\Python\Python313\Scripts'
  }
  stages{
    stage('Checkout'){
      steps{
        checkout scm
      }
    }
  }
  stage('Build'){
    steps{
      bat '''
      set PATH=%PYTHON_PATH%;%PATH%
      pip install -r requirements.txt
      '''
    }
  }
  stage('SonarAnalysis'){
    environment{
      SONAR_TOKEN=credentials('sonar_token')
    }
    steps{
      bat '''
      set PATH=%PYTHON_PATH%;%PATH%
      sonar-scanner -Dsonar.projectKey=integrating_26th_dec ^
      -Dsonar.sources=. ^
      -Dsonar.host.url=http://localhost:9000 ^
      -Dsonar.token=%SONAR_TOKEN%
      '''
    }
  }
}
post{
  success{
    echo 'went well and good'
  }
  failure {
    echo 'failed'
  }
}
