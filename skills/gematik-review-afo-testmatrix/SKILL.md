---
name: gematik-review-afo-testmatrix
description: Prüft eine Afo-Testmatrix (Anforderungs-Testfall-Matrix, Traceability) eines gematik-Produkts gegen den Produkttypsteckbrief und gemKPT_Test (A_25392-01), einschließlich maschinellem Abgleich mit dem Steckbrief-Export. Verwenden bei "Afo-Testmatrix reviewen", "Afo_Testmatrix prüfen", "Testabdeckung gegen Steckbrief prüfen", "Traceability Anforderungen Testfälle gematik", auch für die Afo-Zuordnung eines Anbieters (Betriebshandbuch, Sicherheitsgutachten).
---

# Review Afo-Testmatrix

Hersteller und Anbieter müssen das gematik-Template „Afo_Testmatrix" als Teil der Dokumentation der ausgeführten
und nicht ausgeführten Testfälle nutzen und der gematik bereitstellen (A_25392-01). Testkonzept, Release Notes
und Testbericht müssen auf die ausgefüllte, separat bereitgestellte Matrix verweisen. Der Testansprechpartner
prüft sie zusammen mit dem Testkonzept.

Das Template ist nicht öffentlich abrufbar; es kommt vom Testansprechpartner der gematik. Seine Spaltenstruktur
ist hier deshalb nicht vorgegeben. Die Spalten der vorliegenden Datei zuerst feststellen und im Bericht nennen.

Zuerst `references/gemeinsam.md` lesen.

## Vorgehen

1. Steckbrief-Export (xlsx) in genau der PTV/ATV des Antrags laden (URL-Muster in `references/gemeinsam.md`).
2. Matrix und Steckbrief maschinell abgleichen (`scripts/steckbrief.py abgleich`, siehe unten). Ohne diesen Abgleich ist der
   Review nicht vollständig; wenn er nicht möglich ist, das im Bericht als Einschränkung nennen.
3. Stichprobe inhaltlich prüfen (AM-20 ff.).
4. Abgleich mit Testspezifikation und Testprotokoll.
5. Bericht nach `references/gemeinsam.md` Abschnitt 7, mit den Differenzlisten als Anhang.

## Vollständigkeit gegen den Steckbrief

| ID | Prüfkriterium |
|---|---|
| AM-01 | Steckbriefname und PTV/ATV sind in der Matrix angegeben und entsprechen dem Antrag. |
| AM-02 | **Jede** Afo der Tabelle „Produkttest/Produktübergreifender Test" steht in der Matrix. Fehlende Afos sind FK 1 (unzureichende Abdeckung ist Ablehnungsgrund für den Testbericht). |
| AM-03 | Afo-IDs stimmen **einschließlich Versionssuffix** mit dem Steckbrief überein (z. B. `-03` gegenüber `-04`). |
| AM-04 | Keine Afos, die im Steckbrief nicht vorkommen (Reste aus älteren Versionen oder anderen Produkttypen). |
| AM-05 | Afos, die in mehreren Steckbrieftabellen stehen (z. B. Produkttest und Herstellererklärung oder Sicherheitsgutachten), sind für den Testanteil enthalten. |
| AM-06 | Afos anderer Prüfverfahren sind entweder nicht enthalten oder klar als „kein Testnachweis, Nachweis über Herstellererklärung/Gutachten" markiert. |
| AM-07 | Alle Anwendungsfälle der vom Hersteller erstellten Anwendungsfallliste sind enthalten, wenn das Template sie vorsieht. |

## Zuordnung und Status

| ID | Prüfkriterium |
|---|---|
| AM-10 | Jede Afo hat mindestens einen Testfall (Tab_Test_021); jeder Anwendungsfall ebenso; Interoperabilität ist vollständig abgedeckt. |
| AM-11 | Jeder Testfall ist mit ID und Titel genannt und existiert unter derselben ID in der Testspezifikation. |
| AM-12 | Je Testfall ist der Status „ausgeführt" oder „nicht ausgeführt" angegeben, bei ausgeführten das Ergebnis; identisch zum Testprotokoll. |
| AM-13 | Nicht ausgeführte Testfälle und nicht abgedeckte Afos haben eine Begründung und, wo nötig, eine Abstimmung mit dem Testmanager der gematik. |
| AM-14 | Afos sind logischen Prüfgruppen mit Prüfziel zugeordnet, wie es der Testbericht verlangt (Tab_Test_018). |
| AM-15 | Keine leeren Pflichtzellen, keine Platzhalter („tbd", „siehe oben"), keine ausgeblendeten Zeilen oder Filter, die Afos verbergen. |
| AM-16 | Die Matrix trägt Produktversion und Datum und gehört zu genau der Version aus Testbericht und Release Notes. |

## Inhaltliche Stichprobe

Mindestens 10 % der Afos, mindestens 15, darunter alle MUSS-Afos mit Sicherheits-, Krypto- oder
Interoperabilitätsbezug.

| ID | Prüfkriterium |
|---|---|
| AM-20 | Der zugeordnete Testfall prüft die Afo tatsächlich: Afo-Text lesen, Testfall lesen, erwartetes Ergebnis mit dem geforderten Verhalten vergleichen. |
| AM-21 | Afos mit mehreren Teilanforderungen (Aufzählungen, „und", Tabellenverweise) sind in allen Teilen abgedeckt, ggf. durch mehrere Testfälle. |
| AM-22 | Afos, die Fehlverhalten oder Ablehnung fordern, haben einen Negativtest. |
| AM-23 | Sammel-Testfälle, denen sehr viele Afos zugeordnet sind, werden einzeln geprüft: Ist je Afo ein Schritt oder Ergebnis erkennbar? |
| AM-24 | Unit-Tests ohne Bezug zum spezifizierten Außenverhalten gelten nicht als Nachweis. |
| AM-25 | SOLL-Afos, die nicht umgesetzt sind, sind als solche mit Begründung geführt; KANN-Afos sind als umgesetzt oder nicht umgesetzt gekennzeichnet. |

## Maschineller Abgleich

```
python3 scripts/steckbrief.py verfahren <steckbrief.xlsx>
python3 scripts/steckbrief.py abgleich <steckbrief.xlsx> <afo_testmatrix.xlsx> --verfahren Produkttest
```

Die Ausgabe liefert drei Listen für AM-02 bis AM-04: fehlende Afos, Afos mit abweichendem Versionssuffix und
Afos, die der Steckbrief nicht kennt. Exit-Code 1, wenn Afos fehlen. Der Abgleich sucht die IDs in allen Zellen
der Matrix; er zeigt also, ob eine Afo genannt ist, nicht ob ihr ein Testfall zugeordnet ist. AM-10 bis AM-13
deshalb zusätzlich über die Spalten der Matrix prüfen (leere Testfall- oder Statuszellen je Afo) und die
Testfall-IDs aus Matrix, Testspezifikation und Testprotokoll als Mengen vergleichen.

## Anbieterseite

Für Anbieter gibt es keine Testmatrix im engeren Sinn, aber dieselbe Nachweislogik: Jede Afo des
Anbietertypsteckbriefs ist einem Prüfverfahren zugeordnet (Prozessprüfung, Anbietererklärung, Betriebshandbuch,
Sicherheitsgutachten). Die Prüfkriterien AM-01 bis AM-06 und AM-15 gelten sinngemäß für

- den „Nachweis zur Umsetzung der Anforderungen" im Betriebshandbuch (GS-A_5343-01, Afo → Kapitel),
- die obligatorische Afo-Tabelle zum Sicherheitsgutachten (gemRL_PruefSichEig_DS Kap. 8: Afo-ID, Afo-Titel, Prüfmethoden, Sachverhalt, Sicherheitsmangel, Umsetzungsstatus),
- die interne Nachweisliste zu den Afos der Anbietererklärung.
