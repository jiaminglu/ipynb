import pytest
import importlib


def test_func_ipynb():
    from ipynb.fs.function.func import func
    assert func() == 'foobar'
    assert func('a') == 'abar'

def test_bogus_ipynb():
    with pytest.raises(ImportError):
        import ipynb.fs.full.bogus_ipynb as bogus_ipynb

def test_r_notebook():
    with pytest.raises(ImportError):
        import ipynb.fs.full.r_notebook

def test_nbformat_2():
    with pytest.raises(ImportError):
        import ipynb.fs.full.older_nbformat
