#include <vector>
#include <iostream>
using namespace std;

int main() {
    std::vector<int> list_val = {10,20,30,40,50,100};

    for (auto iter = list_val.begin(); iter != list_val.end();) {
        if (*iter >= 10) {
            std::cout << " erase :" << *iter << std::endl;
            list_val.erase(iter);
            // iter = list_val.erase(iter);
        } else {
            ++iter;
        }
    }
    return 0;
}
