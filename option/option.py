from typing import (
    TypeVar,
    Optional,
    Callable,
    NewType,
    Union,
    Generic,
    Tuple,
    Sequence,
    List,
)


class InvalidArgument(Exception):
    pass


A = TypeVar("A")
B = TypeVar("B")


def some(val: A) -> Optional[A]:
    return val


def none() -> Optional[A]:
    return None


def value(default: A, opt: Optional[A]) -> A:
    return opt if opt else default


def get(opt: Optional[A]) -> A:
    if opt:
        return opt
    else:
        raise (InvalidArgument("Tried to get from empty Optional"))


def bind(opt: Optional[A], func: Callable[[A], Optional[B]]) -> Optional[B]:
    return func(opt) if opt else none()


def join(optopt: Optional[Optional[A]]) -> Optional[A]:
    if optopt:
        if optopt == type(None):
            return none()
        else:
            return optopt
    else:
        return none()


def map(func: Callable[[A], B], opt: Optional[A]) -> Optional[B]:
    return func(opt) if opt else none()


def fold(none: A, func: Callable[[B], A], opt: Optional[B]) -> A:
    return func(opt) if opt else none


def iter(func: Callable[[A], None], opt: A) -> None:
    if opt:
        func(opt)


def is_none(opt: Optional[A]) -> bool:
    return opt == None


def is_some(opt: Optional[A]) -> bool:
    return opt != None


def equal(func: Callable[[A, A], bool], opt1: Optional[A], opt2: Optional[A]) -> bool:
    if opt1 and opt2:
        return func(opt1, opt2)
    elif opt1 == None and opt2 == None:
        return True
    else:
        return False


def compare(func: Callable[[A, A], int], opt1: Optional[A], opt2: Optional[A]) -> int:
    if opt1 and opt2:
        return func(opt1, opt2)
    elif opt1 == None and opt2 == None:
        return 0
    else:
        return 1 if opt1 else -1


def to_list(opt: Optional[A]) -> List[A]:
    return [opt] if opt else []


def to_seq(opt: Optional[A]) -> Sequence[A]:
    return to_list(opt)
