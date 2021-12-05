DROP TABLE if exists books;
DROP TABLE if exists auth;

CREATE TABLE books (
	title text,
	author text,
	synopsis text,
	cover blob
);

CREATE TABLE auth (
	username text,
	password text,
	branch text
);
