import time

def FibioMemor(n):
    if n == 1:
        return 0
    elif n == 2:
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
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = Fibio(n-1) + Fibio(n-2)
    return fib

def FibioSeq(FibList, n):
    if n == 1:
        FibList = [0]
    else:
        FibList.append(FibioSeq(FibList,n-1)) 
    return Fibio(n)

def FibioSeqMemor(FibList, n):
    if n == 1:
        FibList = []
    else:
        FibList.append(FibioSeqMemor(FibList,n-1))
    return FibioMemor(n)


def Comparison(n):
    epltime = time.time()
    fib = Fibio(n)
    epltime = time.time() - epltime
    print("The {}. fibionacci number is {}. It took {} seconds to calculate that without Memoization".format(n,fib,epltime))

    epltime = time.time()
    fib = FibioMemor(n)
    epltime = time.time() - epltime
    print("The {}. fibionacci number is {}. It took {} seconds to calculate that with Memoization".format(n,fib,epltime))

def ComparisonSeq(n):
    epltime = time.time()
    FibList = []
    FibioSeq(FibList,n+1)
    epltime = time.time() - epltime
    print("The Sequence is - {}.\n it took {} second without memoization.".format(FibList,epltime))

    epltime = time.time()
    FibList = []
    FibioSeqMemor(FibList,n+1)
    epltime = time.time() - epltime
    print("The Sequence is - {}.\n it took {} second with memoization.".format(FibList,epltime))


# Test Functions
def MegaTest(a):
    Comparison(a)
    ComparisonSeq(a)

MegaTest(35)