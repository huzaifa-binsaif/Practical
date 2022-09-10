def DNA_strand(x):
    lst = list(x)
    n_lst = []
    if len(x) != 0:
        for i in lst:
            if i == "A":
                n_lst.append("T")
            elif i == "T":
                n_lst.append("A")
            elif i == "G":
                n_lst.append("C")
            elif i == "C":
                n_lst.append("G")
            else:
                return "Error: Incorrect symbol present in half strand"
                break
    else:
        return "Error: DNA half strand can not be empty"
    n_str = ""
    for i in n_lst:
        n_str += i
    return n_str


print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))
print(DNA_strand("ATGHC"))
print(DNA_strand(""))