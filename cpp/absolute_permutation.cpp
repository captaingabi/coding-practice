#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'absolutePermutation' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 */

vector<int> absolutePermutation(int n, int k) {
    // Check contraints if needed.

    vector<int> result;
    unordered_set<int> temp_set;
    for(auto i = 1; i <= n; i++) temp_set.insert(i);

    for(auto i = 1; i <= n; i++){
        auto item = i - k;
        auto temp_it = temp_set.find(item);
    
        if(item >= 1 && item <= n && temp_it != temp_set.end()){
            result.push_back(item);
            temp_set.erase(temp_it);
            continue;
        }

        item = i + k;
        temp_it = temp_set.find(item);

        if(item >= 1 && item <= n && temp_it != temp_set.end()){
            result.push_back(item);
            temp_set.erase(temp_it);
            continue;
        }
        
        return  vector<int>(1, -1);
    }
    
    return result;
}

// SLOW, O(n^2)
/*

void print(vector<int> &v){
    for(auto item : v){
        cout << item << " ";
    }
    cout << endl;
}

vector<int> absolutePermutation(int n, int k) {
    // Check contraints if needed.

    //cout << "n:" << n << " k:" << k << endl;

    vector<int> result, temp;
    for(auto i = 1; i <= n; i++) temp.push_back(i);

    if(k == 0) return temp;
    else {
        int item;
        vector<int>::iterator temp_it;
        for(auto i = 1; i <= n; i++){
            //cout << "i: " << i << endl;
            //cout << "temp: "; print(temp);
            //cout << "result: "; print(result);
            item = i - k;
            //cout << item << endl;
            temp_it = find(temp.begin(), temp.end(), item);
            if(item >= 1 && item <= n && temp_it != temp.end()){
                result.push_back(item);
                temp.erase(temp_it);
                continue;
            }

            item = i + k;
            //cout << item << endl;
            temp_it = find(temp.begin(), temp.end(), item);
            if(item >= 1 && item <= n && temp_it != temp.end()){
                result.push_back(item);
                temp.erase(temp_it);
                continue;
            }
            
            return  vector<int>(1, -1);
        }
        
        return result;
    }
}
*/

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string first_multiple_input_temp;
        getline(cin, first_multiple_input_temp);

        vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

        int n = stoi(first_multiple_input[0]);

        int k = stoi(first_multiple_input[1]);

        vector<int> result = absolutePermutation(n, k);

        for (size_t i = 0; i < result.size(); i++) {
            fout << result[i];

            if (i != result.size() - 1) {
                fout << " ";
            }
        }

        fout << "\n";
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

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
