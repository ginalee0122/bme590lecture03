def firstfunction(number1, number2):
    if(type(number1) == str or type(number2) == str):
        return 0
    sum = number1 + number2
    if(sum > 0):
        return(sum)
    else:
        return(0)

def test_1():
    assert firstfunction(1,2)== 3

def test_2():
    assert firstfunction(-2,1)== 0

def test_3():
    assert firstfunction(-1,5)== 4

def test_4():
    assert firstfunction(0,0)== 0

def test_5():
    assert firstfunction('c','c')== 0



