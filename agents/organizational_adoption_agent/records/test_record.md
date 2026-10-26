# Organizational Adoption Agent Test Record

## Test design

All three cases use the same emerging technology and intended application: multimodal generative AI for draft short-form social marketing video with human review and provenance/disclosure controls.

- **Primary:** a hypothetical multinational consumer-products company with central creative operations and specialist governance functions, but unclosed vendor, provenance, training, ownership, and measurement gaps.
- **Contrast 1:** a hypothetical 25-person beauty brand with rapid decisions but no independent approval, specialist governance functions, managed creator accounts, or proven operating controls.
- **Contrast 2:** a deliberately incomplete organization profile used to test whether the agent asks for evidence instead of inventing readiness.

## Commands actually run

```text
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/organizational_adoption_agent --case agents/organizational_adoption_agent/cases/primary.json
python tools/build_prompt.py --agent agents/organizational_adoption_agent --case agents/organizational_adoption_agent/cases/contrast_1.json
python tools/build_prompt.py --agent agents/organizational_adoption_agent --case agents/organizational_adoption_agent/cases/contrast_2.json
python tools/validate_response.py agents/organizational_adoption_agent/responses/primary_response.json
python tools/validate_response.py agents/organizational_adoption_agent/responses/contrast_1_response.json
python tools/validate_response.py agents/organizational_adoption_agent/responses/contrast_2_response.json
python tests/test_agent_package.py
```

## Primary result

The agent classified Northstar as **conditionally ready for a bounded pre-publication pilot**, but not ready for external publication until vendor review, end-to-end provenance/disclosure testing, independent approval, training, ownership, and measurement gates close.

## Contrast result

The agent classified Harbor Glow as **not ready for the proposed public launch in 30 days** and limited the safe next step to a non-public sandbox. Unlike the primary organization, Harbor Glow lacks independent approval, specialist control capacity, managed accounts, and an operating governance owner.

## Missing-information result

The agent classified the third case as **indeterminate**, rated every dimension unknown, and requested specific ownership, workflow, vendor, training, culture, budget, and measurement evidence.

## What appropriately stayed stable

The general technology finding and the application-specific control demands remained textually identical in all final responses. Both organizations still need governed inputs, human evaluation, rights/vendor controls, disclosure or provenance evidence, monitoring, and named accountability.

## What appropriately changed

The overall readiness class, permitted next step, most consequential gap, action owners, timing, and verification conditions changed with organizational capability. The primary organization can run a bounded pre-publication pilot using existing functions; the small organization should not launch publicly and must first create a minimum independent control structure.

## Failure preserved and revision made

The v0.1 output passed the response validator but returned a generic list of sensible practices. It did not assess all eight dimensions, rank gaps, define gates, bind actions to owners and evidence, or elevate the untested provenance path. Version 1.0 added explicit current-state ratings, non-averaging gate logic, action-quality requirements, and mandatory abstention for missing evidence. The final package test checks these behaviors.

## Remaining limitations

The cases are hypothetical, so readiness conclusions demonstrate contextual behavior rather than certify a real organization. No actual vendor, staff interview, workflow sample, content output, provenance chain, or budget was audited. The agent supports management judgment but does not replace legal, security, procurement, or final strategy authority.
