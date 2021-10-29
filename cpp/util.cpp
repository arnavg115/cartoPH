#include "util.h"
#include <iostream>
#include <vector>
#include <map>
#include <iterator>
#include <fstream>



using namespace std;
map<string,vector<vector<int> > > encode(vector<vector<string> > maze) {
    vector<vector<int> > encoded_maze;
    int inc = 0;
    vector<vector<int> > pos_list;
    for (int i = 0; i < maze.size(); i++)
    {
        vector<int> row;
        for (int j = 0; j < maze[0].size(); j++)
        {
            if(maze[i][j] == "#"){
                row.push_back(-1);
            }
            else {
                row.push_back(inc);
                vector<int> pair;
                pair.push_back(i);
                pair.push_back(j);
                pos_list.push_back(pair);
                inc++;
            }
        }
        encoded_maze.push_back(row);
    }
    map<string,vector<vector<int> > > mp;
    mp.insert(pair<string,vector<vector<int> > >("enc",encoded_maze));
    mp.insert(pair<string,vector<vector<int> > >("pos",pos_list));
    return mp;

}

string readFromFile(){
    fstream newfile;
    newfile.open("maze.txt",ios::in);
    string files;
    if (newfile.is_open()){   //checking whether the file is open
      string tp;
      while(getline(newfile, tp)){
          files= files+tp+"\n";
      }
      newfile.close();   //close the file object.
    }
    return files;
}
