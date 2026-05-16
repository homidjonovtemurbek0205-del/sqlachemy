#1-topshiriq


from sqlalchemy import create_engine, Integer, String, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine('sqlite:///kutubxona.db', echo=True)

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'books'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nomi: Mapped[str] = mapped_column(String, nullable=False)
    muallif: Mapped[str] = mapped_column(String, nullable=False)
    narxi: Mapped[float] = mapped_column(Float)
    sahifa_soni: Mapped[int] = mapped_column(Integer)

Base.metadata.create_all(bind=engine)


with Session(engine) as session:
    k1 = Book(nomi = "Python Asoslari", muallif = "Anvar Karimov", narxi = 45.0, sahifa_soni = 320)
    k2 = Book(nomi = "Clean Code", muallif = "Robert Martin", narxi = 90.0, sahifa_soni = 450)
    k3 = Book(nomi = "Atomic Habits", muallif = "James Clear", narxi = 70.0, sahifa_soni = 280)
    k4 = Book(nomi = "Python Web Development", muallif = "Dilshod Rasulov", narxi = 60.0, sahifa_soni  = 500)
    k5 = Book(nomi = "Algoritmlar", muallif = "Saidbek Xasanov", narxi = 55.0, sahifa_soni = 410)
    
    session.add_all([k1,k2,k3,k4,k5])
    session.commit()

barcha_kitoblar = session.scalars(select(Book)).all()
for b in barcha_kitoblar: print(b)

qimmat_kitoblar = session.scalars(select(Book).where(Book.narxi > 50)).all()
for b in qimmat_kitoblar: print(f"{b.nomi}: {b.narxi}$")

python_kitoblar = session.scalars(select(Book).where(Book.nomi.like('%Python%'))).all()
for b in python_kitoblar: print(b.nomi)

birinchi = session.scalars(select(Book)).first()
print(birinchi)

bitta = session.scalars(select(Book).where(Book.id == 3)).one_or_none()
print(bitta)

session.close()







#2-topshiriq
from sqlalchemy import create_engine, Integer, String, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine('sqlite:///kino.db', echo=True)

class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = 'movies'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nomi: Mapped[str] = mapped_column(String, nullable=False)
    janr: Mapped[str] = mapped_column(String)
    reyting: Mapped[float] = mapped_column(Float)
    yili: Mapped[int] = mapped_column(Integer)

Base.metadata.create_all(engine)

with Session(engine) as session:
    m1 = Movie(nomi = "Interstellar", janr = "Sci-Fi", reyting = 8.7, yili = 2014),
    m2 = Movie(nomi = "The Dark Knight", janr = "Action", reyting = 9.0, yili = 2008),
    m3 = Movie(nomi = "Forrest Gump", janr = "Drama", reyting = 8.8, yili = 1994),
    m4 = Movie(nomi = "The Hangover", janr = "Comedy", reyting = 7.7, yili = 2009),
    m5 = Movie(nomi = "Avengers: Endgame", janr = "Action", reyting = 8.4, yili =2019),
    m6 = Movie(nomi = "Inception", janr = "Sci-Fi", reyting = 8.8, yili = 2010),

    session.commit()

eski = session.scalars(select(Movie).order_by(Movie.yili.asc())).first()
print(eski)

yangi = session.scalars(select(Movie).order_by(Movie.yili.desc())).first()
print(yangi)

res = session.scalars(select(Movie).where(Movie.reyting > 8.0)).all()
for m in res: print(f"{m.nomi} ({m.reyting})")

komediya = session.scalars(select(Movie).where(Movie.janr == "Comedy")).all()
for m in komediya: print(m.nomi)

a_harfli = session.scalars(select(Movie).where(Movie.nomi.ilike('%a%'))).all()
for m in a_harfli: print(m.nomi)

session.close()