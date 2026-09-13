#!/usr/bin/env bash
# Build the Kalpa warehouse the Week 2 SQL days query.
#
# Runs once when the container is created, after setup.sh. Every step tolerates failure and the
# script always exits zero, because a Codespace that will not open is worse than one whose
# database needs a manual reload. Rerun it by hand at any time; it drops and rebuilds.
set +e
log() { echo "[warehouse] $*"; }

WAREHOUSE="content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql"
DB="${PGDATABASE:-kalpa}"
export PGHOST="${PGHOST:-localhost}" PGPORT="${PGPORT:-5432}"
export PGUSER="${PGUSER:-postgres}" PGPASSWORD="${PGPASSWORD:-postgres}"

if ! command -v psql >/dev/null 2>&1; then
  log "psql is not on the path, so the warehouse cannot be loaded. The SQL days need it."
  exit 0
fi

for attempt in 1 2 3 4 5 6 7 8 9 10; do
  pg_isready -q && break
  log "waiting for the server, attempt ${attempt}"
  sleep 2
done
if ! pg_isready -q; then
  log "no server answered on ${PGHOST}:${PGPORT}. Run this script again once one is up."
  exit 0
fi

if [ ! -f "$WAREHOUSE" ]; then
  log "no warehouse file at ${WAREHOUSE}; writing one"
  python3 data/generate_client_zero.py --version v4 --out content/W02/D1/data --stem C2_W02_D01 \
    >/dev/null 2>&1
fi

psql -d postgres -q -c "DROP DATABASE IF EXISTS ${DB};" >/dev/null 2>&1
psql -d postgres -q -c "CREATE DATABASE ${DB};" >/dev/null 2>&1
if psql -d "$DB" -q -v ON_ERROR_STOP=1 -f "$WAREHOUSE" >/dev/null 2>&1; then
  counts=$(psql -d "$DB" -At -c \
    "select string_agg(t || ' ' || n, ', ' order by t) from (
       select 'customers' t, count(*) n from customers union all
       select 'orders', count(*) from orders union all
       select 'payments', count(*) from payments union all
       select 'refunds', count(*) from refunds union all
       select 'campaign_exposure', count(*) from campaign_exposure union all
       select 'plan_line', count(*) from plan_line) s;" 2>/dev/null)
  log "loaded into ${DB}: ${counts}"
else
  log "the warehouse file did not load. Run: psql -d ${DB} -f ${WAREHOUSE}"
fi
exit 0
