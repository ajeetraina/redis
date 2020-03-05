
# Introduction to Lua Script


Redis has an embedded scripting language.

It lets you create your own scripted extensions to the Redis database. That means that with Redis you can execute Lua scripts like this:

```
> EVAL 'local val="Hello Compose" return val' 0
"Hello Compose"
```

The string after the EVAL is the Lua script.

```
local val="Hello Compose"  
return val 
```

The 0 at the end of the EVAL, thats the number of keys being passed to the Lua code, in that example there were none.
But if instead of 0 it was 2 foo bar fizz buzz then the first two items in the list, foo and bar, would be passed as keys and fizz and buzz would be arguments.

You can also write lua script as shown below:


```lua
 local name=redis.call("get", KEYS[1])
 local greet=ARGV[1]
 local result=greet.." "..name
 return result
```

Save it hello.lua 



## Example #2:

Our first Redis Lua script just returns a value without actually interacting with Redis in any meaningful way:
The first line sets up a local variable with our message, and the second line returns that value from the Redis server to the client. Save this file locally as hello.lua and run it like so:

```
cat hello.lua
local msg = "Hello, world!"
return msg
```

Running this will print “Hello, world!”. The first argument of EVAL is the complete lua script — here we’re using the cat command to read the script from a file. The second argument is the number of Redis keys that the script will access. Our simple “Hello World” script doesn’t access any keys, so we use 0.


```
ubuntu@ip-172-31-25-81:~$ redis-cli --eval hello.lua
"Hello, world!"
```

## Example #3:


```
$ redis-cli
127.0.0.1:6379> rpush region:one count:emea count:usa count:atlantic
(integer) 3
127.0.0.1:6379> rpush region:two "count:usa"
(integer) 1
127.0.0.1:6379> exit
```

### Let us write a lua script:

```
~$ cat local.lua 
local count=0  
local broadcast=redis.call("lrange", KEYS[1], 0,-1)  
for _,key in ipairs(broadcast) do 
redis.call("INCR",key)
  count=count+1
end  
return count
```


```
ubuntu@ip-172-31-25-81:~$ redis-cli
127.0.0.1:6379> mget count:usa count:atlantic count:emea
1) "1"
2) "1"
3) "1"
127.0.0.1:6379>
```


