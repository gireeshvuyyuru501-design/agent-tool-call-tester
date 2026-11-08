import json
import unittest
from pathlib import Path
from tool_tester import validate_call, evaluate

class ToolTesterTests(unittest.TestCase):
    def test_valid_call(self):
        self.assertEqual(validate_call({"tool": "search_docs", "arguments": {"query": "hello"}}), [])
    def test_missing_required(self):
        self.assertTrue(validate_call({"tool": "get_order", "arguments": {}}))
    def test_unknown_tool(self):
        self.assertTrue(validate_call({"tool": "bad", "arguments": {}}))
    def test_extra_field(self):
        self.assertTrue(validate_call({"tool": "get_order", "arguments": {"order_id": "1", "secret": "x"}}))
    def test_bool_not_number(self):
        self.assertTrue(validate_call({"tool": "calculate", "arguments": {"a": True, "b": 2, "operation": "add"}}))
    def test_fixture_cases(self):
        cases = json.loads(Path("examples/tool_calls.json").read_text())
        report = evaluate(cases)
        self.assertEqual(report["passed"], len(cases))
        self.assertEqual(report["failed"], 0)

if __name__ == "__main__":
    unittest.main()
