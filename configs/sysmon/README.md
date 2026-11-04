
# TraceFoundry — Sysmon Configuration

## LAB-02: Sysmon Configuration

**Related Issue:** #2  
**Operating System:** Windows Server 2022 Standard Evaluation (x64)  
**Sysmon Version:** 15.22  
**Sysmon Schema:** 4.91  
**Status:** In Progress  
**Reviewer:** Chris (Pending)

---

## 1. Objective

Configure Sysmon to collect Windows endpoint telemetry
for the TraceFoundry detection engineering lab.

The configuration supports investigation of PowerShell
execution, network connections, file creation, and
registry-based persistence.

## 2. Environment

| Component | Configuration |
|---|---|
| Hypervisor | VMware Workstation Pro 17.6.3 |
| Guest OS | Windows Server 2022 Standard Evaluation |
| Architecture | x64 |
| RAM | 8 GB |
| vCPUs | 2 |
| Virtual Disk | 80 GB |
| Network Mode | NAT |
| Sysmon Version | 15.22 |
| Schema Version | 4.91 |

## 3. Configuration

Configuration file:

`configs/sysmon/sysmonconfiguration.xml`

The initial configuration uses SHA-256 hashing.

| Event ID | Event Type | Configured |
|---|---|---|
| 1 | Process Creation | Yes |
| 3 | Network Connection | Yes |
| 11 | File Creation | Yes |
| 12 | Registry Key Created/Deleted | Yes |
| 13 | Registry Value Modified | Yes |
| 14 | Registry Key Renamed | Yes |

The initial configuration uses broad event collection
for controlled testing. This may produce high log volume
and will require tuning before sustained ingestion.

## 4. Installation

Sysmon was downloaded from Microsoft Sysinternals
and extracted to:

`C:\Users\Administrator\Downloads\Sysmon`

Version verification:

```powershell
.\Sysmon64.exe -?
```

Schema verification:

```powershell
.\Sysmon64.exe -s
```

Installation command:

```powershell
.\Sysmon64.exe -i .\sysmonconfiguration.xml
```

Installation output confirmed:

- Configuration file validated
- Sysmon64 installed
- SysmonDrv installed and started
- Sysmon64 started

Installation status: Successful

## 5. Validation

Windows event log channel:

`Microsoft-Windows-Sysmon/Operational`

Service verification:

```powershell
Get-Service Sysmon64
```

Active configuration verification:

```powershell
.\Sysmon64.exe -c
```

Test process:

```powershell
notepad.exe
```

Expected result:

Sysmon Event ID 1 records Notepad process creation.

Actual Event ID 1 result: Passed — Notepad process creation observed in Sysmon Operational log.

Additional Event ID 3, 11, and 12-14 verification:
Pending.

## 6. Configuration Integrity

Hash algorithm: SHA-256

Command:

```powershell
Get-FileHash .\sysmonconfiguration.xml -Algorithm SHA256
```

SHA-256 Hash: F4CC54128674A5844B23E6B602253F3EC36232F2AC3D8457CCF4F52E25CAC3B3

The recorded hash must match the exact XML committed
to this repository.

## 7. Known Limitations

- Broad collection may generate substantial log volume.
- Sysmon does not independently provide complete coverage
  for every scheduled task activity.
- Some detections may require additional Windows logs.
- Splunk ingestion has not yet been validated.
- The configuration is intended for a disposable lab,
  not production deployment.

## 8. LAB-02 Checklist

- [x] Downloaded Sysmon
- [x] Verified version 15.22
- [x] Verified schema 4.91
- [x] Created XML configuration
- [x] Installed Sysmon
- [ ] Confirm service status
- [ ] Confirm active configuration
- [ ] Document Event ID 1 evidence
- [ ] Verify other configured event types
- [ ] Record SHA-256 hash
- [ ] Obtain partner review

## 9. References

Microsoft Sysmon:
https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

Related Issue:
https://github.com/cnaraysingh05/tracefoundry/issues/2
