# Trabalhos Compilador
Trabalhos para a construção de um compilador feito em python
> Funciona apenas no linux

#### Grupo
- Antonio Cicero Azevedo - 811455
- João Paulo Migliati - 802534
- João Otávio Langer - 811797

<details>
<summary><strong> Setup do projeto </strong></summary>

#### Dado que você so tem pip 😔
> O python 3.13 deve estar instalado na sua maquina se for seguir esse caminho 
ou baixar via [pyenv](https://github.com/pyenv/pyenv) 

- Criar o ambiente virtual
```bash
python -m venv .venv
```
- Ativar o ambiente virtual
```bash
source .venv/bin/activate
```
- Baixar as dependências do projeto
```bash
pip install .
```
#### Se voce tiver o [uv](https://docs.astral.sh/uv/) 😊
- Basta rodar
```bash
uv sync
```
- Depois entrar no ambiente virtual
```bash
source .venv/bin/activate
```
</details>

<details>
<summary><strong> Analisador léxico </strong></summary>

- Implementação de um analisador léxico para a linguagem LA.
- Ele deve ler um programa-fonte e produzir uma lista de tokens identificados.
- Como rodar:
- Entra no ambiente virtual
```bash
source .venv/bin/activate
```
- Depois executa o comando corretor automático passando os respectivos diretórios
```bash
java -jar compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar "compilador" gcc compilador/temp compilador/casos-de-teste "811455, 802534, 811797" t1
```
> Ex: $ compilador tests/files/input/test1.la
- O output será gerado no diretório `tests/files/output/`
</details>
