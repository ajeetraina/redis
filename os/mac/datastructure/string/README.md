# Demonstrating Redis String Data Structure

# Strings Operation 

- SET and the GET commands are the way we set and retrieve a string value
- SET performs an assignment
- SET will replace any existing value already stored into the key
- Values can be strings (including binary data) of every kind, for instance you can store a jpeg image inside a key


# Set Command

The SET command has interesting options, that are provided as additional arguments

- EX seconds 
  Set the specified expire time, in seconds
- PX milliseconds 
  Set the specified expire time, in milliseconds
- NX 
  Only set the key if it does not already exist
- XX 
  Only set the key if it already exist

```
127.0.0.1:6379> set a1 101 xx
OK
127.0.0.1:6379> get a1
"101"
127.0.0.1:6379> set a1 102 nx
(nil)

```

# Redis Expire Command

Redis Expire command is used to set the expiry of a key. After the expiry time, the key will not be available in Redis.

```
127.0.0.1:6379> expire alpha 200
(integer) 1
127.0.0.1:6379> get alpha
"100"
127.0.0.1:6379>
```


# String with Integer Values - INCR


- Use Strings as atomic counters using commands in the INCR family: 
    - INCR, 
    - DECR, 
    - INCRBY, 
    - DECRBY
- Even if strings are the basic values of Redis, there are interesting operations you can perform with them 
- For instance, one is atomic increment

## Example:

```
127.0.0.1:6379> set counter 100
OK
127.0.0.1:6379> incr counter
(integer) 101
127.0.0.1:6379> incr counter
(integer) 102
127.0.0.1:6379> incrby counter 50
(integer) 152
127.0.0.1:6379>
```
