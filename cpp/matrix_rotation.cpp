#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'matrixRotation' function below.
 *
 * The function accepts following parameters:
 *  1. 2D_INTEGER_ARRAY matrix
 *  2. INTEGER r
 */

void print(const vector<vector<int>> &matrix) {
    for(auto row : matrix) {
        for(auto item : row) {
            cout << item << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void rotate_ring(
    vector<vector<int>> &matrix,
    int i_first, int i_last,
    int j_first, int j_last,
    int rorations
    )
{
    vector<int> line;

    // Note: using vector<>::insert for the first row would be faster,
    //       but for readibility, I will leave it like this.
    for(auto j = j_first; j < j_last;  j++) line.push_back(matrix[i_first][j]);
    for(auto i = i_first; i < i_last;  i++) line.push_back(matrix[i][j_last]);
    for(auto j = j_last;  j > j_first; j--) line.push_back(matrix[i_last][j]);
    for(auto i = i_last;  i > i_first; i--) line.push_back(matrix[i][j_first]);

    auto line_offset = rorations % line.size();

    vector<int> rotated_line(line.begin() + line_offset, line.end());
    rotated_line.insert(rotated_line.end(), line.begin(), line.begin() + line_offset);

    auto pos = 0;

    for(auto j = j_first; j < j_last;  j++) matrix[i_first][j] = rotated_line[pos++];
    for(auto i = i_first; i < i_last;  i++) matrix[i][j_last]  = rotated_line[pos++];
    for(auto j = j_last;  j > j_first; j--) matrix[i_last][j]  = rotated_line[pos++];
    for(auto i = i_last;  i > i_first; i--) matrix[i][j_first] = rotated_line[pos++];

    return;

}

void matrixRotation(vector<vector<int>> matrix, int rotations) {
    auto rows = matrix.size(), cols = matrix[0].size();

    for(auto offset = 0; offset < min(rows, cols)/2; offset++) {
        rotate_ring(
            matrix,
            offset, rows - 1 - offset,
            offset, cols - 1 - offset,
            rotations
        );
    }

    print(matrix);
}

int main()
{
    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int m = stoi(first_multiple_input[0]);

    int n = stoi(first_multiple_input[1]);

    int r = stoi(first_multiple_input[2]);

    vector<vector<int>> matrix(m);

    for (int i = 0; i < m; i++) {
        matrix[i].resize(n);

        string matrix_row_temp_temp;
        getline(cin, matrix_row_temp_temp);

        vector<string> matrix_row_temp = split(rtrim(matrix_row_temp_temp));

        for (int j = 0; j < n; j++) {
            int matrix_row_item = stoi(matrix_row_temp[j]);

            matrix[i][j] = matrix_row_item;
        }
    }

    matrixRotation(matrix, r);

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
