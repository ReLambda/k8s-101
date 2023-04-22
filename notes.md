# Topic Name
    Container Orchestration With Kubernetes - 101

# Overview
    A hands-on workshop on getting started with kubernetes. We will start with a sample application, dockerize it and deploy it in a local kubernetes cluster. We will be covering high level kubernetes architecture and standard resources like Pod, Deployment, Service and Secret.

# Target Audience
    Anyone who is interested in getting started with kubernetes.

# Agenda/Outline
    - Introduction
        - Speaker
        - Workshop contents
    - Docker Recap
        - Build docker image sample app
        - Push image to dockerhub
        - Run sample app in docker container
        - Expose sample app running inside container
        - Q&A/Discussion/Quiz
    - Basics Of Kubernetes
        - Overview of container orchestration
        - Architecture
        - First contact with kubectl
        - Run sample app as a pod in kubernetes cluster
        - Expose sample app running inside kubernetes cluster
        - Check logs
        - Declarative Vs Imperative
    - Kubernetes In Real World
        - Deployments
            - RS|Pods
        - Services
            - ClusterIP
            - NodePort
            - LoadBalancer
        - Secrets
        - Namespace
        - Prepare YAML for Deployment, Service, Namespace & Secret
        - Configuring Deployment 
            - Replica Count
            - Deployment Strategy
            - ImagePullPolicy

# Setup Details
    - OSX/Linux Operating System
    - Local Kubernetes
        - Docker Desktop (on OSX) OR
        - Minikube (on Linux)
    - DockerHub Account

# Prerequisites
    - Familiarity with Linux command line interface
        - Navigating directories
        - Editing files
        - Using commands with multiple arguments
    - Familiarity with Git
        - Commands like `git add`, `git commit`, `git push`
    - Basic Docker Knowledge 
        - Commands like `docker run`, `docker ps`, `docker build`
        - Dockerfile
        - No expertise in docker is expected

# About the presenters

# Resources
https://github.com/infracloudio/kubernetes-101-workshop/tree/master