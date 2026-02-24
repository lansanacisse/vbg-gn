-- ============================================================
-- VBG Guinée – Script d'initialisation de la base de données
-- À exécuter dans l'éditeur SQL Supabase
-- ============================================================

-- Extension UUID (déjà activée sur Supabase, mais par sécurité)
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ── Enum statut ───────────────────────────────────────────────────────────────
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'case_status') THEN
        CREATE TYPE case_status AS ENUM ('pending', 'validated', 'rejected');
    END IF;
END$$;

-- ── Table associations ────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS associations (
    id         UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    name       TEXT        NOT NULL,
    region     TEXT        NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- ── Table cases ───────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS cases (
    id             UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    association_id UUID        REFERENCES associations(id) ON DELETE SET NULL,
    region         TEXT        NOT NULL,
    prefecture     TEXT        NOT NULL,
    type_violence  TEXT        NOT NULL,
    victim_age     INTEGER     CHECK (victim_age >= 0 AND victim_age <= 120),
    victim_gender  TEXT,
    date_incident  DATE        NOT NULL,
    status         case_status NOT NULL DEFAULT 'pending',
    created_at     TIMESTAMPTZ DEFAULT now()
);

-- ── Index ─────────────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_cases_status   ON cases (status);
CREATE INDEX IF NOT EXISTS idx_cases_region   ON cases (region);
CREATE INDEX IF NOT EXISTS idx_cases_date     ON cases (date_incident);

-- ── Row Level Security (optionnel, recommandé) ────────────────────────────────
-- Activez RLS dans Supabase et créez des politiques selon vos besoins.
-- Exemple de politique : lecture publique des cas validés uniquement.
--
-- ALTER TABLE cases ENABLE ROW LEVEL SECURITY;
--
-- CREATE POLICY "Lecture publique des cas validés"
--   ON cases FOR SELECT
--   USING (status = 'validated');
--
-- CREATE POLICY "Insertion via service role uniquement"
--   ON cases FOR INSERT
--   WITH CHECK (true);  -- restreindre via service_role côté backend

-- ── Données de démo ───────────────────────────────────────────────────────────
INSERT INTO associations (name, region) VALUES
    ('Association Femmes de Conakry', 'Conakry'),
    ('Réseau de Protection N''Zérékoré', 'N''Zérékoré'),
    ('Solidarité Femmes Kankan', 'Kankan')
ON CONFLICT DO NOTHING;

INSERT INTO cases (region, prefecture, type_violence, victim_age, victim_gender, date_incident, status)
VALUES
    ('Conakry',      'Kaloum',      'Violence physique',           28, 'F', '2024-01-15', 'validated'),
    ('Conakry',      'Matam',       'Violence sexuelle',           19, 'F', '2024-02-03', 'validated'),
    ('Kindia',       'Kindia',      'Mariage précoce/forcé',       16, 'F', '2024-03-10', 'validated'),
    ('N''Zérékoré',  'N''Zérékoré', 'Violence psychologique',      34, 'F', '2024-04-22', 'validated'),
    ('Kankan',       'Kankan',      'Violence économique',         41, 'F', '2024-05-07', 'validated'),
    ('Labé',         'Labé',        'Mutilation génitale féminine', 14, 'F', '2024-06-18', 'validated'),
    ('Boké',         'Boké',        'Violence physique',           23, 'F', '2024-07-09', 'validated'),
    ('Faranah',      'Faranah',     'Violence sexuelle',           31, 'F', '2024-08-14', 'validated'),
    ('Mamou',        'Mamou',       'Violence psychologique',      27, 'M', '2024-09-20', 'validated'),
    ('Conakry',      'Dixinn',      'Violence physique',           22, 'F', '2024-10-05', 'pending')
ON CONFLICT DO NOTHING;
