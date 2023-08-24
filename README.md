# djangoproduto

Passos utilizados para gerar o MCVE

- django-admin startproject djangoproduto
- cd djangoproduto
- python startapp produto
- editar o settings.py para adicionar uma nova app `produto`
- adicionar o conteúdo do `models.py`
- executar o comando: `python manage makemigrations`
- executar o comando: `python manage migrate`

Após esses passos, é possível ver o DDL gerado para a tabela `produtos`.
Com o comando:

    python manage.py sqlmigrate produto 0001_initial
    

Este é o conteúdo

    BEGIN;
    --
    -- Create model Produtos
    --
    CREATE TABLE "produtos" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "compra" decimal NOT NULL, "venda" decimal NOT NULL,
        "cotacaoCompra" decimal NOT NULL, 
        "cotacaoVenda" decimal NOT NULL, 
        "dataHoraCotacao" datetime NOT NULL, 
        "tipo" varchar(30) NOT NULL
    );
    COMMIT;


Repare que aqui existe o atributo `id` que é uma chave primária.
