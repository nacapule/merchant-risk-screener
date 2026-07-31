PY := .venv/bin/python

.PHONY: venv fixtures screen decisions monitor eval test lint demo

venv:
	python3 -m venv .venv && .venv/bin/pip install -q -e ".[dev]"

fixtures:
	$(PY) fixtures/generate_fixtures.py

screen:
	$(PY) -m score.decisions --offline

screen-live:
	$(PY) -m score.decisions

monitor:
	$(PY) -m monitor.watch

eval:
	$(PY) -m screen.eval.harness --offline

test:
	$(PY) -m pytest tests/ -q

lint:
	.venv/bin/ruff check collect screen score monitor llm fixtures tests

demo: fixtures screen eval
	@echo "demo complete — see decisions/ and reports/"
