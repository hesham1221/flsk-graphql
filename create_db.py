from db import User , Posts,Base,engine

print("Creating Database.....")

Base.metadata.create_all(bind=engine)