# Docker recap

# Kubernetes Overview
## Architecture
## Building Blocks
- Pods
- Deployments
- Services
- Labels and Selectors

----- Hands On ------
# Docker Recap
Switch to sample-app directory
`cd ~/k8s-101/sample-app`

Build docker image
``
<details>
    <summary>output</summary>

    ```bash
        [+] Building 2.8s (10/10) FINISHED
         => [internal] load build definition from Dockerfile                                                                                                         0.1s
        => => transferring dockerfile: 543B                                                                                                                         0.0s
        => [internal] load .dockerignore                                                                                                                            0.0s
        => => transferring context: 2B                                                                                                                              0.0s
        => [internal] load metadata for docker.io/library/python:3.9                                                                                                2.6s
        => [auth] library/python:pull token for registry-1.docker.io                                                                                                0.0s
        => [1/4] FROM docker.io/library/python:3.9@sha256:2d8875d28ca023a9056a828518adcdd634ba03740e1e3b197c06eb4527c6152c                                          0.0s
        => [internal] load build context                                                                                                                            0.0s
        => => transferring context: 2.79kB                                                                                                                          0.0s
        => CACHED [2/4] WORKDIR /app                                                                                                                                0.0s
        => CACHED [3/4] COPY . /app                                                                                                                                 0.0s
        => CACHED [4/4] RUN pip install -r requirements.txt                                                                                                         0.0s
        => exporting to image                                                                                                                                       0.0s
        => => exporting layers                                                                                                                                      0.0s
        => => writing image sha256:1f62567a00e68173ee2693c9d9da6522e5fdbbfbc2a1abbac20462425be123df                                                                 0.0s
        => => naming to docker.io/library/sample-app:1.0
            ```

</details>

# K8s in 30s
Create a pod that using echo-server image
`kubectl create deployment --replicas=3 echo-server --image=ealen/echo-server`

Expose the pod so that we can access the service in our browser
`kubectl expose deployment echo-server --type=LoadBalancer --port=80 --target-port=80`

Create minikube tunnel (not required in case of eks or other managed services)
`minikube tunnel`

The service is now accessible on port 8080
`curl localhost`

Verify loadbalancing
`watch -d -n1 curl --silent 'localhost/?echo_env_body=HOSTNAME'`

Cleanup
```
kubectl delete deployment echo-server
kubectl delete service echo-server
```
- Discussion
    - Imperative vs Declarative
        Imperative is when you give granular commands, usually in a sequence, to get something done. 
            eg: create secret -> create deployment -> expose a service 
        Declarative is when you describe the desired state (using yml files) and submit them to the orchestrator.
    - Idempotency 
        A property in computer science that describes an operation's ability to produce the same result, regardless of how many times it is executed.
    - Ephemeral
        The resources created are lost in case your cluster crashes. It is always a good idea to store these resources as code (eg: yml files) in a git repository.

# Kube