# AWS CI/CD pipeline

In this repository, the codes of infrastructure, AWS lambda function scripts and thier CI/CD configs are presented.

The steps of CI/CD pipeline as follows:

 - * Build (AWS CodeBuild)
 - * Notify of build outcome (AWS SNS) 
 - * Deliver build to environment (AWS CodeBuild and AWS CodeDeploy)
