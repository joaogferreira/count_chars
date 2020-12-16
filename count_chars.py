import random
import sys
import math


def exact_counter(sequence):
    results = {}
    for char in sequence:
        if char in results:
            results[char]+=1
        else:
            results[char]=1
    return results

def fixed_prob_counter(sequence):
    results = {}
    for char in sequence:
        if char in results:
            value = random.choices([0,1], weights = [7/8, 1/8])
            results[char]+=value[0]
        else:
            value = random.choices([0,1], weights = [7/8, 1/8])
            results[char]=value[0]
    for r in results:
        results[r]*=8
    
    return results

def log_counter(sequence):
    results = {}
    for char in sequence:
        if char in results:
            value = random.choices([0,1], weights = [1-1/(math.sqrt(2)**results[char]), 1/(math.sqrt(2)**results[char])])
            results[char]+=value[0]
        else:
            value = random.choices([0,1], weights = [0, 1]) #math.sqrt(2)**0  = 1
            results[char]=value[0]
    
    for r in results:
        results[r] = math.sqrt(2)**results[r]-1
    

    return results

def main(size):
    name='joãoguilhermemendoncapimentadeoliveiraferreira'
    sequence=''

    for i in range(size):
        sequence += random.choice(name)
    
    exact = exact_counter(sequence)
    print(exact)

    fixed = fixed_prob_counter(sequence)
    print(fixed)

    dec_counter = log_counter(sequence)
    print(dec_counter)

if __name__=='__main__':
    if len(sys.argv)!=2:
        sys.exit("The size of the sequence must be passed as argument!")
    main(int(sys.argv[1]))