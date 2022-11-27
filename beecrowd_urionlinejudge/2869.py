def generate_prime(n):
  prime = []
  for i in range(2,n+1):
    div = 0
    for j in range(2,int(i/2)+1):
      if i%j==0:
        div += 1
    if div == 0:
      prime.append(i)
  
  return prime

def combine_factors(n):
  all_combinations = []
  combination_factor = []

  comb_fat_rec(2,n,all_combinations,combination_factor)
  return all_combinations

def comb_fat_rec(actual_factor, n, all, comb_factor):
  if n <= 1:
    temp = comb_factor[:]
    temp.sort(reverse=True)
    t = tuple(temp)
    if t not in all:
      all.append(t)
  
  for i in range(actual_factor, n+1):    
    if n%i == 0:
      comb_factor.append(i)

      comb_fat_rec(i, n//i, all, comb_factor)

      del comb_factor[-1]

def generate_candidate(prime,combination):
  candidate = 1
  for i in range(len(combination)):
    candidate *= prime[i]**(combination[i]-1)
  return candidate

def calc(n,prime):
  all = combine_factors(n)
  candidates = []
  for c in all:
    candidate = generate_candidate(prime, c)
    candidates.append(candidate)
  
  return min(candidates)

prime = generate_prime(100)

c = int(input())
n = []
for i in range(0,c):
  n.append(int(input()))
  
for i in range(0,len(n)):
  print(calc(n[i],prime)%1000000007)
