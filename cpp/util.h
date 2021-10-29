#include <map>
#include <vector>
#include <string>


std::map<std::string,std::vector<std::vector<int> > > encode(std::vector<std::vector<std::string> > maze);
std::string readFromFile();
void split(char quote[]);