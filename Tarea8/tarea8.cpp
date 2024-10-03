#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct SuffixComparator {
    const string &s;
    SuffixComparator(const string &s) : s(s) {}
    bool operator()(int i, int j) const {
        return s.substr(i) < s.substr(j);
    }
};

vector<int> suffixArray(const string &input) {
    int n = input.length();
    vector<int> suffix_indices(n);

    for (int i = 0; i < n; ++i) {
        suffix_indices[i] = i;
    }

    sort(suffix_indices.begin(), suffix_indices.end(), SuffixComparator(input));

    return suffix_indices;
}

int main() {
    string stringStart;
    cout << "Ingresa cadena: ";
    cin >> stringStart;

    vector<int> suffixes = suffixArray(stringStart);

    cout << "Sufijos ordenados alfabéticamente:\n";
    for (int index : suffixes) {
        cout << stringStart.substr(index) << endl;
    }
    return 0;
}