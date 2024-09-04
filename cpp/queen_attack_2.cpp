#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'queensAttack' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER r_q
 *  4. INTEGER c_q
 *  5. 2D_INTEGER_ARRAY obstacles
 */

int queensAttack(int n, int k, int r_q, int c_q, vector<vector<int>> obstacles) {
    int row_left = c_q - 1;
    int row_right = n - c_q;
    int col_down = r_q - 1;
    int col_up = n - r_q;
    int diag_up_left = min(col_up, row_left);
    int diag_up_right = min(col_up, row_right);
    int diag_down_left = min(col_down, row_left);
    int diag_down_right = min(col_down, row_right);

    //cout << "queen: " << r_q << " " << c_q << endl;

    for(vector<int> obstacle : obstacles ) {
        //cout << "Obstacle: " << obstacle[0] << " " << obstacle[1] << endl;
        if(obstacle[0] == r_q && obstacle[1] == c_q) {
            cout << "Error: obstacle on queen" << endl;
            exit(-1);
        } else if(obstacle[0] == r_q) {
            if(obstacle[1] < c_q){
                row_left = min(row_left, c_q - obstacle[1] - 1);
                //cout << "New row_left: " << row_left << endl;
            } else {
                row_right = min(row_right, obstacle[1] - c_q - 1);
                //cout << "New row_right: " << row_right << endl;
            }
        } else if(obstacle[1] == c_q) {
            if(obstacle[0] < r_q){
                col_down = min(col_down, r_q - obstacle[0] - 1);
                //cout << "New col_down: " << col_down << endl;
            } else {
                col_up = min(col_up, obstacle[0] - r_q - 1);
                //cout << "New col_up: " << col_up << endl;
            }
        } else {
            int diff_row = obstacle[0] - r_q;
            int diff_col = obstacle[1] - c_q;
            if(abs(diff_row) == abs(diff_col)){
                int diff = abs(diff_row);
                if(diff_row > 0 && diff_col > 0) {
                    diag_up_right = min(diag_up_right, diff - 1);
                    //cout << "New diag_up_right: " << diag_up_right << endl;
                } else if(diff_row > 0 && diff_col < 0) {
                    diag_up_left = min(diag_up_left, diff - 1);
                    //cout << "New diag_up_left: " << diag_up_left << endl;
                } else if(diff_row < 0 && diff_col > 0) {
                    diag_down_right = min(diag_down_right, diff - 1);
                    //cout << "New diag_down_right: " << diag_down_right << endl;
                } else if(diff_row < 0 && diff_col < 0) {
                    diag_down_left = min(diag_down_left, diff - 1);
                    //cout << "New diag_down_left: " << diag_down_left << endl;
                }
            }
        }
    }

    //cout << row_left + row_right + col_down + col_up + 
    //       diag_up_left + diag_up_right + diag_down_left + diag_down_right << endl;

    return row_left + row_right + col_down + col_up + 
           diag_up_left + diag_up_right + diag_down_left + diag_down_right;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int k = stoi(first_multiple_input[1]);

    string second_multiple_input_temp;
    getline(cin, second_multiple_input_temp);

    vector<string> second_multiple_input = split(rtrim(second_multiple_input_temp));

    int r_q = stoi(second_multiple_input[0]);

    int c_q = stoi(second_multiple_input[1]);

    vector<vector<int>> obstacles(k);

    for (int i = 0; i < k; i++) {
        obstacles[i].resize(2);

        string obstacles_row_temp_temp;
        getline(cin, obstacles_row_temp_temp);

        vector<string> obstacles_row_temp = split(rtrim(obstacles_row_temp_temp));

        for (int j = 0; j < 2; j++) {
            int obstacles_row_item = stoi(obstacles_row_temp[j]);

            obstacles[i][j] = obstacles_row_item;
        }
    }

    int result = queensAttack(n, k, r_q, c_q, obstacles);

    fout << result << "\n";

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
