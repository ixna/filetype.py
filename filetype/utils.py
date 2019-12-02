# -*- coding: utf-8 -*-

_NUM_SIGNATURE_BYTES = 262


def get_signature_bytes(path):
    """
    Reads file from disk and returns the first 262 bytes
    of data representing the magic number header signature.

    Args:
        path: path string to file.

    Returns:
        First 262 bytes of the file content as bytearray type.
    """
    with open(path, 'rb') as fp:
        return bytearray(fp.read(_NUM_SIGNATURE_BYTES))


def signature(array):
    """
    Returns the first 262 bytes of the given bytearray
    as part of the file header signature.

    Args:
        array: bytearray to extract the header signature.

    Returns:
        First 262 bytes of the file content as bytearray type.
    """
    length = len(array)
    index = _NUM_SIGNATURE_BYTES if length > _NUM_SIGNATURE_BYTES else length

    return array[:index]


def get_bytes(obj):
    """
    Infers the input type and reads the first 262 bytes,
    returning a sliced bytearray.

    Args:
        obj: path to readable, file, bytes or bytearray.

    Returns:
        First 262 bytes of the file content as bytearray type.

    Raises:
        TypeError: if obj is not a supported type.
    """
    try:
        first_bytes = obj.read(_NUM_SIGNATURE_BYTES)
    except AttributeError:
        # duck-typing as readable failed, means no need to read 
        # we'll try to directly access the bytes
        first_bytes = obj
    else:
        # return read pointer to initial so buffered reader object 
        # can be re-read on caller side
        obj.seek(0)

    kind = type(first_bytes)

    if kind is bytearray:
        return signature(first_bytes)

    if kind is str:
        return get_signature_bytes(first_bytes)

    if kind is bytes:
        return signature(first_bytes)

    if kind is memoryview:
        # convert memoryview object to list to be checked later 
        # altough actually without converting it's value can be 
        # directly accessed just like a list
        return signature(first_bytes).tolist()

    raise TypeError('Unsupported type as file input: %s' % kind)