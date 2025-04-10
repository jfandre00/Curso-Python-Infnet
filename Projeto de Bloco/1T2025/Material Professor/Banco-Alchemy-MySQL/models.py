from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Conta(Base):
    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String)
    saldo = Column(Float)

    def __init__(self, id, nome, saldo):
        self.id_cliente = id
        self.nome = nome
        self.saldo = saldo

    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        self.saldo -= valor

    def __str__(self):
        return f"{self.id_cliente} {self.nome} {self.saldo}"