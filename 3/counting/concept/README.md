# Creating and Managing Strings

Keys that hold strings can only hold one value; you cannot store more than one string in a single key. However, strings in Redis are binary-safe, meaning a Redis string can hold any kind of data, from alphanumeric characters to JPEG images. The only limit is that strings must be 512 MB long or less.

To create a string, use the set command. For example, the following set command creates a key named key_Welcome1 that holds the string "Howdy":



### To set multiple strings in one command, use mset:

```
mset key_Welcome2 "there" key_Welcome3 "partners,"
```

### To set multiple strings in one command, use mset:

```
mset key_Welcome2 "there" key_Welcome3 "partners,"
```

You can also use the append command to create strings:

```
append key_Welcome4 "welcome to Texas"
```

If the string was created successfully, append will output an integer equal to how many characters the string includes:

```
(integer) 16
```

Note that append can also be used to change the contents of strings. 


## Retrieving Strings

To retrieve a string, use the get command:

```
get key_Welcome1
```

```
"Howdy"
```

## To retrieve multiple strings with one command, use mget:

```
mget key_Welcome1 key_Welcome2 key_Welcome3 key_Welcome4
```

```
1) "Howdy"
2) "there"
3) "partners,"
4) "welcome to Texas"
```

