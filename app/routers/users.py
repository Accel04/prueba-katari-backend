from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schemas.Usuario)
def create_user(usuario: schemas.UsuarioCreate, empresa_id: int, db: Session = Depends(get_db)):
    user_by_email = crud.get_user_by_email(db, correo=usuario.correo)
    if user_by_email:
        raise HTTPException(status_code=400, detail="Correo registrado")
    return crud.create_user(db=db, usuario=usuario, empresa_id=empresa_id)

@router.get("/{usuario_id}", response_model=schemas.Usuario)
def read_user(usuario_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, usuario_id=usuario_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.get("/", response_model=list[schemas.Usuario])
def list_users(db:Session = Depends(get_db)):
    list_users = crud.get_all_users(db)
    return list_users