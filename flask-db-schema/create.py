from app import db, Users, People

db.drop_all()
db.create_all()

testuser = Users(first_name='Hassan',last_name='Shah')
testpeople = People(name='Jane', height=2.1)
db.session.add(testuser)
db.session.add(testpeople)
db.session.commit()



