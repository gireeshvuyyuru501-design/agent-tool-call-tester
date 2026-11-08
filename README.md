# Agent Tool-Call Tester

Offline contract-testing toolkit for agent-style tool calls. Validates tool names, required/optional arguments, Python/JSON value types, unexpected arguments, and allowed calculator operations.

## Quick start

```bash
python -m unittest discover -s tests -v
python tool_tester.py
```

The command creates `tool_call_report.json` from eight **synthetic** cases. All eight should pass because the expected validity labels match the contract validator's predictions. This is **not** evidence of agent or LLM accuracy.

## Design

- `tool_tester.py`: validation and scoring logic
- `examples/tool_calls.json`: labeled example calls
- `tests/`: unit tests
- `.github/workflows/tests.yml`: GitHub Actions CI

## Limitations / next steps

This is a lightweight Python contract validator, **not a full JSON Schema or OpenAPI implementation**. It does not invoke external tools or an LLM. Future work: JSON Schema, multi-step traces, argument semantics, real agent call logs, and optional Gemini tool-calling evaluation.
