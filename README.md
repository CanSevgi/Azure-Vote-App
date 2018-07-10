**Setting Bash default subscription:**

az account list
az account set --subscription <subscription-id>


**Deploy Azure Container Registry :**

az group create --name VoteResourceGroup --location westeurope
az acr create --resource-group VoteResourceGroup --name VoteContainer --sku Basic

**Container registry login :**

az acr login  --name VoteContainer

**Get loginServer name :**

az acr list --resource-group VoteResourceGroup --query "[].{acrLoginServer:loginServer}" --output table

**Tag container images with loginServer name :**

Docker tag <imageId> <loginservername>/imagename
i.e : “docker tag 123 votecontainer.azurecr.io/front”

**Push images to registry :**

Docker push <loginservername>/imagename
i.e : “ docker push votecontainer.azurecr.io/front”



**Verify pushing is successful by listing images in Registry :**

az acr repository list --name <acrName> --output table
i.e : “az acr repository list --name VoteContainer --output table”





**Create Kubernetes Cluster :**

az acs create --orchestrator-type kubernetes --resource-group VoteResourceGroup --name myK8SCluster --generate-ssh-keys

*if limited available cores not enough, add “--agent-count 1” to end of the line*



**Install the kubectl CLI :**

az acs kubernetes install-cli

**Connect with kubectl :**

az acs kubernetes get-credentials --resource-group VoteResourceGroup --name KubernetesCluster

**Verify the connection**

Kubectl get nodes

**Update Manifest File**

Vi azure-vote.yml


##

apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: azure-vote-back
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: azure-vote-back
    spec:
      containers:
      - name: azure-vote-back
        image: redis
        ports:
        - containerPort: 6379
          name: redis
---
apiVersion: v1
kind: Service
metadata:
  name: azure-vote-back
spec:
  ports:
  - port: 6379
  selector:
    app: azure-vote-back
---
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: azure-vote-front
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: azure-vote-front
    spec:
      containers:
      - name: azure-vote-front
        image: votecontainer.azurecr.io/front 
#image : cansevgi/front
        ports:
        - containerPort: 80
        env:
        - name: REDIS
          value: "azure-vote-back"
---
apiVersion: v1
kind: Service
metadata:
  name: azure-vote-front
spec:
  type: LoadBalancer
  ports:
  - port: 80
  selector:
    app: azure-vote-front    
##


**Deploy Application**

kubectl create -f azure-vote-all-in-one-redis.yml

kubectl get service azure-vote-front --watch

*Wait for external ip and use it for reaching your page.*


