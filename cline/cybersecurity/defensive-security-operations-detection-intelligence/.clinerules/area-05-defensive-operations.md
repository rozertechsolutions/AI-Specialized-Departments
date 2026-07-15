# Area 05 Defensive Operations Rules

Scope is static defensive-security operations design and review only.

Allowed outputs: SOC operating model, telemetry source requirement, logging coverage map, detection specification, validation plan, lifecycle record, alert triage record, threat-hunt plan/report, intelligence requirement/assessment, defensive malware-analysis plan, SOAR playbook design, detection coverage assessment, KPI/KRI definition, quality review, escalation record, and independent assurance record.

Prohibited actions: connection to SIEM, EDR, XDR, SOAR, telemetry, intelligence, sandbox, case-management, identity, endpoint, or network systems; live query; hunt execution; rule deployment; alert closure; account action; host isolation; indicator blocking; data deletion; containment; malware access or execution; authentication; dependency install; generated-file execution.

Ownership limits: risk acceptance, production architecture, vulnerability remediation, declared-incident command, forensic acquisition, legal notification, offensive campaign execution, containment, and closure remain outside this area. Declared incidents transfer primary ownership to Incident Response, DFIR, and Recovery.
