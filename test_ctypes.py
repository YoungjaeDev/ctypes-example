import ctypes
import pathlib
import numpy as np

# path of the shared library
libfile = pathlib.Path(__file__).parent / "libutil.so"
_mylib = ctypes.CDLL(str(libfile))

_mylib.print_string.restype = None
_mylib.print_string.argtypes = [ctypes.c_char_p]
def print_string(words: str) -> None:
    global _mylib
    
    _mylib.print_string(words)
    return

_mylib.csum.restype = ctypes.c_longlong
_mylib.csum.argtypes = [ctypes.c_int, np.ctypeslib.ndpointer(dtype=np.int32)]
def array_element_sum(len: int, array: np.array) -> int:
    global _mylib
    
    return _mylib.csum(len, array)

type_vec = ctypes.POINTER(ctypes.c_double * 3)
_mylib.add.restype = type_vec
_mylib.add.argtypes = [type_vec, type_vec]
def add_among_array(a: list, b: list) -> list:
    a_p = (ctypes.c_double * 3)(*a)
    b_p = (ctypes.c_double * 3)(*b)
    r_p = _mylib.add(a_p, b_p)
    return [l for l in r_p.contents]

if __name__ == "__main__":
    print_string(b"AVIKUS")
    print(array_element_sum(3, np.array([1,2,3], dtype=np.int32)))
    print(add_among_array([1,2,3], [4,5,6]))