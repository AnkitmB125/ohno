#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	cout<<"Hello"<<endl;
	int n;
	cin>>n;
	vector<int>A(n);
	for (int i = 0; i < n; ++i)
	{
		cin>>A[i];
	}
	sort(A.begin(), A.end());
	for(int i=0;i<n;i++)
	{
		cout<<A[i]<<" ";
	}
	cout<<endl;

	return 0;
}