"""
Service de statistiques agrégées.
"""

from collections import Counter
from typing import Optional

from sqlalchemy.orm import Session
from services.cases_service import get_validated_cases, get_all_cases_count


def get_stats(db: Session, year: Optional[int] = None,
              region: Optional[str] = None) -> dict:
    """
    Retourne un dictionnaire de statistiques :
      - total_cases
      - by_region  : {region: count}
      - by_type    : {type_violence: count}
    """
    cases = get_validated_cases(db, year=year, region=region)

    by_region = dict(Counter(c.region for c in cases))
    by_type = dict(Counter(c.type_violence for c in cases))

    return {
        "total_cases": len(cases),
        "by_region": by_region,
        "by_type": by_type,
    }
