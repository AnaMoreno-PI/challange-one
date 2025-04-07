from api.models import characters, users
from sqlalchemy.orm import Session

def db_global_init(engine):
    characters.Base.metadata.create_all(bind=engine)
    users.Base.metadata.create_all(bind=engine)
    initialize_user_types(engine)

def initialize_user_types(engine):
    """
    Inserta los tipos de usuario predeterminados en la tabla user_types si no existen.
    """
    with Session(engine) as session:
        if not session.query(users.UserType).count():
            session.add_all([
                users.UserType(name="Admin"),
                users.UserType(name="User")
            ])
            session.commit()