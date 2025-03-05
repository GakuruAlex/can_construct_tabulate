from typing import List
def can_construct_tabulate(target_str: str, available_strs: List[str])-> bool:
    """_Determine if a target str can be formed by concatenating str from a given list_

    Args:
        target_str (str): _Word to construct_
        available_strs (List[str]): _List of str to choose from_

    Returns:
        bool: _True if possible to concatenate str in list to form word else False_
    """
    can_table: List[bool] = [False for _ in range(len(target_str) + 1)]
    can_table[0] = True

    for index in range(len(target_str)):
        for char in available_strs:
            if target_str[index: index + len(char)] == char and can_table[index]:
                can_table[index + len(char)] = True
    return can_table[len(target_str)]

def main()->None:
    target_str: str = 'abcdef'
    words: List[str] = ['ab', 'abc', 'cd', 'ef','abcd']
    is_p: bool = can_construct_tabulate(target_str=target_str, available_strs= words)
    print(f"Is it possible to form the word '{target_str}' from concatenating str in {words}? {is_p}")

if __name__ =="__main__":
    main()