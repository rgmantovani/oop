class Time {

    public:
        Time();
        void setTime(int, int, int); // confgura hora, minuto, segundo
        void printUniversal();       // imprime a hora no formato de data/hora universal
        void printStandard();        // imprime a hora no formato-padrão de data/hora
    
    private:
        int hour;   // 0 - 23 (formato de relógio de 24 horas)
        int minute; // 0 - 59
        int second; // 0 - 59
};