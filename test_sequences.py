import sequences

def test_fibonacci():
    result=sequences.fibonacci(5)
    correct= [1,1,2,3,5]
    assert result==correct
    
def test2_fibonacci():
    try:
        sequences.fibonacci(-1)
    except:
        return
    print("did not throw exception")
    assert False

    
def test3_fibonacci():
    result=sequences.fibonacci(20)
    correct = [1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765]
    assert result==correct