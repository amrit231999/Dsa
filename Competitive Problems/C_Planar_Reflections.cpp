#include<bits/stdc++.h>
using namespace std;

int main(){
    string str;
    cin>>str;
    stack<char>st;
    int curLen=0,maxLen=0,curCount=0,maxCount=0;
    for(auto c: str){
        if(c=='('){
            st.push(c);
        }
        else{
            if (st.size()!=0){
                curLen+=1;
                if(curLen==maxLen){
                    curCount+=1;
                    maxCount=curCount;
                }
                else if (curLen>maxLen){
                    curCount=1;
                    maxCount=curCount;
                    maxLen=curLen;

                }
                st.pop();

            }
            else{
                curLen=0;
                curCount=0;
            }
        }
    }
    cout<<maxLen*2<<" "<<1+maxCount;
}