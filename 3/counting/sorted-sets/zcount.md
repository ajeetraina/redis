# zcount

- Redis ZCOUNT command is used to return the number of elements in the sorted set at the key with a score between minimum and 
maximum.


## Syntax:

```
ZCOUNT KEY_NAME
```

## Example: Redis ZCOUNT: Any member may belong to the set

```
127.0.0.1:6379> ZADD mycolorset  528 white  2514 black 850 red 128 pink 742 yellow
(integer) 5
127.0.0.1:6379> ZADD mycolorset  158 orange 1500 green 645 blue 426 gray
(integer) 4
127.0.0.1:6379> ZCOUNT mycolorset -inf +inf
(integer) 9
```

## Example : Redis ZCOUNT : When the value is over 800 or more

```
127.0.0.1:6379> ZADD mycolorset  528 white  2514 black 850 red 128 pink 742 yellow
(integer) 5
127.0.0.1:6379> ZADD mycolorset  158 orange 1500 green 645 blue 426 gray
(integer) 4
127.0.0.1:6379> ZCOUNT mycolorset 800 +inf
(integer) 3
```

## Example: Redis ZCOUNT: When the value among 100 and 500

```
127.0.0.1:6379> ZADD mycolorset  528 white  2514 black 850 red 128 pink 742 yellow
(integer) 5
127.0.0.1:6379> ZADD mycolorset  158 orange 1500 green 645 blue 426 gray
(integer) 4
127.0.0.1:6379> ZCOUNT mycolorset 100 500
(integer) 3
```

## Example: Redis ZCOUNT: When the value among 300 and less

```
127.0.0.1:6379> ZADD mycolorset  528 white  2514 black 850 red 128 pink 742 yellow
(integer) 5
127.0.0.1:6379> ZADD mycolorset  158 orange 1500 green 645 blue 426 gray
(integer) 4
127.0.0.1:6379> ZCOUNT mycolorset -inf 300
(integer) 2
```
