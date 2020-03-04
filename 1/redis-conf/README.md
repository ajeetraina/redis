# Exercise #1

The following tasks require that you use OSS Redis directly from the repository (TBD: link to the relavent lesson about installing).

## Launch the server from command line without any arguments (./path/to/your/redis/src/redis-server)
- What port is the server listening at?
- Why is that port number used?
- Stop the server




## Launch the server from command line and make it listen on port 9736 on startup using arguments

- Connect to the server with redis-cli
- Change the runtime configuration to listen on port 6380 (no need to persist the change). Describe and explain what happened.
- Change the value of directive per your choosing (e.g. maxmemory) to a value of your choosing (e.g. '1gb')
- Change the value of the bind directive to '0.0.0.0' and note the result
- Stop the server


## Launch the server from command line with a configuration file that you've prepared. The server should:
- Listen on port 6380
- Be protect by a password
- Use up to 512 megabytes of RAM for data
- Be persisted using RDB every 10 seconds if more than 1000 writes have been made, and every minute if 4000 writes have been made


## Run (if you haven't already) sudo make install from Redis' repository directory to install it on the server. Verify that the server's service starts correctly and that you can connect to it. Locate the configuration file that is used by the deployment.
You've arrived at a customer's site where the OSS is deployed on Ubuntu 16. 

## Assuming that you need to perform a configuration change (e.g. setting maxmemory), what steps will you take?
