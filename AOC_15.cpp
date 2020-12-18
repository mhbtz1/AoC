#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <unordered_map>
using namespace std;

unordered_map< long long int, vector<long long int> > tmp;
vector<long long int> simul(vector<long long int> numbers){
    vector<long long int> turn = numbers;
    for(int i = 0; i < numbers.size(); i++){
        tmp[numbers[i]].push_back(i);
    }
    int tmp_ln = numbers.size();
    for(int j = tmp_ln; j <= 3e7; j++){
        cout << j << endl;
        vector<long long int> tmp_lst = tmp[turn[turn.size()-1]];
        if(tmp_lst.size()>=3){
            tmp_lst.erase(tmp_lst.begin());
            tmp[turn[turn.size()-1]]=tmp_lst;
        }
        if(tmp_lst.size()==0){
            turn.push_back(0);
            tmp[turn[turn.size()-1]].push_back(j);
        } else if(tmp_lst.size()==1){
            turn.push_back(0);
            tmp[turn[turn.size()-1]].push_back(j);
        }else if(tmp_lst.size()==2){
            turn.push_back(tmp_lst[1] - tmp_lst[0]);
            tmp[turn[turn.size()-1]].push_back(j);
        }
    }
    return turn;
}

int main(){
    vector<long long int> ps;
    ps.push_back(15);
    ps.push_back(5);
    ps.push_back(1);
    ps.push_back(4);
    ps.push_back(7);
    ps.push_back(0);
    vector<long long int> res = simul(ps);
    cout << res[29999999] << endl;
}
