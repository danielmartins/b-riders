import alembic
import typer

app = typer.Typer()

DEFAULT_QUEUE = "default"


@app.command()
def migrate():
    alembic_args = [
        '--raiseerr',
        'upgrade', 'head',
    ]
    alembic.config.main(argv=alembic_args)


@app.command()
def create_tables():
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # db = SessionLocal()

    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841


@app.command()
def echo(message: str, queue_name: str = DEFAULT_QUEUE):
    typer.echo(message)
