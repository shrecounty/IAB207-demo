# Purpose: Create the database - run whenever you update/make the models.py file
from travel import db, create_app
from travel.models import *
from sqlalchemy import text

# To recreate one table only:
# db.session.execute(text('DROP TABLE IF EXISTS table_name'))
# db.create_all()

app = create_app()
ctx = app.app_context()
ctx.push()
db.drop_all()
db.create_all()