def knapsack_brute_force_iter(capacity, weights, values, n):
    
    # Initialize a variable to store the maximum value
    max_value = 0
    
    # Generate all possible combinations using bitwise operations
    for i in range(2**n):
        current_value = 0
        current_weight = 0
        
        # Check each bit in the binary representation of i
        for j in range(n):
            if (i >> j) & 1:
                current_value += values[j]
                current_weight += weights[j]
        
        # Check if the current combination is feasible and update max_value
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
    
    return max_value

def knapSack_Recursive(W, wt, val, n):
    # initial conditions
    if n == 0 or W == 0 :
       return 0
    # If weight is higher than capacity then it is not included
    if (wt[n-1] > W):
       return knapSack_Recursive(W, wt, val, n-1)
    # return either nth item being included or not
    else:
       return max(val[n-1] + knapSack_Recursive(W-wt[n-1], wt, val, n-1),
          knapSack_Recursive(W, wt, val, n-1))
    
def knapSackDP(W, wt, val, n):
  K = [[0 for x in range(W + 1)] for x in range(n + 1)]
  # Build tаble K[][] in bоttоm uр mаnner
  for i in range(n + 1):
      for w in range(W + 1):
          if i == 0  or  w == 0:
              K[i][w] = 0
          elif wt[i-1] <= w:
              K[i][w] = max(val[i-1]
                        + K[i-1][w-wt[i-1]],
                            K[i-1][w])
          else:
              K[i][w] = K[i-1][w]
  return K[n][W]

def knapsack_greedy(capacity, weights, values, n):
    # Calculate value-to-weight ratios
    ratios = [(v / w, v, w) for v, w in zip(values, weights)]
    
    # Sort items based on ratios in decreasing order
    ratios.sort(reverse=True)
    
    total_value = 0
    knapsack = []
    
    for ratio, v, w in ratios:
        if capacity >= w:
            knapsack.append((v, w))
            total_value += v
            capacity -= w
            
    return total_value