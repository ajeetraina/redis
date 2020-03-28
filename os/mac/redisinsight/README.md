# Running RedisInsight inside Docker Container

## Pre-requisite

- Docker 18.03


```
docker run -v redisinsight:/db -p 8001:8001 redislabs/redisinsight
```

## Adding Hash Keys

- Click on "Add Key"
- Select Hash
- Enter 
   - key Name: users
   - Field: name
   - Value: Anil
 - Enter 
   - key Name: users
   - Field: email
   - Value: anil@gmail.com
 - Enter
   - key Name: users
   - Field: phone
   - Value: +51540853058

## FEtching Values

- Click on CLI option on the left hand side of RedisInsight
