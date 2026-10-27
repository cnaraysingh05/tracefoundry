# tracefoundry
# TraceFoundry

A collaborative security engineering lab connecting controlled ATT&CK simulations to endpoint telemetry, detection logic, repeatable tests, and reviewed evidence.

TraceFoundry is designed around Windows telemetry collected with Sysmon, detections developed in Splunk and Sigma, paired monitoring and detection comparisons in Wazuh, and an isolated analysis environment for connecting program behavior to detection opportunities.

## Project status

**Planning and initial setup.**

The repository currently contains the project overview and implementation backlog. Lab configurations, detections, automation, and analysis results are planned deliverables and are not yet verified.

The first milestone is one reproducible PowerShell detection path. The initial detection baseline covers three Windows techniques. The full project also requires Wazuh integration, Windows/Linux monitoring, an isolated analysis exercise, a benign C++ simulator, and repeatable validation.

## Objectives

- Reproduce selected ATT&CK behaviors on authorized disposable endpoints.
- Trace those behaviors through raw events and searchable telemetry.
- Develop handwritten SPL and equivalent Sigma detection logic.
- Compare Splunk and Wazuh outcomes against the same labeled Windows cases.
- Demonstrate Windows and Linux file-integrity monitoring.
- Connect static and dynamic program analysis to detection hypotheses.
- Validate detection changes through automated checks and peer review.
- Publish reproducible evidence, limitations, and results.

## Initial detection scope

| Technique | Initial focus | Status |
|---|---|---|
| T1059.001 — PowerShell | Selected execution behavior, command-line and parent-process context, and benign comparisons | Not started |
| T1053.005 — Scheduled Task | Scoped task creation and execution with the required Windows logging | Not started |
| T1547.001 — Registry Run Keys / Startup Folder | A scoped Run Key modification and harmless payload execution | Not started |

A verified test demonstrates coverage of the documented behavior and variant, not every implementation of an ATT&CK technique.

## Planned architecture

| Component | Purpose |
|---|---|
| Windows test VM | Controlled simulations, Sysmon, and Windows event logging |
| Splunk collection and search | Initial telemetry pipeline, SPL detections, and dashboard |
| Wazuh server, indexer, and dashboard | Independent endpoint monitoring and paired detection comparisons |
| Linux test VM | Wazuh monitoring and a scoped file-integrity scenario |
| Isolated analysis VM | Ghidra, static analysis, and bounded dynamic observation |
| GitHub Actions | Rule structure, metadata, conversion, and non-executing fixture checks |

The analysis sandbox remains separate from the normal detection infrastructure. Only reviewed, sanitized evidence is exported after execution has stopped and the sample environment has been shut down or reverted.

## Implementation roadmap

1. **Establish the telemetry path:** configure a Windows VM, Sysmon, and supported Splunk collection; verify the same harmless event locally and in Splunk.
2. **Complete one detection:** review a selected PowerShell test, capture telemetry, write SPL, express the same intent in Sigma, and verify positive and negative outcomes.
3. **Build the three-technique baseline:** add Scheduled Task and Run Key detections using a consistent evidence format and rotating contributor roles.
4. **Integrate Wazuh:** collect Windows telemetry independently, implement comparable rules, and test Windows/Linux file integrity.
5. **Complete the analysis exercise:** connect Ghidra findings and runtime evidence to a core detection using a benign or educational program and a bounded C++ simulator.
6. **Automate validation and testing:** add CI checks, labeled fixtures, actual-engine evaluation, and documented results.
7. **Publish the verified scope:** complete the coverage matrix, Splunk dashboard, setup instructions, and reproducible demonstration.

Expansion toward ten techniques is optional and follows completion of the required project.

## Detection evidence standard

Each core detection is expected to include:

- A scoped behavioral hypothesis and ATT&CK mapping.
- Telemetry prerequisites and relevant event sources.
- A reviewed simulation procedure and cleanup plan.
- Handwritten SPL, Sigma, and generated SPL.
- A Wazuh implementation or an explicitly documented limitation.
- Positive and realistic negative test cases.
- Recorded rule, configuration, tool, and test revisions.
- Sanitized evidence, observed outcomes, and known false positives.
- Peer review and reproduction instructions.

## Validation and testing

TraceFoundry distinguishes three layers of evidence:

| Layer | What it establishes |
|---|---|
| Static CI | Rule syntax, metadata, identifiers, and conversion meet project requirements |
| Fixture execution | The actual target engine matches or excludes the labeled inputs |
| Live integration | The selected endpoint action produces telemetry and the expected detection outcome through the deployed pipeline |

The initial fixture target is three positive variants and five negative cases per core detection: 24 cases across the three detections. This is a planned target, not a completed result.

Metrics will be reported separately for each engine and limited to the tested corpus. Errors, unsupported checks, and unexecuted cases will remain visible. A passing CI workflow does not establish live detection effectiveness.

## Development on macOS

macOS may serve as the development and management workstation. Lab placement depends on the host CPU, memory, storage, guest architecture, and selected tool versions.

Before installation:

- Record hardware, operating systems, versions, licensing, and resource budgets.
- Verify Windows ARM driver and tool compatibility separately on Apple silicon.
- Use an authorized x86 Windows host and supported collector when required.
- Keep collector interfaces private and document recovery procedures.

The project does not assume that every component can run directly on a Mac or inside a single Windows VM.

## Planned repository layout

The following paths will be populated as implementation progresses.

| Path | Contents |
|---|---|
| `detections/<technique>/` | Manifest, Sigma, handwritten/generated SPL, technique-specific Wazuh rule, documentation, and results |
| `attacks/<technique>/` | Reviewed simulation procedures and cleanup |
| `tests/<technique>/` | Fixture manifest and positive/negative cases |
| `results/<run-id>/` | Sanitized observed results |
| `configs/sysmon/` | Versioned Sysmon configuration |
| `configs/wazuh/` | Wazuh collection configuration |
| `wazuh/rules/` | Shared rule dependencies and deployment notes |
| `splunk/dashboards/` | Dashboard definitions |
| `splunk/queries/` | Supporting searches |
| `analysis/reports/` | Static and dynamic analysis reports |
| `simulations/cpp/` | Benign simulator source and safety contract |
| `scripts/` | Validation and result-summary tools |
| `docs/` | Architecture, environment, methodology, coverage, comparisons, and safety |
| `templates/detection-template/` | Standard detection package |
| `.github/workflows/` | Automated validation workflows |

## Collaboration

Work is organized through GitHub issues and reviewed pull requests. Each issue has an owner, reviewer, dependency, and acceptance criterion.

Contributors alternate simulation, telemetry, detection, and review responsibilities. Each person is expected to author and review work and reproduce the complete detection pipeline.

Implementation status progresses from **Not started** to **In progress** to **Verified**, with **Blocked** and **Not applicable** recorded where appropriate. Verified claims require evidence and peer review.

## Lab boundaries

- Use only owned or explicitly authorized disposable systems and test accounts.
- Review simulation commands, dependencies, expected effects, and cleanup before execution.
- Keep dynamic analysis isolated from personal systems and the normal detection lab.
- Exclude secrets, raw sensitive logs, live malware, and executable payloads from Git.
- Do not execute Atomic tests, persistence simulators, or malware in CI.
- Use benign and educational programs for the required analysis exercise; real malware is optional.

## Release criteria

A full release requires:

- Three reviewed Windows detections with reproducible telemetry, SPL, Sigma, positive/negative tests, and cleanup evidence.
- Wazuh monitoring and documented paired Windows detection results or explicit limitations.
- A Windows/Linux file-integrity comparison.
- One isolated analysis report and verified benign C++ exercise.
- Automated validation and recorded target-engine test results.
- An evidence-backed coverage matrix and Splunk dashboard.
- Setup instructions that the other contributor can use to reproduce a positive and negative result.

Incomplete required work will be identified as an interim milestone rather than a completed implementation.

## References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Microsoft Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [Sigma CLI](https://github.com/SigmaHQ/sigma-cli)
- [Sigma Splunk backend](https://github.com/SigmaHQ/pySigma-backend-splunk)
- [Wazuh documentation](https://documentation.wazuh.com/current/)
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra)
