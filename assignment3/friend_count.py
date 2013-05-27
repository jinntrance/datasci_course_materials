import MapReduce
import sys

"""
problem 3
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: friend A
    friendA = record[0]
    mr.emit_intermediate(friendA, 1)

def reducer(key, list_of_values):
    # key: friendA
    # value: list of friends count
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
