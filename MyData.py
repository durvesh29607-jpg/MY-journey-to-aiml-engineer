import pandas

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvare = pandas.DataFrame(mydataset)

print(myvare)