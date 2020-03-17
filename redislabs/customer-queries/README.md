# The customer is 60-70% in MongoDB. The customer wants to replicate from MongoDB to REDIS. 
There might be a lot of solutions but not sure how efficient are they?

# Do you have a “write behind” type of solutions?
Still want to continue using relational database

- There is a lambda like function which we developed called RedisGears
- It’s a module
- Event-driven architecture
- Achieve for write behind architecture

# Elasticsearch comes with 2 major use cases - standard search & part of ELK stack, replicating logs and making it searchable and dashboard on Kibana. Replacing Redis with Elastic Stack. Redis doesn’t store a lot of data. 
- Today consumer based company stores TBs of data
- We have a mechanism called Redis on Flash.
- Redis Time Series allows you to aggregate data into computation and export Prometheus data into time series(more of Financial)


# Does it mean we don’t need Prometheus?
- Export Prometheus data into Redis
- There are some logs which need to be accessed quickly
- Modules are available open source but not scalable. They don’t follow cluster model in open source.
