from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/terms/", response_model=list[schemas.GlossaryItemResponse])
def get_terms(db: Session = Depends(get_db)):
    return crud.get_all_terms(db)

@app.get("/terms/{term}", response_model=schemas.GlossaryItemResponse)
def get_term(term: str, db: Session = Depends(get_db)):
    db_item = crud.get_term_by_name(db, term)
    if not db_item:
        raise HTTPException(status_code=404, detail="Term not found")
    return db_item

@app.post("/terms/", response_model=schemas.GlossaryItemResponse)
def create_term(term: schemas.GlossaryItemCreate, db: Session = Depends(get_db)):
    return crud.create_term(db, term)

@app.put("/terms/{term_id}", response_model=schemas.GlossaryItemResponse)
def update_term(term_id: int, term_data: schemas.GlossaryItemBase, db: Session = Depends(get_db)):
    db_item = crud.update_term(db, term_id, term_data)
    if not db_item:
        raise HTTPException(status_code=404, detail="Term not found")
    return db_item

@app.delete("/terms/{term_id}")
def delete_term(term_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_term(db, term_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Term not found")
    return {"message": "Term deleted successfully"}
