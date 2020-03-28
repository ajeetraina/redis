# A Quick Look at Redis Data Structure Demos and Examples


## Demo #

- Installing Redis on MacOS using brew
- Running Redis Server with/out Authentication
- Demonstrating Data Structure
  - String 
  - Hash 
  - List 
  - Set 
  - Sorted Set 
  - Streams  
- Using Python to insert data structure into Redis
- Demonstrating Geolocation-Aware Demo Applications with Redis
- Open Source UI for Redis OSS
  


## Pre-requisite

- Redis
- Python


- Installing Redis

```
brew install redis
```

- Verifying Redis Installation

```
$redis-server --version
Redis server v=5.0.7 sha=00000000:0 malloc=libc bits=64 build=4bd99862b1ce82a9
```

```
redis-cli --version
redis-cli 5.0.7
```

- Install Python - We will require it for Demo Purpose

```
brew install python
```

- Install pip

```
sudo easy_install pip
```

## Running Redis Server

```
redis-server
```

## Connecting to Redis Server

```
redis-cli 
```

## SET and GET operation


| Key     | Value      |
| ------- | ---------- |
| city1   | Bangalore  |
| city2   | Pune       |
| city3   | Delhi      |

```
127.0.0.1:6379> set city1 bangalore
127.0.0.1:6379> set city2 pune
127.0.0.1:6379> set city3 delhi
```

```
127.0.0.1:6379> keys *
1) "city1"
2) "city2"
3) "city3"
```

## Expiring the key



```
expire city1 10
```

| Key     | Value      |
| ------- | ---------- |
| city2   | Pune       |
| city3   | Delhi      |



## Verify

```
127.0.0.1:6379> keys *
1) "city2"
2) "city3"
127.0.0.1:6379>
```

## Inserting keys using Python

Copy the below content into a file called push-keys.python

```
import redis
# Create connection object
r = redis.Redis(host='localhost', port=6379)
# set a value for the foo object
r.set('foo', 'bar')
# retrieve and print the value for the foo object
print(r.get('foo'))
```


# Protecting Redis with password

Stop the old running redis server and run the below command:

```
redis-server --requirepass redis12#
```

## Connecting to Redis using Python - with auth

```
import redis
# Create connection object
r = redis.StrictRedis(host='localhost', port=6379, db=0, password='redis12#')
# set a value for the foo object
r.set('foo', 'bar')
# retrieve and print the value for the foo object
print(r.get('foo'))
```

[Next >> Redis Data Structure](https://github.com/ajeetraina/redis/blob/master/os/mac/datastructure/string/README.md)


