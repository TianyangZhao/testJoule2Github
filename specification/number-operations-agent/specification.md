# Specification: number-operations-agent

> **Guidelines**: Read all applicable guidelines before executing ANY tasks below:
> - [guidelines.md](../guidelines.md) — Universal execution rules
> - [guidelines-agent.md](../guidelines-agent.md) — Universal agent patterns
> - [guidelines-agent-python.md](../guidelines-agent-python.md) — Python implementation details
> - [guidelines-agent-skills.md](../guidelines-agent-skills.md) — Runtime skills patterns
> - [guidelines-agent-mcp.md](../guidelines-agent-mcp.md) — MCP integration patterns

---

## Basic Setup

- [x] Read the project input (`product-requirements-document.md`, `intent.md`)
- [x] Bootstrap agent code in `assets/number-operations-agent/` using instructions from the sap-agent-bootstrap section (invoke from inside `assets/number-operations-agent/`, use copy commands — do NOT create files manually)
- [x] Install dependencies, validate the agent starts and responds at `/.well-known/agent.json`

---

## Runtime Skills

> No runtime skills are needed for this agent. All operations are implemented as Python tools with deterministic logic. The system prompt is concise and does not require skill decomposition.

---

## Project-Specific Tasks

## Arithmetic Tool

- [x] Create `assets/number-operations-agent/app/tools/arithmetic.py` with a Python tool implementing:
  - Addition (`add`)
  - Subtraction (`subtract`)
  - Multiplication (`multiply`)
  - Division (`divide`) — return a clear error message on division by zero
  - Exponentiation (`power`)
  - Modulo (`modulo`)
- [x] Register the arithmetic tool in the agent's tool list in `app/agent.py`
- [x] Verify the agent correctly routes arithmetic queries to this tool

## Statistics Tool

- [x] Create `assets/number-operations-agent/app/tools/statistics.py` with a Python tool implementing:
  - Mean
  - Median
  - Mode
  - Variance
  - Standard deviation
  - Minimum and maximum
- [x] Accept a list of numbers as input; return a clear error for empty or invalid lists
- [x] Register the statistics tool in the agent's tool list in `app/agent.py`

## Unit Conversion Tool

- [x] Create `assets/number-operations-agent/app/tools/unit_conversion.py` with a Python tool implementing:
  - Length conversions (m, km, ft, miles, inches, cm)
  - Weight conversions (kg, g, lb, oz)
  - Temperature conversions (Celsius, Fahrenheit, Kelvin)
  - Volume conversions (liters, milliliters, gallons, fluid ounces)
- [x] Accept: value, source unit, target unit; return the converted value
- [x] Return a clear error for unsupported unit pairs
- [x] Register the unit conversion tool in the agent's tool list in `app/agent.py`

## Financial Tool

- [x] Create `assets/number-operations-agent/app/tools/financial.py` with a Python tool implementing:
  - Simple interest (`principal * rate * time`)
  - Compound interest (`principal * (1 + rate/n)^(n*time)`)
  - Percentage calculation (`(part / total) * 100`)
  - Percentage of a value (`value * percentage / 100`)
  - Loan monthly repayment (standard amortisation formula)
- [x] Accept clearly named parameters; return the result with a brief explanation
- [x] Register the financial tool in the agent's tool list in `app/agent.py`

## Agent System Prompt

- [x] Update `assets/number-operations-agent/app/agent.py` system prompt to:
  - Describe the agent's purpose: handling number operations via natural language
  - Instruct the agent to select the correct tool based on the user's request
  - Instruct the agent to return clear, accurate results and ask for clarification on ambiguous inputs
  - Instruct the agent to never invent or guess numeric results — always use tools

---

## Business Instrumentation

- [x] Implement business step instrumentation for each milestone from the PRD with the pattern `[MILESTONE_ID].[achieved|missed]: [description]` and OpenTelemetry custom spans:
  - `M1`: Agent initialized and ready
  - `M2`: Basic arithmetic operations available
  - `M3`: Advanced operations (statistics, units, financial) available
  - `M4`: Agent validated across all operation types
  - `M5`: Agent deployed and live
- [x] See [guidelines-agent-python.md](../guidelines-agent-python.md) for Python-specific implementation
- [x] Verify `bootstrap(app)` is called after `app = server.build()` in `main.py`

---

## MCP Tool Integration

> This agent has NO SAP API integrations. All tools are pure Python functions (read/compute only). Skip MCP server creation, mcp-translation-file, and mock generation steps.

---

## Testing

- [x] `conftest.py` only sets `IBD_TESTING=true`
- [x] Write unit tests in `assets/number-operations-agent/tests/`:
  - `test_arithmetic.py` — one test per arithmetic operation, including division by zero
  - `test_statistics.py` — one test per statistical function, including edge cases (empty list, single value)
  - `test_unit_conversion.py` — one test per conversion category, including unsupported unit error
  - `test_financial.py` — one test per financial calculation
- [x] Write one integration test executing end-to-end agent flow by calling the agent's `invoke` function with mocked LLM responses (tests must run offline)
- [x] Run `pytest` from `assets/number-operations-agent/` (no args) — if coverage < 70%, add tests until threshold met
- [x] Run `pytest` again from `assets/number-operations-agent/` (no args) to generate final `test_report.json`
- [x] Verify `test_report.json` exists in `assets/number-operations-agent/`
