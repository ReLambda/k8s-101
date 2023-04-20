# Install Kubernetes
There are multiple ways to install kubernetes on your local machine. You can choose any one of the following options. 
1. Via Docker Desktop
2. Minikube
3. Cloud Provider (You will need an account with the cloud provider)

> You don't need to setup all 3, just choose the one that is best for you.

## 1. Docker Desktop
1. From the Docker Dashboard, select the Settings.
2. Select Kubernetes from the left sidebar.
3. Next to Enable Kubernetes, select the checkbox.
4. Select Apply & Restart.

> By default, Kubernetes containers are hidden from commands like docker ps, because managing them manually is not supported. Most users do not need this option. To see these internal containers, select Show system containers (advanced).


## 2. Via Minikube
1. MacOS
```bash
brew install minikube kubectl

minikube start
```

2. Linux
```bash
# install minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
# install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

minikube start
```

## 3. Cloud Provider
This is an advanced option and we recommend you to go this path only if you have done this before, else choose option 1 or 2. 

# Download Course Material
`git clone ___`

# Docker login [Optional]
Dockerhub is a public container registry where you can push your docker images. A container registry is for docker images what Github is for code. You don't need a dockerhub account to follow this course as we have already pushed the required images to dockerhub, and you can use them.

```
> docker login -u {USERNAME}
Password:

Login Succeeded
```

# Verification
You can verify the local kubernete installation by running the following commands

1. `kubectl version`  
In the output you must ensure that both _Client Version_ and _Server Version_ blocks are present and don't give any error.
    ```bash
    kubectl version

    Client Version: version.Info{Major:"1", Minor:"25", GitVersion:"v1.25.4", GitCommit:"872a965c6c6526caa949f0c6ac028ef7aff3fb78", GitTreeState:"clean", BuildDate:"2022-11-09T13:36:36Z", GoVersion:"go1.19.3", Compiler:"gc", Platform:"darwin/amd64"}
    Kustomize Version: v4.5.7

    Server Version: version.Info{Major:"1", Minor:"23", GitVersion:"v1.23.1", GitCommit:"86ec240af8cbd1b60bcc4c03c20da9b98005b92e", GitTreeState:"clean", BuildDate:"2021-12-16T11:34:54Z", GoVersion:"go1.17.5", Compiler:"gc", Platform:"linux/amd64"}
    WARNING: version difference between client (1.25) and server (1.23) exceeds the supported minor version skew of +/-1
    ```

2. `kubectl get nodes`
    This will list all the nodes attached to your cluster. There should be at-least 1 node in your cluster where you can deploy the applications. In a typical production cluster, this command will have multiple nodes in the output.
    ```bash
    kubectl get nodes
    NAME         STATUS   ROLES                  AGE     VERSION
    k8s-1.23.1   Ready    control-plane,master   9m28s   v1.23.1
    ```
3. `kubectl get pods -A`
    ```bash
    kubectl get pods -A
    NAMESPACE     NAME                                 READY   STATUS    RESTARTS        AGE
    kube-system   coredns-64897985d-q7c67              1/1     Running   0               8m42s
    kube-system   etcd-k8s-1.23.1                      1/1     Running   0               8m55s
    kube-system   kube-apiserver-k8s-1.23.1            1/1     Running   0               8m55s
    kube-system   kube-controller-manager-k8s-1.23.1   1/1     Running   0               8m55s
    kube-system   kube-proxy-6rrmq                     1/1     Running   0               8m43s
    kube-system   kube-scheduler-k8s-1.23.1            1/1     Running   0               8m55s
    kube-system   storage-provisioner                  1/1     Running   1 (8m37s ago)   8m54s
    ```