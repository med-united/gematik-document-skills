---
name: gematik-review-notfallkonzept
description: Prüft ein Notfallkonzept (Notfallvorsorgekonzept und Notfallhandbuch) eines gematik-Anbieters gegen TI-Sec_0340 des TI Security Standards, den BSI-Standard 200-4 in der Prüfsystematik der gematik und das TI-Notfallmanagement nach gemRL_Betr_TI. Verwenden bei "Notfallkonzept reviewen", "Notfallhandbuch prüfen", "BCM-Dokumente für die gematik", "BIA prüfen", "Zulassungs-Dokumentenreview Notfallkonzept".
---

# Review Notfallkonzept (Anbieter)

Die gematik prüft das Notfallkonzept im „Zulassungs-Dokumentenreview" gegen das Control **TI-Sec_0340**
(gemTI_SEC_Standard, verbindlich über A_27098-01, SGL 1–3, jährlich vorzulegen). Weil das Control allgemein
formuliert ist, ergänzt die gematik die Prüfung um die Detailanforderungen des **BSI-Standards 200-4**; TI-Sec_0340
ist dabei die übergeordnete MUSS-Anforderung. Bewertet wird je Prüfpunkt mit ERFÜLLT / TEILWEISE ERFÜLLT /
NICHT ERFÜLLT.

Zuerst `references/gemeinsam.md` lesen.

## Vorgehen

1. Security Governance Level des Produkts bestimmen (gemTI_SEC_Standard Anhang A1) und prüfen, ob TI-Sec_0340,
   TI-Sec_0350 und TI-Sec_0360 gelten.
2. Dokumentensatz feststellen: Notfallvorsorgekonzept, Notfallhandbuch, BIA-Auswertungsbogen, Wiederanlauf- und
   Wiederherstellungspläne (WAP/WHP), Alarmierungsliste, Übungskonzept. Fehlende mitgeltende Dokumente sind Befunde.
3. Formale Prüfung nach F-01 bis F-23.
4. Ebene 1 prüfen (NK-01 bis NK-08), dann Ebene 2 und 3 mit den Leitfragen.
5. TI-Notfallmanagement und Konsistenz prüfen (NK-30 ff.).
6. Bericht nach `references/gemeinsam.md` Abschnitt 7; die P-IDs der gematik in der Spalte Prüfkriterium mitführen.

## Ebene 1: Mindestinhalte nach TI-Sec_0340

| ID | P-ID gematik | Prüfpunkt | Leitfrage |
|---|---|---|---|
| NK-01 | 01-01-00 | Übergeordnete Notfallstrategie und Einordnung der TI-Dienste | Gibt es eine erkennbare BCM-/Notfallleitlinie, und ist die Rolle der TI-Dienste im Leistungsangebot und in der TI eingeordnet? Belege: Ziele des BCM definiert; Bedeutung der TI-Dienste für die Leistungserbringung beschrieben; strategische Verankerung durch Leitlinie oder Managemententscheidung. |
| NK-02 | 01-02-00 | Gesetzliche und vertragliche Anforderungen | Sind gesetzliche, regulatorische und vertragliche BCM-Anforderungen identifiziert und ist ihre Berücksichtigung dargestellt? |
| NK-03 | 01-03-00 | Rollen und Verantwortliche | → Details NK-10, NK-11 |
| NK-04 | 01-04-00 | Notfallvorsorge inkl. Auswirkungsanalyse (BIA) | → Details NK-13, NK-15 |
| NK-05 | 01-05-00 | Szenariounabhängige Bewältigungsstrategie, insbesondere TI-spezifische Eskalation zu weiteren Anbietern und zur gematik | → Details NK-20 bis NK-23 |
| NK-06 | 01-06-00 | Szenariospezifische Notfallpläne | Liegt ein Szenariokatalog vor (Brand, Wassereinbruch usw. und TI-spezifisch: Ausfall verfügbarkeitskritischer TI-Produkte, Schwächung oder Kompromittierung von Schlüsselmaterial), und gibt es zu jedem Szenario einen WAP/WHP? |
| NK-07 | 01-07-00 | Nachbereitung von Notfällen | → Details NK-25 |
| NK-08 | 01-08-00 | Prävention inkl. Fachkunde und Schulungen | → Details NK-12; Übungen siehe NK-33 |

## Ebene 2: Notfallvorsorgekonzept (BSI 200-4 Kap. 4.4.2)

| ID | P-ID | Prüfpunkt (BSI 200-4) | Checkliste der gematik |
|---|---|---|---|
| NK-10 | 02-02-03 | Notfallvorsorgeorganisation, AAO (4.3) | Rollen und Funktionen beschrieben; Aufgaben, Verantwortlichkeiten, Zuständigkeiten festgelegt; Stellvertretungen geregelt; Zusammenwirken der Rollen beschrieben. |
| NK-11 | 02-02-04 | Notfallbewältigungsorganisation, BAO (4.3, 5.1) | Rollen und Funktionen der BAO beschrieben; Aufgaben und Zuständigkeiten festgelegt; Stellvertretungen geregelt. |
| NK-12 | 02-02-05 | Schulung und Sensibilisierung (4.6, 4.7) | Zielgruppen definiert; Schulungsformate definiert; Inhalte oder Ziele beschrieben; regelmäßige oder anlassbezogene Durchführung vorgesehen. |
| NK-13 | 02-02-06 | BIA-Methodik (7.1) | Eigenes Methodikkapitel oder -dokument; Schadensszenarien, Schadenspotenzial, Schadenskategorien; **Untersuchungszeitraum, betrachtete Zeithorizonte, Untragbarkeitsniveau**; Methodik auf alle betrachteten Geschäftsprozesse angewendet. |
| NK-14 | 02-02-08 | Methodik WAP/WHP (12) | Methodik zur Erstellung beschrieben; Ableitung aus den Ergebnissen der Notfallvorsorge (BIA) beschrieben; Verantwortlichkeiten für Erstellung, Pflege, Aktualisierung; Anforderungen an Inhalt, Struktur und Aufbau der Pläne; regelmäßige Überprüfung vorgesehen. |
| NK-15 | 02-02-18 | Ergebnisse der BIA (4.4.1, 7.3) | Ergebnisse verfügbar oder referenziert; Methodik und Ergebnisse verknüpft; Herleitung der Einstufungen dokumentiert. Je Geschäftsprozess: **MTPD, RTO, MBCO, RPO, Single Points of Failure**. |

## Ebene 3: Notfallhandbuch (BSI 200-4 Kap. 4.4.2)

| ID | P-ID | Prüfpunkt (BSI 200-4 / Afo) | Checkliste der gematik |
|---|---|---|---|
| NK-20 | 03-02-04 | Allgemeine Sofortmaßnahmen (5.3 / GS-A_4127) | Sofortmaßnahmen für die initiale Bewältigung beschrieben; **Schutz von Personen (Leib und Leben)**; Reihenfolge oder Priorisierung; Verantwortlichkeiten. |
| NK-21 | 03-02-05 | Szenariospezifische Sofortmaßnahmen (5.3 / GS-A_4127) | Je relevantem Szenario spezifische Maßnahmen; Zuordnung zu Szenarien; Reihenfolge; Verantwortlichkeiten. |
| NK-22 | 03-02-06 | Detektion und Meldung (5.2.1, 5.2.2 / GS-A_4125, GS-A_4126) | Meldestellen definiert; Kriterien zur Unterscheidung Störung / potenzieller Notfall; Eskalationswege zur zentralen Entscheidungsinstanz. |
| NK-23 | 03-02-07 | Alarmierung der BAO (5.2.3) | Wer entscheidet über die Alarmierung; welche Rollen, Funktionen, Gremien werden alarmiert; Alarmierungswege und Kommunikationsmittel (Alarmierungsliste). |
| NK-24 | 03-02-10 | Wiederanlauf und Wiederherstellung (12) | WAP/WHP benannt oder referenziert; Zuordnung zu Ressourcen bzw. Ausfallszenarien; Verantwortlichkeiten für die Durchführung; Aufbau entspricht der Methodik aus NK-14. Je WAP: Geltungsbereich, Zweck und Ziel, Aktivierungsprozess, Rollen mit Kontaktdaten und Stellvertretung, benötigte Ressourcen mit RTO und Dokumentation, Ablauf mit konkreten Tätigkeiten. **Detailgrad: Eine fachkundige dritte Person kann den Wiederanlauf danach durchführen.** |
| NK-25 | 03-02-13 | Analyse und Bewertung der Notfallbewältigung (5.9 / GS-A_4134) | Dokumentierter Nachbereitungsprozess; zu erhebende Erkenntnisse und Bewertungskriterien; Ableitung und Dokumentation von Verbesserungsmaßnahmen; Verantwortliche für Umsetzung und Nachverfolgung; Aktualisierung betroffener BCM-Dokumente geregelt. |
| NK-26 | 03-02-15 | BIA-Auswertungsbogen als mitgeltendes Dokument (4.4.1, 7.3) | Im Notfallhandbuch referenziert; enthält Informationen zur Priorisierung der Bewältigung; mit den übrigen BCM-Dokumenten abgestimmt. |

Die gematik begrenzt ihre Prüfvorlage im Zulassungsreview auf die zulassungsrelevanten Punkte; die volle
Prüfvorlage folgt dem gesamten BSI 200-4. Punkte des Standards, die hier nicht aufgeführt sind, bei Bedarf
ergänzend prüfen und als „über die Zulassungsprüfung hinaus" kennzeichnen.

## TI-Notfallmanagement, Übungen, Konsistenz

| ID | Prüfkriterium |
|---|---|
| NK-30 | Lokaler Notfall und **TI-Notfall** sind unterschieden; TI-Notfallerkennung im Incident Management als Prio-1-Incident mit Kennzeichnung „TI-Notfall" (GS-A_4125). |
| NK-31 | Eskalation an den Gesamtverantwortlichen TI: unverzüglich, persönliche Benachrichtigung (GS-A_4126); Zusammenarbeit mit EMC und Lösungsteam (GS-A_4128 bis GS-A_4130). |
| NK-32 | Auswirkungsanalyse je TI-Service mit Notfallszenario, Wechselwirkungen mit anderen Produkten/TI-Services und Risikobewertung (GS-A_4121); TI-Notfallvorsorgedokumentation (GS-A_4123); Notfall-Logbuch Wann/Wer/Was/Wie/Ergebnis (GS-A_4137); Wiederherstellungsbericht (GS-A_4138). |
| NK-33 | Notfallübungskonzept mit Test- und Übungsplan (TI-Sec_0350, bis 31.01. des Jahres) und quartalsweise Übung für die als kritisch identifizierten Szenarien, Übungskonzept vorab an die gematik (TI-Sec_0360). |
| NK-34 | Meldung von Sicherheitsvorfällen und Datenschutzverstößen binnen 72 Stunden ist im Ablauf verankert (TI-Sec_0330). |
| NK-35 | Zeitziele sind beziffert (Rückmeldung, Alarmierung der Geschäftsführung, Vertretung bei Nichterreichbarkeit, Fristen der Nachbereitung) und durch Übungen belegt oder als Zielwert gekennzeichnet. |
| NK-36 | Konsistenz mit Betriebshandbuch (Aufnahme/Unterbrechung/Wiederaufnahme, Rollen, Kontakte), Sicherheitskonzept (BIA, Schutzbedarf) und Redundanzkonzept (A_25902, A_25903). |
| NK-37 | Offline-Verfügbarkeit: BIA-Auswertungsbogen, Alarmierungsliste und Pläne sind auch ohne die ausgefallene IT erreichbar. |

## Reale Befunde der gematik als Maßstab

Zulassungs-Dokumentenreview eines Notfallkonzepts (11/2026, Prüfstandard BSI 200-4):

- NICHT ERFÜLLT, BIA-Methodik: Kein vollständiges Methodikkapitel. Schadensszenario, Schadenspotenzial und Schadenskategorie waren festgelegt, Untersuchungszeitraum, Zeithorizonte und Untragbarkeitsniveau nicht. „Auf Grundlage der vorliegenden Angaben lassen sich die Ergebnisse derzeit nicht objektiv herleiten."
- NICHT ERFÜLLT, Methodik WAP/WHP; NICHT ERFÜLLT, Alarmierung der BAO; NICHT ERFÜLLT, BIA-Auswertungsbogen nicht referenziert.
- TEILWEISE ERFÜLLT, BIA-Ergebnisse: Ergebnisse lagen vor, aber ohne MTPD, RTO, MBCO, RPO und SPoF.
- TEILWEISE ERFÜLLT, Wiederanlauf: Die Vorgehensweisen beschrieben „überwiegend ein allgemeines Vorgehen"; vollständige WAPs im Sinne von BSI 200-4 Kap. 12.2 fehlten.
- TEILWEISE ERFÜLLT, Schulung: „Der Text beschreibt die Herleitung des Schulungskonzepts, stellt dessen Inhalte jedoch nicht näher dar."
- TEILWEISE ERFÜLLT: Notfallstrategie/Einordnung der TI-Dienste, AAO und BAO (Stellvertretung, Zusammenwirken), allgemeine Sofortmaßnahmen (Schutz von Personen), Detektion und Meldung, Nachbereitung.

Was zur Behebung geführt hat: eigene Abschnitte für BIA-Methodik, WAP/WHP-Methodik mit Planübersicht,
BIA-Auswertungsbogen mit allen Kenngrößen je Geschäftsprozess, Alarmierung mit Alarmierungsliste,
Stellvertretungsregelungen, Zielgruppen- und Schulungsformat-Tabellen, Schritt „Schutz von Personen" vor allen
anderen Sofortmaßnahmen, Meldestellen und Kriterien zur Ersteinschätzung.
