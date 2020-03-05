# Concept

## What is Redis Keyspace?


- Redis' keyspace is the equivalent of a schema in other databases, and is essentially a dictionary (lookup table/associative array/hashmap) for keys' values. It is considered a "schemaless" model, 
although there are two schemas in play:

- The key-value schema, i.e. a "table" of keys and their respective values
- The implicit schema, or how keys are named, which basically dictates how keys are accessed

Redis keys are pairs made of names and values. 
The name is unique, and can be any valid Redis String (binary safe, up to 0.5GB). 
The value can be any one of Redis' core or module data types. 
All keys (and pointers to their values) are stored in the server's global dictionary, a.k.a the keyspace.

## Redis is not a plain key-value store

Redis is not a plain key-value store, it is actually a data structures server, supporting different kinds of values. 
What this means is that, while in traditional key-value stores you associate string keys to string values, in Redis the 
value is not limited to a simple string, but can also hold more complex data structures. 

List of all the data structures supported by Redis:

- Binary-safe strings.
- Lists: collections of string elements sorted according to the order of insertion. They are basically linked lists.
- Sets: collections of unique, unsorted string elements.
- Sorted sets, similar to Sets but where every string element is associated to a floating number value, called score. The elements are always taken sorted by their score, so unlike Sets it is possible to retrieve a range of elements (for example you may ask: give me the top 10, or the bottom 10).
- Hashes, which are maps composed of fields associated with values. Both the field and the value are strings. This is very similar to Ruby or Python hashes.
- Bit arrays (or simply bitmaps): it is possible, using special commands, to handle String values like an array of bits: you can set and clear individual bits, count all the bits set to 1, find the first set or unset bit, and so forth.
- HyperLogLogs: this is a probabilistic data structure which is used in order to estimate the cardinality of a set. Don't be scared, it is simpler than it seems... See later in the HyperLogLog section of this tutorial.
- Streams: append-only collections of map-like entries that provide an abstract log data type. 


## Redis keys

- Redis keys are binary safe, this means that you can use any binary sequence as a key, from a string like "foo" to the content of a JPEG file. The empty string is also a valid key.

A few other rules about keys:

- Very long keys are not a good idea. For instance a key of 1024 bytes is a bad idea not only memory-wise, but also because the lookup of the key in the dataset may require several costly key-comparisons. Even when the task at hand is to match the existence of a large value, hashing it (for example with SHA1) is a better idea, especially from the perspective of memory and bandwidth.
- Very short keys are often not a good idea. There is little point in writing "u1000flw" as a key if you can instead write "user:1000:followers". The latter is more readable and the added space is minor compared to the space used by the key object itself and the value object. While short keys will obviously consume a bit less memory, your job is to find the right balance.
- Try to stick with a schema. For instance "object-type:id" is a good idea, as in "user:1000". Dots or dashes are often used for multi-word fields, as in "comment:1234:reply.to" or "comment:1234:reply-to".
- The maximum allowed key size is 512 MB.

## Redis Strings

- The Redis String type is the simplest type of value you can associate with a Redis key. 
- It is the only data type in Memcached, so it is also very natural for newcomers to use it in Redis.
- Since Redis keys are strings, when we use the string type as a value too, we are mapping a string to another string. The string data type is useful for a number of use cases, like caching HTML fragments or pages.

Let's play a bit with the string type, using redis-cli (all the examples will be performed via redis-cli in this tutorial).

```
> set mykey somevalue
OK
> get mykey
"somevalue"
```

As you can see using the SET and the GET commands are the way we set and retrieve a string value. 
Note that SET will replace any existing value already stored into the key, in the case that the key already exists, 
even if the key is associated with a non-string value. So SET performs an assignment


