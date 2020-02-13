from option import option
import pytest
from typing import Optional, Callable


def test_some():
    opt = option.some(5)
    assert opt == 5
    assert isinstance(opt, int)


def test_some_exception():
    with pytest.raises(option.InvalidArgument):
        option.some(None)


def test_none():
    assert option.none() == None


def test_value():
    opt = option.some(5)
    nopt = option.none()
    assert option.value(1, opt) == 5
    assert option.value(1, nopt) == 1


def test_get():
    opt = option.some("Dave")
    nopt = option.none()
    assert option.get(opt) == "Dave"
    with pytest.raises(option.InvalidArgument):
        assert option.get(nopt)


def test_bind():
    opt = option.some("Dave")
    nopt = option.none()
    assert option.bind(opt, str.upper) == "DAVE"
    assert option.bind(nopt, str.upper) == None


def test_join():
    optopt: Optional[Optional[str]] = option.some(option.some("Dave"))
    assert option.join(optopt) == "Dave"
    noption = None
    assert option.join(noption) == None


def test_map():
    opt: Optional[int] = option.some(55)
    assert option.map(str, opt) == "55"
    assert option.map(lambda n: n / 2, opt) == 27.5
    assert option.map(str, option.none()) == None


def test_fold():
    opt: Optional[int] = option.some(55)
    nopt: Optional[int] = option.none()
    assert option.fold(-1, lambda n: n * 2, opt) == 110
    assert option.fold(-1, lambda n: n * 2, nopt) == -1


def test_iter(capsys):
    opt: Optional[int] = option.some(55)
    option.iter(print, opt)
    captured = capsys.readouterr()
    assert captured.out == "55\n"
    option.iter(print, option.none())
    captured = capsys.readouterr()
    assert captured.out == ""


def test_is_none():
    assert option.is_none(option.some(55)) == False
    assert option.is_none(option.none()) == True


def test_is_some():
    assert option.is_some(option.some(55)) == True
    assert option.is_some(option.none()) == False


def test_equal():
    opt1 = option.some(10)
    opt2 = option.some(10)
    opt3 = option.some(55)
    opt4 = option.none()
    compare: Callable[[int, int], bool] = lambda x, y: x == y
    assert option.equal(compare, opt1, opt2)
    assert option.equal(compare, opt1, opt3) == False
    assert option.equal(compare, opt1, opt4) == False
    assert option.equal(compare, opt4, None)


def test_compare():
    opt1 = option.some(10)
    opt2 = option.some(10)
    opt3 = option.some(55)
    opt4 = option.none()
    compare: Callable[[int, int], int] = lambda x, y: x - y
    assert option.compare(compare, opt1, opt2) == 0
    assert option.compare(compare, opt1, opt3) < 0
    assert option.compare(compare, opt3, opt1) > 0
    assert option.compare(compare, opt1, opt4) > 0
    assert option.compare(compare, opt1, opt4) > 0
    assert option.compare(compare, opt4, None) == 0


def test_to_list():
    opt = option.some(55)
    assert option.to_list(opt) == [55]
    assert option.to_list(option.none()) == []


def test_to_sequence():
    opt = option.some(55)
    assert option.to_seq(opt) == [55]
    assert option.to_seq(option.none()) == []
