# List of Redis OSS Exercises


- [Exercise #1: Redis Configuration File](https://github.com/ajeetraina/redis/tree/master/1/redis-conf)
- [Exercise #2: Redis Keyspace](https://github.com/ajeetraina/redis/blob/master/2/key%20space/README.md)
- [Exercise #3: Counter Patterns](https://github.com/ajeetraina/redis/blob/master/3/counting/README.md)
- [Exercise #4: Redis as a Primary Datastore]()



# RedisLabs Vs Redis OSS 

| Redis OSS       | RedisLabs       | 
| ------------- |:-------------:|
|   Leading OSS in-memory database platform, supporting any high performance operational, analytics or hybrid use case            |  The OSS home and commercial provider of Redis Enterprise technology, platform, products and services          |  

# Redis Enterprise Vs Redis OSS


## Standalone Redis

| Redis OSS       | RedisLabs       | 
| ------------- |:-------------:|
|   No Concept of sharding           |            |  
|   No automatic Failover           |            | 
|   No Scability         |            | 
|   No Multitenancy           |            | 
|   Manual & Complex Operation           |            | 
|   Relaxed (Multiple Replicas) Consistency           |            | 
|   Single instance performance for writes           |            | 
|   Single instance performance for writes           |            | 


## [Redis Sentinel](https://redis.io/topics/sentinel)

| Redis OSS     | RedisLabs      | 
| ------------- |:-------------:|
|   No Scability            |            |  
|   No HA (Yes, but can take comparable long)          |            | 
|   Built-in HA and automatic failover        |            | 
|   Doesn't support standard clients, Sentinel discovery mechanism instead          |            | 
|   Hard to operate          |            | 
|   No Multitenancy          |            | 
|   Relaxed (1 master + 2 replicas)         |            | 
|   Complex+, manual           |            | 


## [Redis OSS Cluster](https://redis.io/topics/cluster-tutorial)

| Redis OSS     | RedisLabs      | 
| ------------- |:-------------:|
|   Built-in HA and automatic failover           |            |  
|   Hash­based sharding (and hash tags)          |            | 
|   No support for multi­key operations      |            | 
|   Doesn't support standard clients, OSS Cluster client required         |            | 
|   Hard to operate        |            | 
|   Scalable        |            | 
|   Lower Performance       |            | 
|   Scalable        |            | 
| Performance dependent on the number of connections per shard |    |
| Each client needs to connect to each shard | |


## [Redis Enterprise]()

| Feature | Redis OSS     | Redis Enterprise      | 
| -----------| ------------- |-------------|
| Scability     |                                 Yes     |       Fully Automated   |  
|  HA           | Built-in HA, manual intervention may be required    |       Fully automated                  | 
|  Performance  |                       Lower                  |   Up to x2 base, Stable            | 
|  Multitenancy |                        None                 |       Yes                          | 
| Consistency   |                  Relaxed (2 replicas per master shard)       |    Tunable                         | 
| Operations    |             Complex++, manual                 |     Minimal, automated             | 
| Sharding      |                                         | Automatic resharding when increasing the shard count |
| Sharding      |                                         | Increasing the shard count leads to a balanced state |
| Proxy         |                                         | Built-in Proxy for connection multiplexing and command re-pipelining |
| Failover      |                                         | Automatic failover and failure recovery (Watchdogs, Supervisor, ...)|
| Sharding.     |                                         | Hash based sharding (and hash tags) |
| Multikey Operations | | Support for several multikey operations (i.e. MSET/MGET) |
| Clients for Database    |  Doesn't support standard clients, OSS Cluster client required     |   Supports standard clients for standard clustered databases |
|                         |       |  Node-based quorum, 1 replica per master shard, doesn't allow to read from replicas |
