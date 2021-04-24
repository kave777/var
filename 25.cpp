#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
bool izi(int n) {
	for (int j = 2; j * j <= n; j++) {
		if (n % j == 0) {
			return false;
		}
	}
	return true;
}
int main() {
	vector<int> ch(0);
	int s = 0;
	for (int i = 412567; i <= 473265; i++) {
		vector<int> izidels(0);
		for (int j = 2; j * j <= i; j++) {
			if (i % j == 0) {
				if (izi(j)) izidels.push_back(j);
				if(j!=i/j && izi(i/j)) izidels.push_back(i/j);
			}
		}
		if (izidels.size() == 2 && izidels[0] * izidels[1] == i) {
			ch.push_back(i);
			s += i;
		}
	}
	cout << ch.size() << " ";
	long double sr = s / ch.size();
	int an = -1100000;
	for (int i = 0; i < ch.size(); i++) {
		if ((abs(an - sr)) > (abs(sr - ch[i]))) {
			an = ch[i];
		}
	}
	cout << an;
}
