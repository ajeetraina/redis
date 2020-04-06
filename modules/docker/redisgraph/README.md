
# Running RedisGraph - A Graph Database Module for Redis

```
docker run -p 6379:6379 redislabs/redismod
```

## Connecting to Redis Server from another terminal

```
docker exec -it <container-id> sh
```

## Creating MotoGP Graph

```
127.0.0.1:6379> GRAPH.QUERY MotoGP "CREATE (:Rider {name:'Valentino Rossi'})-[:rides]->(:Team {name:'Yamaha'}), (:Rider {name:'Dani Pedrosa'})-[:rides]->(:Team {name:'Honda'}), (:Rider {name:'Andrea Dovizioso'})-[:rides]->(:Team {name:'Ducati'})"
1) 1) "Labels added: 2"
   2) "Nodes created: 6"
   3) "Properties set: 6"
   4) "Relationships created: 3"
   5) "Query internal execution time: 3.111500 milliseconds"
127.0.0.1:6379>
```

Now that our MotoGP graph is created, we can start asking questions, for example: Who's riding for team Yamaha?


```
127.0.0.1:6379> GRAPH.QUERY MotoGP "MATCH (r:Rider)-[:rides]->(t:Team) WHERE t.name = 'Yamaha' RETURN r.name, t.name"
1) 1) "r.name"
   2) "t.name"
2) 1) 1) "Valentino Rossi"
      2) "Yamaha"
3) 1) "Query internal execution time: 1.064700 milliseconds"
127.0.0.1:6379>
```

If you want to see it in action on RedisGraph, just paste on RedisGraph query section.

```
MATCH (r:Rider)-[:rides]->(t:Team) WHERE t.name = 'Yamaha' RETURN r.name, t.name
```
