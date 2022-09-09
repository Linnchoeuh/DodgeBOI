"""
find_in.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""


def find_in(src_dict: dict | list,
            path_value: list | int | str,
            not_found_value = None):
    """
    ### Summary:
        This function will return a value if it exist in the given dictionnary.

    ### Args:
        - `dict | list` src_dict: The dict/list you looking at.
        - `list | int | str` path_value: Could be a single value or a list of value that will do

    ### Returns:
        - `Any`: Return a value on success or
        the `not_found_value` (default `None`) when the value doesn't exist in the dict/list.
    """
    final_value = src_dict
    try:
        if (type(path_value) == list):
            for keys in path_value:
                final_value = final_value[keys]
        else:
            final_value = final_value[path_value]
    except:
        return not_found_value
    return final_value
