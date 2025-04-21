# Trabalhos Compilador
Trabalhos para a construção de um compilador feito em python

#### Grupo
- Antonio Cicero Azevedo - 811455
- João Paulo Migliati - 802534
- João Otávio Langer - 811797

</details>
<details>
<summary><strong> Setup do projeto </strong></summary>

#### Dado que você so tem pip
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
#### Se voce tiver o [uv](https://docs.astral.sh/uv/) 
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

```bash
compilador --path
```
> Ex: $ compilador tests/files/input/test1.la
- O output será gerado no diretório `tests/files/output/`
</details>
