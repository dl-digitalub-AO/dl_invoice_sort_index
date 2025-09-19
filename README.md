# DL Invoice Sort Index

Este módulo melhora a ordenação de faturas na lista, utilizando o número sequencial da fatura em vez da string completa.

## Funcionalidade

O Odoo, por padrão, ordena as faturas (account.move) pelo campo `name`, que é uma string. Isso pode levar a uma ordenação incorreta quando os números das faturas não têm o mesmo número de dígitos (por exemplo, `INV/2024/10` vem antes de `INV/2024/2`).

Este módulo resolve o problema adicionando um novo campo `name_sort_index` ao modelo `account.move`. Este campo armazena a parte numérica do nome da fatura como um inteiro. A ordenação padrão da lista de faturas é então alterada para usar este novo campo, garantindo que as faturas sejam ordenadas numericamente.

## Instalação

Para instalar este módulo, coloque-o na sua pasta de addons e instale-o através da lista de Aplicações do Odoo.

## Autor

Digitalub
