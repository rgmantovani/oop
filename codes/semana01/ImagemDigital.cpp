// iostream -> entrada e saída de dados
// input/output stream
#include <iostream>
#include <typeinfo>
#include <string>

// necessário para chamar std::cout (print) e std::endl ('\n')
using namespace std;

// Criando uma classe puramente vazia
class ImagemDigital {

    // atributos
    int altura, largura; // resolucao
    string nome, extensao;
    int canaisDeCores;
    int **imagemDigital;

    // funcoes/métodos
    ImagemDigital();  // construtor
    ~ImagemDigital(); // destrutor
    void mostrar(); 
    int** rotacionar(float angulo);
    int** reescalar(float valor);

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

