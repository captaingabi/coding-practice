#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'noPrefix' function below.
 *
 * The function accepts STRING_ARRAY words as parameter.
 */

/* SLOW
bool check_prefix(string &s1, string &s2){
    for(int i = 0; i < s1.size(); i++){
        if(s1[i] == '\0') return true;
        if(s2[i] == '\0') return true;
        if(s1[i] != s2[i]) return false;
    }
    return true;
}

void noPrefix(vector<string> words) {
    for(int i = 0; i < words.size(); i++){
        for(int j = 0; j < i; j++){
            if(check_prefix(words[i], words[j])) {
                cout << "BAD SET" << endl;
                cout << words[i] << endl;
                return;
            }
        }
    }

    cout << "GOOD SET" << endl;
}
*/

class Node{
    private:
        bool last_character;
        Node *children[10];

    public:
        Node() = default;
        Node(bool last_character){ this->last_character = last_character; }

        bool is_prefix(int idx, bool last_character){
            if(children[idx] == nullptr) {
                children[idx] = new Node(last_character);
                return false;
            } else if(children[idx]->last_character || last_character){
                return true;
            } else {
                return false;
            }
        }

        Node *get_child(int idx) { return children[idx]; }
};

void noPrefix(vector<string> words) {
    Node *root = new Node(), *current = root;

    for (string word : words) {
        for (string:: iterator it = word.begin(); it != word.end(); it++) {
            if((*it) == '\0') break;

            int idx = (*it) - 'a';
            if(idx < 0 || idx > 9) {
                cout << "ERROR: idx: " << idx << " out of bounds!" << endl;
                exit(-1);
            }

            bool last_character = (*(it+1)) == '\0';

            if(current->is_prefix(idx, last_character)) {
                cout << "BAD SET" << endl;
                cout << word << endl;
                return;
            }
            current = current->get_child(idx);
        }
        current = root;
    }

    cout << "GOOD SET" << endl;
}

int main()
{
    string n_temp;
    cin >> n_temp;

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<string> words(n);

    for (int i = 0; i < n; i++) {
        string words_item;
        //getline(cin, words_item);
        cin >> words_item;

        words[i] = words_item;
    }

    noPrefix(words);

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
