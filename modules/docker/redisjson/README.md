
# Demonstrating JSON on Redis running inside Docker container


```
127.0.0.1:6379> JSON.set player:42 . '{ "name":"viraj", "level":4, "hp":20, "gold":40, "race":"Elf" }'
OK
127.0.0.1:6379> JSON.GET player:42 name
"\"viraj\""
127.0.0.1:6379> JSON.GET player:42 level
"4"
127.0.0.1:6379> JSON.NUMINCRBY player:42 gold 80
"120"
127.0.0.1:6379> JSON.STRLEN player:42 race
(integer) 3
127.0.0.1:6379>
```
