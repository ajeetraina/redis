# Exercise #2 - Redis Keyspace

[Concept](https://github.com/ajeetraina/redis/blob/master/2/concept.md)

## Exercise #2.1 - Keyspace Overhead

Find the overhead of an empty database from Redis' (hint: INFO's memory section) and the OS' (e.g. ps)

- What is the empty dataset's overhead?
- Explain the difference between Redis' and the OS' reports of RAM consumption


### Explanation:

Redis maintains several private data structures for managing the internals of the keyspace. 
The most notable data structure is the global dictionary (a hash map) that maps key names to their (pointers to their) respective values.

Naturally, these internal administrative data structures incur some overhead in terms of RAM. 
The bigger the dataset becomes, so do global keyspace overheads. That said, the global overheads are comparatively negligible once the dataset starts growing.

#### Please Note: 

Every key in the keyspace has its own overhead, that is used for managing the key's internal "record" in the global dictionary. This overhead is "charged" for every key in the keyspace, regardless any of the key's properties.


Infra Setup:


redis-cli> flushdb
rdis-cli> flushall

- Memory => 1 GB

```
ubuntu@ip-172-31-25-81:/etc/redis$ free -m
              total        used        free      shared  buff/cache   available
Mem:            990          59         640           3         291         764
Swap:             0           0           0
```


If you run the below command:

```
127.0.0.1:6379> info memory
# Memory
used_memory:853256
used_memory_human:833.26K
used_memory_rss:5619712
used_memory_rss_human:5.36M
used_memory_peak:853256
used_memory_peak_human:833.26K
used_memory_peak_perc:100.01%
used_memory_overhead:841030 => 0.8 MB
used_memory_startup:791336
used_memory_dataset:12226
used_memory_dataset_perc:19.74%
allocator_allocated:1363824
allocator_active:1617920
allocator_resident:8343552
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
allocator_frag_ratio:1.19
allocator_frag_bytes:254096
allocator_rss_ratio:5.16
allocator_rss_bytes:6725632
rss_overhead_ratio:0.67
rss_overhead_bytes:-2723840
mem_fragmentation_ratio:6.92
mem_fragmentation_bytes:4807480
mem_not_counted_for_evict:0
mem_replication_backlog:0
mem_clients_slaves:0
mem_clients_normal:49694
mem_aof_buffer:0
mem_allocator:jemalloc-5.1.0
active_defrag_running:0
lazyfree_pending_objects:0
127.0.0.1:6379>
 ```
 
 OR
 
 ```
 ubuntu@ip-172-31-25-81:/etc/redis$ sudo pmap 14484 | tail -n 1
 total            56100K
 ```
 
 Around 57 MB
 
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

As you can see, the total memory used by the process 14484 is 56100 KB or kilobytes. You can also see how much memory the libraries and other files required to run the process with PID 14484 is using as well here.


## Explain the difference between Redis' and the OS' reports of RAM consumption

<TBD>


## Exercise #2.2 - Key overhead

- Find the minimal overhead of a key with a String value


The MEMORY USAGE command reports the number of bytes that a key and its value require to be stored in RAM.
The reported usage is the total of memory allocations for data and administrative overheads that a key its value require.

```
ubuntu@ip-172-31-25-81:/etc/redis$ sudo redis-cli
127.0.0.1:6379> SET "" ""
OK
127.0.0.1:6379> MEMORY USAGE ""
(integer) 46
127.0.0.1:6379>
```

## Exercise #2.3 - Keyspace Pattern: 'SCAN"

Read, understand and internalize the section covering SCAN's guarantees to understand its limits. Prepare to be quizzed by your customers.

### Concept:

### What is this SCAN command all about?

The SCAN command and the closely related commands SSCAN, HSCAN and ZSCAN are used in order to incrementally iterate over a collection of elements.

- SCAN iterates the set of keys in the currently selected Redis database.
- SSCAN iterates elements of Sets types.
- HSCAN iterates fields of Hash types and their associated values.
- ZSCAN iterates elements of Sorted Set types and their associated scores

As of v2.8, the SCAN offers a way for performing a full keyspace scan similar to KEYS, but in a more polite manner. It is essentially a stateless (server-wise) cursor that allows iterating over the keyspace, and unlike KEYS it is not atomic and blocking.

Note: make sure that you understand the purpose of the COUNT subcommand - it controls the amount of effort performed by the server to locate matching keys, and thus only indirectly the number of actual results returned in each iteration. The higher the COUNT, the longer each call to SCAN will take to complete.


### SCAN basic usage

- SCAN is a cursor based iterator. 
- This means that at every call of the command, the server returns an updated cursor that the user needs to use as the cursor argument in the next call.
- An iteration starts when the cursor is set to 0, and terminates when the cursor returned by the server is 0. The following is an example of SCAN iteration:

```
127.0.0.1:6379> scan 0
1) "0"
2) 1) "a1"
   2) ""
```

# SCAN GUARENTEES

- The SCAN command, and the other commands in the SCAN family, are able to provide to the user a set of guarantees associated to full iterations.

- A full iteration always retrieves all the elements that were present in the collection from the start to the end of a full iteration. This means that if a given element is inside the collection when an iteration is started, and is still there when an iteration terminates, then at some point SCAN returned it to the user.

- A full iteration never returns any element that was NOT present in the collection from the start to the end of a full iteration. So if an element was removed before the start of an iteration, and is never added back to the collection for all the time an iteration lasts, SCAN ensures that this element will never be returned.

However because SCAN has very little state associated (just the cursor) it has the following drawbacks:

- A given element may be returned multiple times. It is up to the application to handle the case of duplicated elements, for example only using the returned elements in order to perform operations that are safe when re-applied multiple times.

- Elements that were not constantly present in the collection during a full iteration, may be returned or not: it is undefined.



