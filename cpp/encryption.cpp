#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'encryption' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string encryption(string s) {
    s.erase(remove_if(s.begin(), s.end(), ::isspace), s.end());
    int len = s.length();
    int rows = 0, cols = 0;
    int floor_my = floor(sqrt(len));
    int ceil_my = ceil(sqrt(len));
    string encoded;

    if(floor_my * floor_my >= len ){ rows = cols = floor_my; }
    else if(floor_my * ceil_my >= len ){ rows = floor_my; cols = ceil_my; }
    else if(ceil_my * ceil_my >= len ){ rows = cols = ceil_my; }
    else {
        cout << "Error: ceil*ceil < length, this should not happen!" <<  endl;
    }
    for(int col = 0; col < cols; col++) {
        for(int row = 0; row < rows; row++) {
            int pos = cols*row+col;
            if(pos >= len) break;
            encoded += s[pos];
        }
        encoded += " ";
    }
    return encoded;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = encryption(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
