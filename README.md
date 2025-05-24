# DesafioDio_CriandoUmSistemaBancario

Este projeto é um sistema bancário simples desenvolvido em Python, executado no terminal. Ele permite ao usuário realizar operações básicas como depósitos, saques e consultar o extrato da conta.

📋 Funcionalidades
1. Depositar
O usuário pode realizar depósitos informando um valor positivo.

O saldo é atualizado e o depósito é registrado no extrato.

Caso o valor informado seja inválido (menor ou igual a zero), a operação é negada.

2. Sacar
Permite ao usuário realizar saques, respeitando as seguintes regras:

Valor do saque não pode exceder R$500 por operação.

O número de saques diários é limitado a 3.

O valor solicitado não pode ser maior que o saldo atual.

O saldo é atualizado e o saque é registrado no extrato.

Caso alguma regra seja violada, a operação é negada com uma mensagem explicativa.

3. Extrato
Exibe todas as movimentações realizadas (depósitos e saques).

Exibe também o saldo atual da conta.

Caso não haja movimentações, exibe uma mensagem informando isso.

4. Sair
Encerra o programa.

🧠 Regras de Negócio
Saldo Inicial: R$0,00

Limite por saque: R$500,00

Limite de saques por dia: 3