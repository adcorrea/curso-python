# Exercício com Abstração, Herança, Encapsulamento e Polimorfismo

# Criar um sistema bancário (extremamente simples) que tem clientes, contas
# e um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente)
# e que possa sacar/depositar nessa conta. contas corrente tem um limite extra.

# Conta(ABC):
#     ContaCorrente
#     ContaPoupanca

# Pessoa(ABC):
#     Cliente
#         Cliente -> Conta

# Banco
#     Banco -> Cliente
#     Banco -> Conta

# Dicas:

# Criar classe Cliente que herda da classe Pessoa (Herança)
#     Pessoa tem nome e idade (com getters)
#     Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupança)

# Criar classes ContaPoupança e ContaCorrente que herdam de Conta
#     ContaCorrente deve ter um limite extra
#     Contas têm agência, número da conta e saldo
#     Contas devem ter método para depósito
#     Conta (super classe) deve ter o método sacar abstrato (Abstração e
#             polimorfismo -  as subclasses que implementam o método sacar)

# Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
# Banco será responsável autenticar o cliente e as contas das seguinte maneira:
#     Banco tem contas e cliente (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco

# Só será possível sacar se passar na autenticação do banco (descrita acima )
# Banco autentica por um método.

from banco.banco import Banco
from banco.conta import ContaCorrente, ContaPoupança
from banco.pessoa import Cliente
from banco.excecoes import SaldoInsuficienteError, AutenticacaoErro


if __name__ == '__main__':

    banco_bamerindus = Banco('Banco Bamerindus')

    correntista = Cliente('Antonio Junior', '12234', 37)
    conta_corrente = ContaCorrente('11', '3366')
    correntista.abrir_conta(conta_corrente)    

    
    banco_bamerindus.incluir_cliente(correntista)

    correntista_poupanca = Cliente('Chuck Norris', '12234', 65)
    conta_poupanca = ContaPoupança('123', '3654')
    correntista_poupanca.abrir_conta(conta_poupanca)

    banco_bamerindus.incluir_cliente(correntista_poupanca)

    banco_bamerindus.listar_clientes()

    try:
        correntista.conta.depositar(1000.00)
        correntista.conta.sacar(500.00)
        correntista.conta.sacar(1500.00)
    except SaldoInsuficienteError as ex:
        print(ex)



    try: 
        correntista.conta.limite_extra = 3000.00
        correntista.conta.sacar(1500.00)
    except SaldoInsuficienteError as ex:
        print(ex)
        correntista.conta.mostrar_saldo()


    try:
        correntista_poupanca.conta.depositar(3000.00)
        correntista_poupanca.conta.sacar(1000)
        correntista_poupanca.conta.sacar(4000.00)
    except SaldoInsuficienteError as ex:
        print(ex)
        correntista_poupanca.conta.mostrar_saldo()



    banco_bamerindus.listar_clientes()


    try:
        banco_bamerindus.autenticar('12', '123', '123456')
    except AutenticacaoErro as ex:
        print(ex)


    try:
        banco_bamerindus.autenticar('123', '3654', '12234')
    except AutenticacaoErro as ex:
        print(ex)


    



