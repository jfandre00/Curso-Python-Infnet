Tema: Sistema de Gerenciamento de Receitas

Objetivo: Criar um sistema para gerenciar receitas de culinária, onde cada receita tem um nome, uma lista de ingredientes e uma categoria (ex.: sobremesa, prato principal, etc.). O sistema deverá incluir funções que exploram diferentes operações e lógicas, utilizando all, any, map, filter, sorted, e outras funções built-in.


O sistema deve permitir as seguintes funcionalidades:

1. Garantir que todas as receitas possuam um determinado ingrediente
Ex.: Verificar se todas as receitas têm "sal".

2. Filtrar receitas por categoria
Ex.: Mostrar apenas receitas da categoria "sobremesa".

3. Verificar se existe uma receita com um determinado ingrediente
Ex.: Verificar se alguma receita contém "chocolate".

4. Ordenar receitas por nome ou número de ingredientes
Ex.: Exibir as receitas ordenadas alfabeticamente ou pela quantidade de ingredientes.

5. Imprimir os nomes das receitas em maiúsculas
Ex.: Exibir uma lista com todos os nomes das receitas em caixa alta.

6. Adicionar novas receitas

7. Listar todas as receitas


--------------------------------------------
Saída esperada

=== Sistema de Gerenciamento de Receitas ===
1. Adicionar receita
2. Listar receitas
3. Garantir que todas as receitas possuam um ingrediente específico
4. Buscar receita com um ingrediente específico
5. Filtrar receitas por alguma categoria específica
6. Ordenar receitas
7. Transformar nomes de receitas para maiúsculas
8. Sair do programa

Exemplo de uso: 

- Opção: 1

Digite o nome da receita: Bolo de Chocolate
Digite os ingredientes separados por vírgula: farinha, açúcar, chocolate, ovo
Digite a categoria (ex.: sobremesa, prato principal): sobremesa
Saída: Receita adicionada com sucesso!

...

- Opção: 3
Digite o ingrediente para verificar: açúcar
Saída: Todas as receitas possuem "açúcar"? Sim

...

- Opção: 6
Ordenar por:
1. Nome
2. Quantidade de ingredientes

Usuário escolhe a opção 2:

Saída:
Receitas ordenadas por quantidade de ingredientes:
--> Omelete (2 ingredientes)
--> Bolo de Chocolate (4 ingredientes)
