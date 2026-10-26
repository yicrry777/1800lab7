#!/usr/bin/env python3
"""Assignment-specific checks for the Organizational Adoption Agent package."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / "agents" / "organizational_adoption_agent"


def load(path: Path):
    return json.loads(path.read_text())


def main():
    cases = {
        name: load(AGENT / "cases" / f"{name}.json")
        for name in ("primary", "contrast_1", "contrast_2")
    }
    responses = {
        "primary": load(AGENT / "responses" / "primary_response.json"),
        "contrast_1": load(AGENT / "responses" / "contrast_1_response.json"),
        "contrast_2": load(AGENT / "responses" / "contrast_2_response.json"),
    }

    assert len({case["emerging_technology"] for case in cases.values()}) == 1
    assert len({case["intended_application"] for case in cases.values()}) == 1

    assert len({r["general_et_finding"] for r in responses.values()}) == 1
    assert len({r["application_finding"] for r in responses.values()}) == 1
    assert "CONDITIONALLY READY" in responses["primary"]["organization_specific_finding"]
    assert "NOT READY" in responses["contrast_1"]["organization_specific_finding"]
    assert "INDETERMINATE" in responses["contrast_2"]["organization_specific_finding"]

    dimensions = (
        "leadership/sponsorship",
        "skills/training",
        "workflow/process",
        "infrastructure/data",
        "resources/budget",
        "governance/risk",
        "culture/change",
        "operating ownership",
    )
    for response in responses.values():
        profile = response["organization_specific_finding"].lower()
        for dimension in dimensions:
            assert dimension in profile, f"Missing dimension {dimension}"
        assert response["abstention_or_more_information_needed"]
        assert len(response["evidence"]) >= 3
        assert any("http" in item["source_or_reference"] for item in response["evidence"])
        assert "P0" in response["recommendation_management_implication"]

    missing_profile = responses["contrast_2"]["organization_specific_finding"]
    assert missing_profile.count(" 0") >= 8
    assert len(responses["contrast_2"]["abstention_or_more_information_needed"]) >= 5

    weak = load(AGENT / "responses" / "primary_response_v0_1_weak.json")
    assert weak["agent"]["version"] == "0.1-draft"
    assert "P0" not in weak["recommendation_management_implication"]
    assert (AGENT / "records" / "v0_1_failure_analysis.md").exists()

    print("AGENT PACKAGE TESTS PASSED")


if __name__ == "__main__":
    main()
