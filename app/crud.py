from sqlalchemy.orm import Session
from . import models, schemas

def get_all_terms(db: Session):
    return db.query(models.GlossaryItem).all()

def get_term_by_name(db: Session, term: str):
    return db.query(models.GlossaryItem).filter(models.GlossaryItem.term == term).first()

def create_term(db: Session, term: schemas.GlossaryItemCreate):
    db_item = models.GlossaryItem(**term.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_term(db: Session, term_id: int, update_data: schemas.GlossaryItemBase):
    db_item = db.query(models.GlossaryItem).get(term_id)
    if db_item:
        for key, value in update_data.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_term(db: Session, term_id: int):
    db_item = db.query(models.GlossaryItem).get(term_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
