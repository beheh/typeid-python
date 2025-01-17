import pytest
from uuid6 import uuid7

from typeid import TypeID, from_string, from_uuid
from typeid.errors import InvalidTypeIDStringException


def test_default_suffix() -> None:
    prefix = "qutab"
    typeid = TypeID(suffix=None, prefix=prefix)

    assert typeid.prefix == prefix
    assert typeid.suffix


def test_construct_typeid() -> None:
    prefix = "plov"
    suffix = "00041061050r3gg28a1c60t3gf"

    typeid = TypeID(prefix=prefix, suffix=suffix)

    assert typeid.prefix == prefix
    assert typeid.suffix == suffix


def test_compare_typeid() -> None:
    prefix = "plov"
    suffix = "00041061050r3gg28a1c60t3gf"

    typeid_1 = TypeID(prefix=prefix, suffix=suffix)
    typeid_2 = TypeID(prefix=prefix, suffix=suffix)
    typeid_3 = TypeID(suffix=suffix)

    assert typeid_1 == typeid_2
    assert typeid_3 != typeid_1


def test_construct_type_from_string() -> None:
    string = "00041061050r3gg28a1c60t3gf"

    typeid = from_string(string)

    assert isinstance(typeid, TypeID)
    assert typeid.prefix == ""
    assert isinstance(typeid.suffix, str)


def test_construct_type_from_string_with_prefix() -> None:
    string = "prefix_00041061050r3gg28a1c60t3gf"

    typeid = from_string(string)

    assert isinstance(typeid, TypeID)
    assert typeid.prefix == "prefix"
    assert isinstance(typeid.suffix, str)


def test_construct_type_from_invalid_string() -> None:
    string = "invalid_string_to_typeid"

    with pytest.raises(InvalidTypeIDStringException):
        from_string(string)


def test_construct_type_from_uuid() -> None:
    uuid = uuid7()

    typeid = from_uuid(suffix=uuid, prefix="")

    assert isinstance(typeid, TypeID)
    assert typeid.prefix == ""
    assert isinstance(typeid.suffix, str)


def test_construct_type_from_uuid_with_prefix() -> None:
    uuid = uuid7()
    prefix = "prefix"

    typeid = from_uuid(prefix=prefix, suffix=uuid)

    assert isinstance(typeid, TypeID)
    assert typeid.prefix == "prefix"
    assert isinstance(typeid.suffix, str)
