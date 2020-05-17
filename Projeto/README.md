#Organizando projeto
##Banco de dados
```
tab_cliente --> pedido
                  |
                  |
                  V
Pizza <----- itens_pedido
```
##Regras de funcionalide 

- Bob pede ao cliente que passe o número de
telefone fixo e caso o cliente já esteja cadastrado, Bob verifica as ultimas pizzas pedidas e as
indica outros sabores. Caso o cliente não tenha cadastro, Bob cadastra o cliente com os
seguintes dados: CODIGO (automático do sistema), TELEFONE FIXO (com DDD e
NÚMERO), TELEFONE CELULAR (com DDD e NÚMERO), NOME DO CLIENTE,
ENDEREÇO, NUMERO, COMPLEMENTO, BAIRRO, CIDADE, UF e CEP.

- Depois de encontrado ou cadastrado o cliente, BOB solicita ao cliente qual a(s) pizza(s)
escolhida(s), juntamente com o(s) tamanho(s), a qual o sistema deve gerar um pedido
(contendo NÚMERO DO PEDIDO, DATA DO PEDIDO, HORA, CLIENTE e os ITENS
(pizza(s)) que o pedido contém)

- Além do VALOR TOTAL que deve fornecer ao cliente, o mesmo precisa saber se o cliente irá
precisar de troco para que o motoboy leve o dinheiro contado ao cliente (O sistema faz a
conta de quanto de troco o motoboy precisa levar para o cliente). O sistema também deve
fazer uma previsão de quanto tempo a(s) pizza(s) será(ão) entregue(s). Em média, o tempo
de espera é de 50 minutos após o pedido ser feito, independente da quantidade de pizzas.

- Os valores das pizzas são calculados com base no Valor Padrão de Custo, sendo:
Tamanho Médio para Venda: 15% a mais do Valor Padrão de Custo;
Tamanho Grande para Venda: 25% a mais do Valor Padrão de Custo;
Tamanho Gigante para Venda: 35% a mais do Valor Padrão de Custo;

- Bob precisa fazer a implementação de um sistema em sua pizzaria e para isso, contratou
você para que desenvolva o sistema, tendo as seguintes funcionalidades:
> - Cadastro e manutenção dos clientes* que estarão fazendo os pedidos de pizzas:
> - Cadastro e manutenção das pizzas* que a Pizzaria prepara. Um fato importante é que a
pizzaria está em expansão, devendo Bob aumentar a quantidade de sabores para melhor
atender seus clientes.
> - Movimentação dos Pedidos* dos clientes, onde serão controlados os pedidos que os
clientes estão fazendo.

##Detalhamentos de funcionalidades:

- Um cliente pode fazer pedidos de até ½ sabor por pizza (do mesmo tamanho), não sendo
possível dividir em mais de 2 partes uma única pizza. Fazendo esse tipo de pedido, será
cobrado o maior valor da pizza escolhido;
- Depois de escolhida a pizza, não há possibilidade de alterar o pedido. Caso o cliente insista
em fazer a alteração, é necessário fazer o cancelamento do pedido por completo e gerar um
novo pedido para o cliente. O funcionário que estará atendendo o mesmo deverá deixar o
cliente ciente de que o horário de entrega também irá ser alterado, pois irá ser colocado ao
final da fila, sendo considerado um novo pedido.
- Cadastro e manutenção das Clientes*: Necessário implementar as rotinas de inclusão,
alteração, consulta e exclusão dos mesmos; As consultas devem ser feitas pelo códigos
(Código do cliente) e pelo número de telefone fixo; As exclusões não podem acontecer caso
o cliente já tenha feito algum pedido;
- Cadastro e manutenção de Pizzas*: Necessário implementar as rotinas de inclusão,
alteração, consulta e exclusão dos mesmos; Para a exclusão de uma pizza é somente
necessário preencher o campo DATA_INATIVACAO (exclusão lógica). Nas consultas de
pizzas, caso o registro contenha este campo preenchido, é necessário não aparecer nas
consultas. (exclusão lógica). Consultas devem ser feitos pelo código; As pizzas do cardápio
já devem estar previamente cadastradas através de uma rotina (função para fazer a inserção
das pizzas padrão).
- Movimentação de Pedidos*: Necessário implementar as rotinas de inclusão, consulta (pelo
CODIGO_PEDIDO), e exclusão. Nos pedidos, o sistema deve calcular o troco do cliente
caso necessário, o tempo previsto para entrega, total do pedido do cliente.

##Resultados
- Relatório de clientes, com todos os dados cadastrais de clientes;
- Relatório de clientes, com CODIGO, NOME e quantidade de clientes cadastrados;
(Parametrizado por período de data inicio e data fim do cadastro);
- Relatório das pizzas, com todos os dados cadastrais da pizza, incluindo o calculo dos
valores vendas (médio, grande e gigante);
- Relatório de pedidos entre um período, com CODIGO_PEDIDO, DATA, CLIENTE E TOTAL
DO PEDIDO, contendo um total geral no fim do relatório; (Parametrizado por data inicial e
final do pedido);
- Qual a pizza que possui maior receita (incluindo todos os tamanhos);
- Qual a pizza que possui menor receita (incluindo todos os tamanhos);