# Gemeinsame Grundlagen für alle gematik-Dokumentenreviews

Diese Datei gilt für jeden Review-Skill in diesem Repository. Die Quelle liegt in `shared/gemeinsam.md`;
`scripts/sync-shared.sh` kopiert sie in jeden Skill nach `references/gemeinsam.md`. Nur die Quelle bearbeiten.

## 1. Grundregeln

1. **Der Steckbrief entscheidet, nicht diese Checkliste.** Welche Anforderung (Afo) für ein Dokument gilt und in
   welcher Fassung, steht im Produkttypsteckbrief (`gemProdT_*`) bzw. Anbietertypsteckbrief (`gemAnbT_*`) der
   Version, gegen die zugelassen wird. Die Afo-Listen in den Skills stammen aus TI-M Pro, KIM und eHealth-CardLink
   (Abruf 27.11.2026) und sind Beispiele für die Abdeckung, kein Ersatz für den Steckbrief.
2. **Keine Afo-ID und keinen Afo-Text erfinden.** Wenn eine ID nicht im geladenen Steckbrief oder im
   Quelldokument steht, als „nicht verifiziert" kennzeichnen.
3. **Versionssuffix beachten.** `TIP1-A_6526-03` und `TIP1-A_6526-04` sind verschiedene Fassungen. Geprüft wird
   gegen die Fassung, die der Steckbrief nennt.
4. **Befunde müssen auffindbar sein.** Jeder Befund nennt Kapitel, Seite oder Tabellenzeile im geprüften Dokument.
5. **Generische Aussagen sind ein Befund.** Die gematik bemängelt regelmäßig Texte, die Möglichkeiten aufzählen,
   statt zu sagen, wie der Antragsteller es konkret macht (siehe Beispiele in Abschnitt 6).
6. **Bestandene Punkte nicht aufblähen.** Im Bericht stehen Befunde vollständig, erfüllte Kriterien nur als Zähler
   oder Kurzliste.

## 2. Vorbereitung jedes Reviews

Vor dem Lesen des Dokuments klären und im Bericht festhalten:

| Frage | Woher |
|---|---|
| Rolle: Hersteller (Produktzulassung) oder Anbieter (Anbieterzulassung)? Anbieterkonstellation I/II/III? | Antrag, gemKPT_Betr Kap. 3.4.2 |
| Produkt-/Anbietertyp und Steckbriefversion (PTV/ATV) | Antrag bzw. Verfahrensschlüssel (VFS_…) |
| Erst- oder Folgezulassung, „neues" oder „bisheriges" Testvorgehen | gemKPT_Test, Steckbrief |
| Version und Stand des zu prüfenden Dokuments | Deckblatt |

Steckbrief maschinenlesbar laden (Muster, Version anpassen):

```
https://gemspec.gematik.de/downloads/gemProdT/<Name>/<Name>_PTV_<x.y.z-n>_V<a.b.c>.xlsx
https://gemspec.gematik.de/downloads/gemAnbT/<Name>/<Name>_ATV_<x.y.z-n>_V<a.b.c>.xlsx
```

Aktuelle HTML-Fassungen: `https://gemspec.gematik.de/docs/<gemProdT|gemAnbT|gemSpec|gemKPT|gemRL>/<Name>/latest/`.
Zulassungsfähige Versionen: `https://gemspec.gematik.de/docs/zulassungsobjekte/`.

Aus dem Steckbrief die Afos herausziehen, die dem Prüfverfahren des Dokuments zugeordnet sind (Abschnitt 3),
und daraus die Soll-Liste für die inhaltliche Prüfung bilden. Dieselbe Afo kann in mehreren Tabellen stehen.
Der Export enthält im Blatt „Festlegungen" je Afo ID, Titel, Beschreibung, Verbindlichkeit, Quelle und
Prüfverfahren. Dafür liegt jedem Skill `scripts/steckbrief.py` bei:

```
python3 scripts/steckbrief.py verfahren <steckbrief.xlsx>                       # Prüfverfahren mit Anzahl
python3 scripts/steckbrief.py liste <steckbrief.xlsx> --verfahren Betriebshandbuch --mit-text
python3 scripts/steckbrief.py liste <steckbrief.xlsx> --quelle gemKPT_Test
python3 scripts/steckbrief.py abgleich <steckbrief.xlsx> <dokument> --verfahren Produkttest
```

`abgleich` meldet Afos, die im Dokument fehlen, nur im Versionssuffix abweichen oder im Steckbrief nicht
vorkommen (xlsx, csv, txt, md; docx und pdf vorher in Text umwandeln). Ein Treffer heißt nur, dass die ID
genannt wird, nicht, dass die Anforderung erfüllt ist.

## 3. Prüfverfahren und zugehörige Nachweise

**Produkttypsteckbrief**

| Prüfverfahren (Wortlaut im Steckbrief) | Nachweis |
|---|---|
| Funktionale Eignung: Produkttest/Produktübergreifender Test | EvT-Testdokumentation des Herstellers, danach Zulassungstest der gematik |
| Funktionale Eignung: Herstellererklärung | Erklärung durch Unterschrift auf dem Zulassungsantrag |
| Sicherheitstechnische Eignung: Sicherheitsgutachten | Gutachten nach gemRL_PruefSichEig_DS |
| Sicherheitstechnische Eignung: Produktgutachten | Produktgutachten (Quellcode-Analyse, Pentest) |
| Sicherheitstechnische Eignung: Herstellererklärung | Erklärung durch Unterschrift auf dem Antrag |

**Anbietertypsteckbrief**

| Prüfverfahren | Nachweis | Prüfende Stelle |
|---|---|---|
| Prozessprüfung betriebliche Eignung | Prozessprüfung (Incident, Problem, Change), Prüfbericht | gematik Operations |
| Anbietererklärung betriebliche Eignung | Erklärung durch Unterschrift auf dem Antrag | Zulassungsstelle |
| Betriebshandbuch betriebliche Eignung | Betriebshandbuch, Prüfprotokoll | gematik Operations |
| Sicherheitsgutachten | Gutachten nach gemRL_PruefSichEig_DS | Datenschutz & Informationssicherheit |
| Prozessprüfung / Dokumentenprüfung sicherheitstechnische Eignung | u. a. A_27098-01 (TI Security Standard) | Sicherheit |

Erklärungen sind kein Freibrief: Die gematik hat Auditrechte (A_19165, A_27099). Für jede Afo unter
„Herstellererklärung"/„Anbietererklärung" sollte intern ein Umsetzungsnachweis vorliegen.

## 4. Formale Prüfkriterien (für jedes Dokument)

Übernommen aus dem Prüfprotokoll-Template der gematik (Stand 01.02.2021, eingesetzt 2024/25 in der
Anbieterzulassung eHealth-CardLink) und den dortigen Hinweisen zum Prüfziel „Formale Korrektheit".

| ID | Prüfziel | Prüfkriterium |
|---|---|---|
| F-01 | Formale Anforderungen | Der Prüfgegenstand liegt mit allen notwendigen Anhängen und Anlagen vor. |
| F-02 | Formale Anforderungen | Zweck und Zielgruppe des Dokuments sind eindeutig. |
| F-03 | Formale Anforderungen | Die Abgrenzung zu anderen Dokumenten ist eindeutig (was ist Gegenstand, was nicht). |
| F-04 | Formale Anforderungen | Interne Referenzen und Querverweise sind richtig, eindeutig und vollständig. |
| F-05 | Formale Anforderungen | Externe Referenzen sind korrekt und für die gematik aufrufbar; übernommene Texte und Grafiken haben eine Quellenangabe. |
| F-06 | Transparenz | Alle Inhalte sind eindeutig beschrieben und nicht interpretierbar. |
| F-07 | Transparenz | Konsistenz zu Festlegungen in anderen eingereichten Dokumenten ist gegeben. |
| F-08 | Formale Anforderungen | Das Dokument ist in sich widerspruchsfrei. |
| F-09 | Vorgaben, Normen, Gesetze | Kein Widerspruch zu Vorgaben, Standards, Normen oder Gesetzen. |
| F-10 | Vorgaben, Normen, Gesetze | Fachbegriffe sind widerspruchsfrei zum Glossar der gematik (gemGlossar). |
| F-11 | Formale Anforderungen | Metadaten sind korrekt gefüllt: Bezeichnung, Version, Stand, Status, Klassifizierung. |
| F-12 | Formale Anforderungen | Dokumentenhistorie mit Version, Stand, Status und Änderungen zur Vorversion ist vorhanden und gepflegt. |
| F-13 | Formale Anforderungen | Inhalts-, Tabellen- und Abbildungsverzeichnis sind vorhanden, aktuell und vollständig; Tabellen und Abbildungen sind beschriftet. |
| F-14 | Formale Anforderungen | Keine schwerwiegenden redaktionellen Mängel (Rechtschreibung, Grammatik, Formatierung, Übersetzungsfehler). |
| F-15 | Formale Anforderungen | Abkürzungen sind im Text korrekt eingeführt und in einem Abkürzungsverzeichnis vollständig aufgeführt. |
| F-16 | Vorgaben, Normen, Gesetze | Fachbegriffe zu Standards, Normen und Gesetzen sind erläutert und im Glossar ausgewiesen. |
| F-17 | Formale Korrektheit | Die gematik-Vorlage wurde verwendet, sofern eine bereitgestellt oder gefordert ist (A_20065, A_25392-01). |
| F-18 | Formale Korrektheit | Deckblatt mit mindestens Titel, Version, Stand, Status, Autor. |
| F-19 | Formale Korrektheit | Kopf- und Fußzeile auf jeder Seite mit Seite x von y, Dokumenttitel, Version, Dateiname, Stand. |
| F-20 | Formale Korrektheit | Kapitel sind nummeriert, Schriftarten einheitlich. |
| F-21 | Formale Korrektheit | Deutsch und verständlich (GS-A_4090; A_24021 erlaubt Deutsch oder Englisch, aber konsistent). |
| F-22 | Verfahrensregeln | Version nach gemSpec_OM gekennzeichnet; Änderungen an Nachweisen eindeutig beschrieben; Dokument unterzeichnet, wo das Verfahren es verlangt (gemZul_Anbieter Kap. 2.3). |
| F-23 | Verfahrensregeln | Versionsidentität: Alle Nachweise beziehen sich auf dieselbe Version des Zulassungsobjekts und dieselbe Steckbriefversion. |

## 5. Bewertung

**Fehlerklassen** (Wortlaut der gematik, Prüfprotokoll-Template „Linie 4"):

| FK | Bezeichnung | Bedeutung |
|---|---|---|
| 1 | sehr schwerer Fehler | Dokument nicht nutzbar; Behebung zwingend; gefährdet Folgedokumente. |
| 2 | schwerer Fehler | Nutzbar nur mit wesentlichen Einschränkungen und Risiken. |
| 3 | mittlerer Fehler | Inhaltliche Auswirkungen nicht ausgeschlossen; extern nicht, intern eingeschränkt verwendbar. |
| 4 | leichter Fehler | In der Regel redaktionell; Weiterverwendung grundsätzlich möglich. |

**Fehlerklasse 1 und 2 verhindern die Abnahme.** FK 3 und 4 werden mit Frist nachgebessert.

Richtwerte aus dem realen Prüfprotokoll: „liest sich wie ein Produkthandbuch, nicht wie ein Betriebshandbuch"
war FK 1; eine nicht konkret beschriebene Skalierung FK 2; fehlendes Glossar, fehlende Verzeichnisse, fehlendes
Abkürzungsverzeichnis, unvollständige Pflichtgliederung FK 3; Übersetzungsfehler und nicht aufrufbare Links FK 4.

**Erfüllungsgrad für inhaltliche Prüfpunkte** (Skala des gematik-Dokumentenreviews):
ERFÜLLT (vollständig und nachweisbar) / TEILWEISE ERFÜLLT (Mängel bestehen) / NICHT ERFÜLLT (kaum, gar nicht
oder nicht vorhanden) / NICHT ANWENDBAR (mit Begründung und Benennung der stattdessen verantwortlichen Stelle).

SOLL-Anforderungen dürfen nicht stillschweigend übergangen werden: Jede Nichtumsetzung braucht eine Begründung
(gemRL_PruefSichEig_DS Kap. 5.4).

## 6. Wiederkehrende Befundmuster aus echten gematik-Reviews

Quellen: Prüfprotokoll Betriebshandbuch eHealth-CardLink (2 Runden, 2024/25), Zulassungs-Dokumentenreview
Notfallkonzept (11/2026), Prüfbericht Alarmierungsübung (02/2026).

- Falsche Perspektive: Produkt- statt Betriebssicht; Kapitel, bei denen nicht erkennbar ist, aus wessen Sicht sie geschrieben sind.
- Optionen statt Festlegung: „man könnte", „es gibt die Möglichkeit" statt „wir machen es so, verantwortlich ist Rolle X".
- Afos nur zitiert: „Die Aufführung einiger Anforderungen ist nicht ausreichend." Gefordert ist, wie die Anforderung umgesetzt wird.
- Methodik fehlt: Ergebnisse (z. B. BIA-Werte) ohne beschriebene Herleitung gelten als nicht objektiv nachvollziehbar.
- Kommunikation fehlt: Wer wird wann wie informiert (gematik, andere Anbieter, Kunden)?
- Rollen ohne Stellvertretung, ohne Aufgabenabgrenzung, ohne Zusammenwirken.
- Links in private Repositories oder Wikis, die der Prüfer nicht öffnen kann.
- Überschriften ohne Inhalt (z. B. „Dokumentenstand-Basis" leer).
- Formales: fehlende Seitenzahlen, Fußzeilen, Kapitelnummern, Verzeichnisse, Glossar; wechselnde Schriftarten; maschinelle Übersetzungsfehler.
- Detailgrad von Plänen und Abläufen: Eine fachkundige dritte Person muss danach handeln können.

## 7. Berichtsformat

Den Bericht im Aufbau des gematik-Prüfprotokolls liefern, damit Befunde 1:1 nachverfolgt werden können.

```
# Review <Dokumenttyp> – <Produkt/Anbieter> – <Dokumentversion, Stand>

Prüfgrundlage: <Steckbrief mit PTV/ATV>, <Quelldokumente mit Version>
Rolle/Verfahren: <Hersteller|Anbieter, Konstellation, Erst-/Folgezulassung>
Prüfdatum: <Datum>

## Ergebnis
Gesamturteil: <einreichbar | einreichbar nach Nachbesserung | nicht einreichbar>
Befunde je Fehlerklasse: FK1 n, FK2 n, FK3 n, FK4 n
Die drei wichtigsten Punkte: …

## Befunde
| ID | Prüfziel | Prüfkriterium (mit Afo/Control) | Quelle im Dokument | Befund | FK | Empfehlung |

## Abdeckung der Anforderungen
| Afo/Control | Fundstelle | Erfüllungsgrad | Bemerkung |

## Nicht geprüft / offene Annahmen
```

Gesamturteil: „nicht einreichbar" bei mindestens einem FK-1- oder FK-2-Befund. Status-Spalten für den Dialog mit
der gematik (NOK, in Klärung, OK, zurückgezogen, zur Wiedervorlage; Antragsteller: offen, in Bearbeitung,
in Klärung, umgesetzt, abgelehnt) erst ergänzen, wenn ein echtes Prüfprotokoll der gematik vorliegt.

## 8. Quellenstand (Abruf 27.11.2026)

| Dokument | Version |
|---|---|
| gemKPT_Test | 3.8.0 |
| gemSpec_DS_Anbieter | 2.2.0 |
| gemTI_SEC_Standard | 1.0.0 |
| gemSpec_DS_Hersteller | 1.7.0 |
| gemRL_PruefSichEig_DS | 3.0.1 |
| gemRL_Betr_TI | 2.23.0 |
| gemKPT_Betr | 3.69.0 |
| gemSpec_Perf | 2.88.0 |
| gemSpec_OM | 1.19.0 |
| gemZul_Anbieter | 2.22.0 |
| gemZul_übergrVerf | 2.12.0 |
| gemZul_Best_SiGu | 1.14.1 |

Vor jedem Review prüfen, ob neuere Fassungen gelten, und Abweichungen im Bericht nennen.
