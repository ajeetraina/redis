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


## 
