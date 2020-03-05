
# Introduction to Lua Script

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
