# gematik-document-skills

Review-Skills für Dokumente, die Hersteller (Produktzulassung) und Anbieter (Anbieterzulassung) bei der gematik
einreichen. Jeder Skill enthält eine Checkliste mit Bezug auf die Anforderungen (Afos) aus
<https://gemspec.gematik.de/> und, wo vorhanden, auf reale Prüfunterlagen der gematik.

| Skill | Dokument | Rolle | Maßgebliche Quelle |
|---|---|---|---|
| `gematik-review-sicherheitskonzept` | Sicherheitskonzept | Hersteller, Anbieter | gemSpec_DS_Hersteller A_19148 ff.; gemTI_SEC_Standard TI-Sec_0020; gemRL_PruefSichEig_DS |
| `gematik-review-notfallkonzept` | Notfallkonzept | Anbieter | TI-Sec_0340, BSI 200-4, gemRL_Betr_TI Kap. 12 |
| `gematik-review-datenschutzkonzept` | Datenschutzkonzept | Hersteller, Anbieter | A_19148; GS-A_2076-01, GS-A_5626, GS-A_5551-01 |
| `gematik-review-testkonzept` | Testkonzept | Hersteller | gemKPT_Test Tab_Test_013 |
| `gematik-review-testspezifikation` | Testspezifikation | Hersteller | gemKPT_Test Tab_Test_014 |
| `gematik-review-testprotokoll` | Testprotokoll | Hersteller | gemKPT_Test Tab_Test_017 |
| `gematik-review-testbericht` | Testbericht | Hersteller | gemKPT_Test Tab_Test_018 |
| `gematik-review-release-notes` | Release Notes | Hersteller | gemKPT_Test Tab_Test_015, gemSpec_OM |
| `gematik-review-produktdokumentation` | Produktdokumentation | Hersteller | gemKPT_Test Tab_Test_016, GS-A_5033 |
| `gematik-review-afo-testmatrix` | Afo-Testmatrix | Hersteller (sinngemäß Anbieter) | A_25392-01, Steckbrief |
| `gematik-review-betriebshandbuch` | Betriebshandbuch | Anbieter | gemRL_Betr_TI GS-A_5343-01, Anbietertypsteckbrief |

## Aufbau

```
shared/gemeinsam.md      Grundregeln, formale Prüfkriterien, Fehlerklassen, Berichtsformat (Quelle)
shared/steckbrief.py     Afos je Prüfverfahren aus dem Steckbrief-Export lesen, Abgleich mit einem Dokument (Quelle)
scripts/sync-shared.sh   kopiert beide Dateien in jeden Skill
skills/<skill>/SKILL.md  Checkliste des Dokumenttyps
skills/<skill>/references/gemeinsam.md, scripts/steckbrief.py   Kopien, nicht direkt bearbeiten
```

Nach Änderungen in `shared/` einmal `./scripts/sync-shared.sh` ausführen.

## Installation

Als Plugin (Manifest in `.claude-plugin/plugin.json`) oder einzelne Skills kopieren bzw. verlinken:

```
ln -s "$PWD/skills/gematik-review-betriebshandbuch" ~/.claude/skills/
```

## Verwendung

„Prüfe das Betriebshandbuch `<Datei>` für die Anbieterzulassung TI-M Pro, ATV 1.2.0-0." Der Skill lädt den
Steckbrief, prüft formal und inhaltlich und liefert einen Bericht im Aufbau des gematik-Prüfprotokolls
(Prüfziel, Prüfkriterium, Quelle im Dokument, Befund, Fehlerklasse, Empfehlung).

`steckbrief.py` braucht `openpyxl`.

## Herkunft der Checklisten

- **gematik-Spezifikationen**, Abruf 27.11.2026; Versionen in `shared/gemeinsam.md` Abschnitt 8. Afo-Beispiele
  aus den Steckbriefen TI-M Pro, KIM und eHealth-CardLink. Maßgeblich ist immer der Steckbrief des Antrags.
- **Prüfprotokoll der gematik zum Betriebshandbuch eHealth-CardLink** (zwei Runden, 2024/25; Jira CAZ-296,
  CAZ-313): 16 formale und 3 fachliche Prüfkriterien, Fehlerklassen, Befunde und Nachforderungen.
- **Zulassungs-Dokumentenreview der gematik zum Notfallkonzept** (11/2026; Jira INFRA-2558): Prüfpunkte mit
  P-IDs, Leitfragen und Checklisten nach BSI 200-4.
- **Prüfbericht Alarmierungsübung** (02/2026; Jira INFRA-1617): Befunde zur Erreichbarkeit und Ticketrückgabe.

## Bekannte Lücken

- Die gematik-Vorlagen für Testkonzept, Testspezifikation, Testprotokoll, Testbericht und das Template
  „Afo_Testmatrix" sind nicht öffentlich abrufbar (Bezug über den Testansprechpartner). Die Skills prüfen gegen
  die Inhaltsvorgaben aus gemKPT_Test, nicht gegen die Spaltenstruktur der Vorlagen.
- Für die Testdokumente, Release Notes und Produktdokumentation lag kein ausgefülltes Prüfprotokoll der gematik
  vor; das Prüfprotokoll-Template enthält dafür nur leere Blätter.
- Die Checklisten für Sicherheits- und Datenschutzkonzept stützen sich auf die Spezifikationen und die
  Gutachterrichtlinie, nicht auf ein reales Review der gematik.
- BSI CON.2, BSI 200-4 und ISO/IEC/IEEE 29119 sind nur über die Verweise der gematik eingeflossen.
