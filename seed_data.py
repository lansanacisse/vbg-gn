"""
Script de peuplement : insère 100 cas dans vbg_guinee.db (SQLite local).
"""

import sqlite3
import uuid
import random
from datetime import date, timedelta

DB_PATH = "vbg_guinee.db"

REGIONS_PREFECTURES = {
    "Conakry":    ["Kaloum", "Dixinn", "Matam", "Ratoma", "Matoto"],
    "Kindia":     ["Kindia", "Coyah", "Dubréka", "Forécariah", "Télimélé"],
    "Boké":       ["Boké", "Boffa", "Fria", "Gaoual", "Koundara"],
    "Labé":       ["Labé", "Koubia", "Lélouma", "Mali", "Tougué"],
    "Mamou":      ["Mamou", "Dalaba", "Pita"],
    "Faranah":    ["Faranah", "Dabola", "Dinguiraye", "Kissidougou"],
    "Kankan":     ["Kankan", "Kérouané", "Kouroussa", "Mandiana", "Siguiri"],
    "N'Zérékoré": ["N'Zérékoré", "Beyla", "Guéckédou", "Lola", "Macenta", "Yomou"],
}

TYPES_VIOLENCE = [
    "Violence physique",
    "Violence sexuelle",
    "Violence psychologique",
    "Violence économique",
    "Mariage précoce / forcé",
    "Mutilation génitale féminine",
    "Autre",
]

STATUSES = ["pending", "validated", "rejected"]
STATUS_WEIGHTS = [0.3, 0.6, 0.1]

GENDER_CHOICES = ["F", "F", "F", "F", "M"]  # majorité féminine

START_DATE = date(2024, 1, 1)
END_DATE   = date(2025, 3, 1)


def random_date(start: date, end: date) -> date:
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, delta))


def get_association_ids(conn) -> list[str]:
    rows = conn.execute("SELECT id FROM associations").fetchall()
    return [r[0] for r in rows]


def build_cases(assoc_ids: list[str], n: int = 100) -> list[tuple]:
    rows = []
    for _ in range(n):
        region = random.choice(list(REGIONS_PREFECTURES.keys()))
        prefecture = random.choice(REGIONS_PREFECTURES[region])
        type_viol = random.choice(TYPES_VIOLENCE)
        age = random.randint(10, 65) if random.random() > 0.05 else None
        gender = random.choice(GENDER_CHOICES)
        d_incident = random_date(START_DATE, END_DATE)
        status = random.choices(STATUSES, STATUS_WEIGHTS)[0]
        assoc_id = random.choice(assoc_ids) if random.random() > 0.3 else None
        rows.append((
            str(uuid.uuid4()),
            assoc_id,
            region,
            prefecture,
            type_viol,
            age,
            gender,
            d_incident.isoformat(),
            status,
        ))
    return rows


def main():
    conn = sqlite3.connect(DB_PATH)
    assoc_ids = get_association_ids(conn)

    cases = build_cases(assoc_ids, n=100)

    conn.executemany(
        """
        INSERT INTO cases
            (id, association_id, region, prefecture, type_violence,
             victim_age, victim_gender, date_incident, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        cases,
    )
    conn.commit()

    total = conn.execute("SELECT COUNT(*) FROM cases").fetchone()[0]
    conn.close()
    print(f"100 cas insérés. Total dans la table cases : {total}")


if __name__ == "__main__":
    main()
