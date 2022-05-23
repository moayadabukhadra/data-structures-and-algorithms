# Hashtables

Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

## Terminology:

1. Hash - A hash is the result of some algorithm taking an incoming string and converting it into a value that could be used for either security or some other purpose. In the case of a hashtable, it is used to determine the index of the array.

2. Buckets - A bucket is what is contained in each index of the array of the hashtable. Each index is a bucket. An index could potentially contain multiple key/value pairs if a collision occurs.

3. Collisions - A collision is what happens when more than one key gets hashed to the same location of the hashtable.

## methods

### 1. set

Arguments: key, value

Returns: nothing

This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.
time complexity: O(1)
space complexity: O(1)

### 2. get

Arguments: key
Returns: Value associated with that key in the table
BigO
time complexity: O(1)
space complexity: O(1)


### 2. contains

Arguments: key
Returns: Boolean, indicating if the key exists in the table already.
BigO
time complexity: O(1)
space complexity: O(1)


### 4. keys

Returns: Collection of keys
time complexity: O(N)
space complexity: O(1)


### 5. hash

Arguments: key
Returns: Index in the collection for that key
BigO
time complexity: O(1)
space complexity: O(1)




## repeated word

![whiteboard](../images/Untitled%20(14).jpg)

![whiteboard](../images/Untitled%20(16).jpg)

![whiteboard](../images/Untitled%20(17).jpg)


