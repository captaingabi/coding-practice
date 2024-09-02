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


# This only assembles a list of nodes that have duplicates
def find_duplicates(node: Node, root: Node, result: set) -> set[Node]:
    if node not in result:
        dup = compare_all_nodes(node, root)
        if dup:
            result.add(dup)
        else:
            for child in node.children:
                result.union(find_duplicates(child, root, result))

    return result


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
        Node('cc2', (),),
    ),)

result = find_duplicates(root, root, set())

for dup in result:
    print(dup)
