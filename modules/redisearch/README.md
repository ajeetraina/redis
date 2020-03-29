# Installing RediSearch

## Infra

- MacOS


## Cloning the RediSearch

```
ajeetraina@Ajeet-Rainas-Macbook-Pro ~ % git clone --recursive https://github.com/RediSearch/RediSearch.git
Cloning into 'RediSearch'...
remote: Enumerating objects: 185, done.
remote: Counting objects: 100% (185/185), done.
remote: Compressing objects: 100% (138/138), done.
remote: Total 25141 (delta 109), reused 77 (delta 47), pack-reused 24956
Receiving objects: 100% (25141/25141), 17.12 MiB | 2.99 MiB/s, done.
Resolving deltas: 100% (18167/18167), done.
Submodule 'deps/readies' (https://github.com/RedisLabsModules/readies.git) registered for path 'deps/readies'
Cloning into '/Users/ajeetraina/RediSearch/deps/readies'...
remote: Enumerating objects: 175, done.        
remote: Counting objects: 100% (175/175), done.        
remote: Compressing objects: 100% (131/131), done.        
remote: Total 481 (delta 98), reused 102 (delta 43), pack-reused 306        
Receiving objects: 100% (481/481), 92.71 KiB | 310.00 KiB/s, done.
Resolving deltas: 100% (262/262), done.
Submodule path 'deps/readies': checked out 'a3b8dab21db25d599feb40713ccf8df2094fdda6'
ajeetraina@Ajeet-Rainas-Macbook-Pro ~ % 
```

## Installing Pre-requisite

```
cd RediSearch
./system-setup.py
make build
```

```
[ 98%] Building C object CMakeFiles/rscore.dir/src/util/quantile.c.o
[ 98%] Building C object CMakeFiles/rscore.dir/src/value.c.o
[ 99%] Building C object CMakeFiles/rscore.dir/src/varint.c.o
1 warning generated.
[ 99%] Built target rscore
Scanning dependencies of target redisearch
[ 99%] Building C object CMakeFiles/redisearch.dir/src/module-init/module-init.c.o
[100%] Linking C shared library redisearch.so
ld: warning: directory not found for option '-L/usr/local/Cellar/zlib/1.2.11/lib'
[100%] Built target redisearch
cp build/redisearch.so src/redisearch.so
```

```
ajeetraina@Ajeet-Rainas-Macbook-Pro RediSearch % make run 
Makefile:98: warning: overriding commands for target `clean'
deps/readies/mk/build.rules:17: warning: ignoring old commands for target `clean'
8188:C 29 Mar 2020 02:01:57.670 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
8188:C 29 Mar 2020 02:01:57.670 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=8188, just started
8188:C 29 Mar 2020 02:01:57.670 # Configuration loaded
8188:M 29 Mar 2020 02:01:57.671 * Increased maximum number of open files to 10032 (it was originally set to 2560).
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 5.0.7 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 8188
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

8188:M 29 Mar 2020 02:01:57.671 # Server initialized
8188:M 29 Mar 2020 02:01:58.046 * <ft> RediSearch version 99.99.99 (Git=v1.6.6-49-g331636b2)
8188:M 29 Mar 2020 02:01:58.046 * <ft> Low level api version 1 initialized successfully
8188:M 29 Mar 2020 02:01:58.046 * <ft> concurrent writes: OFF, gc: ON, prefix min length: 2, prefix max expansions: 200, query timeout (ms): 500, timeout policy: return, cursor read size: 1000, cursor max idle (ms): 300000, max doctable size: 1000000, search pool size: 20, index pool size: 8, 
8188:M 29 Mar 2020 02:01:58.046 * <ft> Initialized thread pool!
8188:M 29 Mar 2020 02:01:58.047 * Module 'ft' loaded from src/redisearch.so
8188:M 29 Mar 2020 02:01:58.047 * Ready to accept connections
```

```
127.0.0.1:6379> module list
1) 1) "name"
   2) "ft"
   3) "ver"
   4) (integer) 999999
127.0.0.1:6379> 
```

# Example:

Let us start adding document to RediSearch.

## Create Index with fields

```
FT.create myindex schema title TEXT weight 5.0 body TEXT url TEXT
```

## Syntax:

```
FT.CREATE idx SCHEMA name TEXT SORTABLE age NUMERIC SORTABLE myTag TAG SORTABLE
```

- index: the index name to create. If it exists the old spec will be overwritten
- SCHEMA {field} {options...}: After the SCHEMA keyword we define the index fields. They can be numeric, textual or geographical. For textual fields we optionally specify a weight. The default weight is 1.0.
- WEIGHT {weight}
For TEXT fields, declares the importance of this field when calculating result accuracy. This is a multiplication factor, and defaults to 1 if not specified.


## Adding documents to Index

```
FT.add myindex doc1 1.0 fields title “Collabnix” collabnix “My Personal Website” URL “http://www.collabnix.com“
```

## Syntax

Format¶

```
FT.ADD {index} {docId} {score} 
  [NOSAVE]
  [REPLACE [PARTIAL] [NOCREATE]]
  [LANGUAGE {language}] 
  [PAYLOAD {payload}]
  [IF {condition}]
  FIELDS {field} {value} [{field} {value}...]
```


## Parameters

```
index: The Fulltext index name. The index must be first created with FT.CREATE
docId: The document's id that will be returned from searches.
score: The document's rank based on the user's ranking. This must be between 0.0 and 1.0. If you don't have a score just set it to 1
FIELDS: Following the FIELDS specifier, we are looking for pairs of {field} {value} to be indexed. Each field will be scored based on the index spec given in FT.CREATE. Passing fields that are not in the index spec will make them be stored as part of the document, or ignored if NOSAVE is set
```

FT.ADD will actually create a hash in Redis with the given fields and value. This means that if the hash already exists, it will override with the new values. Moreover, if you try to add a document with the same id to two different indexes one of them will override the other and you will get wrong responses from one of the indexes. For this reason, it is recommended to create global unique documents ids (this can e.g. be achieved by adding the index name to the document id as prefix).

## Redisearch


```
ft.search myindex “hello world” limit 0 10
```

This will tell RediSearch to intersect the lists of documents for each term and return all documents containing the two terms. Of course, more complex queries can be performed, and the full syntax of the query language is detailed below.

```
ft.search myindex “collabnix” limit 0 10
```

```
127.0.0.1:6379> ft.search myindex “collabnix” limit 0 10
1) (integer) 1
2) "doc1"
3) 1) "title"
   2) "\xe2\x80\x9cCollabnix\xe2\x80\x9d"
   3) "collabnix"
   4) "\xe2\x80\x9cMy"
   5) "Personal"
   6) "Website\xe2\x80\x9d"
   7) "URL"
   8) "\xe2\x80\x9chttp://www.collabnix.com\xe2\x80\x9c"

```


## Dropping an Index

```
ft.drop myindex
```


# FAQs

## What type of Data structures does RediSearch uses?

RediSearch uses its own custom data structures and uses Redis' native structures only for storing the actual document content (using Hash objects).

Using specialized data structures allows faster searches and more memory effective storage of index records, utilizing compression techniques like delta encoding.

These are the data structures RediSearch uses under the hood:

## Index and document metadata¶

For each search index, there is a root data structure containing the schema, statistics, etc - but most importantly, little compact metadata about each document indexed.

Internally, inside the index, RediSearch uses delta encoded lists of numeric, incremental, 32-bit document ids. This means that the user given keys or ids for documents, need to be replaced with the internal ids on indexing, and back to the original ids on search.

For that, RediSearch saves two tables, mapping the two kinds of ids in two ways (one table uses a compact trie, the other is simply an array where the internal document ID is the array index). On top of that, for each document, we store its user given a priory score, some status bits, and an optional "payload" attached to the document by the user.

Accessing the document metadata table is an order of magnitude faster than accessing the hash object where the document is actually saved, so scoring functions that need to access metadata about the document can operate fast enough.

## Inverted index

For each term appearing in at least one document, we keep an inverted index, basically a list of all the documents where this term appears. The list is compressed using delta coding, and the document ids are always incrementing.

When the user indexes the documents "foo", "bar" and "baz" for example, they are assigned incrementing ids, For example 1025, 1045, 1080. When encoding them into the index, we only encode the first ID, followed by the deltas between each entry and the previous one, in this case, 1025, 20, 35.

Using variable-width encoding, we can use one byte to express numbers under 255, two bytes for numbers between 256 and 16383 and so on. This can compress the index by up to 75%.

On top of the ids, we save the frequency of each term in each document, a bit mask representing the fields in which the term appeared in the document, and a list of the positions in which the term appeared.

The structure of the default search record is as follows. Usually, all the entries are one byte long:


+----------------+------------+------------------+-------------+------------------------+
|  docId_delta   |  frequency | field mask       | offsets len | offset, offset, ....   |
|  (1-4 bytes)   | (1-2 bytes)| (1-16 bytes)     |  (1-2 bytes)| (1-2 bytes per offset) |
+----------------+------------+------------------+-------------+------------------------+
Optionally, we can choose not to save any one of those attributes besides the ID, degrading the features available to the engine.

## Numeric index

Numeric properties are indexed in a special data structure that enables filtering by numeric ranges in an efficient way. One could view a numeric value as a term operating just like an inverted index. For example, all the products with the price $100 are in a specific list, that is intersected with the rest of the query (see Query Execution Engine).

However, in order to filer by a range of prices, we would have to intersect the query with all the distinct prices within that range - or perform a union query. If the range has many values in it, this becomes highly inefficient.

To avoid that, we group numeric entries with close values together, in a single "range node". These nodes are stored in binary range tree, that allows the engine to select the relevant nodes and union them together. Each entry in a range node contains a document Id, and the actual numeric value for that document. To further optimize, the tree uses an adaptive algorithm to try to merge as many nodes as possible within the same range node.

## Tag index

Tag indexes are similar to full-text indexes, but use simpler tokenization and encoding in the index. The values in these fields cannot be accessed by general field-less search and can be used only with a special syntax.

The main differences between tag fields and full-text fields are:

An entire tag field index resides in a single Redis key and doesn't have a key per term as the full-text one.

The tokenization is simpler: The user can determine a separator (defaults to a comma) for multiple tags, and we only do whitespace trimming at the end of tags. Thus, tags can contain spaces, punctuation marks, accents, etc. The only two transformations we perform are lower-casing (for latin languages only as of now), and whitespace trimming.

Tags cannot be found from a general full-text search. If a document has a field called "tags" with the values "foo" and "bar", searching for foo or bar without a special tag modifier (see below) will not return this document.

The index is much simpler and more compressed: we only store document ids in the index, usually resulting in 1-2 bytes per index entry.

## Geo index

Geo indexes utilize Redis' own geo-indexing capabilities. In query time, the geographical part of the query (a radius filter) is sent to Redis, returning only the ids of documents that are within that radius.

#Auto-complete

The auto-complete engine (see below for a fuller description) utilizes a compact trie or prefix tree, to encode terms and search them by prefix.

