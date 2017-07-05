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
    email text,
    feedback_text text
);

CREATE TABLE region(
    id integer primary key autoincrement,
    name text
);
INSERT INTO region(id, name)
VALUES
    (1, 'Краснодарский край'),
    (2, 'Ростовская область'),
    (3, 'Ставропольский край')
;

CREATE TABLE city(
    id integer primary key autoincrement,
    name text,
    region_id integer
);
INSERT INTO city(id, name, region_id)
VALUES
    (1, 'Краснодар', 1),
    (2, 'Кропоткин', 1),
    (3, 'Славянск', 1),
    (4, 'Ростов', 2),
    (5, 'Шахты', 2),
    (6, 'Батайск', 2),
    (7, 'Ставрополь', 3),
    (8, 'Пятигорск', 3),
    (9, 'Кисловодск', 3)
;

COMMIT;
