# Exercise #1

The following tasks require that you use OSS Redis directly from the repository (TBD: link to the relavent lesson about installing).

## Task #1: 
- Launch the server from command line without any arguments (./path/to/your/redis/src/redis-server)
- What port is the server listening at?
- Why is that port number used?
- Stop the server


### Pre-requisite

- Installing WGET on Macbook

```
brew install wget
```


- Downloading Redis & Installing it

```
wget http://download.redis.io/redis-stable.tar.gz


--2020-03-04 22:06:50--  http://download.redis.io/redis-stable.tar.gz
Resolving download.redis.io (download.redis.io)... 109.74.203.151
Connecting to download.redis.io (download.redis.io)|109.74.203.151|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2023006 (1.9M) [application/x-gzip]
Saving to: ‘redis-stable.tar.gz’

redis-stable.tar.gz 100%[===================>]   1.93M  1.16MB/s    in 1.7s    

2020-03-04 22:06:52 (1.16 MB/s) - ‘redis-stable.tar.gz’ saved [2023006/2023006]
```

```
tar xvzf redis-stable.tar.gz
cd redis-stable
make
```

If you see the below message, then we are good to go ahead

```
   CC redis-cli.o
    LINK redis-cli
    CC redis-benchmark.o
    LINK redis-benchmark
    INSTALL redis-check-rdb
    INSTALL redis-check-aof

Hint: It's a good idea to run 'make test' ;)
```

It is a good idea to copy both the Redis server and the command line interface into the proper places, either manually using the following commands:

```
cp src/redis-server /usr/local/bin/
cp src/redis-cli /usr/local/bin/
```

Or just using 

```
make install
```

You can test if your build has worked correctly by typing make test, but this is an optional step.

While I ran '''make test''' command, it threw error:

```
!!! WARNING The following tests failed:

*** [err]: WAIT should not acknowledge 1 additional copy if slave is blocked in tests/unit/wait.tcl
Expected condition '[$master wait 1 3000] == 0' to be true ([::redis::redisHandle73 wait 1 3000] == 0)
Cleanup: may take some time... OK
make[1]: *** [test] Error 1
make: *** [test] Error 2
```

I still need to see why this error popped up.

After compilation the src directory inside the Redis distribution is populated with the different executables that are part of Redis:

- redis-server is the Redis Server itself.
- redis-sentinel is the Redis Sentinel executable (monitoring and failover).
- redis-cli is the command line interface utility to talk with Redis.
- redis-benchmark is used to check Redis performances.
- redis-check-aof and redis-check-rdb (redis-check-dump in 3.0 and below) are useful in the rare event of corrupted data files.

## Launch the server from command line without any arguments (./path/to/your/redis/src/redis-server)

```
./src/redis-server 
8211:C 04 Mar 2020 22:16:45.366 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
8211:C 04 Mar 2020 22:16:45.366 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=8211, just started
8211:C 04 Mar 2020 22:16:45.366 # Warning: no config file specified, using the default config. In order to specify a config file use ./src/redis-server /path/to/redis.conf
8211:M 04 Mar 2020 22:16:45.367 * Increased maximum number of open files to 10032 (it was originally set to 256).
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 5.0.7 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 8211
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

8211:M 04 Mar 2020 22:16:45.368 # Server initialized
8211:M 04 Mar 2020 22:16:45.368 * Ready to accept connections
```

## What port is the server listening at?

Port: 6379


## Why is that port number used?

As per this [link](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=3&page=45), the creator of Redis, Salvatore Sanfilippo requested to reserve this port number for redis. By default, the Redis server is configured to run on the default port 6379. You can connect to the server locally or remotely using the redis-cli command line tool using this port number

## Stop the server

If you're on Macbook, then the clean way to stop the redis server would be killing the process ID.

```
killall redis-server
```

OR

find redis process and kill

```
ps aux | grep redis-server
ajeetraina        8378   0.1  0.0  4302216   2040 s001  S+   10:32PM   0:00.08 ./src/redis-server *:6379
ajeetraina        9050   0.0  0.0  4297992    760 s003  S+   10:33PM   0:00.01 grep redis-server
```

```
kill -9 8378
```

If you're on Ubuntu OS,

```
/etc/init.d/redismaster stop
/etc/init.d/redismaster start
```


# Task #2 -  Launch the server from command line and make it listen on port 9736 on startup using arguments

- Connect to the server with redis-cli

```
./src/redis-server
9091:C 04 Mar 2020 22:41:02.489 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
9091:C 04 Mar 2020 22:41:02.489 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=9091, just started
9091:C 04 Mar 2020 22:41:02.489 # Warning: no config file specified, using the default config. In order to specify a config file use ./src/redis-server /path/to/redis.conf
9091:M 04 Mar 2020 22:41:02.491 * Increased maximum number of open files to 10032 (it was originally set to 256).
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 5.0.7 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 9091
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

9091:M 04 Mar 2020 22:41:02.492 # Server initialized
9091:M 04 Mar 2020 22:41:02.492 * DB loaded from disk: 0.000 seconds
9091:M 04 Mar 2020 22:41:02.492 * Ready to accept connections
```

Using Redis-cli to connect to Redis Server

```
./src/redis-cli 
127.0.0.1:6379> 
```


- Change the runtime configuration to listen on port 6380 (no need to persist the change). Describe and explain what happened.

Open a new terminal and run the below command:

```
./src/redis-server --port 6380
9105:C 04 Mar 2020 22:43:15.073 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
9105:C 04 Mar 2020 22:43:15.073 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=9105, just started
9105:C 04 Mar 2020 22:43:15.073 # Configuration loaded
9105:M 04 Mar 2020 22:43:15.075 * Increased maximum number of open files to 10032 (it was originally set to 2560).
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 5.0.7 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6380
 |    `-._   `._    /     _.-'    |     PID: 9105
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

9105:M 04 Mar 2020 22:43:15.076 # Server initialized
9105:M 04 Mar 2020 22:43:15.077 * DB loaded from disk: 0.000 seconds
9105:M 04 Mar 2020 22:43:15.077 * Ready to accept connections
```

As shown above, I have passed --port 6380 directly on the commandline.

Open a new terminal and run the below command

```
./src/redis-cli -p 6380
127.0.0.1:6380> 
```


- Change the value of directive per your choosing (e.g. maxmemory) to a value of your choosing (e.g. '1gb')

```
./src/redis-server --maxmemory 1gb --port 6381
9136:C 04 Mar 2020 22:47:39.543 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
9136:C 04 Mar 2020 22:47:39.543 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=9136, just started
9136:C 04 Mar 2020 22:47:39.543 # Configuration loaded
9136:M 04 Mar 2020 22:47:39.544 * Increased maximum number of open files to 10032 (it was originally set to 2560).
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 5.0.7 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6381
 |    `-._   `._    /     _.-'    |     PID: 9136
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

9136:M 04 Mar 2020 22:47:39.545 # Server initialized
9136:M 04 Mar 2020 22:47:39.546 * DB loaded from disk: 0.000 seconds
9136:M 04 Mar 2020 22:47:39.546 * Ready to accept connections
```




- Change the value of the bind directive to '0.0.0.0' and note the result

```


```


- Stop the server

```


```


## Launch the server from command line with a configuration file that you've prepared. The server should:
- Listen on port 6380
- Be protect by a password
- Use up to 512 megabytes of RAM for data
- Be persisted using RDB every 10 seconds if more than 1000 writes have been made, and every minute if 4000 writes have been made


## Run (if you haven't already) sudo make install from Redis' repository directory to install it on the server. Verify that the server's service starts correctly and that you can connect to it. Locate the configuration file that is used by the deployment.
You've arrived at a customer's site where the OSS is deployed on Ubuntu 16. 

## Assuming that you need to perform a configuration change (e.g. setting maxmemory), what steps will you take?
