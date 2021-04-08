insert into "addresses"
("address_id", "street", "street_number", "postal_code", "city", "country_iso", "comment") values
(0, 'Borgfelder Str.', '16', '20537', 'Hamburg', 'DE', '');

insert into "dormitories"
("dormitory_id", "name", "address_id") values
(0, 'Gustav-Radbruch-Haus', 0);

insert into "users"
("user_id", "email", "full_name", "dormitory_id", "flat", "password_hash", "salt", "enabled", "comment") values
(0, 'chris.23.thiele@gmail.com', 'Chris Thiele', 0, null, '1234', '1234', true, 'What the heck im doing?'),
(1, 'thiele.23.chris@gmail.com', 'Thiele Chris', 0, null, '4321', '4321', true, 'Doing im heck the what?');

insert into "roles"
("role_id", "name") values
(0, 'ADMIN'),
(1, 'DORM-ADMIN'),
(2, 'SHC-MEMBER'),
(3, 'RESIDENT'),
(4, 'GUEST');

insert into "users_roles"
("user_id", "role_id") values
(0, 0),
(0, 1),
(0, 2),
(0, 3);