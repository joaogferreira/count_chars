import random
import sys
import math
import numpy

def abs_mean_deviation(counter):
    total=0
    for i in counter:
        total += counter[i]
    avg = total/len(counter)

    mean_dev = 0
    for j in counter:
        mean_dev += abs(counter[j]-avg)
    mean_dev *= (1/len(counter))

    return mean_dev

def max_deviation(counter):
    total=0
    for i in counter:
        total += counter[i]
    avg = total/len(counter)
    max_dev = max(abs(counter[c] - avg) for c in counter)
    
    return max_dev

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

def logarithmic_counter(sequence):
    results = {}
    for char in sequence:
        if char in results:
            value = random.choices([0,1], weights = [1-1/(math.sqrt(2)**results[char]), 1/(math.sqrt(2)**results[char])])
            results[char]+=value[0]
        else:
            value = random.choices([0,1], weights = [0, 1]) # 1 / math.sqrt(2)**0  = 1
            results[char]=value[0]
    
    for r in results:
        results[r] *= math.sqrt(2)**results[r]
    

    return results

def main(size):
    name='joãoguilhermemendoncapimentadeoliveiraferreira'
    sequence=''

    for i in range(size):
        sequence += random.choice(name)

    print("Sequence size: "+str(len(sequence))+" chars \n")
    

    '''
        Exact counter
    '''
    exact = exact_counter(sequence)
    #ordenar por ordem crescente
    exact = dict(sorted(exact.items(), key=lambda item: item[1]))
    
    print("Exact Counter:")
    print(str(exact)+"\n")

    '''
        Fixed counter
    '''
    fixed = fixed_prob_counter(sequence)
    #ordenar por ordem crescente 
    fixed = dict(sorted(fixed.items(), key=lambda item: item[1]))
    
    print("Fixed Probability Counter:")
    print(str(fixed)+"\n")


    '''
        Logarithmic Counter
    '''
    log_counter = logarithmic_counter(sequence)
    #ordenar por ordem crescente 
    log_counter = dict(sorted(log_counter.items(), key=lambda item: item[1]))
    

    print("Decreasing Probability Logarithmic Counter:")
    print(str(log_counter)+"\n")



    print("*** Exact vs Fixed Counter ***")
    avg_exact_fixed, max_exact_fixed, min_exact_fixed = relative_error(exact,fixed)
    print("Average Relative Error:  "+(str(avg_exact_fixed)+"%"))
    print("Max Relative Error:  "+(str(max_exact_fixed)+"%"))
    print("Min Relative Error:  "+(str(min_exact_fixed)+"%")) 
    print("\n")
    
    print("*** Exact vs Logarithmic Counter ***")
    avg_exact_log, max_exact_log, min_exact_log = relative_error(exact,log_counter)
    print("Average Relative Error:  "+(str(avg_exact_log)+"%"))
    print("Max Relative Error:  "+(str(max_exact_log)+"%"))
    print("Min Relative Error: "+(str(min_exact_log)+"%")) 
    print("\n")


    print("*** Max Deviation ***")
    print("Exact counter max deviation: "+str(max_deviation(exact)))
    print("Fixed Probability counter max deviation: "+str(max_deviation(fixed)))
    print("Logarithmic counter max deviation: "+str(max_deviation(log_counter)))
    print("\n")


    print("*** Absolute Mean Deviation ***")
    print("Exact counter absolute mean deviation: "+str(abs_mean_deviation(exact)))
    print("Fixed Probability counter absolute mean deviation: "+str(abs_mean_deviation(fixed)))
    print("Logarithmic counter absolute mean deviation: "+str(abs_mean_deviation(log_counter)))
    print("\n")

    print("*** Standard Deviation ***")
    print("Exact counter standard deviation: "+str(numpy.std(list(exact.values()))))
    print("Fixed Probability counter standard deviation: "+str(numpy.std(list(fixed.values()))))
    print("Logarithmic counter standard deviation: "+str(numpy.std(list(log_counter.values()))))
    print("\n")

    print("*** Variance ***")
    print("Exact counter variance: "+str(numpy.var(list(exact.values()))))
    print("Fixed Probability counter variance: "+str(numpy.var(list(fixed.values()))))
    print("Logarithmic counter variance: "+str(numpy.var(list(log_counter.values()))))
    print("\n")

    print("**************************************************************************")
if __name__=='__main__':
    if len(sys.argv)==1:
        sys.exit("usage: python count_chars.py <sequence_size>")
    
    for i in range(1,len(sys.argv)):
        try:
            int(sys.argv[i])
        except ValueError:
            sys.exit("Argument is not a number.")
        main(int(sys.argv[i]))

    #python3 count_chars.py 100 1000 10000 100000 1000000 (etc)