# Automação de Testes com Selenium

Este repositório contém um script Python que automatiza testes para um sistema web utilizando o Selenium. O script executa ações como cadastro de alunos, cursos, disciplinas e valida mensagens de retorno apresentadas na interface.

## Requisitos

Certifique-se de que o ambiente atenda aos seguintes requisitos:

- **Python 3.8 ou superior** instalado.
- Navegador **Google Chrome** instalado.
- **Driver do Chrome** compatível com a versão do navegador.
- Bibliotecas Python listadas no [requirements.txt](#instalação).

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/antoniosvale/automacao_testes.git
   cd automacao_testes

## Execução
   - Instale os requisitos do projeto
   ```bash
   pip install -r requirements.txt
   ```
   - Execute o teste de exemplo. Garanta que o Chrome esteja instalado na sua máquina.
   ```bash
   python -m pytest -k test_final_exercise_raw.py
