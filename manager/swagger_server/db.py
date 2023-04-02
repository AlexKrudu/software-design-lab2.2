from datetime import datetime
from datetime import timedelta

from psycopg2.errors import UniqueViolation
import pytz


def add_user_info(connection, user_name, phone_number):
    cur = connection.cursor()
    try:
        cur.execute(
            f"INSERT INTO users(user_name, phone_number) VALUES ('{user_name}', '{phone_number}') RETURNING user_id")
        user_id = cur.fetchone()[0]
        cur.close()
        return user_id
    except UniqueViolation:
        connection.commit()
        cur.close()
        return None


def add_user_membership_event(connection, user_id, membership_duration_days, event_type):
    event_at = str(datetime.now(pytz.UTC))

    cur = connection.cursor()
    cur.execute(
        f"INSERT INTO membership_events(event_at, event_type, user_id, membership_duration_days) VALUES ('{event_at}', '{event_type}', {user_id}, {membership_duration_days})")
    cur.close()
    return event_at


def get_user_subscription_events(connection, phone_number):
    cur = connection.cursor()
    cur.execute(
        f"SELECT user_name, users.user_id, event_at, event_type, membership_duration_days FROM"
        f" membership_events INNER JOIN users ON membership_events.user_id = users.user_id"
        f" WHERE users.phone_number = '{phone_number}' ORDER BY membership_events.event_at "
    )
    user_name = None
    user_id = None
    events = []
    for row in cur:
        user_name = row[0]
        user_id = row[1]
        events.append({"event_at": row[2], "event_type": row[3], "membership_duration_days": row[4]})
    cur.close()
    return user_name, user_id, events
