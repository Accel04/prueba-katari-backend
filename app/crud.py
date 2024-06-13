from sqlalchemy.orm import Session
from . import models, schemas
from .security import get_password_hash

def get_company(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()

def get_all_companies(db:Session):
    return db.query(models.Empresa).all()

def get_company_by_subdomain(db: Session, subdominio: str):
    return db.query(models.Empresa).filter(models.Empresa.subdominio == subdominio).first()

def create_company(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(nombre=empresa.nombre, subdominio=empresa.subdominio)
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def get_user(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def get_all_users(db: Session):
    return db.query(models.Usuario).all()

def get_user_by_email(db: Session, correo: str):
    return db.query(models.Usuario).filter(models.Usuario.correo == correo).first()

def create_user(db: Session, usuario: schemas.UsuarioCreate, empresa_id: int):
    hashed_password = get_password_hash(usuario.password)
    db_usuario = models.Usuario(nombre=usuario.nombre, apellidos=usuario.apellidos, dni=usuario.dni,
                                correo=usuario.correo, hashed_password=hashed_password, empresa_id=empresa_id)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario