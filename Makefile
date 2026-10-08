PY := .venv/bin/python

.PHONY: venv fixtures screen screen-live monitor monitor-offline monitor-select monitor-eval \
        memos memos-offline test lint demo

venv:
	python3 -m venv .venv && .venv/bin/pip install -q -e ".[dev,monitor]"

fixtures:
	$(PY) fixtures/generate_fixtures.py

screen:
	$(PY) -m score.decisions --offline

screen-live:
	$(PY) -m score.decisions

monitor:
	$(PY) -m monitor.watch

monitor-offline:
	$(PY) -m monitor.watch --events reports/monitor_events_416-baseline.csv.gz

monitor-select:
	$(PY) -m monitor.evaluate select --events reports/monitor_events_416-baseline.csv.gz

monitor-eval:
	$(PY) -m monitor.evaluate report --events reports/monitor_events_416-baseline.csv.gz

memos:
	$(PY) -m monitor.memo

memos-offline:
	$(PY) -m monitor.memo --offline

test:
	$(PY) -m pytest tests/ -q

lint:
	.venv/bin/ruff check collect screen score monitor llm fixtures tests

demo: fixtures screen monitor-offline memos-offline
	@echo "demo complete — see decisions/ and reports/"
