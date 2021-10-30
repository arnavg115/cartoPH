#include "util.h"
#include <vector>
#include <string>
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    string file;
    file = readFromFile();
    
    split(file);
    return 0;
}