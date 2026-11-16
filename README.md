
A menu-driven console application written in Python 3. It lets you add students, mark daily attendance as present or absent, view each student's attendance percentage, and list the students who are below the 75% requirement. All data is saved to a file.

## Features

- Add a student with a unique roll number and a name
- Mark attendance as Present (P) or Absent (A)
- View a student's attendance percentage
- List students below the 75% minimum (and show those who meet it)
- Load data from `attendance.txt` at start and save it after every change
- Input validation, including protection against dividing by zero when no classes have been held

## Concepts Used

Lists, dictionaries, functions, and file handling.

## Requirements

- Python 3.6 or later
- No external libraries

## How to Run

```bash
python attendance_manager.py
```

## Menu

```
1. Add student
2. Mark attendance
3. Show attendance percentage
4. Shortage list (below 75%)
5. Exit
```

## Data Storage

Each student is a dictionary stored in a list:

```python
{"roll": 101, "name": "Aman", "held": 4, "attended": 3}
```

Records are saved in `attendance.txt`, one student per line in the format `roll|name|held|attended`:

```
101|Aman|4|3
102|Riya|4|2
```

The file is created automatically on the first save. If it is missing at start, the program begins with no records.

## Test Cases

| # | Scenario | Input | Expected Output |
|---|----------|-------|-----------------|
| 1 | Normal input | Option 1, Roll `101`, Name `Aman` | `Student added: 101 \| Aman \| Held: 0 \| Attended: 0` |
| 2 | Boundary / minimum input | Student 101 has no classes held; option 3, Roll `101` | `Aman: Attendance 0.00% (no classes held yet)` |
| 3a | Invalid input (roll) | Option 2, Roll `999` | `Roll number 999 not found.` |
| 3b | Invalid input (status) | Option 2, Roll `101`, Status `X` | `Invalid status. Enter P or A.` |
| 4 | Different valid scenario | 101 Aman (4 held, 3 attended), 102 Riya (4 held, 2 attended); option 4 | `Below 75%: 102 \| Riya \| 50.00%` and `Aman (75.00%) meets the requirement.` |

Test cases run in order on the same records.

## Sample Session

```
===== Student Attendance Manager =====
1. Add student
2. Mark attendance
3. Show attendance percentage
4. Shortage list (below 75%)
5. Exit
Choose an option: 1
Roll: 101
Name: Aman
Student added: 101 | Aman | Held: 0 | Attended: 0
```

## Notes

- Each time attendance is marked, one class is counted as held for that student, so mark every student once per class day.
- Students with no classes held yet are left out of the shortage list.
- Roll numbers must be whole numbers and must be unique.

## Project Structure

```
.
├── attendance_manager.py   # main program
├── attendance.txt          # data file (created automatically)
└── README.md
```
