import MapReduce
import sys

"""
assignment 3, problem 2
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # table: table name
    # key: order id
    table = record[0]
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    if 2 == list_of_values:
        mr.emit((key, list_of_values[0]+list_of_values[1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
