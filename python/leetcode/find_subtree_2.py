#!/bin/python3
from dataclasses import dataclass


@dataclass(frozen=True)
class Node():
    name: str
    children: tuple


def compare_all_nodes(node_to_check: Node, node: Node) -> list[Node]:
    result: list[Node] = []
    if node_to_check == node and node_to_check is not node:
        result += [node, node_to_check]
    for child in node.children:
        result += compare_all_nodes(node_to_check, child)

    return result


def find_duplicates(node: Node, root: Node) -> list[tuple]:
    result: list[tuple] = []
    for child in node.children:
        result += find_duplicates(child, root)

    dup_nodes = tuple(compare_all_nodes(node, root))
    # print(node, dup_nodes)
    if dup_nodes:
        result.append(dup_nodes)

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
    ),)

result = set(find_duplicates(root, root))

for dups in result:
    print()
    for dup in dups:
        print(dup)
