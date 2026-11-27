---
name: gematik-review-release-notes
description: Prüft Release Notes eines gematik-Produkts für Erst- oder Folgezulassung gegen gemKPT_Test Tab_Test_015, die Versionsregeln aus gemSpec_OM und die Anforderungen an Änderungsanzeigen. Verwenden bei "Release Notes reviewen", "Release Notes für die gematik prüfen", "Änderungsanzeige Zulassung", "Versionsnummer gemSpec_OM prüfen".
---

# Review Release Notes

Release Notes „dokumentieren beim Release eines Produkts die Änderungen des Produkts gegenüber dem vorherigen
Release". Sie sind vor Beginn der Zulassungstests zu liefern (Eingangskriterium) und bei jeder Einreichung eines
aktualisierten Produkts im laufenden Verfahren, **bei Erst- und Folgezulassungen immer**. Sie sind außerdem die
Testbasis für die Regression (Tab_Test_022) und die Grundlage der Entscheidung, ob eine Folgezulassung nötig ist.

Zuerst `references/gemeinsam.md` lesen.

## Vorgehen

1. Vorversion der Release Notes, aktuelle Afo_Testmatrix, Testbericht und, wenn zugänglich, die Liste der
   Änderungen aus der Versionsverwaltung bzw. dem Ticketsystem danebenlegen.
2. Formale Prüfung nach F-01 bis F-23.
3. Pflichtinhalte RN-01 bis RN-05, Versionierung RN-10 ff., Konsistenz RN-20 ff.
4. Bericht nach `references/gemeinsam.md` Abschnitt 7.

## Pflichtinhalte nach Tab_Test_015

| ID | Geforderter Inhalt | Worauf achten |
|---|---|---|
| RN-01 | Verweis auf die ausgefüllte und separat bereitzustellende Afo_Testmatrix | Dateiname und Version; die Matrix gehört zu genau dieser Produktversion. |
| RN-02 | Über die Anforderungen der Spezifikation hinausgehende Änderungen | Zusatzfunktionen, Herstellererweiterungen, Änderungen an Bibliotheken und Laufzeitumgebung; „keine" ausdrücklich schreiben. |
| RN-03 | Behobene Fehler | Je Fehler ID, Kurzbeschreibung, betroffene Afo/Funktion; Fehler aus dem vorigen Testbericht bzw. Fehlerbehebungsplan sind hier wiederzufinden. |
| RN-04 | Offene und bekannte Fehler und deren Beeinträchtigung | Je Fehler Schweregrad nach gemKPT_Test, Auswirkung auf Nutzer und auf andere TI-Produkte, Workaround, geplanter Behebungstermin. |
| RN-05 | Beschreibung und Auswirkungen der Änderungen (**Auswirkungsanalyse**) sowie **Risikoanalyse** | Je Änderung: betroffene Komponenten, Schnittstellen, Afos; Auswirkung auf Außenverhalten, Interoperabilität, Sicherheit, Datenschutz, Betrieb; Risiko und Gegenmaßnahme; abgeleiteter Regressionstestumfang. |

Bei einer Erstzulassung gibt es kein Vorrelease: RN-03 entfällt begründet, RN-02, RN-04 und RN-05 beziehen sich
auf den Stand gegenüber der Spezifikation.

## Versionierung nach gemSpec_OM

| ID | Afo | Prüfkriterium |
|---|---|---|
| RN-10 | GS-A_3695 | Produktversion hat den Aufbau Haupt.Neben.Revision mit Trenner und optionalem Suffix. |
| RN-11 | GS-A_5038 | Jede Produktänderung führt zu einer höheren Produktversion; niedrigere Stellen sind auf 0 gesetzt; keine führenden Nullen. |
| RN-12 | GS-A_5040-01 | Die Höhe des Versionssprungs passt zur Änderung: signifikant → Hauptversion, moderat → Nebenversion, Außenverhalten betroffen → Revision, sonst Patchlevel. |
| RN-13 | GS-A_5039-01, GS-A_4542 | Die Produktversion basiert auf einer definierten Produkttypversion; ändert sich deren Haupt-/Nebenversion, ändert sich die Hauptversion des Produkts. Die PTV ist genannt. |
| RN-14 | GS-A_3696, GS-A_3697 | Neue Versionsnummer spätestens bei Freigabe zur Nutzung; Anlass der Erhöhung ist genannt. |
| RN-15 | Verfahren | Die Version ist identisch in Antrag, Testbericht, Testprotokoll, Sicherheitsgutachten und im Produkt selbst (Selbstauskunft, About-Dialog, Build-Metadaten). |

## Konsistenz und Folgewirkung

| ID | Quelle | Prüfkriterium |
|---|---|---|
| RN-20 | gemZul_übergrVerf 3.6 | Die Release Notes tragen die **Änderungsanzeige**: detaillierte Beschreibung der Änderungen und Auswirkungsanalyse. Aus RN-05 geht hervor, ob die Umsetzung von Anforderungen betroffen ist (Folgezulassung) oder nur ein Patchlevel (kein Zulassungstest durch das Testlabor). Auch geringfügige Änderungen sind anzuzeigen. |
| RN-21 | Vollständigkeit | Jede Änderung zwischen Vorversion und dieser Version ist aufgeführt; Stichprobe gegen Commits, Tickets oder Changelog. Nicht erwähnte Änderungen sind FK-2-Befunde, weil die Regressionstestbasis unvollständig ist. |
| RN-22 | Konsistenz | Offene Fehler = nicht behobene Probleme im Testbericht und Fehlerbehebungsplan. |
| RN-23 | A_19160, A_17179 | Geänderte Drittkomponenten sind mit alter und neuer Version genannt; SBOM aktualisiert, wo gefordert (A_27432 ff.). |
| RN-24 | A_19150 | Sicherheitsrelevante Änderungen und behobene Schwachstellen (CVE/CVSS) sind gekennzeichnet; Sicherheitstestbericht zur neuen Version ist referenziert. |
| RN-25 | gemRL_PruefSichEig_DS | Aussage, ob die Änderungen sicherheits- oder datenschutzrelevant sind und ein Delta- oder neues Gutachten auslösen. Der Gutachter muss die letzte Version geprüft haben. |
| RN-26 | Betrieb | Auswirkungen auf Betrieb und Anwender: Migrationsschritte, Konfigurationsänderungen, Abwärtskompatibilität, Parallelbetrieb mehrerer Versionen (TIP1-A_7333); Bezug zum Change im TI-ITSM, wenn die Version in die PU geht. |
| RN-27 | Qualität | Einträge sind für den Prüfer verständlich. „Diverse Bugfixes" oder reine Ticketnummern ohne Beschreibung sind Befunde. |
