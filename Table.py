number = int (raw_input("Enter the number for which you want to print table"))

for i in xrange(1,21):  # generate data on fly - for memory efficiency
    table = number*i
    print number,"*",i,"=",table



