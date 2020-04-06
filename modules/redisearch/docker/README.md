# Running RediSearch Docker container


```
docker run -p 6379:6379 redislabs/redisearch:latest
```

```
Digest: sha256:a1e1b2407919e669f7e986dc254f61fa32897c02b54464413812227895e7381d
Status: Downloaded newer image for redislabs/redisearch:latest
1:C 06 Apr 2020 15:01:28.902 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
1:C 06 Apr 2020 15:01:28.902 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=1, just started
1:C 06 Apr 2020 15:01:28.902 # Configuration loaded
1:M 06 Apr 2020 15:01:28.904 * Running mode=standalone, port=6379.
1:M 06 Apr 2020 15:01:28.904 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
1:M 06 Apr 2020 15:01:28.904 # Server initialized
1:M 06 Apr 2020 15:01:28.904 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
1:M 06 Apr 2020 15:01:28.905 * <ft> RediSearch version 1.6.10 (Git=v1.6.10)
1:M 06 Apr 2020 15:01:28.905 * <ft> Low level api version 1 initialized successfully
1:M 06 Apr 2020 15:01:28.905 * <ft> concurrent writes: OFF, gc: ON, prefix min length: 2, prefix max expansions: 200, query timeout (ms): 500, timeout policy: return, cursor read size: 1000, cursor max idle (ms): 300000, max doctable size: 1000000, search pool size: 20, index pool size: 8,
1:M 06 Apr 2020 15:01:28.905 * <ft> Initialized thread pool!
1:M 06 Apr 2020 15:01:28.905 * Module 'ft' loaded from /usr/lib/redis/modules/redisearch.so
1:M 06 Apr 2020 15:01:28.906 * Ready to accept connections
```

## Connecting to Redis Server loaded with RediSearch Module

```
ajeetraina@Ajeet-Rainas-Macbook-Pro ~ % docker ps
CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS              PORTS                    NAMES
a8a8061b053c        redislabs/redisearch:latest   "docker-entrypoint.s…"   2 minutes ago       Up 2 minutes        0.0.0.0:6379->6379/tcp   sweet_euler
ajeetraina@Ajeet-Rainas-Macbook-Pro ~ % docker exec -it a8 sh
# bash
root@a8a8061b053c:/data# redis-cli
127.0.0.1:6379> FT.create key ...options...
```

## Running RedisInsight using Docker Container

```
docker run -v redisinsight:/db -p 8001:8001 redislabs/redisinsight
```

```
ajeetraina@Ajeet-Rainas-Macbook-Pro ~ % docker ps
CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS              PORTS                    NAMES
e66ce908e758        redislabs/redisinsight        "bash ./docker-entry…"   4 minutes ago       Up 4 minutes        0.0.0.0:8001->8001/tcp   tender_euler
a8a8061b053c        redislabs/redisearch:latest   "docker-entrypoint.s…"   10 minutes ago      Up 10 minutes       0.0.0.0:6379->6379/tcp   sweet_euler
```

## Connecting to 

```
docker exec -t a8 sh
127.0.0.1:6379> module list
1) 1) "name"
   2) "ft"
   3) "ver"
   4) (integer) 10610
```

Let us start adding document to RediSearch.

## Create Index with fields


```
127.0.0.1:6379> FT.create myindex schema title TEXT weight 5.0 body TEXT url TEXT
OK
127.0.0.1:6379>
```

## Adding documents to Index

```
FT.add myindex doc1 1.0 fields title “Collabnix” collabnix “My Personal Website” URL “http://www.collabnix.com“
```

## Searching

Just put “collabnix” limit 0 10 into the box section and it will search it in no time.


