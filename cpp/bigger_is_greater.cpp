#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'biggerIsGreater' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING w as parameter.
 */
 
void move(string &s, char c, int pos) {
    for(int i = pos + 1; i < s.length(); i++) {
        if(s[i] > c) {
            s.insert(pos, 1, s[i]);
            s.erase(i+1, 1);
            return;
        }
    }
}

string biggerIsGreater(string w) {
    for(int i = w.length() - 2; i >= 0; i--){
        if(w[i] < w[i+1]) {
            char temp =  w[i];
            sort(w.begin() + i, w.end());
            move(w, temp, i);
            return w;
        }
    }

    return "no answer";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string T_temp;
    cin >> T_temp;

    int T = stoi(ltrim(rtrim(T_temp)));

    for (int T_itr = 0; T_itr < T; T_itr++) {
        string w;
        cin >> w;

        string result = biggerIsGreater(w);

        fout << result << endl;
    }

    fout.close();

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
