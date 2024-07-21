#!/bin/python3

from dataclasses import dataclass


# dataclass will create auto __init__, __eq__, __repr__
# frozen will also create default __hash__
@dataclass(frozen=True)
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


apple = InventoryItem("apple", 100, 5)
apple2 = InventoryItem("apple", 100, 5)
orange = InventoryItem("orange", 120, 7)

print(apple)

print(f"{apple == apple2=}")
print(f"{apple == orange=}")

items = {apple, orange}
print(items)
