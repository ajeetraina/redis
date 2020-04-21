```
ajeet_raina_redislabs_com@ajeet-demo-migtest1:~$ redis-cli -p 12000
127.0.0.1:12000> MULTI
(error) NOAUTH Authentication required
127.0.0.1:12000> auth redis12#
OK
127.0.0.1:12000> MULTI
OK
127.0.0.1:12000> SET "key1" "value1"
QUEUED
127.0.0.1:12000> SET "key2" "value2"
(error) CROSSSLOT Keys in request don't hash to the same slot (context='within MULTI', command='SET', original-slot='9189', wrong-slot='4998', first-
key='key1', violating-key='key2')
127.0.0.1:12000> EXEC
(error) EXECABORT Transaction discarded because of previous errors.
127.0.0.1:12000> MULTI
OK
127.0.0.1:12000> INCRBY "counter" 1
QUEUED
127.0.0.1:12000> INCRBY "counter" 1
QUEUED
127.0.0.1:12000> INCRBY "counter" 1
QUEUED
127.0.0.1:12000> INCRBY "counter" -1
QUEUED
127.0.0.1:12000> EXEC
1) (integer) 1
2) (integer) 2
3) (integer) 3
4) (integer) 2
127.0.0.1:12000> get counter
"2"
127.0.0.1:12000> MULTI
OK
127.0.0.1:12000> HSET "user:dmaier" "first_name" "David"
QUEUED
127.0.0.1:12000> HSET "user:dmaier" "last_name" "Maier"
QUEUED
127.0.0.1:12000> EXEC
1) (integer) 1
2) (integer) 1
127.0.0.1:12000>
```
