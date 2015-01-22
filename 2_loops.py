iterations = [100000, 1000000, 10000000]

def inefficient_loop(n, lowerlist):
    """ Evaluate function inside of the loop """
    print 'Inefficient loop @ {0}:\t'.format(n),
    upperlist = []
    for word in lowerlist:
        upperlist.append(word.upper())
    return upperlist

def efficient_loop(n, lowerlist):
    """ Evaluate a function outside of the loop """
    print 'Efficient loop @ {0}:\t'.format(n),
    upper = str.upper
    upperlist = []
    append = upperlist.append
    for word in lowerlist:
        append(upper(word))
    return upperlist

if __name__ == '__main__':
    import timeit
    for num in iterations:
        lowerlist = [str(x) for x in range(num)]
        print '--- {0} iterations ---'.format(num)
        print(
            timeit.timeit(
                'inefficient_loop(' + str(num) + ', lowerlist)',
                setup='from __main__ import inefficient_loop, lowerlist',
                number=1))
        print(
            timeit.timeit(
                'efficient_loop(' + str(num) + ', lowerlist)',
                setup='from __main__ import efficient_loop, lowerlist',
                number=1))
