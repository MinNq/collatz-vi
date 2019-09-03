import numpy as np
import matplotlib.pyplot as plt

"create a list of prime numbers not exceeding n"
"with eratosthenes sieve"
def prime_list(n):
  sieve = [1]*(n+1)
  prime_list = []
  for index in range(2, n+1):
    if sieve[index]:
      prime_list.append(index)
      for further_index in range(index+1, n+1):
        if not further_index%index:
          sieve[further_index] = 0
  return prime_list
    
"the generalized collatz function"
def generate(seed, prime):
  trigger = 0
  deno = 1
  for element in prime_list(prime)[:-1]:
    if not seed%element:
      if trigger == 0:
        trigger = 1
      deno *= element
  if trigger == 1:
    return seed/deno
  else:
    return seed*prime + 1

class collatz:
  def __init__(self, seed, prime, max_iter = 10000, early_break = True):
    self.seed = seed
    self.max_iter = max_iter
    self.early_break = early_break
    self.prime = prime
  def main(self):
    self.log = [0]*self.max_iter
    self.log[0] = self.seed
    self.trigger = False
    for index in range(1, self.max_iter):
      self.log[index] = generate(self.log[index - 1], self.prime)
      if not self.trigger and self.log[index] == 1:
        self.first = index
        self.trigger = True
        if self.early_break:
          break
      
def main_plot(prime, max_value, log_scale = (False, False)):
  stopping_time = []
  legal_seed = []
  for seed in range(1, max_value + 1):
    tmp = collatz(seed = seed, prime = prime)
    tmp.main()
    if tmp.trigger:
      legal_seed.append(seed)
      stopping_time.append(tmp.first + 1)
  plt.figure(figsize=(16,9))
  ax = plt.gca()
  if log_scale[0]:
    ax.set_xscale('log')
  if log_scale[1]:
    ax.set_yscale('log')
  plt.scatter(legal_seed ,stopping_time, alpha = 0.3, s = 50000/max_value)
  plt.ylabel('Total stopping time')
  plt.xlabel('Beginning value')
