# 📚 Arrays and Strings – Notes

Arrays and strings are among the most fundamental and commonly used data structures in computer science. They represent **ordered collections of elements**, making them ideal for a wide variety of problems — from simple iteration to complex algorithmic challenges.

---

## ✨ Why Arrays & Strings Matter

- ✅ Arrays and strings **appear in almost every coding interview** and competitive programming problem.
- ✅ Mastering these two structures builds a strong foundation for:
  - Sliding window techniques
  - Two-pointer strategies
  - In-place modifications
  - String manipulation tricks
- ✅ They help you **recognize common patterns** and improve your problem-solving speed.

---

## 🧵 Arrays in Python

In Python, arrays are usually represented using lists. Here's how to initialize them:

```python
my_list = []  # an empty list
```

## Key Characteristics:
- Python lists are dynamic - You do not need to define their size in advance
- They can store elements of any data types, including mix of types:

```python
example = [1, "two", 3.142, True]
```

- Lists are mutable - You can change and remove elements after creation.

---
## Some useful list methods:
- Below are some useful methods that will come in handy when dealing with lists in python:

| **Function**              | **Description**                              | **Example**                              |
|---------------------------|----------------------------------------------|------------------------------------------|
| `append(x)`               | Adds element `x` to the end                  | `arr.append(5)`                          |
| `pop(i)`                  | Removes and returns element at index `i`     | `arr.pop(2)`                             |
| `remove(x)`               | Removes the first occurrence of `x`          | `arr.remove(3)`                          |
| `insert(i, x)`            | Inserts `x` at index `i`                     | `arr.insert(1, 10)`                      |
| `sort()` / `sorted()`     | Sorts in place / returns sorted copy         | `arr.sort()` / `sorted(arr)`            |
| `reverse()`               | Reverses the list in place                   | `arr.reverse()`                          |
| `sum(arr)`                | Returns the sum of elements                  | `sum([1, 2, 3]) → 6`                     |
| `max(arr)` / `min(arr)`   | Returns the max/min value                    | `max(arr)` / `min(arr)`                 |
| `len(arr)`                | Returns number of elements                   | `len(arr)`                               |
| `arr[i:j]`                | Returns a slice from index `i` to `j`        | `arr[1:4]`                               |

###

---

## 🧵 Strings in Python
- Strings are a sequence of characters, defined using quotes:

```python
my_string = "Hello, World!"
```

### Key Characteristics:
- Strings are immutable in Python. Once a string is created, it cannot be changed.
- String methods like .replace() or .lower() do not modify the original string. They instead create a new string

---
## Some useful string methods:
- Below are some useful methods that will come in handy when dealing with lists in python:

| **Method**                    | **Description**                        | **Example**                                          |
|------------------------------|----------------------------------------|------------------------------------------------------|
| `split()`                    | Splits into list by delimiter          | `"a,b,c".split(',') → ['a','b','c']`                 |
| `join()`                     | Joins list into a string               | `",".join(['a','b']) → 'a,b'`                        |
| `strip()`                    | Removes leading/trailing spaces        | `"  hello  ".strip()`                                |
| `replace(old, new)`          | Replaces substrings                    | `"apple".replace("p", "b") → 'abble'`                |
| `lower()` / `upper()`        | Converts to lowercase / uppercase      | `"Hi".lower() → 'hi'`                                |
| `startswith()` / `endswith()`| Checks beginning/end of string         | `"file.txt".endswith(".txt")`                        |
| `in` keyword                 | Checks for substring presence          | `'a' in "apple" → True`                              |
| `len(s)`                     | Returns string length                  | `len("hello") → 5`                                   |

###
---

# ⏱️ Time Complexity of Common Operations:

| **Operation**                    | **Array/List** | **String** |
|----------------------------------|----------------|------------|
| Appending from end               | O(1)           | O(n)       |
| Popping from end                 | O(1)           | O(n)       |
| Inserting at beginning/middle    | O(n)           | O(n)       |
| Deleting from beginning/middle   | O(n)           | O(n)       |
| Access by index                  | O(1)           | O(1)       |
| Updating by index                | O(1)           | O(n)       |
| Searching for element (`in`)     | O(n)           | O(n)       |
| Iterating over all elements      | O(n)           | O(n)       |
| Sorting                          | O(n log n)     | ❌ Not supported directly       |
| Concatenation (`+`)              | O(n)           | O(n)       |
| Slicing                          | O(k)           | O(k)       |

