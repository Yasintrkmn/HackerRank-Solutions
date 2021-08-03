#include<iostream>
#include <vector>

using namespace std;
vector<int> vect{ 10, 20, 30, 40, 50 };

int findIndex(int V, vector<int> vect)
{
	for (int i = 0; i < vect.size(); i++)
	{
		if (vect[i] == V) { return i; }
	}
}
int main()
{
	cout << findIndex(30, vect) << endl;

	return 0;
}
