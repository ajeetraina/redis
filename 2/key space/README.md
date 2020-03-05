# Exercise #2 - Redis Keyspace

[Concept]()

## Find the overhead of an empty database from Redis' (hint: INFO's memory section) and the OS' (e.g. ps)
- What is the empty dataset's overhead?
- Explain the difference between Redis' and the OS' reports of RAM consumption


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
 
 
