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

<!-- PORTFOLIO-OVERVIEW-START -->

## Project overview

Validate synthetic AI agent tool-call fixtures and expected tool interaction behavior.

### Technologies and concepts

 - python
 - ai agents
 - tool calling
 - agent testing
 - quality assurance

### Repository information

- **Category:** AI Quality Engineering / Software Testing
- **Evaluation type:** Offline and/or synthetic fixtures, as documented in this repository
- **Source code:** [GitHub repository](https://github.com/gireeshvuyyuru501-design/agent-tool-call-tester.git)
- **License:** MIT (subject to repository license file)

### AI Quality Engineering portfolio

This project is part of an 11-project portfolio covering evaluation datasets, structured-output validation, offline scoring, prompt regression, retrieval benchmarking, adversarial testing, agent tool calls, and quality monitoring.

[Explore the integrated AI Quality Engineering Platform](https://github.com/gireeshvuyyuru501-design/ai-quality-engineering-platform)

<!-- PORTFOLIO-OVERVIEW-END -->
