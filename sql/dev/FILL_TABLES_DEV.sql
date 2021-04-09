insert into "addresses"
("address_id", "street", "street_number", "postal_code", "city", "country_iso", "comment") values
(0, 'Borgfelder Str.', '16', '20537', 'Hamburg', 'DE', '');

insert into "dormitories"
("dormitory_id", "name", "address_id") values
(0, 'Gustav-Radbruch-Haus', 0);

-- password Marian Peters : 1234
-- password Thomas Müller : 4321
insert into "users"
("user_id", "email", "full_name", "dormitory_id", "flat", "password_hash", "enabled", "comment") values
(0, 'meine-email@gmail.com', 'Marian Peters', 0, null, '$2a$12$eCaNFe3p9noKmQ3Je9g38egcH9wrcw9g8LIzEMp9vARccza1fNj1u', true, ''),
(1, 'meine-email2@gmail.com', 'Thomas Müller', 0, null, '$2a$12$v7kSQ/tgnUnkWCc3fijxju4qP/HG0dLg.SdKZ8PEoAemJmyM7IDTq', true, '');

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
(0, 3),
(1, 2),
(1, 3);