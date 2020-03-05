# ZADD

- Redis ZADD command is used to add all the specified members with the specified scores to the sorted set stored at key. 
- If a specified member is an existing member of the stored set, the score is updated and the element reinserted at the right 
position to ensure the correct ordering. 
- A new sorted set with the specified members as sole members is created, when key dies not exists or the sorted set was empty. 
If the key exists but does not hold a sorted set, an error is returned.


Syntax:

```
ZADD KEY_NAME SCORE1 VALUE1.. SCOREN VALUEN
```

```
127.0.0.1:6379> ZADD mycolorset 1 white
(integer) 1
127.0.0.1:6379> ZADD mycolorset 2 black
(integer) 1
127.0.0.1:6379> ZADD mycolorset 3 red
(integer) 1
127.0.0.1:6379> ZRANGE mycolorset 0 -1
1) "white"
2) "black"
3) "red"
127.0.0.1:6379> ZRANGE mycolorset 0 -1 WITHSCORES
1) "white"
2) "1"
3) "black"
4) "2"
5) "red"
6) "3"
```


