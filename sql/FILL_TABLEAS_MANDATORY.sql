insert into "addresses"
("address_id", "street", "street_number", "postal_code", "city", "country_iso", "comment") values
(0, 'Borgfelder Str.', '16', '20537', 'Hamburg', 'DE', '');

insert into "dormitories"
("dormitory_id", "name", "address_id") values
(0, 'Gustav-Radbruch-Haus', 0);

insert into "roles"
("role_id", "name") values
(0, 'ADMIN'),
(1, 'DORM-ADMIN'),
(2, 'SHC-MEMBER'),
(3, 'RESIDENT'),
(4, 'GUEST');