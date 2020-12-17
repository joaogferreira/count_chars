import random
import sys
import math
import logging

def relative_error(counter1,counter2):
    errors = []
    for i in counter1:
        errors.append(round((abs(counter1[i]-counter2[i])/counter1[i])*100,2))
    avg = round(sum(errors)/len(errors),2)
    max_error = max(errors)
    min_error = min(errors)

    return avg, max_error, min_error
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
    print("Exact Counter:")
    print(exact)
    print("\n")

    print("Fixed Probability Counter:")
    fixed = fixed_prob_counter(sequence)
    print(fixed)
    print("\n")

    print("Decreasing Probability Logarithmic Counter:")
    dec_counter = log_counter(sequence)
    print(dec_counter)
    print("\n")

    print("*** Exact vs Fixed Counter ***")
    avg_exact_fixed, max_exact_fixed, min_exact_fixed = relative_error(exact,fixed)
    print("Average Relative Error: % s" %(str(avg_exact_fixed)+"%"))
    print("Max Relative Error: % s" %(str(max_exact_fixed)+"%"))
    print("Min Relative Error: % s" %(str(min_exact_fixed)+"%")) 
    print("\n")
    
    print("*** Exact vs Logarithmic Counter ***")


if __name__=='__main__':
    if len(sys.argv)!=2:
        sys.exit("Usage: python3 count_chars.py <sequence_size>")
    main(int(sys.argv[1]))