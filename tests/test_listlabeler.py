from __future__ import division, print_function
import pytest
import listlabeler

def test_str():
    ll = listlabeler.LabeledList(['cat', 'dog', 'moose'])
    assert str(ll) == "['cat', 'dog', 'moose']"
    assert repr(ll) == "LabeledList(['cat', 'dog', 'moose'])"

    ll = listlabeler.LabeledList(('cat', 'dog', 'moose'))
    assert str(ll) == "('cat', 'dog', 'moose')"
    assert repr(ll) == "LabeledList(('cat', 'dog', 'moose')"




if __name__ == '__main__':
    pytest.main()
