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




