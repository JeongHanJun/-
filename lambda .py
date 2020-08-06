func = [ lambda x,y : str(x)+str(y), lambda x,y : x-y, lambda x,y : x*y, lambda x,y : x/y , lambda x,y : x%y]
def menu():
    print("0. add")
    print("1. sub")
    print("2. mul")
    print("3. div")
    print("4. mod")
    print("5. quit")
    return int(input('Select menu: '))
while True:
    sel = menu()
    if sel < 0  or sel > len(func):
        print("Not correct, Try again")
    if sel == len(func):
        break
    else:
        x = int(input('First Operand : '))
        y = int(input('Seond Operand : '))
        print('result =', func[sel](x,y))
