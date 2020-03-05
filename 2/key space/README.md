# Exercise #2 - Redis Keyspace

[Concept](https://github.com/ajeetraina/redis/blob/master/2/concept.md)

## Find the overhead of an empty database from Redis' (hint: INFO's memory section) and the OS' (e.g. ps)
- What is the empty dataset's overhead?
- Explain the difference between Redis' and the OS' reports of RAM consumption


### Explanation:

Redis maintains several private data structures for managing the internals of the keyspace. 
The most notable data structure is the global dictionary (a hash map) that maps key names to their (pointers to their) respective values.

Naturally, these internal administrative data structures incur some overhead in terms of RAM. 
The bigger the dataset becomes, so do global keyspace overheads. That said, the global overheads are comparatively negligible once the dataset starts growing.


Infra Setup:

- Memory => 1 GB

```
ubuntu@ip-172-31-25-81:/etc/redis$ free -m
              total        used        free      shared  buff/cache   available
Mem:            990          59         640           3         291         764
Swap:             0           0           0
```


If you run the below command:

```
127.0.0.1:6379> INFO memory
# Memory
used_memory:574848
used_memory_human:561.38K
used_memory_rss:5328896
used_memory_rss_human:5.08M
used_memory_peak:575824
used_memory_peak_human:562.33K
used_memory_peak_perc:99.83%
used_memory_overhead:563630
used_memory_startup:513864
used_memory_dataset:11218
used_memory_dataset_perc:18.39%
allocator_allocated:1181000
allocator_active:1540096
allocator_resident:8314880
total_system_memory:1038770176
total_system_memory_human:990.65M
used_memory_lua:37888
used_memory_lua_human:37.00K
used_memory_scripts:0
used_memory_scripts_human:0B
number_of_cached_scripts:0
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
allocator_frag_ratio:1.30
allocator_frag_bytes:359096
allocator_rss_ratio:5.40
allocator_rss_bytes:6774784
rss_overhead_ratio:0.64
rss_overhead_bytes:-2985984
mem_fragmentation_ratio:9.98
mem_fragmentation_bytes:4795064
mem_not_counted_for_evict:0
mem_replication_backlog:0
mem_clients_slaves:0
mem_clients_normal:49694
mem_aof_buffer:0
mem_allocator:jemalloc-5.1.0
active_defrag_running:0
lazyfree_pending_objects:0
```

```
ubuntu@ip-172-31-25-81:/etc/redis$ ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
  PID  PPID CMD                         %MEM %CPU
 1565     1 /usr/lib/snapd/snapd         1.9  0.0
 1193     1 /usr/bin/python3 /usr/share  1.3  0.0
 1762     1 /snap/amazon-ssm-agent/1480  1.0  0.0
    1     0 /sbin/init                   0.5  0.0
14421     1 /usr/local/bin/redis-server  0.5  0.1
 1931  1924 -bash                        0.4  0.0
 1107     1 /usr/lib/accountsservice/ac  0.4  0.0
 1178     1 /usr/lib/policykit-1/polkit  0.4  0.0
 1861  1334 sshd: ubuntu [priv]          0.4  0.0
 ```
 
 OR
 
 ```
 ubuntu@ip-172-31-25-81:/etc/redis$ sudo pmap 14484 | tail -n 1
 total            56100K
 ```
 
 
 ```
 ubuntu@ip-172-31-25-81:/etc/redis$ sudo pmap 14484
14484:   /usr/local/bin/redis-server 127.0.0.1:6379       
0000000000400000   1692K r-x-- redis-server
00000000007a7000      8K r---- redis-server
00000000007a9000     24K rw--- redis-server
00000000007af000   2196K rw---   [ anon ]
000000000269c000    132K rw---   [ anon ]
00007f204b47d000   5632K rw---   [ anon ]
00007f204b9fd000      4K -----   [ anon ]
00007f204b9fe000   8192K rw---   [ anon ]
00007f204c1fe000      4K -----   [ anon ]
00007f204c1ff000   8192K rw---   [ anon ]
00007f204c9ff000      4K -----   [ anon ]
00007f204ca00000   8192K rw---   [ anon ]
00007f204d200000   8192K rw---   [ anon ]
00007f204db75000   1792K r-x-- libc-2.23.so
00007f204dd35000   2048K ----- libc-2.23.so
00007f204df35000     16K r---- libc-2.23.so
00007f204df39000      8K rw--- libc-2.23.so
00007f204df3b000     16K rw---   [ anon ]
00007f204df3f000     96K r-x-- libpthread-2.23.so
00007f204df57000   2044K ----- libpthread-2.23.so
00007f204e156000      4K r---- libpthread-2.23.so
00007f204e157000      4K rw--- libpthread-2.23.so
00007f204e158000     16K rw---   [ anon ]
00007f204e15c000     28K r-x-- librt-2.23.so
00007f204e163000   2044K ----- librt-2.23.so
00007f204e362000      4K r---- librt-2.23.so
00007f204e363000      4K rw--- librt-2.23.so
00007f204e364000     12K r-x-- libdl-2.23.so
00007f204e367000   2044K ----- libdl-2.23.so
00007f204e566000      4K r---- libdl-2.23.so
00007f204e567000      4K rw--- libdl-2.23.so
00007f204e568000   1056K r-x-- libm-2.23.so
00007f204e670000   2044K ----- libm-2.23.so
00007f204e86f000      4K r---- libm-2.23.so
00007f204e870000      4K rw--- libm-2.23.so
00007f204e871000    152K r-x-- ld-2.23.so
00007f204ea8a000     24K rw---   [ anon ]
00007f204ea96000      4K r---- ld-2.23.so
00007f204ea97000      4K rw--- ld-2.23.so
00007f204ea98000      4K rw---   [ anon ]
00007fff2a43e000    132K rw---   [ stack ]
00007fff2a469000      8K r----   [ anon ]
00007fff2a46b000      8K r-x--   [ anon ]
ffffffffff600000      4K r-x--   [ anon ]
 total            56100K
```

As you can see, the total memory used by the process 14484 is 56100 KB or kilobytes. You can also see how much memory the libraries and other files required to run the process with PID 14484 is using as well here
