-- country_iso is ISO 3166-1 alpha-2 code
create table "addresses" (
   "address_id" int not null primary key,
   "street" varchar(256) not null,
   "street_number" varchar(16) not null,
   "city" varchar(32) not null,
   "postal_code" varchar(32) not null,
   "country_iso" varchar(32) not null,
   "comment" text
);

create table "dormitories" (
   "dormitory_id" int not null primary key,
   "name" varchar(128) not null,
   "address_id" int,
   constraint "address_fk" foreign key ("address_id") references "addresses" ("address_id")
);

create table "users" (
  "user_id" int not null primary key,
  "email" varchar(64) not null unique,
  "full_name" varchar(64) not null,
  "dormitory_id" int,
  "flat" varchar(64),
  "password_hash" varchar(128) not null,
  "enabled" boolean default null,
  "comment" text,
  constraint "dormitory_fk" foreign key ("dormitory_id") references "dormitories" ("dormitory_id")
);

create table "roles" (
  "role_id" int not null primary key,
  "name" varchar(45) not null
);

create table "users_roles" (
  "user_id" int not null,
  "role_id" int not null,
  unique ("user_id", "role_id"),
  constraint "role_fk" foreign key ("role_id") references "roles" ("role_id"),
  constraint "user_fk" foreign key ("user_id") references "users" ("user_id")
);