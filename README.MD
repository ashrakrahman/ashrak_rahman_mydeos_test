## QUESTION C: Implemetation of Geo Distributed LRU (Least Recently Used) cache with time expiration.

Workflows:

- lru_cache.py is a python library built Doubly Link List and a simple hash dictionary. The LRUCache class has following methods:

  1. insert({key,value}) to add a key value pair into cache
  2. get({key}) to get any key from cache. If not found in cache read from DB and insert into cache
  3. get_list() / get_cache() to get current items from nodes / cache
  4. evict_expired_entries to clear all expired cache entry. This will call only when get_list() is called. This can be customised as per the requirements.

- server.py is simple Flask server running on localhost post 5000. This server exposes the following endpoints (postman collection inclued):

  ```
  1. http://127.0.0.1:5000/insert - POST
  2. http://127.0.0.1:5000/get?key={key_id} - GET
  3. http://127.0.0.1:5000/get_list - GET

  ```
