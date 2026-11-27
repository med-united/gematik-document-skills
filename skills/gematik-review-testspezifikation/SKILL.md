---
name: gematik-review-testspezifikation
description: Prüft eine Testspezifikation (Testentwurf, Testfälle, Testablauf, Standardkonfigurationen) für ein gematik-Produkt gegen gemKPT_Test Tab_Test_014. Verwenden bei "Testspezifikation reviewen", "Testfälle für die gematik prüfen", "Testfallspezifikation EvT", "Gherkin-Szenarien für die Zulassung prüfen".
---

# Review Testspezifikation

Die Testspezifikation ist vor Beginn von EvT bzw. Zulassungstest zu liefern; bei Folgezulassung wird sie
erweitert, wenn Testfälle hinzugekommen oder geändert sind. Struktur nach „Level Test Design", „Level Test Case"
und „Level Test Procedure" (ISO/IEC/IEEE 29119).

Zuerst `references/gemeinsam.md` lesen.

## Vorgehen

1. Steckbrief laden; die Afos der Tabelle „Produkttest/Produktübergreifender Test" und die Liste der
   Anwendungsfälle sind der Maßstab für die Abdeckung.
2. Testkonzept und Afo_Testmatrix danebenlegen.
3. Formale Prüfung nach F-01 bis F-23. Liegt die Spezifikation in einem Testmanagementsystem oder als
   Feature-Dateien vor, gelten die formalen Kriterien für den Export, der eingereicht wird.
4. Die vier Teildokumente prüfen (TS-01 bis TS-16).
5. Stichprobe: mindestens 10 % der Testfälle, mindestens 10 Stück, darunter alle zu sicherheits- und
   interoperabilitätsrelevanten Afos, einzeln gegen TS-05 bis TS-09 lesen.
6. Bericht nach `references/gemeinsam.md` Abschnitt 7; bei Stichproben den Umfang nennen.

## Teildokumente nach Tab_Test_014

### Testentwurfsspezifikation

| ID | Prüfkriterium |
|---|---|
| TS-01 | Zu testende Leistungsmerkmale sind aufgeführt und decken sich mit dem Testkonzept. |
| TS-02 | Vorgehen beim Testentwurf ist beschrieben und die Wahl der Entwurfstechniken begründet (Äquivalenzklassen, Grenzwerte, Zustandsübergänge, Fehlerfälle). |
| TS-03 | Logische Testfälle sind vorhanden. |
| TS-04 | Jeder logische Testfall ist eindeutig einem Leistungsmerkmal zugeordnet. |

### Testfallspezifikation

| ID | Prüfkriterium |
|---|---|
| TS-05 | Konkrete Testfälle haben detaillierte Schritte, die eine dritte Person ohne Rückfrage ausführen kann. |
| TS-06 | Vor- und Nachbedingungen, Testdaten, Konfiguration (Referenz auf eine Standardkonfiguration), Anforderungen an die Testumgebung und Abhängigkeiten sind angegeben. |
| TS-07 | Erwartete Ergebnisse sind konkret und prüfbar (Statuscode, Feldwert, Zustand), nicht „funktioniert". |
| TS-08 | Jeder Testfall hat ein Erfolgreich-/Fehlgeschlagen-Kriterium (gemKPT_Test 4.2.4). |
| TS-09 | Jeder konkrete Testfall ist eindeutig einem logischen Testfall zugeordnet und trägt die Afo-IDs bzw. Anwendungsfall-IDs, die er nachweist, in der Fassung des Steckbriefs. |
| TS-10 | Negativtests und Fehlerfälle sind vorhanden, wo die Afo ein Fehlverhalten, eine Ablehnung oder einen Fehlercode fordert. |

### Testablaufspezifikation

| ID | Prüfkriterium |
|---|---|
| TS-11 | Reihenfolge und Priorisierung der Testfälle sind festgelegt. |
| TS-12 | Aktivitäten zu Aufbau, Start, Abbruch, Wiederaufnahme und Ende sind beschrieben. |
| TS-13 | Kriterien für eine erfolgreiche Durchführung des Ablaufs sind genannt. |

### Spezifikation der Standardkonfigurationen

| ID | Prüfkriterium |
|---|---|
| TS-14 | Alle Konfigurationsparameter mit ihren möglichen Werten sind aufgeführt. |
| TS-15 | Je Standardkonfiguration sind die Werte festgelegt; Testfälle referenzieren genau eine davon. |

## Abdeckung und Sonderthemen

| ID | Afo / Quelle | Prüfkriterium |
|---|---|---|
| TS-16 | Tab_Test_021 | Mindestens ein Testfall pro Anforderung der Produkttest-Tabelle und pro Anwendungsfall; Interoperabilität vollständig abgedeckt. Lücken sind in der Afo_Testmatrix als nicht ausgeführt mit Begründung geführt. |
| TS-17 | Tab_Test_014 | Bei Testautomatisierung: Testskripte sind selbst getestet; Skriptversion ist dem Testfall zugeordnet. |
| TS-18 | Tab_Test_014 | Implementierungsleitfäden für Clientsysteme sind berücksichtigt, wo einschlägig. |
| TS-19 | A_26675 | Nur neues Testvorgehen (z. B. PoPP, ZETA): Testszenarien in BDD-Technik, z. B. Gherkin; jedes Szenario mit Afo-Bezug. |
| TS-20 | TIP1-A_4191, GS-A_2162 | Testdaten sind synthetisch; kein produktives Schlüsselmaterial. |
| TS-21 | TIP1-A_6772, TIP1-A_6529 | Interoperabilitätstestfälle nennen das Referenzobjekt bzw. die Gegenstelle und deren Version. |
| TS-22 | Tab_Test_022 | Bei Folgezulassung: Regressionstestfälle sind markiert und aus der Auswirkungsanalyse der Release Notes abgeleitet. |
| TS-23 | Konsistenz | Testfall-IDs sind stabil und identisch in Testspezifikation, Testprotokoll, Testbericht und Afo_Testmatrix. Ein Testfall, der in der Matrix steht, existiert hier, und umgekehrt. |
| TS-24 | Qualität | Ein Testfall weist nicht pauschal zwanzig Afos nach. Wo ein Testfall mehrere Afos trägt, ist je Afo erkennbar, welcher Schritt oder welches erwartete Ergebnis sie belegt. |
| TS-25 | Qualität | Testfälle prüfen das Außenverhalten nach Spezifikation, nicht nur die eigene Implementierung (Unit-Tests ohne Schnittstellenbezug sind kein Afo-Nachweis). |
