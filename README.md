# You Don't Know Hash Tables

But after this, you will.

In this assignment, you will engage in a test-driven development process to implement a hash table that enables O(1) retrieval and storage
of key-value pairs. Your implementation will use a list-based (dynamic array) collection of k-v pairs to handle any key collisions. While retrieval
of values involving key collisions have a cost, the final tests that assert the time complexity use intentionally large hash tables, which result
in very large internal array sizes. This reduces the chance of key collisions in exchange for an increase in size.

## Run the Test Suite

`python3 -m unittest test_hash_table`

Open both *test_hash_table.py* and *hash_table.py* in your editor of choice. Modify the implementation in *hash_table.py* to pass the first test. Once it passes, create a commit. Then, uncomment the next test, and re-run the test suite. Implement what's necessary to pass the test, and then repeat this process.

**But wait!**

As you progress, you should be thinking about the algorithmic efficiency of each operation, and the data structures that your hash table uses.
What should be O(1)? What should be linear?

## Best Done in Pairs!

Get together with a colleague in front of just one machine, and take turns being the driver. Change drivers after each test is passed. Don't forget to commit after each test.

(c) 2019 Yong Joseph Bakos. All rights reserved.
