# Running Redis Modules inside Docker Container

Modules included in the container
- RediSearch: a full-featured search engine
- RedisGraph: a graph database
- RedisTimeSeries: a timeseries database
- RedisAI: a tensor and deep learning model server
- RedisJSON: a native JSON data type
- RedisBloom: native Bloom and Cuckoo Filter data types
- RedisGears: a dynamic execution framework


```
docker run -p 6379:6379 redislabs/redismod
```

Once you run this Docker container, all modules are imported.
