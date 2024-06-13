from pydantic import BaseModel
from typing import List, Optional

class UsuarioBase(BaseModel):
    nombre: str
    apellidos: str
    dni: str
    correo: str

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    empresa_id: int

    class Config:
        orm_mode = True

class EmpresaBase(BaseModel):
    nombre: str
    subdominio: str

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int
    usuarios: List[Usuario] = []

    class Config:
        orm_mode = True