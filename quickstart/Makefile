.PHONY: setup data seed dbt all clean

setup:
	python3 -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

data:
	. .venv/bin/activate && python scripts/create_sample_data.py

seed:
	. .venv/bin/activate && python scripts/seed_duckdb.py

dbt:
	cd dbt && DBT_PROFILES_DIR=. dbt deps && DBT_PROFILES_DIR=. dbt build

all: setup data seed dbt

clean:
	rm -f warehouse/quickstart.duckdb
	rm -rf dbt/logs dbt/target
