---
name: gematik-review-betriebshandbuch
description: Prüft ein Betriebshandbuch (BHB) eines gematik-Anbieters vor der Einreichung zur Anbieterzulassung gegen GS-A_5343-01, die Betriebshandbuch-Afos des Anbietertypsteckbriefs und die Kriterien des gematik-Prüfprotokolls. Verwenden bei "Betriebshandbuch reviewen", "BHB prüfen", "betriebliche Eignung", "Prüfprotokoll BHB", "Feedback der gematik zum Betriebshandbuch einarbeiten".
---

# Review Betriebshandbuch (Anbieter)

Das Betriebshandbuch ist der Nachweis für das Prüfverfahren „Betriebshandbuch betriebliche Eignung" im
Anbietertypsteckbrief. Die gematik (Operations: Service Delivery Management und Transition Management) prüft es
mit einem Prüfprotokoll und vergibt Fehlerklassen; FK 1 und 2 verhindern die Abnahme.

Zuerst `references/gemeinsam.md` lesen (Grundregeln, formale Kriterien F-01 bis F-23, Fehlerklassen, Berichtsformat).

## Vorgehen

1. Anbietertypsteckbrief in der Antragsversion laden und die Tabelle „Betriebshandbuch betriebliche Eignung"
   als Soll-Liste übernehmen. Zusätzlich die Tabellen „Prozessprüfung" und „Anbietererklärung" laden: Deren
   Afos werden nicht am BHB geprüft, das BHB darf ihnen aber nicht widersprechen.
2. Anbieterkonstellation klären (gemKPT_Betr 3.4.2, Steckbrief 3.1.4): Was erbringt der Anbieter selbst, was ein
   Unterauftragnehmer? Was nicht ausgelagert werden darf, muss im BHB beim Anbieter liegen.
3. Formale Prüfung nach F-01 bis F-23.
4. Pflichtgliederung prüfen (BHB-01 bis BHB-07).
5. Jede Afo der Soll-Liste einer Fundstelle zuordnen und den Erfüllungsgrad bewerten (BHB-08 ff.).
6. Perspektivtest über das ganze Dokument (BHB-P).
7. Bericht nach `references/gemeinsam.md` Abschnitt 7.

## Checkliste

### Perspektive (häufigster FK-1-Befund)

| ID | Prüfkriterium |
|---|---|
| BHB-P1 | Das Dokument beschreibt den **Betrieb durch den Anbieter**, nicht das Produkt. Jedes Kapitel beantwortet: Wer tut was, wann, womit, und wer wird informiert? |
| BHB-P2 | Bei jedem Kapitel ist erkennbar, aus welcher Sicht es geschrieben ist (Anbieter, Unterauftragnehmer, Hersteller). |
| BHB-P3 | Keine Optionskataloge. Wo Alternativen genannt werden, steht die gewählte Lösung dabei. |

### Pflichtgliederung nach GS-A_5343-01 (gemRL_Betr_TI 2.2.1)

| ID | Prüfkriterium |
|---|---|
| BHB-01 | **Einführung:** betriebliche Rolle und Identifikation (Teilnehmer-ID), Version, Freigabe- und Prüfungsverantwortung, ergänzende Dokumente, Dokumentenstand-Basis. Kein Punkt ist nur Überschrift. |
| BHB-02 | **Systemüberblick:** Architektur, System, Komponenten, Außenschnittstellen des Produkttyps. |
| BHB-03a | **Initiale Aufnahme des Betriebs:** Reihenfolge und Rahmenbedingungen, aus betrieblicher Sicht (Onboarding TI-ITSM, Change, Freigaben). |
| BHB-03b | **(Kontrollierte) Unterbrechung / Übergang in den Notbetrieb:** Wann tritt sie ein, welche Gründe, wer entscheidet, wer wird wie informiert? |
| BHB-03c | **Wiederaufnahme des Normalbetriebs:** Was ist zu beachten, wer wird informiert, wie laufen Kommunikation, Koordination und Dokumentation? |
| BHB-03d | **Beendigung des Betriebs:** Reihenfolge der Abschaltung, Aufräumarbeiten, Datenlöschung, Information der Kunden und der gematik. |
| BHB-04 | **Lokales ITSM:** Incident, Problem, Change und die weiteren Prozesse der Richtlinie sind in den internen Abläufen kompakt dargestellt, mit Rollen und Aktivitäten je Prozess. Weitere interne ITSM-Prozesse sind aufgelistet und kurz beschrieben. |
| BHB-05 | **Integration in das TI-ITSM:** Die Bedienung der übergreifenden Prozesse ist ausführlich beschrieben; Schnittstellen und Interaktionen zwischen lokalem ITSM und TI-ITSM sind dokumentiert (Ticketübergabe, Rückgabe, Status, Verifikation). |
| BHB-06 | **Relevanter Teil des Servicekatalogs** (GS-A_5607: Leistung, Abruf-/Freigabeprozess, Kosten, Reaktions-/Lösungs-/Verifikationsfrist, Input-Daten, Betriebsumgebung). |
| BHB-07 | **Nachweis zur Umsetzung der Anforderungen:** Tabelle Afo → Kapitel für alle Afos der Soll-Liste. |

### Fachliche Abdeckung (Beispiel gemAnbT_TI-M_Pro, Tabelle „Betriebshandbuch"; je Steckbrief anpassen)

| ID | Thema | Afos (Beispiele) | Worauf achten |
|---|---|---|---|
| BHB-08 | Rollen und Kontakte | A_26501, GS-A_5561 | Partner Manager, Service Delivery Manager, Service Executive Manager, TI-ITSM-Prozessmanager, Notfallbeauftragter, Ansprechpartner Informationssicherheit/Datenschutz/Vertrag; 24/7-Kontaktpunkt, SPOC, Manager-on-Duty; Stellvertretungen. |
| BHB-09 | Support / UHD | TIP1-A_7260-01, TIP1-A_6389-02 | Servicezeiten, Kanäle; was laut Konstellation nicht ausgelagert werden darf (Befund 2024: Versichertenhelpdesk muss beim Anbieter liegen). |
| BHB-10 | Kommunikation | GS-A_4085, GS-A_4086, GS-A_3920-01 | Telefon, E-Mail, TI-ITSM-System; Erreichbarkeit; Eskalation an den Gesamtverantwortlichen TI mit Auslösern. |
| BHB-11 | Incident Management | GS-A_3876, GS-A_3884, GS-A_3888, GS-A_3889, GS-A_3902 ff., GS-A_5449, GS-A_5450, GS-A_4125 | Wann wird ein übergreifender Incident eröffnet; Priorität aus Dringlichkeit und Auswirkung; Kennzeichnung sicherheits-/datenschutzrelevant; TI-Notfall-Kennzeichnung; Rückgabe des Tickets an die gematik nach Abschluss. |
| BHB-12 | Problem Management | GS-A_3958 ff., GS-A_5377 | Pro- und reaktive Problemerkennung, RCA, Known Errors. |
| BHB-13 | Change Management | A_13575, GS-A_4398-02, GS-A_4407-01, GS-A_4424-01, GS-A_5361, GS-A_5601-01, GS-A_5610-03 | Vollständiger RfC, Vorprüfung auf Genehmigungspflicht, Fallbackplan, Emergency Change, Verifikation mit Frist, Vorlaufzeiten; Inbetriebnahme und Außerbetriebnahme als Change. |
| BHB-14 | Service Level und Reporting | GS-A_4100, GS-A_5604 | Messung, Bericht, Begründung und Maßnahmen bei Untererfüllung. |
| BHB-15 | Konfiguration | GS-A_4114, GS-A_4115 | Konfigurationsdaten, Pflege. |
| BHB-16 | TI-Notfallmanagement | GS-A_4121, GS-A_4123, GS-A_4124, GS-A_4126, GS-A_4127, GS-A_4132, GS-A_4136, GS-A_4137, GS-A_4138 | Auswirkungsanalyse je TI-Service, Notfallvorsorgedokumentation, Eskalation, Sofortmaßnahmen, Wiederherstellung, Statusinformation, Notfall-Logbuch, Wiederherstellungsbericht. Konsistent zum Notfallkonzept. |
| BHB-17 | Verfügbarkeit und Performance | produkttypspezifisch, z. B. A_23117-01 (TI-M), A_24813 (CardLink Skalierung) | Konkrete Umsetzung: Wie wird skaliert, wer überwacht welche Schwelle, was passiert bei Überschreitung? Abweichungen (z. B. On-Premise) je Betrieb dokumentiert. |
| BHB-18 | Produkttypspezifische Betriebs-Afos | aus dem Steckbrief | Jede Afo einzeln, nicht pauschal. |
| BHB-19 | Audits | GS-A_3917, GS-A_4855-02 | Bereitstellung der ITSM-Dokumentation bei Audits ist beschrieben (Befund 2024: fehlte, FK 1). |

### Konsistenz

| ID | Prüfkriterium |
|---|---|
| BHB-20 | Rollen, Kontakte, Servicezeiten und Eskalationswege stimmen mit Notfallkonzept, Sicherheitskonzept und den Stammdaten im TI-ITSM überein. |
| BHB-21 | Alarmierungsstrecke ist Ende zu Ende beschrieben (Annahme → Ticket → Alarmierung Rufbereitschaft → fachliche Bearbeitung → Rückmeldung), einschließlich externer Erreichbarkeitsdienste und der Abfrage der V-ID bei Anrufen der gematik. |
| BHB-22 | Was im BHB steht, hält der Prozessprüfung stand: Die benannten Personen können Incident, Problem und Change im TI-ITSM so vorführen, wie beschrieben. |

## Reale Befunde der gematik als Maßstab

Aus dem Prüfprotokoll zum Betriebshandbuch eHealth-CardLink (Runde 1: V0.4, Runde 2: Stand 05.01.2025; 19
Prüfkriterien, nach Runde 2 noch 5 NOK):

- FK 1: „Es liest sich wie ein Produkthandbuch eines Herstellers, aber leider nicht wie ein Betriebshandbuch. Die betrieblichen Aspekte kommen zu kurz oder sind teilweise nicht erkennbar."
- FK 1: GS-A_3917 „findet sich nicht im Betriebshandbuch wieder".
- FK 3 zu GS-A_5343: Aufnahme/Unterbrechung/Beendigung nur produktseitig beschrieben; interne ITSM-Abläufe fehlen (welche Rolle übernimmt welche Aktivität in Change, Incident, Problem); Integration in das TI-ITSM nicht erkennbar; „Die Aufführung einiger Anforderungen ist nicht ausreichend."
- Nachforderung Runde 2: Unterbrechung des Betriebs unvollständig (wann, welche Gründe, wer wird wie informiert); Wiederaufnahme zu knapp (was beachten, wen informieren, Kommunikation, Koordination, Dokumentation).
- FK 2 zu A_24813: Es werden Herausforderungen und Möglichkeiten der Skalierung dargestellt, aber nicht, wie der Anbieter konkret damit umgeht.
- FK 3/4 formal: keine Referenzen; GitHub-Links nicht aufrufbar; fehlende Quellenangaben für übernommene Grafiken aus der TI-Wissensdatenbank; Glossar, Abkürzungs-, Tabellen- und Abbildungsverzeichnis fehlen; Inhaltsverzeichnis ohne Überschrift und nicht auf eigener Seite; Seitenzahlen, Fußzeile, Kapitelnummern fehlen; Übersetzungsfehler; „Dokumentenstand-Basis" nur als Überschrift.

Aus dem Prüfbericht einer Alarmierungsübung (02/2026), relevant für BHB-21: fachliche Erreichbarkeit trotz
erreichbarer Hotline nicht gegeben (kritisch), V-ID nicht abgefragt (kritisch), ZIS-Ticket nach Abschluss nicht
an die gematik zurückgegeben (niedrig), Rückrufe erreichten die gematik nicht (Hinweis).
