# The assignment expression operator := (or the "walrus" operator)

import pprint



#  The walrus operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
val_data = {
    "length": len(values),
    "total": sum(values),
    "average": sum(values) / len(values)
}
pprint.pp(val_data)

val_data = {
    "length": (l:= len(values)),
    "total": (s := sum(values)),
    "average": s / l
}
pprint.pp(val_data)