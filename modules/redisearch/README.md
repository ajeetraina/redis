# Installing RediSearch

## Infra

- MacOS
- Ensure that redis server is not running

## Cloning the RediSearch

```
ajeetraina@Ajeet-Rainas-Macbook-Pro ~ % git clone --recursive https://github.com/RediSearch/RediSearch.git
Cloning into 'RediSearch'...
remote: Enumerating objects: 185, done.
remote: Counting objects: 100% (185/185), done.
remote: Compressing objects: 100% (138/138), done.
remote: Total 25141 (delta 109), reused 77 (delta 47), pack-reused 24956
Receiving objects: 100% (25141/25141), 17.12 MiB | 2.99 MiB/s, done.
Resolving deltas: 100% (18167/18167), done.
Submodule 'deps/readies' (https://github.com/RedisLabsModules/readies.git) registered for path 'deps/readies'
Cloning into '/Users/ajeetraina/RediSearch/deps/readies'...
remote: Enumerating objects: 175, done.        
remote: Counting objects: 100% (175/175), done.        
remote: Compressing objects: 100% (131/131), done.        
remote: Total 481 (delta 98), reused 102 (delta 43), pack-reused 306        
Receiving objects: 100% (481/481), 92.71 KiB | 310.00 KiB/s, done.
Resolving deltas: 100% (262/262), done.
Submodule path 'deps/readies': checked out 'a3b8dab21db25d599feb40713ccf8df2094fdda6'
ajeetraina@Ajeet-Rainas-Macbook-Pro ~ % 
```

## Installing Pre-requisite

```
cd RediSearch
./system-setup.py
make build
```

```
[ 98%] Building C object CMakeFiles/rscore.dir/src/util/quantile.c.o
[ 98%] Building C object CMakeFiles/rscore.dir/src/value.c.o
[ 99%] Building C object CMakeFiles/rscore.dir/src/varint.c.o
1 warning generated.
[ 99%] Built target rscore
Scanning dependencies of target redisearch
[ 99%] Building C object CMakeFiles/redisearch.dir/src/module-init/module-init.c.o
[100%] Linking C shared library redisearch.so
ld: warning: directory not found for option '-L/usr/local/Cellar/zlib/1.2.11/lib'
[100%] Built target redisearch
cp build/redisearch.so src/redisearch.so
```

```
ajeetraina@Ajeet-Rainas-Macbook-Pro RediSearch % make run 
Makefile:98: warning: overriding commands for target `clean'
deps/readies/mk/build.rules:17: warning: ignoring old commands for target `clean'
8188:C 29 Mar 2020 02:01:57.670 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
8188:C 29 Mar 2020 02:01:57.670 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=8188, just started
8188:C 29 Mar 2020 02:01:57.670 # Configuration loaded
8188:M 29 Mar 2020 02:01:57.671 * Increased maximum number of open files to 10032 (it was originally set to 2560).
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 5.0.7 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 8188
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

8188:M 29 Mar 2020 02:01:57.671 # Server initialized
8188:M 29 Mar 2020 02:01:58.046 * <ft> RediSearch version 99.99.99 (Git=v1.6.6-49-g331636b2)
8188:M 29 Mar 2020 02:01:58.046 * <ft> Low level api version 1 initialized successfully
8188:M 29 Mar 2020 02:01:58.046 * <ft> concurrent writes: OFF, gc: ON, prefix min length: 2, prefix max expansions: 200, query timeout (ms): 500, timeout policy: return, cursor read size: 1000, cursor max idle (ms): 300000, max doctable size: 1000000, search pool size: 20, index pool size: 8, 
8188:M 29 Mar 2020 02:01:58.046 * <ft> Initialized thread pool!
8188:M 29 Mar 2020 02:01:58.047 * Module 'ft' loaded from src/redisearch.so
8188:M 29 Mar 2020 02:01:58.047 * Ready to accept connections
```
