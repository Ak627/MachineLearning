from scipy.stats import binom
import matplotlib.pyplot as plt

n = 10 # number of trials
p = 0.37 #propability

values = list(range(n+1))
print("Values are:", values)

#pmf stands for probability mass function
#it's the probability that a discrete random varibale will be exactly equal to a particular value
#the binomial distribution is kind of pmf
#here r is our iterator, n is trials, and p is probability
dist = [binom.pmf(r,n,p) for r in values]
print("binomial distribution is:", dist)

plt.bar(values, dist)
plt.show()
