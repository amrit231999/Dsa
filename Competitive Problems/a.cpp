#include<bits/stdc++.h>
using namespace std;
#define int long long
vector<int>v;
int n,y,c;
int good(int m){
    int r=0;
    for (int i=0;i<n;i++){
        r+=max(v[i]-m,0ll);
    }
    if (r>=y)
        return r;
    else return 0;

}
signed main() {
    
    cin>>n>>c>>y;
    v.resize(n);
    map<int,int>freq;
    for(int i=0;i<n;i++){
        cin>>v[i];
        freq[v[i]]+=1;
    }
    int cnt=0;
    int prev=0;
    int del=0;
    for (auto i: freq){
        if (cnt<c){
            del+=i.first-prev;
            prev=i.first;
        }
        
        else{
            break;
        }

        cnt+=1;
        
    }
    for (int i=0;i<n;i++){v[i]-=del;v[i]=max(v[i],0ll);}

    sort(v.begin(),v.end());

    for (auto i:v)cout<<i<<" ";
    cout<<endl;


    int low=0;
    int high=1e11;
    pair<int,int>ans(-1,-1);
    while (low<high-1){
        int mid=(low+high)/2;
        c=good(mid);
        if (c){
            low=mid;
            ans.first=mid;
            ans.second=c;
        }
        else{
            high=mid;
        }
    }
    if (good(low)){
        ans.first=low;
        ans.second=good(low);
    }
    if ((ans.first)!=-1){
    cout<<ans.first<<" "<<ans.second<<"\n";
    return 0;
    }
    cout<<-1<<"\n";




    return 0;
}