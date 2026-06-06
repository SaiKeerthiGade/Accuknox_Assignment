# Accuknox_Assignment

## Accuknox Django Trainee Assignment

This repository contains solutions for the Accuknox Django Trainee Assignment.

### Topics Covered

1. Django Signals

   * Synchronous execution
   * Thread behavior
   * Database transaction behavior

2. Custom Classes in Python

   * Rectangle class with iterator implementation

---

## Django Signals

### Question 1: Are Django signals synchronous or asynchronous by default?

**Answer:** Django signals are synchronous by default.

**Output:**

```text
Caller Thread ID : 2736

Signal Started

Signal Thread ID : 2736

Signal Completed

Request Completed in 5.01 seconds
```

**Conclusion:** The request waits until the signal completes, proving synchronous execution.

---

### Question 2: Do Django signals run in the same thread as the caller?

**Answer:** Yes.

**Output:**

```text
Caller Thread ID : 2736
Signal Thread ID : 2736
```

**Conclusion:** Both thread IDs are identical, proving the signal executes in the same thread as the caller.

---

### Question 3: Do Django signals run in the same database transaction as the caller?

**Answer:** Yes.

**Output:**

```text
Signal Started

Signal Thread ID: 7596

Signal sees record count = 22

Signal Completed

Object Created

Transaction Rolled Back
```

Browser Output:

```text
Final Database Count = 21
```

**Conclusion:** The signal could see uncommitted data before rollback, proving it executed in the same transaction context.

---

## Rectangle Class

```python
class Rectangle:

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}
```

### Example Output

```text
{'length': 10}
{'width': 5}
```

---

## Project Structure

```text
Accuknox_Assignment/
│
├── manage.py
├── README.md
├── config/
├── signals_app/
└── rectangle_app/
```

<img width="1631" height="971" alt="Screenshot 2026-06-06 082446" src="https://github.com/user-attachments/assets/243b4d91-fd70-4161-8b0f-0457027d822e" />

