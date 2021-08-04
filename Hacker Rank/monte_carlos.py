import random

def coin_toss():
    x = random.uniform(0, 1)
     
    if x > 0.5:
        # Heads for True
        return True
    else:
        # Tails for False
        return False

prob = []
 
# Make 1000 experiments
for i in range(1000):
     
    # Each experiment have 10 coin tosses
    N = 10
    results = []
 
    # Toss the coin 10 times and store that in a list
    for i in range(N):
        result = coin_toss()
        results.append(result)
 
    n_heads = sum(results)
    p_heads = n_heads/N
    prob.append(p_heads)
 
# average the probability of heads over 1000 experiments
p_total_heads = sum(prob)/1000
 
print(f"Probability is {p_total_heads :.3f}")