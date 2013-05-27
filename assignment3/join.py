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
    items = []
    order = []
    for v in list_of_values:
        if "order" == v[0]:
            order.append(v)
        elif "line_item" == v[0]:
                items.append(v)

    for o in order:
        for i in items:
            mr.emit(o + i)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
