from datetime import date

from singer import Singer
from track import Track
from base import engine, Session, Base

# generate tables in database
Base.metadata.create_all(engine)

# create session
session = Session()


# singers created
acdc = Singer(nickname="AC/DC", released=date(1990, 11, 1))
bowie = Singer("David Bowie", released=date(1962, 1, 1))
pixies = Singer("Pixies", released=date(1986, 4, 2))
stones = Singer("12 Stones", released=date(2000, 5, 6))



# create tracks
thun = Track("Thunderstruck",
              4,
              "rock",
              acdc,
              date(1990, 5, 6))
highway = Track("Highway to Hell",
              6,
              "rock",
              acdc,
              date(1979, 3, 8))

mars = Track("Life on Mars?",
              6,
              "rock",
              bowie,
              date(1971, 2, 4))


# singers added
session.add_all([acdc, bowie, pixies, stones, thun, highway, mars])

# save data and close session
session.commit()
session.close()