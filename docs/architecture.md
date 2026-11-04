# TraceFoundry lab architecture

**Status:** Proposed design, pending deployment verification  
**Owner:** Chris  
**Reviewer:** Laura

Laura’s ThinkPad hosts the planned lab VMs in VMware. Chris’s M1 Mac is the workstation for Git, documentation, and Splunk searches. Host specifications, proposed VM allocations, tool versions, and recovery checkpoints are tracked in the [environment record](environment.md).

## Detection lab

The first milestone is to follow one Windows process from execution on the endpoint to a searchable event in Splunk. After the three Windows detections are tested in Splunk, Wazuh will collect the same endpoint activity independently so Chris and Laura can compare results.

```mermaid
flowchart TD
    W["Windows 11 test VM"] --> S["Sysmon Operational log"]
    S --> F["Windows forwarder"]
    F --> P["Splunk on a Linux VM"]
    M["Chris's Mac"] -. planned private search access .-> P
    S -. later via Windows Wazuh agent .-> Z["Wazuh server, indexer and dashboard"]
    L["Linux test VM"] -. later via Linux Wazuh agent .-> Z
```

| Component | Planned role | What still needs verification |
|---|---|---|
| Windows 11 VM on Laura’s ThinkPad | Run controlled simulations and record process activity in `Microsoft-Windows-Sysmon/Operational` | Actual hostname, guest build, Sysmon configuration, and clean snapshot restore |
| Splunk Linux VM on Laura’s ThinkPad | Receive Windows events, index them, and run SPL searches | Linux and Splunk versions, forwarding configuration, index, sourcetype, and timestamp handling |
| Chris’s Mac | Maintain the repository and reproduce Splunk searches | Private access method and successful login from the Mac |
| Wazuh and Linux test VMs | Compare Windows detection results and test file-integrity monitoring on Windows and Linux | Agent enrollment, collection settings, and paired test results in the later Wazuh phase |

## Network and recovery

NAT is proposed for Windows setup and updates. Chris and Laura will record the actual VMware network mode, the route from the Windows endpoint to Splunk, and the private access method from Chris’s Mac. The collector and dashboard interfaces will be restricted to authorized lab access.

Laura will take a clean Windows snapshot before installing telemetry tools and test that the VM can revert to it. The environment record will identify the snapshot and the observed restore result.

## Isolated analysis environment

The later Ghidra and runtime analysis exercise will use a separate disposable VM. During execution, the VM will have internet egress and host-sharing features disabled and will have no route to the detection lab. Laura and Chris will verify isolation and snapshot recovery before running the exercise. After shutdown or rollback, they will export reviewed, sanitized evidence for the analysis report.

## First telemetry check

For [LAB-04](https://github.com/cnaraysingh05/tracefoundry/issues/4), launch `notepad.exe` in the Windows guest and locate its Sysmon Event ID 1 locally. Record the guest hostname, `UtcTime`, `Image`, and `ProcessGuid`. Search for that same event in Splunk and compare those values. Save the search and sanitized evidence so both Chris and Laura can reproduce the match.

## Architecture review

- [ ] Chris records the deployed VM names, versions, and network settings in the environment record.
- [ ] Laura confirms the diagram matches the deployed Windows and Splunk path.
- [ ] Chris and Laura verify the documented access and recovery steps.
- [ ] Chris links the reviewed evidence and updates the diagram wherever deployment differs from the plan.
