"""
14 ADVANCE feature
"""


# 1. Typing Overloads

from typing import Literal, overload



@overload

def transform(data: str, mode: Literal["split"]) -> list[str]:

    ...



@overload

def transform(data: str, mode: Literal["upper"]) -> str:

    ...



def transform(data: str, mode: Literal["split", "upper"]) -> list[str] | str:

    if mode == "split":

        return data.split()

    else:

        return data.upper()



split_words = transform("hello world", "split")  # Return type is list[str]

split_words[0]  # Type checker is happy



upper_words = transform("hello world", "upper")  # Return type is str

upper_words.lower()  # Type checker is happy



upper_words.append("!")  # Cannot access attribute "append" for "str"



"""
2. Keyword-only and Positional-only Arguments

keywords arguments are after the  '*'

positional argumnents are before '/'

"""

def foo(a, b, /, c, d, *, e, f):
    ...



"""
3. Future Annotations
Because it allows forward references and makes your code cleaner and faster—especially useful for:

Classes that refer to themselves

Avoiding unnecessary imports

Improving runtime performance with annotations
"""

class TreeNode:
     """
        You need to use 'TreeNode' in quotes, because the class isn’t fully defined yet.
        """
    def add_child(self, child: 'TreeNode') -> None:
        ...


"""
'from __future__ import annotations' importing this solves the class reference problem which is not defined yet

"""
from __future__ import annotations

class TreeNode:
    def add_child(self, child: TreeNode) -> None:
