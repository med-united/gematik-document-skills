---
name: gematik-review-testbericht
description: Prüft einen Testbericht (EvT-Testbericht, Performance-Testbericht) eines Herstellers oder Anbieters für ein gematik-Produkt gegen gemKPT_Test Tab_Test_018 und die Ablehnungsgründe der gematik. Verwenden bei "Testbericht reviewen", "EvT-Testbericht prüfen", "Testbericht für die Zulassung", "Performance-Testbericht gemSpec_Perf".
---

# Review Testbericht

Der Testbericht fasst je Produktversion die Testdurchführung zusammen und enthält einen zusammenfassenden
Problemreport sowie „eine abschließende Risikobetrachtung und Einschätzung der testdurchführenden Instanz".
Der EvT-Testbericht geht **unterschrieben** an das Testmanagement der gematik und ist Voraussetzung für den
Zulassungstest. Struktur nach „Level Test Report" bzw. „Master Test Report"; die gematik stellt eine Vorlage.

Zuerst `references/gemeinsam.md` lesen.

## Ablehnungsgründe der gematik (zuerst prüfen)

Die gematik lehnt einen Testbericht ab, wenn

1. die Anforderungen unzureichend abgedeckt sind,
2. nicht behobene Fehler zu schwerwiegend sind,
3. Testaufbau und Testmittel offensichtlich ungeeignet sind.

Trifft einer dieser Punkte zu, ist das ein FK-1-Befund unabhängig vom Rest.

## Vorgehen

1. Testkonzept, Testprotokoll, Afo_Testmatrix und Release Notes derselben Produktversion danebenlegen.
2. Ablehnungsgründe prüfen.
3. Formale Prüfung nach F-01 bis F-23, zusätzlich TB-01.
4. Pflichtinhalte TB-02 bis TB-12, Konsistenz TB-20 ff.
5. Bericht nach `references/gemeinsam.md` Abschnitt 7.

## Pflichtinhalte nach Tab_Test_018

| ID | Abschnitt | Prüfkriterium |
|---|---|---|
| TB-01 | Formal | Abgestimmte gematik-Vorlage verwendet (A_20065); Bericht ist unterschrieben; Aussteller ist die testdurchführende Instanz. |
| TB-02 | Testobjekt | Tabellarisch: Produkttyp, Herstellerversion, Version der gematik-Spezifikation (PTV und Spezifikationsstände). |
| TB-03 | Testobjekt | Kurzbeschreibung, z. B. Komponentendiagramm; passt zur Produktdokumentation. |
| TB-04 | Testaufbau | Testinfrastruktur, Testtreiber, Platzhalter, Simulatoren sind beschrieben; die Eignung für die geprüften Afos ist erkennbar. |
| TB-05 | Testumfang | Tabellarisch; **Verweis auf die Afo_Testmatrix** mit Dateiname und Version. |
| TB-06 | Testumfang | Die zu einer Anforderung gehörenden Testfälle sind mit Titel aufgeführt. |
| TB-07 | Testumfang | Anforderungen sind logischen Prüfgruppen zugeordnet, je Gruppe mit Prüfziel. |
| TB-08 | Probleme | Nicht behobene Probleme tabellarisch: ob und wann sie behoben werden und welche Einschränkungen sie verursachen. |
| TB-09 | Probleme | Zulässigkeit: Nicht behobene Probleme sind nur akzeptabel, wenn sie nicht „Sehr schwer" oder „Schwer" sind und keine Verzögerung oder Mehraufwand in folgenden Teststufen verursachen. |
| TB-10 | Risiken | Nicht erfüllte Eingangs- und Ausgangskriterien sind genannt und bewertet. |
| TB-11 | Bewertung | Abschließende Risikobetrachtung und Einschätzung der testdurchführenden Instanz: klare Aussage zur Testbereitschaft für die nächste Stufe. |
| TB-12 | Abdeckung | Erreichter Abdeckungsgrad gegenüber dem Ziel des Testkonzepts; 100 % der Produkttest-Afos des Steckbriefs oder begründete, mit der gematik abgestimmte Ausnahmen. |

## Konsistenz und Sonderberichte

| ID | Afo / Quelle | Prüfkriterium |
|---|---|---|
| TB-20 | Konsistenz | Zahlen (Testfälle gesamt, bestanden, fehlgeschlagen, nicht ausgeführt, offene Probleme je Schweregrad) stimmen mit Testprotokoll und Afo_Testmatrix überein. |
| TB-21 | Versionsidentität | Produktversion im Bericht = Version im Antrag, in den Release Notes und im Testprotokoll. Allen Prüfinstanzen muss dieselbe Version vorliegen. |
| TB-22 | Konsistenz | Offene Probleme im Bericht = offene und bekannte Fehler in den Release Notes. |
| TB-23 | Eingangskriterien Folgestufe | Die Eingangskriterien der nächsten Stufe sind adressiert: EvT abgeschlossen, keine blockierenden bzw. zulassungstestverhindernden Probleme, Behebungsplan, Testdokumentation geliefert, Testobjekt komplett, Testdaten/-karten/Konfiguration bereit. |
| TB-24 | A_26241 | **Performance-Testbericht** zu den gemSpec_Perf-Vorgaben liegt separat vor: Lastprofil, Messpunkte, Umgebung, Ergebnisse gegen die geforderten Werte, Abweichungen. |
| TB-25 | A_19150 | Sicherheitstestbericht zur Produktversion liegt vor oder ist referenziert (Umsetzung des Sicherheitstestplans). |
| TB-26 | produktspezifisch | Produktspezifische Berichtsteile vorhanden, wo gefordert: KIM (PKI-Testsuite als Teil des EvT-Testberichts; Clientmodul ohne Fachdienst gegen alle zugelassenen Fachdienste getestet), TI-M (Ergebnisse der Tests mit der Referenzimplementierung bzw. Testsuite). |
| TB-27 | TIP1-A_7358 | Nicht im EvT getestete Funktionen des Produktmusters sind dokumentiert. |
| TB-28 | A_27475, A_20061 | Im neuen Testvorgehen: Fehlerbehebungsplan ist mit EvT-Abschluss erstellt und wird mindestens wöchentlich aktualisiert; Art und Umfang geplanter Fehlerkorrekturen können auf Anfrage beschrieben werden. |
| TB-29 | Qualität | Der Bericht wertet aus. Er wiederholt nicht das Protokoll, sondern sagt, was die Ergebnisse für die Zulassungsreife bedeuten. |
| TB-30 | Qualität | Einschränkungen des Testaufbaus (Simulatoren, fehlende Gegenstellen, nicht testbare Afos) sind offen benannt und in der Risikobetrachtung bewertet. |

## Hinweis

Bei Änderungen, die nur einen neuen Patchlevel erfordern, findet kein Zulassungstest durch das Testlabor statt
(gemZul_übergrVerf 3.6.1). Der Testbericht des Herstellers ist dann der einzige Testnachweis und muss die
Regression auf Basis der Auswirkungsanalyse besonders sorgfältig belegen.
