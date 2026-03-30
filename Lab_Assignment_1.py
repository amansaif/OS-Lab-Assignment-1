# CPU Scheduling: FCFS & SJF (Non-Preemptive)

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0


# -------------------- INPUT --------------------
def take_input():
    processes = []
    n = int(input("Enter number of processes: "))

    for i in range(n):
        print(f"\nEnter details for Process {i+1}")
        pid = input("Process ID: ")
        at = int(input("Arrival Time: "))
        bt = int(input("Burst Time: "))
        processes.append(Process(pid, at, bt))

    return processes


# -------------------- DISPLAY --------------------
def display(processes, title):
    print(f"\n{title}")
    print("PID\tAT\tBT\tCT\tTAT\tWT")

    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")


# -------------------- FCFS --------------------
def fcfs(processes):
    processes.sort(key=lambda x: x.at)
    time = 0
    gantt = []

    for p in processes:
        if time < p.at:
            time = p.at

        start = time
        time += p.bt

        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        gantt.append((p.pid, start, time))

    return gantt


# -------------------- SJF --------------------
def sjf(processes):
    n = len(processes)
    completed = 0
    time = 0
    visited = [False] * n
    gantt = []

    while completed < n:
        idx = -1
        min_bt = float('inf')

        for i in range(n):
            if processes[i].at <= time and not visited[i]:
                if processes[i].bt < min_bt:
                    min_bt = processes[i].bt
                    idx = i

        if idx == -1:
            time += 1
            continue

        p = processes[idx]
        start = time
        time += p.bt

        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        visited[idx] = True
        completed += 1

        gantt.append((p.pid, start, time))

    return gantt


# -------------------- GANTT CHART --------------------
def print_gantt(gantt, title):
    print(f"\n{title} Gantt Chart:")

    for pid, start, end in gantt:
        print(f"| {pid} ", end="")
    print("|")

    print("0", end="")
    for pid, start, end in gantt:
        print(f"    {end}", end="")
    print()


# -------------------- AVERAGES --------------------
def calculate_avg(processes):
    total_wt = sum(p.wt for p in processes)
    total_tat = sum(p.tat for p in processes)

    print(f"\nAverage Waiting Time = {total_wt / len(processes):.2f}")
    print(f"Average Turnaround Time = {total_tat / len(processes):.2f}")


# -------------------- MAIN --------------------
import copy

processes = take_input()

# Show Input Table
print("\nInitial Process Table:")
print("PID\tAT\tBT")
for p in processes:
    print(f"{p.pid}\t{p.at}\t{p.bt}")

# FCFS
fcfs_processes = copy.deepcopy(processes)
fcfs_gantt = fcfs(fcfs_processes)

display(fcfs_processes, "FCFS Result")
print_gantt(fcfs_gantt, "FCFS")
calculate_avg(fcfs_processes)

# SJF
sjf_processes = copy.deepcopy(processes)
sjf_gantt = sjf(sjf_processes)

display(sjf_processes, "SJF Result")
print_gantt(sjf_gantt, "SJF")
calculate_avg(sjf_processes)