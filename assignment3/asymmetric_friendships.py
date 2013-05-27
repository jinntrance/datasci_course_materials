import MapReduce
import sys

"""
problem 4
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: friend A
    #value:tuple (friend,sign)
    friendA = record[0]
    friendB = record[1]
    mr.emit_intermediate((friendA, friendB), 1)
    mr.emit_intermediate((friendB, friendA),-1)

def reducer(key, list_of_values):
    # key: (friendA,friendB)
    # value: list of relationships
    total=0
    for v in list_of_values:
        total+=v
    if 0!= total:
        mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
