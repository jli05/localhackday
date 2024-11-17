CREATE TABLE posts (
  title TEXT,
  body TEXT,
  publisher TEXT,
  email TEXT,
  time TEXT,
  PRIMARY KEY(email, time, title)
);
