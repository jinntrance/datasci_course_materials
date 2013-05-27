from operator import itemgetter
import MapReduce
import sys

"""
problem 6
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

Ldim = 10 #TODO hard code is evil
Ndim = 10


def mapper(record):
    # key: (row,col)
    # value: record
    matrix=record[0]
    row=record[1]
    column=record[2]
    if "a" == matrix:
        for k in range(Ndim):
            mr.emit_intermediate((row,k), record)
    if "b" == matrix:
        for i in range(Ldim):
            mr.emit_intermediate((i,column),record)

def reducer(key, elements):
    # key: (row,col)
    # value: list of sequence
    # for e in set(list_of_values):
    rowA= []
    columnB= []
    total=0
    for e in sorted(elements):
        if "a" == e[0]:
            rowA.append(e)
        if "b" == e[0]:
            columnB.append(e)
    for a in sorted(rowA,key=itemgetter(1)):
        print a
        for b in sorted(columnB,key=itemgetter(1,2)):
            if a[2]==b[1]:
                total+=a[3]*b[3]
    if 0 !=total:
        r,c=key
        mr.emit((r,c,total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  # mr.execute(inputdata, dimM,reducer)
  mr.execute(inputdata, mapper, reducer)
