# Redis as a Primary Datastore


## Task #1:

- Requirements

- Product details should include a name, a description, a vendor, a price, a main category and some images
- It needs to be possible to create/update/delete product details in a save way by taking the logical consistency of the catalouge into account (e.g. a product can not belong to a category which is not existent)
- Each object indeed needs to be accessible via its unique key
- It needs to be possible to retrieve a product by searching by its name or a part of its name
- Products can be listed by their main category

## Data model

### Product Image

Id : Number
Value : Binary

### Product

Id : Number
Name : String
Description: String
Vendor : String
Price : Number
Currency : String
MainCategory : Category (1)
Images : Image (0..n)

### Category

Id : Number
Name : String
Products : Product (0..n)

## Implementation

- Implement a simple product catalogue!

   - Use Python as the implementation language!
   - The result is a REST service, any UI is optional
   - Products are stored as HASHes
   - If necessary then a type has it's own counter item for the id generation
   - Implement the following ways to search by name
   - Perform a scan on a HASH index with a pattern
   - Use the Redisearch module
   - Implement the following way to search by category
   -  Perform a range 'query' by using ZRANGEBYSCORE
   
 <TBD>  
