#include <iostream>
#include <string>

using namespace std;

// Criando uma classe puramente vazia
class ImagemDigital {

    //  Atributos da classe
    public:
        int largura;
        int altura;
        int **imagem;  //imagem é uma matriz [altura x largura]
        string canaisCor;
        string nome;
        string extensao;
        // ... 

        ImagemDigital(int l, int a, string n, string e) {
            largura = l;
            altura = a;
            nome = n;
            extensao = e;        
        }

        string criaNome() {
            return(nome + extensao);
        }

        string retornaResolucao() {
            return(to_string(altura)+ " x " + to_string(largura));
        } 
};

// Função principal
int main(int argc, char const *argv[]) {
    cout << "Criando objeto" << endl;
    ImagemDigital foto(256, 256, "teste", ".png");
    cout << "Arquivo: " + foto.criaNome() << endl;
    cout << "Resolucao: " + foto.retornaResolucao() << endl;
    return 0;
}
