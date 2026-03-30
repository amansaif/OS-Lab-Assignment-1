# 🧠 CPU Scheduling — FCFS & SJF

### OS Lab Assignment 1 | ENCA252

**BCA (AI & Data Science) | K.R. Mangalam University, Gurugram**

---

## 📌 Problem Statement

CPU Scheduling determines the order in which processes are executed by the CPU.
This project implements:

* **FCFS (First Come First Serve)**
* **SJF (Shortest Job First - Non-Preemptive)**

and evaluates their performance using CT, TAT, and WT.

---

## 🎯 Objectives

* Understand CPU scheduling concepts
* Implement FCFS and SJF algorithms
* Calculate CT, TAT, WT
* Compare performance of both algorithms

---

## 🗂️ File Structure

```bash
OS-Lab-Assignment-1/
│
├── Screenshot/                         # Output screenshots
├── FOS Lab Assignment 1 Question.pdf   # Assignment questions
├── Lab_Assignment_1.py                 # Main Python code
├── OS_Lab Assignment_1.pdf             # Final report
└── README.md
```

---

## 📚 Concepts Used

| Term                  | Formula  | Description                    |
| --------------------- | -------- | ------------------------------ |
| Completion Time (CT)  | —        | Time at which process finishes |
| Turnaround Time (TAT) | CT − AT  | Total execution time           |
| Waiting Time (WT)     | TAT − BT | Waiting time in queue          |
| Arrival Time (AT)     | —        | Process arrival                |
| Burst Time (BT)       | —        | CPU execution time             |

---

## ▶️ How to Run

Make sure Python 3.x is installed.

```bash
python Lab_Assignment_1.py
```

---

## 🧪 Sample Input Used

| PID | AT | BT |
| --- | -- | -- |
| A   | 0  | 7  |
| B   | 2  | 4  |
| C   | 4  | 1  |
| D   | 5  | 4  |
| E   | 6  | 6  |

---

## 📊 Sample Output

### 🔵 FCFS Result

```
PID   AT   BT   CT   TAT   WT
A     0    7    7     7     0
B     2    4   11     9     5
C     4    1   12     8     7
D     5    4   16    11     7
E     6    6   22    16    10
```

---

### 🟢 SJF Result

```
PID   AT   BT   CT   TAT   WT
A     0    7    7     7     0
C     4    1    8     4     3
B     2    4   12    10     6
D     5    4   16    11     7
E     6    6   22    16    10
```

---

## 📈 Performance Comparison

| Algorithm | Avg WT | Avg TAT | Observation            |
| --------- | ------ | ------- | ---------------------- |
| FCFS      | Higher | Higher  | Simple but inefficient |
| SJF       | Lower  | Lower   | Better performance     |

---

## 🔍 Result Analysis

SJF performs better than FCFS because it executes shorter processes first, reducing average waiting time.

---

## 📸 Output Screenshots

(Screenshots are available in the `Screenshot/` folder)

---

## 🛠️ Tools & Technologies

* Python 3.x
* VS Code
* Windows OS

---

## 👨‍💻 Submitted By

| Detail         | Info                           |
| -------------- | ------------------------------ |
| **Name**       | Mohd Aman                      |
| **Program**    | BCA (AI & Data Science)        |
| **Course**     | Operating System Lab (ENCA252) |
| **University** | K.R. Mangalam University       |

---
