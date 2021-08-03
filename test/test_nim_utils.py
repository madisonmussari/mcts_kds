from context import nim 

def test_nim_sum():
    num_list = [2, 3, 4]
    assert 5 == nim.nim_sum(num_list)