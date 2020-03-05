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


##  Change the runtime configuration to listen on port 6380 (no need to persist the change). Describe and explain what happened.

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


##  Change the value of directive per your choosing (e.g. maxmemory) to a value of your choosing (e.g. '1gb')

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
./src/redis-server --port 6380 --bind 0.0.0.0
9210:C 04 Mar 2020 22:53:40.047 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
9210:C 04 Mar 2020 22:53:40.047 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=9210, just started
9210:C 04 Mar 2020 22:53:40.047 # Configuration loaded
9210:M 04 Mar 2020 22:53:40.049 * Increased maximum number of open files to 10032 (it was originally set to 256).
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 5.0.7 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6380
 |    `-._   `._    /     _.-'    |     PID: 9210
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

9210:M 04 Mar 2020 22:53:40.050 # Server initialized
9210:M 04 Mar 2020 22:53:40.050 * DB loaded from disk: 0.000 seconds
9210:M 04 Mar 2020 22:53:40.050 * Ready to accept connections
```



```

ajeetraina@ajeetraina redis-stable % ./src/redis-cli -h 192.168.1.4 -p 6380
192.168.1.4:6380> set a1 true
OK
192.168.1.4:6380> get a1
"true"
192.168.1.4:6380>
```


## Stop the server

If you have multiple redis-server instance running , first try to find out the specific process-id and then try to kill it

```
ajeetraina@ajeetraina redis-stable % ps aux | grep redis-server
ajeetraina        9252   1.6  0.0  4268188    384 s004  R+   10:59PM   0:00.01 grep redis-server
ajeetraina        9136   0.1  0.0  4322696   2108   ??  S    10:47PM   0:01.22 ./src/redis-server *:6381    
ajeetraina        9210   0.1  0.0  4330888   2988 s001  S+   10:53PM   0:00.63 ./src/redis-server 0.0.0.0:6380    
ajeetraina@ajeetraina redis-stable % 
```

```
kill -9 9210
```


## Launch the server from command line with a configuration file that you've prepared. The server should:
- Listen on port 6380

Open up redis-stable/redis.conf and ensure that the following entry have been made:

```
port 6380
```

- Be protect by a password


```
authpass P@ssw0rd
```

- Use up to 512 megabytes of RAM for data

```
maxmemory 512mb
```


- Be persisted using RDB every 10 seconds if more than 1000 writes have been made, and every minute if 4000 writes have been made

By default Redis saves snapshots of the dataset on disk, in a binary file called dump.rdb. You can configure Redis to have it save the dataset every N seconds if there are at least M changes in the dataset, or you can manually call the SAVE or BGSAVE commands.

For example, this below configuration will make Redis automatically dump the dataset to disk every 10 seconds if at least 1000 keys changed:

```
save 10 1000
```

```
save 60 4000
```


This strategy is known as snapshotting.

## How does it works?

- Whenever Redis needs to dump the dataset to disk, this is what happens:
- Redis forks. We now have a child and a parent process.
- The child starts to write the dataset to a temporary RDB file.
- When the child is done writing the new RDB file, it replaces the old one.

This method allows Redis to benefit from copy-on-write semantics.


## Time to Run Redis-Server

Make all the above changes and store it in custom-redis.conf file.


```
./src/redis-server custom-redis.conf 
1764:C 05 Mar 2020 13:27:03.428 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
1764:C 05 Mar 2020 13:27:03.428 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=1764, just started
1764:C 05 Mar 2020 13:27:03.428 # Configuration loaded
1764:M 05 Mar 2020 13:27:03.430 * Increased maximum number of open files to 10032 (it was originally set to 256).
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 5.0.7 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6380
 |    `-._   `._    /     _.-'    |     PID: 1764
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

1764:M 05 Mar 2020 13:27:03.432 # Server initialized
1764:M 05 Mar 2020 13:27:03.433 * DB loaded from disk: 0.001 seconds
1764:M 05 Mar 2020 13:27:03.433 * Ready to accept connections
```

```
% ./src/redis-cli -p 6380            
127.0.0.1:6380> auth P@ssw0rd
OK
127.0.0.1:6380> config get
127.0.0.1:6380> CONFIG GET * 
  1) "dbfilename"
  2) "dump.rdb"
  3) "requirepass"
  4) "P@ssw0rd"
  5) "masterauth"
  6) ""
  7) "cluster-announce-ip"
  8) ""
  9) "unixsocket"
 10) ""
 11) "logfile"
 12) ""
 13) "pidfile"
 14) "/var/run/redis_6379.pid"
 15) "slave-announce-ip"
 16) ""
 17) "replica-announce-ip"
 18) ""
 19) "maxmemory"
 20) "536870912"
 21) "proto-max-bulk-len"
 22) "536870912"
 23) "client-query-buffer-limit"
 24) "1073741824"
 25) "maxmemory-samples"
 26) "5"
 27) "lfu-log-factor"
 28) "10"
 29) "lfu-decay-time"
 30) "1"
 31) "timeout"
 32) "0"
 33) "active-defrag-threshold-lower"
 34) "10"
 35) "active-defrag-threshold-upper"
 36) "100"
 37) "active-defrag-ignore-bytes"
 38) "104857600"
 39) "active-defrag-cycle-min"
 40) "5"
 41) "active-defrag-cycle-max"
 42) "75"
 43) "active-defrag-max-scan-fields"
 44) "1000"
 45) "auto-aof-rewrite-percentage"
 46) "100"
 47) "auto-aof-rewrite-min-size"
 48) "67108864"
 49) "hash-max-ziplist-entries"
 50) "512"
 51) "hash-max-ziplist-value"
 52) "64"
 53) "stream-node-max-bytes"
 54) "4096"
 55) "stream-node-max-entries"
 56) "100"
 57) "list-max-ziplist-size"
 58) "-2"
 59) "list-compress-depth"
 60) "0"
 61) "set-max-intset-entries"
 62) "512"
 63) "zset-max-ziplist-entries"
 64) "128"
 65) "zset-max-ziplist-value"
 66) "64"
 67) "hll-sparse-max-bytes"
 68) "3000"
 69) "lua-time-limit"
 70) "5000"
 71) "slowlog-log-slower-than"
 72) "10000"
 73) "latency-monitor-threshold"
 74) "0"
 75) "slowlog-max-len"
 76) "128"
 77) "port"
 78) "6380"
 79) "cluster-announce-port"
 80) "0"
 81) "cluster-announce-bus-port"
 82) "0"
 83) "tcp-backlog"
 84) "511"
 85) "databases"
 86) "16"
 87) "repl-ping-slave-period"
 88) "10"
 89) "repl-ping-replica-period"
 90) "10"
 91) "repl-timeout"
 92) "60"
 93) "repl-backlog-size"
 94) "1048576"
 95) "repl-backlog-ttl"
 96) "3600"
 97) "maxclients"
 98) "10000"
 99) "watchdog-period"
100) "0"
101) "slave-priority"
102) "100"
103) "replica-priority"
104) "100"
105) "slave-announce-port"
106) "0"
107) "replica-announce-port"
108) "0"
109) "min-slaves-to-write"
110) "0"
111) "min-replicas-to-write"
112) "0"
113) "min-slaves-max-lag"
114) "10"
115) "min-replicas-max-lag"
116) "10"
117) "hz"
118) "10"
119) "cluster-node-timeout"
120) "15000"
121) "cluster-migration-barrier"
122) "1"
123) "cluster-slave-validity-factor"
124) "10"
125) "cluster-replica-validity-factor"
126) "10"
127) "repl-diskless-sync-delay"
128) "5"
129) "tcp-keepalive"
130) "300"
131) "cluster-require-full-coverage"
132) "yes"
133) "cluster-slave-no-failover"
134) "no"
135) "cluster-replica-no-failover"
136) "no"
137) "no-appendfsync-on-rewrite"
138) "no"
139) "slave-serve-stale-data"
140) "yes"
141) "replica-serve-stale-data"
142) "yes"
143) "slave-read-only"
144) "yes"
145) "replica-read-only"
146) "yes"
147) "slave-ignore-maxmemory"
148) "yes"
149) "replica-ignore-maxmemory"
150) "yes"
151) "stop-writes-on-bgsave-error"
152) "yes"
153) "daemonize"
154) "no"
155) "rdbcompression"
156) "yes"
157) "rdbchecksum"
158) "yes"
159) "activerehashing"
160) "yes"
161) "activedefrag"
162) "no"
163) "protected-mode"
164) "yes"
165) "repl-disable-tcp-nodelay"
166) "no"
167) "repl-diskless-sync"
168) "no"
169) "aof-rewrite-incremental-fsync"
170) "yes"
171) "rdb-save-incremental-fsync"
172) "yes"
173) "aof-load-truncated"
174) "yes"
175) "aof-use-rdb-preamble"
176) "yes"
177) "lazyfree-lazy-eviction"
178) "no"
179) "lazyfree-lazy-expire"
180) "no"
181) "lazyfree-lazy-server-del"
182) "no"
183) "slave-lazy-flush"
184) "no"
185) "replica-lazy-flush"
186) "no"
187) "dynamic-hz"
188) "yes"
189) "maxmemory-policy"
190) "noeviction"
191) "loglevel"
192) "notice"
193) "supervised"
194) "no"
195) "appendfsync"
196) "everysec"
197) "syslog-facility"
198) "local0"
199) "appendonly"
200) "no"
201) "dir"
202) "/Users/ajeetraina/redis-stable"
203) "save"
204) "10 1000 60 4000"
205) "client-output-buffer-limit"
206) "normal 0 0 0 slave 268435456 67108864 60 pubsub 33554432 8388608 60"
207) "unixsocketperm"
208) "0"
209) "slaveof"
210) ""
211) "notify-keyspace-events"
212) ""
213) "bind"
214) "127.0.0.1"
```



## Run (if you haven't already) sudo make install from Redis' repository directory to install it on the server. Verify that the server's service starts correctly and that you can connect to it. Locate the configuration file that is used by the deployment.

```
make install
cd src && /Library/Developer/CommandLineTools/usr/bin/make install

Hint: It's a good idea to run 'make test' ;)

    INSTALL install
    INSTALL install
    INSTALL install
    INSTALL install
    INSTALL install
```

### You've arrived at a customer's site where the OSS is deployed on Ubuntu 16. Assuming that you need to perform a configuration change (e.g. setting maxmemory), what steps will you take?

I assume that customer is running Ubuntu 16.04 LTS on AWS Cloud. They might be logging into Ubuntu OS instance via:

```
ssh -i "mynewkey.pem" ubuntu@ec2-54-187-128-174.us-west-2.compute.amazonaws.com
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-1101-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

0 packages can be updated.
0 updates are security updates.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ip-172-31-25-81:~$ cat /etc/os-release
NAME="Ubuntu"
VERSION="16.04.6 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.6 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
```


I assume that they might have installed redis following the below steps:

```
curl -O http://download.redis.io/redis-stable.tar.gz
tar xzvf redis-stable.tar.gz
cd redis-stable
make
```

```
ubuntu@ip-172-31-25-81:~/redis-stable$ sudo mkdir /etc/redis
ubuntu@ip-172-31-25-81:~/redis-stable$ 
ubuntu@ip-172-31-25-81:/etc/redis$ ls
ubuntu@ip-172-31-25-81:/etc/redis$ sudo cp -rf ~/redis-stable/redis.conf .
ubuntu@ip-172-31-25-81:/etc/redis$ ls
redis.conf
ubuntu@ip-172-31-25-81:/etc/redis$ 
```

Open up redis.conf and make the below changes

```
supervisord systemd
dir /var/lib/redis
```

Create redis.service under /etc/systemd/system directory and add the below contents



cat /etc/systemd/system/redis.service

```
[Unit]
Description=Redis In-Memory Data Store
After=network.target

[Service]
User=redis
Group=redis
ExecStart=/usr/local/bin/redis-server /etc/redis/redis.conf
ExecStop=/usr/local/bin/redis-cli shutdown
Restart=always

[Install]
WantedBy=multi-user.target
```

```
ubuntu@ip-172-31-25-81:/etc/redis$ sudo adduser --system --group --no-create-home redis
Adding system user `redis' (UID 112) ...
Adding new group `redis' (GID 116) ...
Adding new user `redis' (UID 112) with group `redis' ...
Not creating home directory `/home/redis'.
ubuntu@ip-172-31-25-81:/etc/redis$ sudo mkdir /var/lib/redis
ubuntu@ip-172-31-25-81:/etc/redis$ sudo chown redis:redis /var/lib/redis
ubuntu@ip-172-31-25-81:/etc/redis$ sudo chmod 770 /var/lib/redis
ubuntu@ip-172-31-25-81:/etc/redis$ sudo systemctl start redis
ubuntu@ip-172-31-25-81:/etc/redis$ sudo systemctl status redis
● redis.service - Redis In-Memory Data Store
   Loaded: loaded (/etc/systemd/system/redis.service; disabled; vendor preset: enabled)
   Active: active (running) since Thu 2020-03-05 09:02:15 UTC; 10s ago
 Main PID: 14421 (redis-server)
    Tasks: 4
   Memory: 1.0M
      CPU: 16ms
   CGroup: /system.slice/redis.service
           └─14421 /usr/local/bin/redis-server 127.0.0.1:6379       

Mar 05 09:02:15 ip-172-31-25-81 redis-server[14421]:  |    `-._`-._        _.-'_.-'    |
Mar 05 09:02:15 ip-172-31-25-81 redis-server[14421]:   `-._    `-._`-.__.-'_.-'    _.-'
Mar 05 09:02:15 ip-172-31-25-81 redis-server[14421]:       `-._    `-.__.-'    _.-'
Mar 05 09:02:15 ip-172-31-25-81 redis-server[14421]:           `-._        _.-'
Mar 05 09:02:15 ip-172-31-25-81 redis-server[14421]:               `-.__.-'
Mar 05 09:02:15 ip-172-31-25-81 redis-server[14421]: 14421:M 05 Mar 2020 09:02:15.586 # WARNING: The TCP ba
Mar 05 09:02:15 ip-172-31-25-81 redis-server[14421]: 14421:M 05 Mar 2020 09:02:15.586 # Server initialized
Mar 05 09:02:15 ip-172-31-25-81 redis-server[14421]: 14421:M 05 Mar 2020 09:02:15.586 # WARNING overcommit_
Mar 05 09:02:15 ip-172-31-25-81 redis-server[14421]: 14421:M 05 Mar 2020 09:02:15.586 # WARNING you have Tr
Mar 05 09:02:15 ip-172-31-25-81 redis-server[14421]: 14421:M 05 Mar 2020 09:02:15.586 * Ready to accept con
lines 1-20/20 (END)
```

```
sudo redis-cli
127.0.0.1:6379> set a1 true
OK
127.0.0.1:6379> get a1
"true"
127.0.0.1:6379> 
```

For any config changes, all you need is to follow below steps:

- Edit redis.conf file under /etc/redis
- Save it
- Restart - sudo systemctl restart redis
