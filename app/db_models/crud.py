from sqlalchemy.orm import Session
from app.db_models.base import Project, Ticket

def create_project(db: Session, name: str, description: str) -> Project:
  new_project = Project(name=name, description=description)
  db.add(new_project)
  db.commit()
  db.refresh(new_project)
  return new_project


def get_project(db: Session, project_id: int) -> Project:
  return db.query(Project).filter(Project.id == project_id).first()


def update_project(db: Session, project_id: int, name: str, description: str) -> Project:
  project = db.query(Project).filter(Project.id == project_id).first()
  if project:
    project.name = name
    project.description = description
    db.commit()
    db.refresh(project)
  return project


def delete_project(db: Session, project_id: int) -> Project:
  project = db.query(Project).filter(Project.id == project_id).first()
  if project:
    db.delete(project)
    db.commit()
  return project


def create_ticket(db: Session, project_id: int, title: str, description: str, status: str, priority: str) -> Ticket:
  new_ticket = Ticket(project_id=project_id, title=title, description=description, status=status, priority=priority)
  db.add(new_ticket)
  db.commit()
  db.refresh(new_ticket)
  return new_ticket


def get_ticket(db: Session, ticket_id: int) -> Ticket:
  return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def update_ticket(db: Session, ticket_id: int, title: str, description: str, status: str, priority: str) -> Ticket:
  ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
  if ticket:
    ticket.title = title
    ticket.description = description
    ticket.status = status
    ticket.priority = priority
    db.commit()
    db.refresh(ticket)
  return ticket


def delete_ticket(db: Session, ticket_id: int) -> Ticket:
  ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
  if ticket:
    db.delete(ticket)
    db.commit()
  return ticket
