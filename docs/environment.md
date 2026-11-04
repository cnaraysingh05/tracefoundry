# TraceFoundry Environment

Status: The Windows detection VM is running. Laura tested clean-snapshot recovery. Chris's LAB-01 review and telemetry verification are pending.

This document records the host hardware, planned lab placement, and setup decisions for TraceFoundry. Pending entries must be confirmed before installation. Planning allocations are not vendor requirements or verified capacity.

## Host inventory

| Detail | Chris | Laura |
|---|---|---|
| Computer | MacBook Air (M1, `MacBookAir10,1`) | Lenovo ThinkPad (`21OS00XG00`) |
| CPU | Apple M1 | AMD Ryzen AI 7 PRO 350 with Radeon 860M |
| CPU architecture | ARM64 | x86-64 |
| Installed RAM | 8 GiB | 59,749,613,568 bytes (about 55.6 GiB usable) |
| Available disk space | 11 GiB on the data volume at time of inventory | 850,728,255,488 bytes (about 792.3 GiB) on `C:` |
| Host OS and version | macOS 26.6.2 | Windows 11 Pro, version 10.0.26200, 64-bit |
| Virtualization software and version | No virtualization app found in the checked location | VMware Workstation Pro 17.6.3 |
| Starting condition | Personal development workstation | Reported factory-reset machine |
| Virtualization readiness | No virtualization app detected; insufficient current free space for the planned lab | Firmware virtualization enabled |

Do not include serial numbers, credentials, product keys, or personal account details in this document.

## Planned component placement

| Component | Proposed host | Guest OS / architecture | Resources | Status |
|---|---|---|---|---|
| Development, Git, and documentation | Chris's Mac | Host macOS | Not applicable | Planned |
| Windows detection endpoint | Laura's ThinkPad | Windows Server 2022 Standard Evaluation (Desktop Experience), x64 | 2 logical processors and approximately 2 GiB RAM observed in the guest. Laura reports an 80 GB virtual disk. | Running. Selected as the detection endpoint. Tool compatibility and telemetry verification pending. |
| Splunk collection and search | Laura's ThinkPad | Supported x86-64 Linux VM; exact distribution/version pending | Proposed: 4 vCPU, 12 GiB RAM, 120 GiB dynamically allocated disk | Proposed allocation; verify selected Splunk release support |
| Wazuh server, indexer, and dashboard | Laura's ThinkPad | Supported x86-64 Linux VM | Proposed: 4 vCPU, 8 GiB RAM, 100 GiB dynamically allocated disk | Later phase; run within measured host capacity after the three-detection baseline |
| Linux monitoring endpoint | Laura's ThinkPad | Linux x86-64 VM; distribution/version pending | Proposed: 2 vCPU, 4 GiB RAM, 40 GiB dynamically allocated disk | Later phase |
| Isolated analysis environment | Laura's ThinkPad | Windows x86-64 disposable VM | Resources pending; run separately from collector VMs when practical | Later phase; isolated from detection infrastructure |

VM hosting does not determine issue ownership. Both collaborators must be able to reproduce the agreed detection workflow through an authorized access method.

## Initial implementation sequence

1. Confirm both hosts' CPU, RAM, free storage, operating systems, and virtualization software.
2. Choose the Windows VM configuration and supported Splunk deployment path.
3. Build the Windows endpoint with a local lab account and test clean-snapshot recovery.
4. Install and configure Sysmon; verify a harmless process creation event locally.
5. Establish Sysmon-to-Splunk collection and locate the same event by host, timestamp, and process.
6. Save sanitized configuration and evidence for peer review.

The first telemetry gate is passed only when both collaborators can find a fresh Sysmon Event ID 1 in Splunk. Wazuh follows the three-technique Splunk baseline; the analysis environment is a separate later phase.

## Compatibility and resource decisions

- Chris's M1 Mac is reserved for development, Git, documentation, and browser-based access. Its 8 GiB RAM and 11 GiB available storage do not support the planned local VM lab.
- Verify the selected Splunk release supports its actual host OS and CPU. Use a separate supported host if needed.
- The ThinkPad has sufficient preliminary capacity for the Windows endpoint and a separate Splunk VM. Proposed allocations remain subject to observed host and guest performance.
- Record actual VM allocations, event retention, and disk limits after the deployment choices are made.
- Record licensing or evaluation terms and expiration dates without committing keys or credentials.
- Confirm snapshot support in the selected virtualization product and test recovery before simulations.

## Networking and access

| Decision | Value |
|---|---|
| Detection-lab virtual network mode | Windows detection VM uses NAT. Collector networking and access from Chris's Mac are pending. |
| Windows-to-Splunk collection method | Pending |
| Private collector address and required ports | Pending |
| Authorized access method for Chris | Pending |
| Firewall scope | Pending; restrict access to the agreed lab systems |
| Clock synchronization method | Pending; record test times in UTC |
| Internet access during setup | Pending; document required downloads |
| Analysis network | Separate disposable environment; not connected to normal collectors |

Keep collector interfaces private. Store credentials outside Git. Verify connectivity and clock alignment before interpreting missing events or detection latency.

For later dynamic analysis, verify disabled internet egress, bridged networking, shared folders, clipboard, drag-and-drop, USB passthrough, and cloud sync. Test rollback and use a controlled export process for sanitized evidence after execution has stopped and the sample environment has been shut down or reverted.

## Installed versions and configuration record

Confirmed versions are listed below. Pending entries still require verification.

| Item | Version / build | Configuration or evidence |
|---|---|---|
| Virtualization product | VMware Workstation Pro 17.6.3 | Reported by Laura |
| Windows guest | Windows Server 2022 Standard Evaluation (Desktop Experience), x64 | Edition and architecture confirmed in guest inventory. Exact OS build pending. |
| Sysmon | Pending | Configuration path and SHA-256 pending |
| Splunk and collection component | Pending | Index, sourcetype, field mappings, and retention pending |
| Atomic Red Team | Pending | Selected test ID and revision pending |
| Sigma CLI, Splunk backend, and pipeline | Pending | Pinned versions and mapping configuration pending |
| Wazuh components and agents | Pending | Later phase |
| Linux guest | Pending | Later phase |
| Ghidra and required runtime | Pending | Later phase |
| C++ compiler / build tools | Pending | Later phase |

## Snapshot and recovery record

| Checkpoint | VM | Snapshot identifier | Recovery tested | Evidence |
|---|---|---|---|---|
| Clean Windows baseline | Windows Server 2022 detection VM | LAB-01 Clean Baseline | Laura reports a successful restore | Chris's review pending |
| Working telemetry baseline | Pending | Pending | Not tested | Pending |
| Isolated analysis baseline | Pending | Pending | Not tested | Later phase |

## Session checklist

- [x] Confirm host specifications and firmware virtualization support.
- [x] Confirm VMware installation and version.
- [ ] Agree on VM allocations and Splunk placement.
- [ ] Document network mode and authorized access.
- [x] Create Windows VM and verify clean-snapshot recovery.
- [ ] Confirm a harmless Sysmon Event ID 1 locally.
- [ ] Find the corresponding event in Splunk.
- [ ] Have both collaborators reproduce the search.
- [ ] Commit sanitized configuration and evidence through a reviewed PR.

## Ownership and review

| Responsibility | Lead | Reviewer |
|---|---|---|
| Environment and architecture record — DOC-01 / #11 | Chris | Laura |
| Windows VM — LAB-01 / #1 | Laura | Chris |
| Sysmon configuration — LAB-02 / #2 | Laura | Chris |
| Splunk installation — LAB-03 / #3 | Laura | Chris |
| Sysmon-to-Splunk ingestion — LAB-04 / #4 | Chris | Laura |

Assignments follow the proposed session split and should be confirmed together. Update this file when a deployment decision changes; mark an item verified only after its evidence has been reviewed.

## Observed Windows guest

Laura booted Windows Server 2022 Standard Evaluation (64-bit) in VMware.
The guest reported 2 logical processors and approximately 2 GiB of RAM.
Its C: volume reported 79.37 GB total and 67.51 GB free.

The architecture draft specifies Windows 11 as the planned detection endpoint.
Chris and Laura still need to confirm the final guest OS and verify snapshot recovery.

[Guest inventory screenshot](screenshots/windows-server-2022-inventory.png)
