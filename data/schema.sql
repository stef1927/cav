CREATE TABLE Donations (
  id INTEGER,
  date_of_donation DATE,
  requested TEXT,
  given TEXT,
  amount DOUBLE,
  mother INTEGER,
  operator INTEGER
);

CREATE TABLE Children (
  id INTEGER,
  name TEXT,
  date_of_birth DATE,
  sex CHARACTER(1),
  mother INTEGER
);

CREATE TABLE Mothers (
  id INTEGER,
  surname TEXT,
  name TEXT,
  date_of_birth DATE,
  place_of_birth TEXT,
  civil_status TEXT,
  residency TEXT,
  origin_country TEXT,
  highest_academic_achievement TEXT,
  job TEXT,
  registration_date DATE,
  husband_surname TEXT,
  husband_job TEXT,
  city TEXT,
  address TEXT,
  income DOUBLE,
  fixed_expenditures DOUBLE,
  operator INTEGER,
  phone_1 TEXT,
  phone_2 TEXT,
  notes TEXT
);

CREATE TABLE Operators (
  id INTEGER,
  name TEXT
);
