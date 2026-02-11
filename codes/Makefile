# Makefile para compilar todos os exemplos C++

CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra

# Encontra todos os arquivos .cpp
CPP_FILES := $(shell find . -name "*.cpp" -not -path "./semana13/*" -not -path "./semana15/*")
EXECUTABLES := $(CPP_FILES:.cpp=)

.PHONY: all clean test

all: $(EXECUTABLES)
	@echo "✅ Todos os programas compilados com sucesso!"

%: %.cpp
	@echo "Compilando $<..."
	@$(CXX) $(CXXFLAGS) $< -o $@

clean:
	@echo "Limpando executáveis..."
	@find . -type f -executable -delete
	@echo "✅ Limpeza concluída!"

test: all
	@echo "🧪 Executando testes..."
	@for exe in $(EXECUTABLES); do \
		echo ""; \
		echo "=== Testando $$exe ==="; \
		./$$exe || true; \
	done

help:
	@echo "Comandos disponíveis:"
	@echo "  make         - Compila todos os exemplos C++"
	@echo "  make clean   - Remove todos os executáveis"
	@echo "  make test    - Compila e executa todos os programas"
	@echo "  make help    - Mostra esta ajuda"
