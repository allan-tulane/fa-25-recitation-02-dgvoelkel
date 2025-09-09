from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(16, 2, 2) == 80
	assert simple_work_calc(32, 2, 2) == 192
	assert simple_work_calc(64, 2, 2) == 448

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(16,2,2,lambda n: n) == 80
	assert work_calc(16, 2, 2, lambda n : n*n) == 496
	assert work_calc(16,2,2, lambda n: 1) == 31


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	a, b = 2, 2
	n = 1000


	work_fn1 = lambda val: work_calc(val, a, b, lambda x: x**0.5)


	work_fn2 = lambda val: work_calc(val, a, b, lambda x: x)


	work_fn3 = lambda val: work_calc(val, a, b, lambda x: x**2)

	res1 = work_fn1(n)
	res2 = work_fn2(n)
	res3 = work_fn3(n)

	assert res3 > res2 > res1

	
def test_compare_span():
	a, b = 2, 2
	n = 1000

	span_fn1 = lambda val: span_calc(val, a, b, lambda x: 1)

	span_fn2 = lambda val: span_calc(val, a, b, lambda x: math.log2(x) if x > 1 else 1)

	span_fn3 = lambda val: span_calc(val, a, b, lambda x: x)

	res1 = span_fn1(n)
	res2 = span_fn2(n)
	res3 = span_fn3(n)

	assert res3 > res2 > res1
