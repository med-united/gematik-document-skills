---
name: gematik-review-datenschutzkonzept
description: Prüft ein Datenschutzkonzept für ein gematik-Produkt (Hersteller, A_19148 gemSpec_DS_Hersteller) oder einen gematik-Anbieter (GS-A_2076-01, GS-A_5626, GS-A_5551-01) vor Sicherheitsgutachten und Zulassung. Verwenden bei "Datenschutzkonzept reviewen", "Datenschutzkonzept für die gematik prüfen", "Datenschutz im Sicherheitsgutachten vorbereiten".
---

# Review Datenschutzkonzept (Hersteller und Anbieter)

Ein eigenes Prüfverfahren „Datenschutzgutachten" gibt es in den aktuellen Steckbriefen nicht. Datenschutz wird im
Sicherheits- bzw. Produktgutachten mitgeprüft („Einhaltung der Vorschriften zum Schutz personenbezogener Daten",
gemRL_PruefSichEig_DS Kap. 3). Leser des Konzepts ist also der Gutachter.

Die gematik-Dokumente fordern DSFA, Verzeichnis von Verarbeitungstätigkeiten und Löschkonzept **nicht** als eigene
Einreichungsdokumente. Sie ergeben sich aus der DSGVO. Im Review werden sie deshalb als „DSGVO-Pflicht, nicht
gematik-Afo" geführt (Teil C), damit der Bericht beides sauber trennt.

Zuerst `references/gemeinsam.md` lesen.

## Vorgehen

1. Rolle bestimmen (Hersteller → Teil A, Anbieter → Teil B) und klären, wer Verantwortlicher und wer
   Auftragsverarbeiter ist. Die gematik ist grundsätzlich kein Verantwortlicher (gemKPT_DS_Sich_TI).
2. Steckbrief laden; Datenschutz-Afos aus den Tabellen „Sicherheitsgutachten" und „Herstellererklärung/
   Anbietererklärung sicherheitstechnische Eignung" heraussuchen, einschließlich produktspezifischer Afos zu
   Protokollierung, Löschung und Profiling.
3. Formale Prüfung nach F-01 bis F-23.
4. Inhaltliche Prüfung Teil A bzw. B, dann C und D.
5. Bericht nach `references/gemeinsam.md` Abschnitt 7.

## Teil A: Hersteller (A_19148)

| ID | Prüfkriterium |
|---|---|
| DS-A01 | Beschreibung des Produkts bezüglich Datenschutzaspekten: Zwecke, Prozesse, Akteure, Architektur, Systemgrenzen. |
| DS-A02 | Rahmenbedingungen des Datenschutzes identifiziert: DSGVO, BDSG, SGB V (insb. §§ 306 ff.), § 203 StGB, produktspezifische Vorgaben. |
| DS-A03 | Personenbezogene Daten und Anwendungsprozesse identifiziert: welche Datenarten (Gesundheitsdaten nach Art. 9 DSGVO gesondert), in welchem Prozess, durch wen, wo gespeichert, wie lange. |
| DS-A04 | Umsetzung der Grundsätze für die Verarbeitung personenbezogener Daten (Art. 5 DSGVO) je Prozess, mit Datenschutz-Risiken und Datenschutz-Hinweisen. |
| DS-A05 | Das Konzept ist dokumentiert und kann der gematik auf Verlangen vorgelegt werden; Version passt zur Produktversion. |

## Teil B: Anbieter

| ID | Afo / Control | Prüfkriterium |
|---|---|---|
| DS-B01 | GS-A_2076-01 | Datenschutzmanagement nach BSI-Baustein CON.2 ist eingerichtet und beschrieben (Verantwortliche, Prozesse, Kontrollen). |
| DS-B02 | GS-A_5626 | Als Auftragsverarbeiter ist verbindlich geregelt, wie die Pflichten aus den gematik-Vorgaben erfüllt werden; AVV mit Kunden und Unterauftragsverarbeitern liegen vor. |
| DS-B03 | GS-A_5551-01 | Verarbeitung ausschließlich in Deutschland, EU, EWR oder der Schweiz; gilt auch für Support-, Monitoring- und Backup-Dienstleister. |
| DS-B04 | TI-Sec_0320 | Dienstleisterübersicht mit Datenschutzbezug (welcher Dienstleister sieht welche Daten), vertragliche Regelung, Steuerung. |
| DS-B05 | TI-Sec_0330 | Datenschutzverstöße: Erkennung, Bewertung, Meldung an die gematik binnen 72 Stunden, Nachweise 3 Jahre; abgestimmt mit Art. 33/34 DSGVO. |
| DS-B06 | TI-Sec_0060 | Zugriff des Betriebspersonals auf personenbezogene und medizinische Daten ist ausgeschlossen oder auf das Erforderliche begrenzt, im Vier-Augen-Prinzip und überwacht. |

## Teil C: Inhalte, die der Gutachter erwartet (DSGVO, gemMeth_DSKonz als freiwillige Gliederungshilfe)

| ID | Prüfkriterium |
|---|---|
| DS-C01 | Datenschutzrechtlich Verantwortliche und Auftragsverarbeiter je Verarbeitung benannt. |
| DS-C02 | Rechtsgrundlage je Verarbeitung. |
| DS-C03 | **Datenminimierung:** Notwendigkeit jedes Datums begründet; Privacy by Default. |
| DS-C04 | **Löschen:** Löschfristen und Löschmechanismen je Datenart, einschließlich Backups und Logs. |
| DS-C05 | **Nichtverkettung:** Pseudonymisierung/Anonymisierung, Datentrennung (Mandanten), keine Profilbildung. |
| DS-C06 | **Transparenz:** Information der Betroffenen, Auskunft, Protokollierung, Dokumentationspflichten. |
| DS-C07 | **Intervenierbarkeit:** Widerspruch, Berichtigung, Löschung/Einschränkung, Datenübertragbarkeit; Prozess für Betroffenenanfragen. |
| DS-C08 | Datenschutz-Risiken sind bewertet; Aussage, ob eine DSFA erforderlich ist, mit Ergebnis oder Begründung. Die DSFA erstellt der Verantwortliche produktspezifisch; die gematik-Spezifikation ersetzt sie nicht. |
| DS-C09 | Verzeichnis von Verarbeitungstätigkeiten existiert und ist referenziert. |
| DS-C10 | Technische und organisatorische Maßnahmen sind beschrieben oder verweisen versioniert auf das Sicherheitskonzept. |
| DS-C11 | Vertraulichkeitsverpflichtungen der Mitarbeitenden und Dienstleister (inkl. § 203 StGB, wo einschlägig) sind dokumentiert. |

## Teil D: Produktspezifische Afos und Konsistenz

| ID | Prüfkriterium |
|---|---|
| DS-D01 | Produktspezifische Datenschutz-Afos des Steckbriefs sind einzeln behandelt. Beispiele: A_25317 (TI-M: Protokolldaten nur im erforderlichen Umfang, nach Fehlerbehebung unverzüglich löschen), A_25315/A_25316 (Profiling-Verbot), GS-A_3813 (keine personenbezogenen oder medizinischen Daten in Fehlermeldungen), GS-A_4864 (erweitertes Test-Logging in der PU gesperrt). |
| DS-D02 | Betriebs- und Ereignisdaten, die an die gematik geliefert werden (Rohdaten, Bestandsdaten), enthalten keinen unzulässigen Personenbezug; das Konzept sagt, was geliefert wird. |
| DS-D03 | Keine Echtdaten in RU und TU (TIP1-A_4191); Umgang mit Testdaten beschrieben. |
| DS-D04 | Datenarten, Speicherorte, Fristen und Dienstleister stimmen mit Sicherheitskonzept, Betriebshandbuch und Produktdokumentation überein. |
| DS-D05 | Jede Aussage ist konkret: Datum, Frist, System, verantwortliche Rolle. „Daten werden gemäß DSGVO gelöscht" ist ein Befund. |
