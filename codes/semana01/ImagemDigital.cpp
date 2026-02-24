// iostream -> entrada e saída de dados
// input/output stream
#include <iostream>
#include <typeinfo>

// necessário para chamar std::cout (print) e std::endl ('\n')
using namespace std;

// Criando uma classe puramente vazia
class ImagemDigital {

};

// Função principal
int main(int argc, char const *argv[])
{
    cout << "Criando objeto vazio diretamente!" << endl;
    ImagemDigital foto;
    cout << typeid(foto).name() << endl;
    cout << "Criando objeto vazio via ponteiro!" << endl;
    ImagemDigital* foto2 = new ImagemDigital();
    return 0;
}

