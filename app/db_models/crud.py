from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db_models.base import Project, Ticket

class RecordNotFound(Exception):
    pass

def create_project(db: Session, name: str, description: str) -> Project:
    try:
        new_project = Project(name=name, description=description)
        db.add(new_project)
        db.commit()
        db.refresh(new_project)
        return new_project
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_project(db: Session, project_id: int) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise RecordNotFound(f"Project with id {project_id} not found")
    return project

def update_project(db: Session, project_id: int, name: str, description: str) -> Project:
    project = get_project(db, project_id)
    try:
        project.name = name
        project.description = description
        db.commit()
        db.refresh(project)
        return project
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def delete_project(db: Session, project_id: int) -> Project:
    project = get_project(db, project_id)
    try:
        db.delete(project)
        db.commit()
        return project
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def create_ticket(db: Session, project_id: int, title: str, description: str, status: str, priority: str) -> Ticket:
    try:
        new_ticket = Ticket(project_id=project_id, title=title, description=description, status=status, priority=priority)
        db.add(new_ticket)
        db.commit()
        db.refresh(new_ticket)
        return new_ticket
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_ticket(db: Session, ticket_id: int) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise RecordNotFound(f"Ticket with id {ticket_id} not found")
    return ticket

def update_ticket(db: Session, ticket_id: int, title: str, description: str, status: str, priority: str) -> Ticket:
    ticket = get_ticket(db, ticket_id)
    try:
        ticket.title = title
        ticket.description = description
        ticket.status = status
        ticket.priority = priority
        db.commit()
        db.refresh(ticket)
        return ticket
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def delete_ticket(db: Session, ticket_id: int) -> Ticket:
    ticket = get_ticket(db, ticket_id)
    try:
        db.delete(ticket)
        db.commit()
        return ticket
    except SQLAlchemyError as e:
        db.rollback()
        raise e
