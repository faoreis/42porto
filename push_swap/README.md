*This project has been created as part of the 42 curriculum by faribeir.*

# push_swap

## Description

An optimized sorting algorithm implemented in C, using two stacks and constrained operations to achieve minimal instruction count.

---

## Objective

- Sort a list of integers
- Use only the allowed operations
- Minimize the number of moves
- Ensure good performance for large inputs (100 / 500 numbers)

---

## How it works

The program uses two stacks:

- Stack A: contains the initial numbers
- Stack B: auxiliary stack used during sorting

---

## Allowed operations

| Operation | Description                              |
|----------|------------------------------------------|
| sa       | swap the first two elements of A         |
| sb       | swap the first two elements of B         |
| ss       | swap both stacks                         |
| pa       | push from B to A                         |
| pb       | push from A to B                         |
| ra       | rotate A (first element goes to the end) |
| rb       | rotate B                                 |
| rr       | rotate both stacks                       |
| rra      | reverse rotate A                         |
| rrb      | reverse rotate B                         |
| rrr      | reverse rotate both stacks               |

---

## Sorting strategy

### 1. Indexing

All values are converted into sorted indices to simplify comparisons.

```
Input: 40 10 30 20
Index:  3  0  2  1
Sorted: 10 20 30 40
Index:   0  1  2  3
```
---

### 2. Small inputs

- 2 numbers: swap if needed
- 3 numbers: handled with `sort_3`
- 4-5 numbers: handled with `sort_5`

Strategy for 5 elements:
1. Find the smallest value
2. Push it to stack B
3. Repeat until 3 elements remain
4. Sort the remaining 3 elements
5. Push everything back to stack A

---

### 3. Large inputs (chunk-based algorithm)

For larger inputs, the program uses a chunk-based approach.

#### Phase 1: Push to B

- Split the data into chunks
- Push elements from A to B using `pb`
- Use rotations (`rb`) to partially organize stack B

#### Phase 2: Push back to A

- Find the largest element in B
- Rotate B (`rb` or `rrb`) to bring it to the top
- Push it back to A using `pa`

---

## Instructions

### Compile

```
Make
```

### Run

```
./push_swap "5 4 3 2 1"
```

---


## Resources

- 42 subject (push_swap)
- Linked list documentation (C)
- Sorting algorithms overview (Quicksort, Radix)
