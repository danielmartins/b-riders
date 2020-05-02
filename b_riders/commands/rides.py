import typer

from b_riders import crud, schemas
from b_riders.db.session import SessionLocal

app = typer.Typer()

DEFAULT_QUEUE = "default"


@app.command()
def create(begin: str, end: str, experience: int, user: int, classification: int):
    """
    Cria uma corrida
    """
    db = SessionLocal()
    ride_in = schemas.RideCreate(
        begin=begin,
        end=end,
        experience=experience,
        owner_id=user,
        classification_id=classification
    )
    crud.ride.create(db, obj_in=ride_in)  # noqa: F841
    typer.echo("Ride created!")


@app.command()
def ls():
    """
    Lista corridas
    """
    db = SessionLocal()

    # Base.metadata.create_all(bind=engine)

    rides = crud.ride.get_multi(db)
    for r in rides:
        typer.echo(f"{r}")
