def generator(start,stop):
    print("GENERATOR START",start,stop)
    while (start<=stop):
        print(start,"<=",stop)
        yield start
        print("yield", start)
        print(f'start={start}')
        start+=1
        print("count",start)
for counter in generator(3,4):
    print(f'counter={counter}')