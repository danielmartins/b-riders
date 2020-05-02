import typer

from b_riders.commands import db, users, rides

app = typer.Typer()

app.add_typer(db.app, name="db")
app.add_typer(users.app, name="users")
app.add_typer(rides.app, name="rides")
