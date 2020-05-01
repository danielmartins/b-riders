

# SQLAlchemy specific code, as with any other app
import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

categories = sqlalchemy.Table(
    "Category",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.Text),
)

rides = sqlalchemy.Table(
    "Ride",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("begin", sqlalchemy.DateTime),
    sqlalchemy.Column("end", sqlalchemy.DateTime),
    sqlalchemy.Column("category", sqlalchemy.Integer),
    sqlalchemy.Column("grade", sqlalchemy.ForeignKey()),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)