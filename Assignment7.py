import numpy as np 

def quiz34rv(m): 
    answers = np.random.uniform(0,4,m)
    for sample in answers: 
        print(sample)

def quiz34rvCD(m): 
    answers = np.random.uniform(0,4,m)
    return np.sum(answers>1.5)/m 



print("="*100)
print("B")
quiz34rv(25)
print("="*100)
c = []
d = []
for i in range(5):
    c.append(quiz34rvCD(100))
    d.append(quiz34rvCD(1000))

print(c) 
print (sum(c)/5)

print(d)
print(sum(d)/5)

