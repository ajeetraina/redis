


# Demonstrating Redis TimeSeries running inside Docker Container



```
127.0.0.1:6379> TS.CREATE temperature:3:11 RETENTION 6000 LABELS sensor_id 2 area_id 32
OK
127.0.0.1:6379> TS.ADD temperature:3:11 1548149181 30
(integer) 1548149181
127.0.0.1:6379> TS.ADD temperature:3:11 1548149191 42
(integer) 1548149191
127.0.0.1:6379> TS.RANGE temperature:3:11 1548149180 1548149210 AGGREGATION avg 5
1) 1) (integer) 1548149180
   2) "30"
2) 1) (integer) 1548149190
   2) "42"
127.0.0.1:6379>
```
