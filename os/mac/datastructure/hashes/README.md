# Demonstrating Hashes



Redis hashes data structure contains field-value pairs


```                                      
HMSET hmset user:1000     username      antirez    birthyear      1977      verified      1
                           <field>      <value>   <field>        <value>     <field>     <value>
```


Note: You might notice above that  the key “user:1000” this way we can simulate a table name + PK in the single key. This is just like any other key and can be used anywhere in Redis. 

## API
  - HMSET
  - HGET 
  - HMGET 
      - Is similar to HGET but might returns  an array of values
