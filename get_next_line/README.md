# Get_next_line

*This project has been created as part of the 42 curriculum by faribeir.*


## Description

'Get_next_line' is a function capable of reading a file line by line from a file descriptor. It returns each line one at a time, including the newline character when present, and continues reading from where it left off on the previous call. The function handles memory allocation internally and ensures efficient reading based on a defined buffer size.

### Function Prototype

The prototype of the function is:

```c
char *get_next_line(int fd);
```

## Instructions

To use `get_next_line`, follow these steps:

### 1. Clone the repository

```
git clone https://github.com/faoreis/42porto.git
```

```
cd get_next_line
```

### 2. Compile the library

```
make
```

### 3. clean compiled files

```
make clean

make fclean

make re
```

### 4. Usage

```
#include "get_next_line.h"
```

# Tester

To ensure the correctness and robustness of get_next_line, this project was tested using Francinette.

Link tester:
``` link 
https://github.com/xicodomingues/francinette?tab=readme-ov-file
```
