# TraceFoundry Environment

Status: Planning — lab deployment and compatibility are not yet verified.

This document records the host hardware, planned lab placement, and setup decisions for TraceFoundry. Pending entries must be confirmed before installation. Planning allocations are not vendor requirements or verified capacity.

## Host inventory

| Detail | Chris | Project partner |
|---|---|---|
| Computer | Mac; exact model pending | Lenovo ThinkPad; exact model pending |
| CPU | Pending | AMD Ryzen 7; exact model pending |
| CPU architecture | Pending | x86-64 |
| Installed RAM | Pending | Pending |
| Available disk space | Pending | Pending |
| Host OS and version | macOS; version pending | Pending confirmation |
| Virtualization software and version | Pending | VMware previously reported; installation after reset and exact product/version pending |
| Starting condition | Personal development workstation | Reported factory-reset machine |
| Virtualization readiness | Pending | Firmware virtualization status pending |

Do not include serial numbers, credentials, product keys, or personal account details in this document.

## Planned component placement

| Component | Proposed host | Guest OS / architecture | Resources | Status |
|---|---|---|---|---|
| Development, Git, and documentation | Chris's Mac | Host macOS | Not applicable | Planned |
| Windows detection endpoint | Partner's ThinkPad | Windows 11 x86-64; edition/build pending | CPU, RAM, and disk pending | Proposed; capacity and compatibility review required |
| Splunk collection and search | Pending | Supported OS and architecture for selected release | Pending | Deployment choice pending |
| Wazuh server, indexer, and dashboard | Pending | Supported Linux release and architecture | Pending | Later phase; after three-detection baseline |
| Linux monitoring endpoint | Pending | Linux distribution/version pending | Pending | Later phase |
| Isolated analysis environment | Pending | Selected for analysis tools and sample architecture | Pending | Later phase; separate from detection infrastructure |

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

- Confirm the Mac's CPU architecture before choosing guest images. If it uses Apple silicon, verify Windows ARM drivers and tool support separately from application emulation.
- Verify the selected Splunk release supports its actual host OS and CPU. Use a separate supported host if needed.
- Confirm the ThinkPad's available resources before assigning multiple simultaneous VMs.
- Record actual VM allocations, event retention, and disk limits after the deployment choices are made.
- Record licensing or evaluation terms and expiration dates without committing keys or credentials.
- Confirm snapshot support in the selected virtualization product and test recovery before simulations.

## Networking and access

| Decision | Value |
|---|---|
| Detection-lab virtual network mode | Pending |
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

These entries are pending verification; this table does not indicate installation.

| Item | Version / build | Configuration or evidence |
|---|---|---|
| Virtualization product | Pending | Pending |
| Windows guest | Pending | Pending |
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
| Clean Windows baseline | Pending | Pending | Not tested | Pending |
| Working telemetry baseline | Pending | Pending | Not tested | Pending |
| Isolated analysis baseline | Pending | Pending | Not tested | Later phase |

## Session checklist

- [ ] Confirm host specifications and VMware installation.
- [ ] Agree on VM allocations and Splunk placement.
- [ ] Document network mode and authorized access.
- [ ] Create Windows VM and verify clean-snapshot recovery.
- [ ] Confirm a harmless Sysmon Event ID 1 locally.
- [ ] Find the corresponding event in Splunk.
- [ ] Have both collaborators reproduce the search.
- [ ] Commit sanitized configuration and evidence through a reviewed PR.

## Ownership and review

| Responsibility | Lead | Reviewer |
|---|---|---|
| Environment and architecture record — DOC-01 / #11 | Chris | Project partner |
| Windows VM — LAB-01 / #1 | Project partner | Chris |
| Sysmon configuration — LAB-02 / #2 | Project partner | Chris |
| Splunk installation — LAB-03 / #3 | Project partner | Chris |
| Sysmon-to-Splunk ingestion — LAB-04 / #4 | Chris | Project partner |

Assignments follow the proposed session split and should be confirmed together. Update this file when a deployment decision changes; mark an item verified only after its evidence has been reviewed.
