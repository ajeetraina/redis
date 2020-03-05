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

## Example: Redis ZADD : The score member can have multiple input

```
127.0.0.1:6379> ZADD mycolorset 4 blue 5 green
(integer) 2
127.0.0.1:6379> ZRANGE mycolorset 0 -1 WITHSCORES
 1) "white"
 2) "1"
 3) "black"
 4) "2"
 5) "red"
 6) "3"
 7) "blue"
 8) "4"
 9) "green"
10) "5"
```

## Example: Redis ZADD : score is equal to the member being sort

```
127.0.0.1:6379> ZADD mycolorset 1 white 1 black 1 red 1 blue 1 green
(integer) 5
127.0.0.1:6379> ZRANGE mycolorset 0 -1 WITHSCORES
 1) "black"
 2) "1"
 3) "blue"
 4) "1"
 5) "green"
 6) "1"
 7) "red"
 8) "1"
 9) "white"
10) "1"
```

## Example: Redis ZADD : duplicate member is not permitted

```
127.0.0.1:6379> ZADD mycolorset 1 orange
(integer) 1
127.0.0.1:6379> ZRANGE mycolorset 0 -1 WITHSCORES
 1) "black"
 2) "1"
 3) "blue"
 4) "1"
 5) "green"
 6) "1"
 7) "orange"
 8) "1"
 9) "red"
10) "1"
11) "white"
12) "1"
```
