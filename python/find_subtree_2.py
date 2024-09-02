#!/bin/python3
from dataclasses import dataclass


@dataclass(frozen=True)
class Node():
    name: str
    children: tuple


def compare_all_nodes(
    node_to_check: Node,
    node: Node,
    result: tuple[Node, ...]
) -> tuple[Node, ...]:
    if node_to_check == node and node_to_check is not node:
        result += (node,)
    else:
        for child in node.children:
            result = compare_all_nodes(node_to_check, child, result)

    return result


# This returns a set of tuples where tuple contains all duplicate instances
def find_duplicates(
    node: Node,
    root: Node,
    result: set[tuple[Node, ...]]
) -> set[tuple[Node, ...]]:
    if node not in result:
        dups = compare_all_nodes(node, root, ())
        if dups:
            result.add(dups + (node,))
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

result: set[tuple[Node, ...]] = find_duplicates(root, root, set())

for dups in result:
    print(f"Found {dups[0].name} {len(dups)} times:")
    for dup in dups:
        print(dup)
