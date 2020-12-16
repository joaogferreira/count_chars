import random
import sys


def exact_counter(sequence):
    results = {}
    for char in sequence:
        if char in results:
            results[char]+=1
        else:
            results[char]=1
    return results


def main(size):
    name='joãoguilhermemendoncapimentadeoliveiraferreira'
    sequence=''

    for i in range(size):
        sequence += random.choice(name)
    
    exact = exact_counter(sequence)

    print(exact)

if __name__=='__main__':
    if len(sys.argv)!=2:
        sys.exit("The size of the sequence must be passed as argument!")
    main(int(sys.argv[1]))