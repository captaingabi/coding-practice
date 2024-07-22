#!/bin/python3
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Node():
    name: str
    children: tuple


def compare_all_nodes(node_to_check: Node, node: Node) -> Optional[Node]:
    if node_to_check == node and node_to_check is not node:
        return node_to_check
    for child in node.children:
        result = compare_all_nodes(node_to_check, child)
        if result:
            return result

    return None


result = set()


def find_duplicates(node: Node, root: Node):
    for child in node.children:
        if child not in result:
            dup = find_duplicates(child, root)
            result.add(dup) if dup else None

    dup = compare_all_nodes(node, root)
    result.add(dup) if dup else None


root = \
    Node("root", (
        Node('c1', (
            Node('cc1', (Node('ccc1', (),),),),
            Node('cc2', (),),
        )),
        Node('c2', (
            Node('c1', (
                Node('cc1', (Node('ccc1', (),),),),
                Node('cc2', (),),
            ),),
        ),),
    ),)

find_duplicates(root, root)

for dup in result:
    print(dup)
