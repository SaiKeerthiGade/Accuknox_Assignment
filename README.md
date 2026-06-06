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
Caller Thread ID : <same thread as signal>

Signal Started

Signal Thread ID : <same thread as caller>

Signal Completed

Request Completed in 5.01 seconds
```

**Conclusion:** The request waits until the signal completes, proving synchronous execution.

---

<img width="1631" height="971" alt="Screenshot 2026-06-06 082446" src="https://github.com/user-attachments/assets/9e7e0927-1d63-4d0f-bad3-e6c3037658ef" />


### Question 2: Do Django signals run in the same thread as the caller?

**Answer:** Yes.

**Output:**

```text
Caller Thread ID : <same thread as signal>
Signal Thread ID : <same thread as caller>
```

**Conclusion:** Both thread IDs are identical, proving the signal executes in the same thread as the caller.

---

### Question 3: Do Django signals run in the same database transaction as the caller?

**Answer:** Yes.

**Output:**

```text
Signal Started

Signal Thread ID: 7596

Signal sees record count = 24

Signal Completed

Object Created

Transaction Rolled Back
```

Browser Output:

```text
Final Database Count = 23
```

**Conclusion:** The signal could see uncommitted data before rollback, proving it executed in the same transaction context.

---

<img width="1606" height="958" alt="image" src="https://github.com/user-attachments/assets/5cbdf821-4d92-4ff5-95ee-7c110c9d3af3" />


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
<img width="1300" height="362" alt="image" src="https://github.com/user-attachments/assets/6d399400-4d6d-4f62-8034-3f0b2293ce57" />

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

## How to Run

1. Create a virtual environment

 python -m venv venv

2. Activate virtual environment

 venv\Scripts\activate

3. Install dependencies

 pip install -r requirements.txt

4. Run migrations

 python manage.py makemigrations
 python manage.py migrate

5. Start the server

 python manage.py runserver

