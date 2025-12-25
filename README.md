duplicate-file-manager: Python tool to scan folders and subfolders, detect duplicate files reliably (e.g., by size + hash), and assist with safe cleanup. Roadmap includes optional deletion of duplicates, organization into year/month directories (e.g., 2025/01), and reporting for auditing.

# Duplicate File Manager

Duplicate File Manager é um aplicativo Python com interface gráfica (Tkinter) para encontrar arquivos duplicados em qualquer pasta do seu computador (Windows, Linux ou Mac).

## Funcionalidades
- Interface gráfica simples e intuitiva
- Seleção de pasta raiz para busca
- Busca de arquivos duplicados por hash (MD5)
- Exibição dos arquivos duplicados encontrados

## Instalação
O aplicativo utiliza apenas bibliotecas padrão do Python. Tkinter já vem incluso na maioria das instalações.

**Se necessário, instale o Tkinter:**
- **Ubuntu/Debian:**
	```bash
	sudo apt-get install python3-tk
	```
- **Mac:** já incluso
- **Windows:** já incluso

## Como executar
1. Clone ou baixe este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute:
	 ```bash
	 python3 duplicate_file_manager.py
	 ```

## Como usar
1. Clique em "Procurar" e selecione a pasta raiz onde deseja buscar duplicados.
2. Clique em "Buscar Duplicados".
3. Os arquivos duplicados encontrados serão exibidos em uma nova janela.

## Roadmap
- Exclusão segura de duplicados (opcional)
- Organização automática em subpastas por ano/mês
- Relatórios para auditoria

## Requisitos
Veja o arquivo `requirements.txt` para detalhes.

---
Desenvolvido com Python 3 e Tkinter.
