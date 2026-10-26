# Organizational Adoption Agent

Student: Shuoying Wang

Assignment: 7 - Organizational Adoption of Emerging Technologies

Version: 1.0

## Technology and application

The agent evaluates organizational readiness for multimodal generative AI used to create and govern short-form TikTok and Instagram marketing video. The technology and application remain constant across test cases; organizational capabilities and evidence change.

## Package contents

- `specialist_instructions.md` - bounded readiness logic and abstention rules
- `cases/` - primary, low-capacity contrast, and missing-information cases
- `responses/` - validated outputs, including the preserved v0.1 weak output
- `records/readiness_framework.md` - eight-dimension readiness framework
- `records/test_record.md` - commands, results, contrast inspection, and revision evidence
- `records/sources.md` - dated authoritative sources
- `records/agent_record.md` - concise assignment record and independent judgment

## Reproduce

From the repository root, use the Python standard library:

```text
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/organizational_adoption_agent --case agents/organizational_adoption_agent/cases/primary.json
python tools/validate_response.py agents/organizational_adoption_agent/responses/primary_response.json
python tests/test_agent_package.py
```

Repeat the prompt build and response validation for `contrast_1` and `contrast_2`. Prompt packets are generated under ignored `work/`; representative inputs and outputs are preserved under the agent folder.
