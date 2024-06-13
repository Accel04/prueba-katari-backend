from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/companies", tags=["companies"])

@router.post("/", response_model=schemas.Empresa)
def create_company(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    company_by_subdomain = crud.get_company_by_subdomain(db, subdominio=empresa.subdominio)
    if company_by_subdomain:
        raise HTTPException(status_code=400, detail="Subdominio ya se encuentra registrado")
    return crud.create_company(db=db, empresa=empresa)

@router.get("/{empresa_id}", response_model=schemas.Empresa)
def read_company(empresa_id: int, db: Session = Depends(get_db)):
    company = crud.get_company(db, empresa_id=empresa_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return company

@router.get("/", response_model=list[schemas.Empresa])
def list_companies(db: Session = Depends(get_db)):
    company_list = crud.get_all_companies(db)
    return company_list