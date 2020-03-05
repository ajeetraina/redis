## Counting with Strings

### Why does Redis have so many commands for manipulating numbers? Is there a redundancy you can identify?


- Counters are widespread in all applications
- They are usually monotonously growing, so make sure they can accomodate their maximal expected value. Example: a 64-bit counter can be incremented a million times a second for a million years without overflowing.
- An application that decrements counters should also be able to deal with negative counter values.

- INCR URL
- DECR URL
- INCRBY URL
- DECRBY URL
- INCRBYFLOAT URL
- DECRBYFLOAT URL
- HINCRBY URL
- HINCRBYFLOAT URL
- ZADD's INCR subcommand URL
- BITCOUNT URL
- BITFIELD URL
- PFCOUNT URL
- PFADD URL



