#include <iostream>

using namespace std;

class remote
{

public:
    string name;
    string alpha_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    void encrypt(int shift)
    {
        cout << "ENTER THE STRING FOR ENCRYPT :";
        cin >> name;

        int l = name.length();
        for (int i = 0; i < l; i++)
        {
            char c = name[i];
            int num = alpha_char.find(toupper(c));
            num = num + shift;
            if (num > 26){
                num = num - 26;
            }
            char cypher = alpha_char[num];
            cout << cypher;
        }
        cout << "\n";
    };
    void decrypt(int shift)
    {
        cout << "ENTER THE CYPHER FOR DECRYPT :";
        cin >> name;

        int l = name.length();
        for (int i = 0; i < l; i++)
        {
            char chr = name[i];
            int num_ = alpha_char.find(toupper(chr));
            num_ = num_ - shift;
            if (num_ < 0){
                num_ = num_ + 26;
            }
            char cypher_ = alpha_char[num_];
            cout << cypher_;
        }
        cout<<"\n";
    };
};

int main()
{
    double user;
    int shift;
    cout<<"[+] ENTER THE SHIFT NO [+] :";
    cin>>shift;
   
    remote r;
    
    while (1)
    {
       
        cout << "[1] FOR ENCRYPT :: [2] FOR DECRYPT : \n";
        cin >> user;

        if (user == 1)
        {
            r.encrypt(shift);
        }
        else if (user == 2)
        {
            r.decrypt(shift);
        }
        else
        {
            cout << "ENTER WRONG CHOICE : \n";
            
        }
    }

    return 0;
}
