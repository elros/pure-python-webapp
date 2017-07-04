PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
INSERT INTO region(id, name)
VALUES
    (1, 'Краснодарский край'),
    (2, 'Ростовская область'),
    (3, 'Ставропольский край')
;

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