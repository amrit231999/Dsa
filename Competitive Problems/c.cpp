#include<bits/stdc++.h>
using namespace std;
#define int long long
int n,h;
vector<int>v;
bool good(int m){
    map<int,vector<int>>pyr;
    for(int i=0;i<m;i++)pyr[i].push_back(v[i]);
    int j=0;

    for(int i=m;i<n;i++){
        auto s=pyr[j];
        
        if (pyr[j].size()>=1 && s[pyr[j].size()-1]>v[i]){
            pyr[j].push_back(v[i]);
            j+=1;
            j%=m;
        }
    }
    for(int i=0;i<m;i++){
        if (pyr[j].size()<h)return false;
    }
    return true;

}
signed main(){
    int t;
    cin>>t;
    while(t--){
        cin>>n>>h;
        v.resize(n);
        for (int i=0;i<n;i++)cin>>v[i];
        int low=0;
        int high=n+1;
        //edited
        reverse(v.begin(),v.end());
        while(low<high-1){
            int mid=(low+high)/2;
            if (good(mid)){
                low=mid;
            }
            else{
                high=mid;
            }
        }
        if(good(low)){  
            cout<<low<<endl;
        }
        else{
            cout<<0<<endl;
        }
    }


}