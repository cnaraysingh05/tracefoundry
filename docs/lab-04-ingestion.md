# LAB-04 · Trace one Sysmon event into Splunk

Chris owns this check. Laura reproduces the search. Status: prepared, awaiting live execution.

## Capture on the Windows Server 2022 guest

After LAB-02 enables Sysmon process creation and LAB-03 provides a Splunk receiver, configure the Windows forwarder to read `Microsoft-Windows-Sysmon/Operational`. Record the actual receiver, input configuration, destination index, and sourcetype in the private lab record. Verify the receiver connection and synchronize guest clocks before generating a fresh event.

Run in guest PowerShell. The PID and start time narrow the lookup to this launch.

```powershell
$start = Get-Date
$process = Start-Process notepad.exe -PassThru
Start-Sleep -Seconds 3
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1; StartTime=$start} | Where-Object {
    $xml = [xml]$_.ToXml()
    ($xml.Event.EventData.Data | Where-Object Name -eq 'ProcessId').'#text' -eq [string]$process.Id
} | Select-Object -First 1 -ExpandProperty Message
```

Copy the event's ProcessGuid, Computer (from the event details), UtcTime, Image, and CommandLine. If the query returns nothing, check Sysmon locally before troubleshooting the forwarder.

## Reproduce in Splunk

Replace both placeholders. Use the lab index and paste the GUID from the local event. Start with the raw event so this check works before field aliases are established.

```spl
index=<lab_index> earliest=-15m latest=now "<ProcessGuid>"
```

Compare the guest computer name, ProcessGuid, UTC event time, image, and command line with the local event. Record the actual sourcetype, extracted field names, and how Splunk's `_time` compares with Sysmon's UtcTime. If the event is missing, check channel input permissions, forwarder connection, receiver/index routing, then the search time window.

## Evidence for issue #4

Record the run time, configuration revision, sanitized local event, exact SPL, observed result, and Laura's reproduction result. A pass requires Chris and Laura to find the same fresh event in Splunk and match it to the local record. Current result: pending.
