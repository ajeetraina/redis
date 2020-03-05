## Counting with Strings

### Exercise #1.0 - Why does Redis have so many commands for manipulating numbers? Is there a redundancy you can identify?


Refer [this](https://github.com/ajeetraina/redis/blob/master/3/counting/concept/README.md) link

### Exercise #1.1 - Counting with Sorted Sets

Script in Lua the equivalents of ZINCRBY and ZINCRBYFLOAT


Before you begin with lua script, let us get familiar with two important stuffs:

- Sorted Sets
- Lua Script

For Sorted Sets, refer [this](https://github.com/ajeetraina/redis/blob/master/3/counting/sorted-sets/README.md) link
  




##### What is Lua Script?

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






## ZINCRBY

- Increments the score of member in the sorted set stored at key by increment. 
- If member does not exist in the sorted set, it is added with increment as its score (as if its previous score was 0.0). 
- If key does not exist, a new sorted set with the specified member as its sole member is created.
- An error is returned when key exists but does not hold a sorted set.
- The score value should be the string representation of a numeric value, and accepts double precision floating point numbers. - It is possible to provide a negative value to decrement the score.
