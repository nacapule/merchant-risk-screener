PY := .venv/bin/python

.PHONY: venv fixtures screen screen-live monitor monitor-offline monitor-select monitor-eval \
        monitor-calibrate monitor-gate memos memos-offline test lint demo

EVENTS := reports/monitor_events_416-baseline.csv.gz
SHIPMENTS := reports/monitor_shipments_416-baseline.csv.gz

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
	$(PY) -m monitor.watch --events $(EVENTS) --shipments $(SHIPMENTS)

monitor-select:
	$(PY) -m monitor.evaluate select --events $(EVENTS)

monitor-calibrate:
	$(PY) -m monitor.evaluate calibrate --shipments $(SHIPMENTS)

monitor-gate:
	$(PY) -m monitor.evaluate gate --events $(EVENTS) --shipments $(SHIPMENTS)

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
