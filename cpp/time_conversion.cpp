#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string timeConversion(string s) {
    if(
        s.compare(0, 2, "12") == 0 &&
        s.compare(8, 2, "AM") == 0
    ) {
        return "00" + s.substr(2, 6);
    }

    if(s.compare(8, 2, "PM") == 0 ) {
        if(s.compare(0, 2, "12") != 0 ) {
            return to_string(stoi(s.substr(0, 2)) + 12) + s.substr(2, 6);
        }
        else{
            return s.substr(0, 8);
        }
    }

    return s.substr(0, 8);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
