insert into "addresses"
("address_id", "street", "street_number", "postal_code", "city", "country_iso", "comment") values
(0, 'Borgfelder Str.', 16, '20537', 'Hamburg', 'DE', '');

insert into "dormitories"
("dormitory_id", "name", "address_id") values
(0, 'Gustav-Radbruch-Haus', 0);

insert into "users"
("user_id", "email", "full_name", "dormitory_id", "flat", "password_hash", "salt", "enabled", "comment") values
(0, 'chris.23.thiele@gmail.com', 'Chris Thiele', 0, null, '1234', '1234', true, 'What the heck im doing?');

insert into "roles"
("role_id", "name") values
(0, 'ADMIN'),
(1, 'SHC-MEMBER'),
(2, 'RESIDENT'),
(3, 'GUEST');

insert into "users_roles"
("user_id", "role_id") values
(0, 0);