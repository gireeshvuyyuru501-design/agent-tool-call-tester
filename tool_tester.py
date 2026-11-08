"""Offline agent tool-call contract evaluation; no model inference."""
import argparse
import json
from pathlib import Path

TOOLS = {
    "search_docs": {"required": {"query": str}, "optional": {"limit": int}},
    "get_order": {"required": {"order_id": str}, "optional": {}},
    "calculate": {"required": {"a": (int, float), "b": (int, float), "operation": str}, "optional": {}},
}


def validate_call(call):
    if not isinstance(call, dict):
        return ["call must be an object"]
    name = call.get("tool")
    if name not in TOOLS:
        return [f"unknown tool: {name}"]
    args = call.get("arguments")
    if not isinstance(args, dict):
        return ["arguments must be an object"]
    spec = TOOLS[name]
    errors = []
    for field, typ in spec["required"].items():
        if field not in args:
            errors.append(f"missing required argument: {field}")
        elif not isinstance(args[field], typ) or (isinstance(args[field], bool) and typ in (int, float, (int, float))):
            errors.append(f"invalid type for {field}")
    for field, value in args.items():
        if field not in spec["required"] and field not in spec["optional"]:
            errors.append(f"unexpected argument: {field}")
        elif field in spec["optional"] and (not isinstance(value, spec["optional"][field]) or isinstance(value, bool)):
            errors.append(f"invalid type for {field}")
    if name == "calculate" and args.get("operation") not in {"add", "subtract", "multiply", "divide"}:
        errors.append("unsupported operation")
    return errors


def evaluate(cases):
    results = []
    for case in cases:
        errors = validate_call(case["call"])
        actual_valid = not errors
        expected_valid = case["expected_valid"]
        results.append({"id": case["id"], "expected_valid": expected_valid,
                        "actual_valid": actual_valid, "passed": actual_valid == expected_valid,
                        "errors": errors})
    return {"total": len(results), "passed": sum(x["passed"] for x in results),
            "failed": sum(not x["passed"] for x in results), "results": results,
            "note": "Offline schema-contract checks on synthetic tool calls; no LLM evaluated."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", default="examples/tool_calls.json")
    parser.add_argument("--output", default="tool_call_report.json")
    args = parser.parse_args()
    cases = json.loads(Path(args.cases).read_text(encoding="utf-8"))
    report = evaluate(cases)
    Path(args.output).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("total", "passed", "failed")}, indent=2))


if __name__ == "__main__":
    main()
