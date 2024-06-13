from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    subdominio = Column(String, unique=True, index=True)

    usuarios = relationship("Usuario", back_populates="empresa")


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellidos = Column(String, index=True)
    dni = Column(String, unique=True, index=True)
    correo = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    empresa = relationship("Empresa", back_populates="usuarios")