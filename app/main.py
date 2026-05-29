from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    notes = db.query(models.Note).order_by(models.Note.created_at.desc()).all()
    return templates.TemplateResponse(request=request, name="index.html", context={"notes": notes})


@app.post("/notes")
def create_note(title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    note = models.Note(title=title, content=content)
    db.add(note)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/notes/{note_id}/delete")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
    return RedirectResponse("/", status_code=303)