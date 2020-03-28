# Demonstrating Hashes



Redis hashes data structure contains field-value pairs


```                                      
HMSET hmset user:1000     username      antirez    birthyear      1977      verified      1
                           <field>      <value>   <field>        <value>     <field>     <value>
```


Note: You might notice above that  the key “user:1000” this way we can simulate a table name + PK in the single key. This is just like any other key and can be used anywhere in Redis. 

## API
  - HMSET
  - HGET 
  - HMGET 
      - Is similar to HGET but might returns  an array of values


# Storing object data in hashes

## HSET

Let’s assume we want to store a number of fields about our users, such as a full name, email address, phone number, and number of visits to our application. We’ll
use Redis’s hash management commands—like HSET, HGET, and HINCRBY—to store this information


## Adding John Details

```
127.0.0.1:6379> hset users:john name "John Doe"
(integer) 1
127.0.0.1:6379> hset users:john email "johndoe@gmail.com"
(integer) 1
127.0.0.1:6379> hset users.paul phone "+1555313940"
(integer) 1
```

## Retrieving the John Information

```
127.0.0.1:6379> hgetall users:john
1) "name"
2) "John Doe"
3) "visits"
4) "1"
5) "email"
6) "johndoe@gmail.com"
127.0.0.1:6379>
```



## Adding Paul Details


```
127.0.0.1:6379> hset users:paul name "Paul S"
(integer) 1
127.0.0.1:6379> hset users:paul email "pauls@gmail.com"
(integer) 1
127.0.0.1:6379> hset users.paul phone "+919665656565"
(integer) 1
```






## HINCRBY

```
127.0.0.1:6379> hincrby users:john visits 1
(integer) 1
127.0.0.1:6379> hincrby users:paul visits 10
(integer) 10
127.0.0.1:6379> hincrby users:mike visits 100
(integer) 100
```

## HGET

```
127.0.0.1:12000>  hget users:john email
"johndoe@test.com"
```

## HGETALL

```
127.0.0.1:12000> hgetall users:john
1) "name"
2) "John Doe"
3) "email"
4) "johndoe@gmail.com"
5) "phone"
6) "+1555313940"
7) "visits"
8) "1"
127.0.0.1:12000>
```
