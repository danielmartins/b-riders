import typer

from b_riders import crud, schemas
from b_riders.db.session import SessionLocal

app = typer.Typer()

DEFAULT_QUEUE = "default"


@app.command()
def create(email: str, password: str, is_superuser: bool = False):
    """
    Cria usuário
    """
    db = SessionLocal()
    user = crud.user.get_by_email(db, email=email)
    if not user:
        user_in = schemas.UserCreate(
            email=email,
            password=password,
            is_superuser=is_superuser,
        )
        crud.user.create(db, obj_in=user_in)  # noqa: F841
        typer.echo("User created!")
    else:
        typer.echo("User already exists")


@app.command()
def ls():
    """
    Lista usuários
    """
    db = SessionLocal()

    # Base.metadata.create_all(bind=engine)

    users = crud.user.get_multi(db)
    for user in users:
        typer.echo(f"{user.email}")
