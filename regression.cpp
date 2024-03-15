#include <bits/stdc++.h>
#include<fstream>

using namespace std;

float mean(vector<pair<float,float>> data,int index){
    float mean = 0;
    int n = data.size();
    for(int i = 0;i<n;i++){
        if(index==0) mean = mean + data[i].first;
        else mean = mean + data[i].second;
    }

    mean = mean/n;

    return mean;
}


pair<float,float> linRegression(vector<pair<float,float>> data){
    int n = data.size();
    float mean_x = mean(data,0);
    float mean_y = mean(data,1);

    float exp1 = 0,exp2 = 0;
    for(int i = 0;i<n;i++){
        exp1 += (data[i].first-mean_x)*(data[i].second-mean_y);
        exp2 += pow(data[i].first-mean_x,2);
    }

    float a = exp1/exp2;
    float b = mean_y - (a*mean_x);
    
    return {a,b};
}


int main(){

    ofstream datafile("data.txt");

    
    vector<pair<float,float>> data;
    for(int i = 0;i<100;i++){
        data.push_back({i,i*i});
    }

    pair<float,float> ans = linRegression(data);

    for(int i = 0;i<100;i++){
        datafile <<i<<" "<<i*i<<" "<<ans.first*i+ans.second<<endl;
    }
    cout<<ans.first<<" "<<ans.second<<endl;
    datafile.close();
}