
from banco import Banco
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
bb = Banco('bb')


c = ContaCorrente('maria',100,bb)
c.set_depositar(100)
c.set_sacar(10)
c.saldo
c.set_depositar(500)
print(c.extrato())

cp = ContaPoupanca('joao',bb,100)
cp.set_depositar(500)
print(cp.saldo)
cp.set_sacar(400)
# print(cp.encerrarConta())
print(cp.extrato())

print(f"corrente{ContaCorrente.mostrarContasC()}")
print(f"pupanca{ContaPoupanca.mostrarContasP()}")
