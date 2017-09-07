import pytest

def simpleFunction (numone, numtwo):
	if type(numone) != int or type(numtwo) != int:
		raise TypeError ('Wrong input types!')
	if numone+numtwo<0:
		return 0
	else:
		return numone + numtwo

def test_type():
	with pytest.raises(TypeError) as errinfo:
		simpleFunction(1.1, 2)
	assert 'Wrong input types!' in str(errinfo.value)

def test_zero():
	assert simpleFunction(1, -6) == 0
	assert simpleFunction(-8, -1) == 0

def test_sum():
	assert simpleFunction(2, 6) == 8
	assert simpleFunction(3, 5) == 8