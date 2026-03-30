class Time {

    public:
        Time(int = 0, int = 0, int = 0); //construtor-padrão
        
        void setTime(int, int, int);     // confgura hora, minuto, segundo
        void setHour(int);               // configura hora (depois da validação)
        void setMinute(int);             // configura minutos (depois da validação
        void setSecond(int);             // configura segundos  (depois da validação

        int getHour();
        int getMinute();
        int getSecond();

        void printUniversal();           // imprime a hora no formato de data/hora universal
        void printStandard();            // imprime a hora no formato-padrão de data/hora
    
    private:
        int hour;   // 0 - 23 (formato de relógio de 24 horas)
        int minute; // 0 - 59
        int second; // 0 - 59
};