
# TraceFoundry Lab Environment

## LAB-01: Windows Detection Endpoint

### 1. Environment Overview

TraceFoundry is a collaborative detection engineering lab designed to connect controlled endpoint behavior to security telemetry, detection logic, testing, and documented evidence.

The initial detection endpoint is a disposable Windows Server 2022 virtual machine hosted on a Lenovo ThinkPad using VMware Workstation Pro.

This environment is intended to support Windows endpoint monitoring, Sysmon telemetry collection, Splunk ingestion, Atomic Red Team simulations, and Wazuh agent integration.

The malware analysis environment will be deployed separately with stricter isolation controls.

**Environment Status:** In Progress  
**Related Issue:** LAB-01 (#1)  
**Partner Review:** Pending

---

### 2. Host Computer

| Component | Configuration |
|---|---|
| Manufacturer | Lenovo |
| Device | ThinkPad |
| Host Operating System | Windows 11 (edition/build pending verification) |
| Processor | AMD Ryzen AI 7 PRO 350 |
| Integrated Graphics | AMD Radeon 860M |
| CPU Architecture | x86-64 (AMD64) |
| Physical CPU Cores | 8 |
| Logical Processors | 16 |
| CPU Base Speed | 2.00 GHz |
| Hardware Virtualization | Enabled |
| Installed RAM | Pending verification |
| Usable Memory Reported by Task Manager | 55.6 GB |
| Storage Type | NVMe SSD |
| Total Storage Capacity | Pending verification |
| Available Storage | Pending verification |

The host uses an AMD x86-64 processor with hardware virtualization enabled.

Windows ARM compatibility considerations do not apply to the selected host architecture.

Additional resource allocation decisions will be based on measured host utilization.

---

### 3. Virtualization Platform

| Component | Configuration |
|---|---|
| Hypervisor | VMware Workstation Pro |
| Version | 17.6.3 |
| Host Platform | Windows |
| Licensing | Free-use distribution |
| Snapshot Capability | Supported and tested |
| Virtual Networking | Supported |
| VMware Tools | Installed in guest |

VMware Workstation Pro is used to create and manage the project's disposable virtual machines.

Virtualization provides a controlled testing environment, although additional network and host-integration restrictions are required for higher-risk analysis activities.

---

### 4. Windows Detection Endpoint

| Component | Configuration |
|---|---|
| Virtual Machine Name | Windows Server 2022 |
| Guest Operating System | Windows Server 2022 Standard Evaluation |
| Installation Type | Desktop Experience |
| Guest Architecture | x64 |
| Virtual CPUs | 2 |
| Allocated RAM | 8 GB (8192 MB) |
| Virtual Disk Capacity | 80 GB |
| Virtual Disk Interface | NVMe |
| Network Adapter Mode | NAT |
| IP Assignment | DHCP |
| PowerShell Version | 5.1.20348.558 |
| VMware Tools | Installed |
| VM Status | Operational |
| Snapshot Recovery | Passed |

Windows Server 2022 was selected as the initial Windows detection endpoint.

The TraceFoundry framework requires a Windows environment capable of supporting endpoint telemetry, security simulations, and detection validation. It does not mandate Windows 11 specifically.

The selected Windows Server endpoint will be retained unless compatibility or performance testing identifies a reason to change the operating system.

---

### 5. Operating System Licensing

#### Windows Server 2022

- Edition: Windows Server 2022 Standard Evaluation
- Licensing Type: Time-limited evaluation
- Activation Expiration: April 25, 2027
- Expiration Time: 5:04:45 PM
- Verification Command: `slmgr /xpr`
- Verification Status: Confirmed

The Windows Server evaluation license is intended for testing and evaluation, not production use.

The evaluation expiration must be considered when scheduling project milestones and maintaining lab reproducibility.

#### VMware Workstation Pro

- Product: VMware Workstation Pro
- Version: 17.6.3
- Licensing: Free-use distribution
- Installation Status: Installed and operational

---

### 6. Network Configuration

#### Virtual Network Settings

| Setting | Configuration |
|---|---|
| VMware Network Mode | NAT |
| Guest Network Adapter | Intel(R) 82574L Gigabit Network Connection |
| IP Address Assignment | DHCP |
| IPv4 Address Type | Private |
| Network Routing | VMware NAT |
| Bridged Networking | Not configured |
| Network Isolation | Separate malware-analysis sandbox planned |

The Windows detection endpoint currently uses VMware NAT networking.

NAT provides network access through the host's virtual network configuration without directly bridging the virtual machine to the physical network.

NAT is not equivalent to complete network isolation.

#### Network Verification

The following command was executed inside Windows Server:

`ipconfig /all`

Observed results:

- Hostname: Windows Server VM (machine-specific name omitted)
- Ethernet adapter: Ethernet0
- DHCP Enabled: Yes
- IPv4 address assigned successfully
- Private IPv4 subnet in use
- Default gateway configured
- DNS server configured
- IP Routing Enabled: No

The VM's full IP configuration and hardware identifiers are excluded from public documentation.

#### Network Safety Requirements

The Windows detection lab and malware-analysis lab will remain separate.

Dynamic malware analysis requires:

- No internet egress
- No bridged networking
- No shared folders
- No clipboard or drag-and-drop sharing
- No USB passthrough
- No mounted host drives
- No cloud synchronization

Any internal virtual network used during malware analysis must be restricted to authorized disposable analysis peers or simulated network services.

---

### 7. Tool Compatibility

The Windows detection endpoint uses Windows Server 2022 x64.

Compatibility assessments are based on documented platform support. Tool versions, selected configurations, and successful integration will be verified during their respective implementation phases.

| Tool | Compatibility Assessment | Installation Status |
|---|---|---|
| Windows PowerShell 5.1 | Confirmed working | Installed |
| Microsoft Sysmon | Windows platform supported; configuration testing pending | Not installed |
| Splunk Universal Forwarder | Windows Server 2022 x64 supported | Not installed |
| Splunk Enterprise | Windows Server 2022 x64 supported; deployment host and sizing TBD | Not installed |
| Atomic Red Team | Windows supported; individual test prerequisites require review | Not installed |
| Wazuh Agent | Windows Server 2022 supported | Not installed |
| Git | Windows compatible; selected version TBD | Not verified |
| Sigma CLI | Version and execution environment TBD | Not installed |

#### Compatibility Notes

- The endpoint uses AMD64/x64 architecture.
- Windows ARM driver compatibility does not apply to this VM.
- Sysmon configuration and event generation will be validated during LAB-02.
- Splunk installation and deployment decisions belong to LAB-03.
- Sysmon-to-Splunk event ingestion belongs to LAB-04.
- Atomic Red Team simulations will be reviewed individually before execution.
- Wazuh agent deployment and log collection will be verified during WAZ-01.
- Sigma conversion and validation will be implemented during detection development.
- Vendor platform support does not establish successful installation or integration.

#### Official References

- Sysmon: https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
- Atomic Red Team: https://github.com/redcanaryco/atomic-red-team
- Splunk Documentation: https://help.splunk.com/
- Wazuh Documentation: https://documentation.wazuh.com/
- Sigma CLI: https://github.com/SigmaHQ/sigma-cli

---

### 8. Snapshot and Recovery Validation

#### Baseline Snapshot

| Field | Result |
|---|---|
| Snapshot Name | LAB-01 Clean Baseline |
| Snapshot Platform | VMware Workstation Pro |
| Guest OS | Windows Server 2022 |
| VMware Tools | Installed |
| Snapshot Created | Yes |
| Recovery Test Performed | Yes |
| Recovery Test Result | Passed |
| Snapshot Creation Date | Pending verification |

A clean baseline snapshot was created after operating system installation and before deployment of the TraceFoundry detection tools.

The VM's RAM allocation was subsequently increased from 2 GB to 8 GB.

A new baseline snapshot reflecting the final hardware configuration is recommended before beginning LAB-02.

#### Recovery Test Procedure

1. Created a clean baseline snapshot in VMware Workstation.
2. Powered on the Windows Server 2022 virtual machine.
3. Logged into the guest operating system.
4. Created a temporary desktop file named `snapshot-test.txt`.
5. Shut down the guest operating system.
6. Opened VMware Snapshot Manager.
7. Selected `LAB-01 Clean Baseline`.
8. Restored the selected snapshot.
9. Powered on Windows Server and logged in.
10. Verified that the temporary test file no longer existed.

#### Verification Command

```powershell
Test-Path "$env:USERPROFILE\Desktop\snapshot-test.txt"
```

#### Observed Result

```text
False
```

**Recovery Test Status: PASSED**

The result confirms that the temporary test file created after the baseline snapshot was absent following restoration.

Windows Server remained accessible after recovery.

#### Recovery Limitations

- Restoring a snapshot discards changes made after the selected recovery point.
- Snapshots are not substitutes for full VM backups.
- Snapshots may preserve earlier virtual hardware configurations.
- Environment settings should be revalidated after significant configuration changes.
- A clean recovery point should be maintained before executing security simulations.

---

### 9. Safety and Authorization Boundaries

The TraceFoundry Windows endpoint is a disposable environment intended for authorized security engineering exercises.

The following boundaries apply:

- Use only owned or explicitly authorized systems.
- Do not use production credentials or sensitive organizational information.
- Do not connect unauthorized systems to the lab.
- Review simulation commands, prerequisites, and cleanup procedures before execution.
- Record test outcomes and unexpected behavior.
- Maintain clean recovery snapshots.
- Do not modify the host operating system unnecessarily.
- Keep the malware-analysis environment separate from the detection lab.
- Do not upload real malware, secrets, credentials, or sensitive raw logs to GitHub.
- Export only reviewed and sanitized evidence.

The detection environment and isolated malware-analysis environment will remain separate.

---

### 10. Resource Planning

The Windows Server 2022 detection endpoint is currently configured with:

- Virtual CPUs: 2
- Allocated RAM: 8 GB (8192 MB)
- Virtual Disk: 80 GB
- Network Mode: NAT

The VM was initially configured with 2 GB of RAM and subsequently increased to 8 GB to better support endpoint monitoring, telemetry collection, and security testing.

Additional resources will be required for:

- Splunk Enterprise and associated ingestion services
- Wazuh server, indexer, and dashboard
- Linux endpoint monitoring
- Isolated malware-analysis virtual machines

Collector services may be deployed on separate supported hosts or run in different sessions to reduce resource contention.

Actual CPU, memory, and disk utilization will be monitored before deploying additional endpoints or increasing the number of concurrently running virtual machines.

Disk consumption will also be monitored as security logs and telemetry accumulate. Event retention and storage limits will be configured as necessary to avoid exhausting available disk space.

No formal performance benchmarks have been completed at this stage.

---

### 11. Pending Verification

The following items remain open:

- [ ] Confirm host Windows edition and build
- [ ] Confirm installed physical RAM
- [ ] Record total NVMe SSD capacity
- [ ] Record available host disk space
- [x] Confirm final guest RAM allocation: 8 GB
- [ ] Verify exact guest operating system build and architecture using CIM
- [ ] Record selected tool versions and remaining compatibility decisions
- [ ] Record snapshot creation date
- [ ] Create and verify a final baseline snapshot after RAM allocation change
- [ ] Attach or reference sanitized snapshot evidence
- [ ] Obtain partner review

---

### 12. Partner Review

| Field | Status |
|---|---|
| Related Issue | LAB-01 (#1) |
| Environment Owner | Project partner |
| Reviewer | Chris |
| Review Status | Pending |
| Snapshot Verification | Passed |
| Documentation Status | Draft / In Progress |
| Approval Date | Pending |

#### Review Criteria

The reviewer should confirm:

1. The Windows VM boots and operates normally.
2. Host and guest specifications are accurately documented.
3. Operating system licensing is recorded.
4. Network mode and safety boundaries are understood.
5. Required tool compatibility has been evaluated.
6. A clean recovery snapshot exists.
7. Snapshot restoration was successfully tested.
8. Evidence supports the reported results.
9. Remaining limitations are documented.

LAB-01 will be considered complete after the required environment information, recovery evidence, and partner review have been verified.

---

### 13. Next Implementation Steps

After LAB-01 is completed and reviewed:

#### LAB-02 — Sysmon Configuration

- Select and document a Sysmon configuration.
- Install Sysmon on the Windows endpoint.
- Generate harmless process activity.
- Verify Event ID 1 in the local Windows Event Log.
- Document event coverage and configuration hash.

#### LAB-03 — Splunk Installation

- Select a supported deployment host.
- Install and configure Splunk.
- Record version, resource requirements, and configuration.

#### LAB-04 — Sysmon to Splunk Ingestion

- Establish event forwarding.
- Confirm fresh Sysmon events in Splunk.
- Validate timestamps, source fields, and host attribution.
- Have both collaborators reproduce the results.

The project will proceed to detection engineering only after the required telemetry collection path is functional and reproducible.
