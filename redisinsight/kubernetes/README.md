# Running RedisInsight on Docker Desktop for Mac running Kubernetes

## Pre-requisite

- Docker Desktop for Mac
- Enable Kubernetes 


## Verifying Single Node Kubernetes Cluster

```
kubectl get nodes
NAME             STATUS   ROLES    AGE   VERSION
docker-desktop   Ready    master   15h   v1.15.5
```

## Running RedisInsight inside Kubernetes Pods

```
ajeetraina@Ajeet-Rainas-Macbook-Pro ~ % kubectl get po,svc,deploy
NAME                                READY   STATUS    RESTARTS   AGE
pod/redisinsight-6b6b9d69c5-sfztk   1/1     Running   0          4m24s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   15h

NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
deployment.extensions/redisinsight   1/1     1            1           4m24s
ajeetraina@Ajeet-Rainas-Macbook-Pro ~ % 
```


## Port Forwarding

Once the deployment has been successfully applied and the deployment complete, access RedisInsight. This can be accomplished by exposing the deployment as a K8s Service or by using port forwarding, as in the example below:

```
kubectl port-forward deployment/redisinsight 8001
```

Open your browser and point to http://localhost:8001
