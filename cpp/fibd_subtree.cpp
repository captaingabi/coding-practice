#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <list>
using namespace std;

class Node{
    public:
        Node *myself;
        string name;
        list<Node> children;

        Node() = default;

        friend bool operator==(const Node&, const Node&);
};

bool operator==(const Node& lhs, const Node& rhs) {
    return lhs.name == rhs.name && 
           lhs.children == rhs.children &&
           lhs.myself != rhs.myself;
}

int compare_all_nodes(
    const Node &node_to_check,
    const Node &node,
    list<Node> &result
){
    int results = 0;

    //cout << "compate " << node_to_check.name << " " << node.name << endl;
    //cout << "compate " << &node_to_check << " " << &node << endl;

    if (node_to_check == node){
        //cout << "compate push_back " << node.name << endl;
        result.push_back(node);
        results++;
    } else {
        for (Node child : node.children) {
            //cout << "compate child " << child.name << " " << &child << endl;
            results += compare_all_nodes(node_to_check, child, result);
        }
    }
    return results;
}

void find_duplicates(
    const Node &node,
    const Node &root,
    list<Node> &result
){
    if(find(result.begin(), result.end(), node) == result.end() ){
        list<Node> temp;
        //cout << "find " << node.name << " " << root.name << endl;
        //cout << "find " << &node << " " << &root << endl;

        if(compare_all_nodes(node, root, temp) > 0){
            result.splice(result.end(), temp);
            result.push_back(node);
        }
        else{
            for (Node child : node.children) {
                //cout << "find child " << child.name << " " << &child << endl;
                find_duplicates(child, root, result);
            }
        }
    }
}

void print_graph(const Node &root, int tab){
    cout << string( tab, ' ' ) << root.name << " " << &root << " " << root.myself << endl;
    for (Node child : root.children) {
        print_graph(child, tab + 2);
    }
}

void print_result(const list<Node> &result){
    for (Node node : result) {
        cout << node.name << " " << &node << " " << node.myself << endl;
    }
    cout << endl;
}

int main()
{
    Node ccc1_1 = Node(); ccc1_1.name = "ccc1"; ccc1_1.myself = &ccc1_1;
    Node ccc1_2 = Node(); ccc1_2.name = "ccc1"; ccc1_2.myself = &ccc1_2;

    Node cc1_1 = Node(); cc1_1.name = "cc1"; cc1_1.myself = &cc1_1;
    cc1_1.children.push_back(ccc1_1);

    Node cc1_2 = Node(); cc1_2.name = "cc1"; cc1_2.myself = &cc1_2;
    cc1_2.children.push_back(ccc1_2);

    Node cc2_1 = Node(); cc2_1.name = "cc2"; cc2_1.myself = &cc1_2;
    Node cc2_2 = Node(); cc2_2.name = "cc2"; cc2_2.myself = &cc2_2;
    Node cc2_3 = Node(); cc2_3.name = "cc2"; cc2_3.myself = &cc2_3;

    Node c1_1 = Node(); c1_1.name = "c1"; c1_1.myself = &c1_1;
    c1_1.children.push_back(cc1_1);
    c1_1.children.push_back(cc2_1);

    Node c1_2 = Node(); c1_2.name = "c1"; c1_2.myself = &c1_2;
    c1_2.children.push_back(cc1_2);
    c1_2.children.push_back(cc2_2);


    Node c2 = Node(); c2.name = "c2"; c2.myself = &c2;
    c2.children.push_back(c1_2);

    Node root = Node(); root.name = "root";  root.myself = &root;
    root.children.push_back(c1_1);
    root.children.push_back(c2);
    root.children.push_back(cc2_3);

    print_graph(root, 0); cout << endl;

    list<Node> result;

    find_duplicates(root, root, result);
    print_result(result);

    return 0;
}