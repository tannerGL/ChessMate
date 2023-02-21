DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS posts;

CREATE TABLE accounts (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    username char(30) NOT NULL,
    email char(60) NOT NULL,
    pwd CHAR(60) NOT NULL
);