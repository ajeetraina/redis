
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

## Example: Redis ZINCRBY: using decimal

```
127.0.0.1:6379> ZADD myliteracy 8.3 Canada 6.7 Brazil 5.1 India 4.2 Koria 7.9 Japan
(integer) 5
127.0.0.1:6379> ZREVRANGE myliteracy 0 -1 WITHSCORES
 1) "Canada"
 2) "8.3000000000000007"
 3) "Japan"
 4) "7.9000000000000004"
 5) "Brazil"
 6) "6.7000000000000002"
 7) "India"
 8) "5.0999999999999996"
 9) "Koria"
10) "4.2000000000000002"
127.0.0.1:6379> ZINCRBY myliteracy 1.7 India
"6.7999999999999998"
```

## Example: Redis ZINCRBY: generate key member

If you do not have to create and save an existing key or member. At this time, the criteria score is 0.0.

```
127.0.0.1:6379> ZINCRBY dailyviewers 1 450205
"1"
127.0.0.1:6379> ZINCRBY dailyviewers 1 450205
"2"
127.0.0.1:6379> ZINCRBY dailyviewers 1 450205
"3"
127.0.0.1:6379> ZINCRBY dailyviewers 1 450306
"1"
127.0.0.1:6379> ZINCRBY dailyviewers 1 450306
"2"
127.0.0.1:6379> ZREVRANGE dailyviewers 0 -1 WITHSCORES
1) "450205"
2) "3"
3) "450306"
4) "2"
```

