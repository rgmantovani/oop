// --------------------------------------------
// --------------------------------------------

#include "Time2.h"

#include<iostream>
#include<iomanip>

using namespace std;

// --------------------------------------------
// --------------------------------------------

Time::Time(int hr, int min, int sec) {
    setTime(hr, min, sec);
}

// --------------------------------------------
// --------------------------------------------

void Time::setTime(int h, int m, int s) {
    setHour(h);
    setMinute(m);
    setSecond(s);
}

// --------------------------------------------
// --------------------------------------------

void Time::setHour(int h) {
    hour   = (h >= 0 && h < 24) ? h : 0; // valida horas
}

// --------------------------------------------
// --------------------------------------------
void Time::setMinute(int m) {
    minute = (m >= 0 && m < 60) ? m : 0; // valida minutos
}

// --------------------------------------------
// --------------------------------------------
void Time::setSecond(int s) {
    second = (s >= 0 && s < 60) ? s : 0;
}

// --------------------------------------------
// --------------------------------------------
int Time::getHour() {
    return hour;
}

// --------------------------------------------
// --------------------------------------------
int Time::getSecond() {
    return second;
}

// --------------------------------------------
// --------------------------------------------
int Time::getMinute() {
    return minute;
}

// --------------------------------------------
// --------------------------------------------

void Time::printUniversal() {
    cout << setfill('0') << setw(2) << hour << ":" << setw(2) 
        << minute << ":" << setw(2) << second;
}

// --------------------------------------------
// --------------------------------------------

void Time::printStandard() {
    cout << ( ( hour == 0 || hour == 2) ? 12 : hour%12 ) << ":"
        << setfill('0') << setw(2) << minute << ":" << setw(2)
        << second << (hour < 12 ? "AM" : "PM");
}

// --------------------------------------------
// --------------------------------------------

int main(int argc, char* argv[]) {

    // todos os argumentos convertidos para sua configuração padrão
    Time t1;
    // hour especificada, minute e second convertidos para padrão
    Time t2 (2);
    // hour e minute especificados, second para padrão
    Time t3 (21, 24);
    // hour, minute, second especificados
    Time t4 (12, 25, 42);
    // valores inválidos especificados
    Time t5 (27, 74, 99);

    cout << "The initial universal time is ";
    t1.printUniversal();
    cout << "\nThe initial standard time is ";
    t1.printStandard();

    cout << "\nThe initial universal time is ";
    t2.printUniversal();
    cout << "\nThe initial standard time is ";
    t2.printStandard();

    cout << "\nThe initial universal time is ";
    t3.printUniversal();
    cout << "\nThe initial standard time is ";
    t3.printStandard();

    cout << "\nThe initial universal time is ";
    t4.printUniversal();
    cout << "\nThe initial standard time is ";
    t4.printStandard();

    cout << "\nThe initial universal time is ";
    t5.printUniversal();
    cout << "\nThe initial standard time is ";
    t5.printStandard();

    // Construtor por copia, implícito
    Time t6 = t5;
    cout << "\nThe initial universal time is ";
    t6.printUniversal();
    cout << "\nThe initial standard time is ";
    t6.printStandard();

    return 0;
}

// --------------------------------------------
// --------------------------------------------