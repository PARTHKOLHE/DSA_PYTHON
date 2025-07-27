def bubble_sort(val):
    for j in range(len(val)):
        for i in range(1, len(val)):
            if  val[j] >  val[i]:
                temp = val[j]
                val[j] = val[i]
                val[i] = temp
    return val

val = [32,5,3,6,7,54,87]
bubble_sort(val)