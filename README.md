# Swarm-tutorials

### [1] Build image

```
docker build -t api_counts:1.0 .
```

### [2] Swarm init

```
docker swarm init
```

<u>One node can only use in one swarm group.</u>  
Use `docker swarm leave` to leave this swarm and join another one.

### [3] Deploy the stack to the swarm

```
docker stack deploy --compose-file docker-compose.yml app_counts
```

Bring the stack down with `docker stack rm app_counts`