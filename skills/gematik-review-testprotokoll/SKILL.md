---
name: gematik-review-testprotokoll
description: Prüft ein Testprotokoll der Eigenverantwortlichen Tests oder Zulassungstests eines gematik-Produkts gegen gemKPT_Test Tab_Test_017. Verwenden bei "Testprotokoll reviewen", "Testprotokoll für die gematik prüfen", "EvT-Ergebnisse prüfen", "Testlog Zulassung".
---

# Review Testprotokoll

Das Testprotokoll dokumentiert die detaillierten Ergebnisse der Testdurchführung je Produktversion. Es wird mit
Abschluss von EvT bzw. Zulassungstest geliefert, bei Erst- und Folgezulassung immer. Struktur nach „Level Test
Log" bzw. „Anomaly Report" (ISO/IEC/IEEE 29119).

Zuerst `references/gemeinsam.md` lesen.

## Vorgehen

1. Testspezifikation, Afo_Testmatrix und Release Notes derselben Produktversion danebenlegen.
2. Formale Prüfung nach F-01 bis F-23 (bei Werkzeug-Exporten: Deckblatt und Metadaten des eingereichten Dokuments).
3. Pflichtinhalte TP-01 bis TP-09.
4. Abgleich: Menge der Testfälle in Spezifikation, Protokoll und Matrix (TP-10 bis TP-14). Wenn die Dateien
   maschinenlesbar vorliegen, den Abgleich per Skript machen und Differenzlisten in den Bericht aufnehmen.
5. Bericht nach `references/gemeinsam.md` Abschnitt 7.

## Pflichtinhalte nach Tab_Test_017

| ID | Prüfkriterium |
|---|---|
| TP-01 | Identifikation: Produkttyp, Produktversion nach gemSpec_OM (inkl. Build/Hash, wenn verwendet), Steckbriefversion, Testumgebung (RU/TU, Gegenstellen mit Version), Zeitraum, Tester. |
| TP-02 | **Nachweis über die Durchführung aller Testfälle:** Für jeden Testfall der Spezifikation gibt es einen Eintrag mit Ergebnis. |
| TP-03 | Ergebnis je Testfall ist eindeutig (bestanden / fehlgeschlagen / blockiert / nicht ausgeführt) und folgt dem Erfolgreich-/Fehlgeschlagen-Kriterium der Spezifikation. |
| TP-04 | **Erreichter Abdeckungsgrad** ist ausgewiesen, getrennt nach funktional, nicht-funktional und produktübergreifend, und mit dem Ziel aus dem Testkonzept verglichen. |
| TP-05 | **Chronologische Übersicht** der relevanten Vorgänge: Start, Ende, Unterbrechungen, Wiederholungen, Wechsel von Build oder Konfiguration. |
| TP-06 | **Problemreport** für TI-relevante Probleme, einschließlich der offen gebliebenen. |
| TP-07 | Jedes Problem hat einen Schweregrad nach gemKPT_Test 4.2.4.1 („Sehr schwer", „Schwer", „Mittel", „Leicht") **mit Begründung**. |
| TP-08 | Jedes offene Problem hat einen **Behebungsplan** (Maßnahme, Termin, Verantwortlicher); im neuen Testvorgehen als Fehlerbehebungsplan nach A_27475 mit ID, Kurz- und Detailbeschreibung, betroffenen Produkten, Schweregrad, Termin und Status. |
| TP-09 | Nicht ausgeführte und blockierte Testfälle sind einzeln begründet; betroffene Afos sind genannt. |

## Nachvollziehbarkeit und Konsistenz

| ID | Prüfkriterium |
|---|---|
| TP-10 | Menge der Testfall-IDs im Protokoll = Menge in der Testspezifikation. Zusätzliche oder fehlende IDs sind Befunde. |
| TP-11 | Ergebnisse im Protokoll = Status in der Afo_Testmatrix (ausgeführt / nicht ausgeführt, bestanden / fehlgeschlagen). |
| TP-12 | Alle Testläufe beziehen sich auf **dieselbe Produktversion**, die zur Zulassung eingereicht wird. Läufe gegen frühere Builds sind als solche gekennzeichnet; nach Fehlerkorrektur gibt es einen Nachtest gegen die Einreichversion und eine Aussage zur Regression. |
| TP-13 | Belege sind vorhanden oder referenziert und auffindbar: Logs, Screenshots, Mitschnitte, Reports der automatisierten Läufe, Ergebnisdateien der gematik-Testsuite. |
| TP-14 | Bei automatisierten Tests: Werkzeug, Version der Testskripte und Lauf-ID sind angegeben; der Report ist unverändert aus dem Werkzeug. |
| TP-15 | Wiederholte Testfälle zeigen alle Durchläufe, nicht nur den erfolgreichen. |
| TP-16 | Keine Echtdaten und keine produktiven Schlüssel in Logs und Anhängen (TIP1-A_4191, GS-A_2162); keine personenbezogenen Daten in Screenshots. |
| TP-17 | Fehlgeschlagene Testfälle sind mit dem zugehörigen Problemeintrag verknüpft und umgekehrt. |
| TP-18 | Produktspezifische Protokollpflichten erfüllt, wo im Steckbrief gelistet (z. B. A_29795: in-toto-Testreport je Testlauf in ePA-nahen Verfahren; KIM: Ergebnis der PKI-Testsuite). |
| TP-19 | Plausibilität: Durchlaufzeiten, Zeitstempel und Reihenfolge passen zur Testablaufspezifikation; ein Protokoll mit 100 % „bestanden" ohne jeden Problemeintrag ist zu hinterfragen und mit der Stichprobe der Belege abzusichern. |

## Hinweis

Die gematik bricht den Zulassungstest u. a. ab, wenn ihre Ergebnisse von den dokumentierten EvT-Ergebnissen
abweichen (gemKPT_Test 4.3.3). Das Protokoll muss deshalb den tatsächlichen Stand zeigen, einschließlich
bekannter Fehler. Ein ehrlich dokumentiertes offenes Problem mit Schweregrad „Mittel" oder „Leicht" und
Behebungsplan ist akzeptabel; ein verschwiegenes ist ein Abbruchgrund.
