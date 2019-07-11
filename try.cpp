#include <iostream>

#define print cout<<
#define input cin>>

using namespace std;

void getBMI(){
    double weight, height, bmi;

    print "\nInput Weight(kg): ";
    input weight;
    print "\nInput Height(m): ";
    input height;

    bmi = weight / (height * height);

    print "\nYour BMI: [" << bmi << "]\n";

    print "\nTable Values\nUnderweight:\t18.5 Below\nNormal:\t\tbetween 18.5 and 24.9\nOverweight:\t25 and 29.9\nObese:\t\tAbove 30\n";

}

void getGasMileage(){
    double miles, gas, mpg, tMiles = 0, tGas = 0, tMpg;
    int ctr = 1, dec;

    do{
        print "\nInput Miles in Trip #" << ctr << ": ";
        input miles;
        print "\nInput Gas in Trip #" << ctr << ": ";
        input gas;

        tMiles += miles;
        tGas += gas;

        mpg = miles / gas;
        tMpg = tMiles / tGas;

        print "\nMPG in Trip #" << ctr << ": [" << mpg << "]";
        print "\nTotal MPG for all the Trip: [" << tMpg<< "]";

        print "\n==================\nCon" << ctr << ": ";
        input miles;
        ctr++;
    }while(dec == 0);


}

int main(){
    int dec;
    print "\n(0) for BMI and (1) for Gas Mileage\nYour Input: ";
    input dec;

    dec == 0 ? getBMI() : getGasMileage();
    return 0;
}