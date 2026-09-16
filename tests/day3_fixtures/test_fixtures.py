import pytest




# def test_one(input_value1,input_value2):
#     input_value1 = input_value1
#     input_value2 = input_value2
#     assert input_value1 == input_value2
#
# def test_two(input_value1,input_value2):
#     input_value1 = input_value1
#     input_value2 = input_value2
#     assert input_value1 > input_value2
#
def test_three(read_inputs):
    a,b = read_inputs
    assert  a == b
#
# def test_four(input_value1,input_value2):
#     assert True