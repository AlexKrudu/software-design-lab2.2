CREATE TYPE membership_event_type AS ENUM ('RENEWED', 'CREATED');
CREATE TYPE user_event_type AS ENUM ('ENTER', 'EXIT');

CREATE TABLE IF NOT EXISTS users
(
    user_id      SERIAL PRIMARY KEY,
    user_name    TEXT,
    phone_number TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS membership_events
(
    event_id                 SERIAL PRIMARY KEY,
    event_at                 TIMESTAMPTZ,
    event_type               membership_event_type,
    user_id                  SERIAL REFERENCES users (user_id),
    membership_duration_days INTEGER
);

CREATE TABLE IF NOT EXISTS user_events
(
    event_id   SERIAL PRIMARY KEY,
    event_at   TIMESTAMPTZ,
    event_type user_event_type,
    user_id    SERIAL REFERENCES users (user_id)
);