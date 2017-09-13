import sequences
def test_fibonacci():
    result=sequences.fibonacci(5)
    correct= [1,1,2,3,5]
    assert result==correct