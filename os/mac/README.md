# Demonstrating Redis on MacOS

## Pre-requisite

- Install Python

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

```
set a1 100
set a2 200
set a3 300
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



