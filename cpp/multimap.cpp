#include <iostream>
#include <map>

using namespace std;

int main ()
{
  multimap<char,int> mymm;

  mymm.insert(pair<char,int>('a',10));
  mymm.insert(pair<char,int>('b',20));
  mymm.insert(pair<char,int>('b',30));
  mymm.insert(pair<char,int>('b',40));
  mymm.insert(pair<char,int>('c',50));
  mymm.insert(pair<char,int>('c',60));
  mymm.insert(pair<char,int>('d',60));

  cout << "mymm contains:\n";
  for (auto ch='a'; ch<='d'; ch++)
  {
    auto ret = mymm.equal_range(ch);
    cout << ch << " =>";
    for (auto it = ret.first; it != ret.second; it++)
      cout << ' ' << it->second;
    cout << '\n';
  }

  return 0;
}