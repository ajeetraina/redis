
# zincrby

- Redis ZINCRBY command is used to increment the score or member in the sorted setat key by an incremental value. 
-  If no member exists in the sorted set,it is added with incremental value as specified. 
- If the  key does not exist, a new sorted set stored  with the specified member as its sole member is created. 
- When key exists but does not hold a sorted set an error will return.

## Syntax:

```
ZINCRBY KEY INCREMENT MEMBER
```

## Example: Redis ZINCRBY: score increase, decrease

```
127.0.0.1:6379> ZADD myvisit 1200 facebook.com 1800 google.com 1500 stackoverflow.com
(integer) 3
127.0.0.1:6379> ZREVRANGE myvisit 0 -1 WITHSCORES
1) "google.com"
2) "1800"
3) "stackoverflow.com"
4) "1500"
5) "facebook.com"
6) "1200"
```

The facebook.com increased by 500

```
127.0.0.1:6379> ZINCRBY myvisit 500 facebook.com
"1700"
127.0.0.1:6379> ZREVRANGE myvisit 0 -1 WITHSCORES
1) "google.com"
2) "1800"
3) "facebook.com"
4) "1700"
5) "stackoverflow.com"
6) "1500"
```

The google.com decreased by 200

```
127.0.0.1:6379> ZINCRBY myvisit -200 google.com
"1600"
```

The rank has changed

```
127.0.0.1:6379> ZREVRANGE myvisit 0 -1 WITHSCORES
1) "facebook.com"
2) "1700"
3) "google.com"
4) "1600"
5) "stackoverflow.com"
6) "1500"
```
