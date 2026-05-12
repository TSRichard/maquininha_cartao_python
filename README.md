# 🏦 Maquininha de Cartão Simulada

Um sistema simples em Python que simula as funcionalidades básicas de uma maquininha de cartão de crédito/débito, incluindo cálculos de acréscimos por parcelamento.

## ✨ Funcionalidades

- ✅ Vendas com cartão de **débito** (sem acréscimo)
- ✅ Vendas com cartão de **crédito** (com opção de parcelamento)
- ✅ Cálculo automático de acréscimos por número de parcelas:
  - À vista (1x): sem acréscimo
  - 2x a 3x: 2% de acréscimo
  - 4x a 6x: 4% de acréscimo
  - 7x a 12x: 6% de acréscimo
- ✅ Exibição do valor total final e valor por parcela
- ✅ Validação de entradas do usuário

## 📋 Pré-requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária (apenas bibliotecas padrão)

## 🚀 Como executar

1. **Clone ou baixe o projeto**
   ```bash
   git clone https://github.com/seu-usuario/maquininha-python.git
   cd maquininha-python
2. **Execute o programa
   ```bash
   python main.py

📁 Estrutura do projeto

    maquininha/
    ├── main.py           # Interface principal do programa
    ├── transacao.py      # Lógica de negócio (cálculos de transação)
    ├── utils.py          # Funções auxiliares (validação de entrada)
    └── README.md         # Documentação do projeto
    └── LICENSE 

🎯 Possíveis melhorias futuras

    -Salvar histórico de transações em arquivo (JSON/CSV)
    -Adicionar taxa da maquininha (ex: 2% sobre cada venda
    -Função de cancelamento de venda
    -Interface gráfica (Tkinter ou PyQt)
    -Gerar comprovante em PDF
    -Integração com APIs reais de adquirentes (Cielo, Stone, PagSeguro)

👨‍💻 Autor
Richard Teixeira

Estudante de Sistemas de Informação apaixonado por tecnologia.
📚 Atualmente: Python, JSON
🎯 Meta: Primeira oportunidade como desenvolvedor

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/TSRichard)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tsrichard/)

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
