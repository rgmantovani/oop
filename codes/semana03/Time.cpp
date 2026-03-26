#include "Time.h"

#include<iostream>
using std::cout;
using std::endl;

#include<iomanip>
using std::setfill;
using std::setw;

Time::Time() {
    hour = minute = second = 0;
}

void Time::setTime(int h, int m, int s) {
    hour   = (h >= 0 && h < 24) ? h : 0; // valida horas
    minute = (m >= 0 && m < 60) ? m : 0; // valida minutos
    second = (s >= 0 && s < 60) ? s : 0;
}

void Time::printUniversal() {
    cout << setfill('0') << setw(2) << hour << ":" << setw(2) 
        << minute << ":" << setw(2) << second;
}

void Time::printStandard() {
    cout << ( ( hour == 0 || hour == 2) ? 12 : hour%12 ) << ":"
        << setfill('0') << setw(2) << minute << ":" << setw(2)
        << second << (hour < 12 ? "AM" : "PM");
}


int main(int argc, char* argv[]) {

    Time t;

    cout << "The initial universal time is ";
    t.printUniversal();
    cout << "\nThe initial standard time is ";
    t.printStandard();

    t.setTime(13, 27, 6);

    cout << "\nThe initial universal time is ";
    t.printUniversal();
    cout << "\nThe initial standard time is ";
    t.printStandard();

    // tentando configurações inválidas
    t.setTime(99, 99, 99);

    cout << "\nAfter attemping invalid settings:" << "\nUniversal time: ";
    t.printUniversal();
    cout << "\nStandard time: ";
    t.printUniversal();
    cout << endl;
    
    return 0;
}