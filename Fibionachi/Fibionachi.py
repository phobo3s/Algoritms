import time

def FibioMemor(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if CheckMemor(n):
            fib = memory[n]
        else:
            fib = FibioMemor(n-1) + FibioMemor(n-2)
            RecordMemor(n, fib)
    return fib

memory = {}

def RecordMemor(n,val):
    memory[n] = val

def CheckMemor(n):
    if n in memory:
        return True
    else:
        return False

def Fibio(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = Fibio(n-1) + Fibio(n-2)
    return fib

def Comparison(n):
    epltime = time.time()
    fib = FibioMemor(n)
    epltime = time.time() - epltime
    print("The {}. fibionacci number is {}. It took {} seconds to calculate that with Memoization".format(n,fib,epltime))

    epltime = time.time()
    fib = Fibio(n)
    epltime = time.time() - epltime
    print("The {}. fibionacci number is {}. It took {} seconds to calculate that without Memoization".format(n,fib,epltime))

Comparison(35)