#!/bin/python3

from typing import Dict, Generic, TypeVar

T = TypeVar("T")


class Registry(Generic[T]):
    def __init__(self) -> None:
        self._store: Dict[str, T] = {}

    def set_item(self, key: str, value: T) -> None:
        self._store[key] = value

    def get_item(self, key: str) -> T:
        return self._store[key]


if __name__ == "__main__":
    family_name_reg = Registry[str]()
    family_age_reg = Registry[int]()

    family_name_reg.set_item("husband", "steve")
    family_name_reg.set_item("dad", "john")

    family_age_reg.set_item("steve", 30)

    print(family_name_reg.get_item("husband"))
    print(family_name_reg.get_item("dad"))
    print(family_age_reg.get_item("steve"))

#    family_age_reg.set_item("steve", "yeah")  # mymy shows the error
