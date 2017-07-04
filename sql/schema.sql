PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE comment(
    id integer primary key autoincrement,
    first_name text,
    middle_name text,
    last_name text,
    region_id integer,
    city_id integer,
    phone_number text,
    email text
);
CREATE TABLE region(
    id integer primary key autoincrement,
    name text
);
CREATE TABLE city(
    id integer primary key autoincrement,
    name text,
    region_id integer
);
COMMIT;
