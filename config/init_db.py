from api.models import characters


def db_global_init(engine):
    characters.Base.metadata.create_all(bind=engine)