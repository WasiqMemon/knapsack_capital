from project import *
import timeit
import matplotlib.pyplot as plt

def read_knapsack_data(file_name):
    with open(file_name, 'r') as file:
        # Read n and wmax from the first line
        n, wmax = map(int, file.readline().split())
        
        # Initialize lists to store values and weights
        values = []
        weights = []
        
        # Read each line containing vi and wi
        for _ in range(n):
            v, w = map(int, file.readline().split())
            values.append(v)
            weights.append(w)
        
        return values, weights, wmax

def measure_time(func, dataset):
    n = len(dataset[0])
    start_time = timeit.default_timer()
    func(dataset[2], dataset[1], dataset[0], n)
    return timeit.default_timer() - start_time

ns = [
    "f1_l-d_kp_10_269", 
    "f8_l-d_kp_23_10000", 
    "knapPI_2_100_1000_1", 
    "knapPI_1_200_1000_1", 
    "knapPI_1_500_1000_1",
    "knapPI_1_1000_1000_1", 
    "knapPI_1_2000_1000_1", 
    "knapPI_1_5000_1000_1",
    "knapPI_1_10000_1000_1"
] 
cn = [10, 23, 100, 200, 500, 1000, 2000, 5000, 10000]
times_bf = []
times_rec = []
times_dp = []
times_ga = []

data = []

for n in ns:
    values, weights, capacity = read_knapsack_data(n)
    data.append([values, weights, capacity])

for dataset in data: 
    time = measure_time(knapsack_brute_force_iter, dataset)
    times_bf.append(time)
    print("Brute Force", len(dataset[0]), time)

    time = measure_time(knapSack_Recursive, dataset)
    times_rec.append(time)
    print("Recursive", len(dataset[0]), time)

    time = measure_time(knapSackDP, dataset)
    times_dp.append(time)
    print("Dynamic", len(dataset[0]), time)

    time = measure_time(knapsack_greedy, dataset)
    times_ga.append(time)
    print("Greedy", len(dataset[0]), time)

plt.figure(figsize=(10, 6))
plt.plot(cn, times_rec, label='Recursive')
plt.plot(cn, times_dp, label='Dynamic')
plt.plot(cn, times_ga, label='Greedy')
plt.plot(cn, times_bf, label='Brute Force')
plt.ylim(0, 500)
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time (seconds)')
plt.title('Analysis of 0/1 Knapsack')
plt.legend()
plt.grid(True)
plt.savefig('knapsack_running_time.png')
plt.show()