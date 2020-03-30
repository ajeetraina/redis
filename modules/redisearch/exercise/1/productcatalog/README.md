# Exercise #1:

Implement a simple product catalogue!
- Use Python as the implementation language!
- The result is a REST service, any UI is optional
- Products are stored as HASHes
- If necessary then a type has it's own counter item for the id generation
- Implement the following ways to search by name
  - Perform a scan on a HASH index with a pattern
  - Use the Redisearch module
- Implement the following way to search by category
  - Perform a range 'query' by using ZRANGEBYSCORE


## Requirement:


- Product details should include a name, a description, a vendor, a price, a main category and some images
- It needs to be possible to create/update/delete product details in a save way by taking the logical consistency of the catalogue into account (e.g. a product can not belong to a category which is not existent)
- Each object indeed needs to be accessible via its unique key
- It needs to be possible to retrieve a product by searching by its name or a part of its name
- Products can be listed by their main category

## Data Model


Product Image
- Id : Number
- Value : Binary
Product
- Id : Number
- Name : String
- Description: String
- Vendor : String
- Price : Number
- Currency : String
- MainCategory : Category (1)
- Images : Image (0..n)
Category
- Id : Number
- Name : String
- Products : Product (0..n)


Solution:

## Defining the Index - Category

```
> FT.CREATE category SCHEMA title TEXT WEIGHT 50 description TEXT product TEXT 
```


```
> FT.ADD category cat1 1.0 FIELDS title "Mobile" description "Range of Phones" product “Samsung”
```

```
> FT.ADD category cat2 1.0 FIELDS title "Laptop" description "Range of Laptops" product “Apple”
```

```
> FT.ADD category cat3 1.0 FIELDS title "TV" description "Range of TVs" product “Xiaomi”
```

## Defining the Index - Product

```
>  FT.CREATE products SCHEMA title TEXT WEIGHT 50 description TEXT vendor TEXT price NUMERIC currency TEXT catergory TEXT
```

```
> FT.ADD products prod1 1.0 FIELDS title "Macbook Pro 13 inch" description "14 Inch Brand New Apple Macbook Pro 2019 Model" vendor "Apple" price 1325 category cat2
```

```
> FT.ADD products prod2 1.0 FIELDS title "Samsung S7" description "Good Camera Quality" vendor "Samsung" price 325 category cat1
```

```
> FT.ADD products prod3 1.0 FIELDS title "Xiaomi" description "Big TV" vendor "Xiaomi" price 1325 category cat3
```


## Searching




## searching Products

```
127.0.0.1:6379> ft.search products "Apple"
1) (integer) 1
2) "prod1"
3)  1) "title"
    2) "Macbook Pro 13 inch"
    3) "description"
    4) "14 Inch Brand New Apple Macbook Pro 2019 Model"
    5) "vendor"
    6) "Apple"
    7) "price"
    8) "1325"
    9) "category"
   10) "cat2"
127.0.0.1:6379>
```

```
127.0.0.1:6379> ft.search products "Samsung"
1) (integer) 1
2) "prod2"
3)  1) "title"
    2) "Samsung S7"
    3) "description"
    4) "Good Camera Quality"
    5) "vendor"
    6) "Samsung"
    7) "price"
    8) "325"
    9) "category"
   10) "cat1"
```



