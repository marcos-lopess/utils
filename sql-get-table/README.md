# SQL Get Table

O script `sql_get_table.py` é um utilitário Python que percorre arquivos SQL em uma pasta específica e extrai informações sobre as tabelas presentes nas queries. Ele pode ser útil para analisar rapidamente quais tabelas são referenciadas em um conjunto de scripts SQL.

### Como Usar

1. Certifique-se de ter o Python instalado em seu ambiente.

2. Clone o repositório:

   ```bash
   git clone https://github.com/marcos-lopess/utils.git

3. Navegue até o diretório `utils`:
    ```bash
   cd utils

4. Execute o script com o caminho para a pasta contendo os arquivos SQL e um texto de saida (opcional):
    ```bash
    python sql_get_table.py caminho/para/sua/pasta "SELECT * FROM # LIMIT 10;"

A saída será o arquivo `tables.txt` no mesmo diretório do script.
