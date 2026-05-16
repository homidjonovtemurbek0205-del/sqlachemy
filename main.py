#1-topshiriq


from sqlalchemy import create_engine, Integer, String, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

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

    def repr(self):
        return f"Book(id={self.id}, nomi='{self.nomi}', narxi={self.narxi})"

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

if session.scalar(select(Book)) is None:
    books_data = [
        ("Python Asoslari", "Anvar Karimov", 45, 320),
        ("Clean Code", "Robert Martin", 90, 450),
        ("Atomic Habits", "James Clear", 70, 280),
        ("Python Web Development", "Dilshod Rasulov", 60, 500),
        ("Algoritmlar", "Saidbek Xasanov", 55, 410),
    ]
    for nomi, muallif, narxi, sahifa_soni in books_data:
        session.add(Book(nomi=nomi, muallif=muallif, narxi=narxi, sahifa_soni=sahifa_soni))
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
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

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

    def repr(self):
        return f"Movie('{self.nomi}', {self.janr}, {self.reyting}, {self.yili})"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if session.scalar(select(Movie)) is None:
    movies_data = [
        ("Interstellar", "Sci-Fi", 8.7, 2014),
        ("The Dark Knight", "Action", 9.0, 2008),
        ("Forrest Gump", "Drama", 8.8, 1994),
        ("The Hangover", "Comedy", 7.7, 2009),
        ("Avengers: Endgame", "Action", 8.4, 2019),
        ("Inception", "Sci-Fi", 8.8, 2010),
    ]
    for nomi, janr, reyting, yili in movies_data:
        session.add(Movie(nomi=nomi, janr=janr, reyting=reyting, yili=yili))
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
