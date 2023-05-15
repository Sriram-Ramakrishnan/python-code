
def value_approx(val1,val2):
    ans = abs(val1-val2)
    final = ans/val1
    print(final)
    print(round(final*100,3))

while True:
    val1 = float(input("TH: "))
    val2 = float(input("PR: "))
    value_approx(val1,val2)