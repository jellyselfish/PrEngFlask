from sqlalchemy import create_engine, text


def find_largest_teams(db_name):
    engine = create_engine(f'sqlite:///{db_name}')
    with engine.connect() as conn:
        query = text("""
            SELECT u.surname, u.name
            FROM jobs j
            JOIN users u ON j.team_leader = u.id
            WHERE LENGTH(j.collaborators) - LENGTH(REPLACE(j.collaborators, ',', '')) + 1 = (
                SELECT MAX(team_size) FROM (
                    SELECT LENGTH(collaborators) - LENGTH(REPLACE(collaborators, ',', '')) + 1 AS team_size
                    FROM jobs
                )
            )
        """)
        result = conn.execute(query).fetchall()
        for surname, name in result:
            print(f"{surname} {name}")


find_largest_teams(input())