---
name: gematik-review-sicherheitskonzept
description: Prüft ein Sicherheitskonzept für ein gematik-Produkt (Hersteller, A_19148 ff. gemSpec_DS_Hersteller) oder einen gematik-Anbieter (TI-Sec_0020 des TI Security Standards, gemSpec_DS_Anbieter) vor Sicherheitsgutachten und Zulassung. Verwenden bei "Sicherheitskonzept reviewen", "Sicherheitskonzept für die gematik prüfen", "Vorbereitung Sicherheitsgutachten", "Schutzbedarf/Bedrohungsanalyse/Restrisiken prüfen".
---

# Review Sicherheitskonzept (Hersteller und Anbieter)

Das Sicherheitskonzept wird selten direkt von der Zulassungsstelle geprüft. Es ist die Hauptgrundlage des
Sicherheitsgutachters (gemRL_PruefSichEig_DS) und wird beim Anbieter zusätzlich jährlich als PDF an die gematik
geliefert (TI-Sec_0020). Der Review simuliert deshalb zwei Leser: den Gutachter, der je Afo einen Sachverhalt
belegen muss, und die gematik, die auf Vollständigkeit, Sorgfalt, Objektivität und Nachvollziehbarkeit achtet.

Zuerst `references/gemeinsam.md` lesen.

## Vorgehen

1. Rolle bestimmen. Hersteller → Teil A. Anbieter → Teil B. Wer beides ist, liefert in der Regel zwei Konzepte
   oder ein Konzept mit klar getrennten Teilen.
2. Steckbrief laden; Soll-Liste aus der Tabelle „Sicherheitsgutachten" (und beim Anbieter „Prozessprüfung
   sicherheitstechnische Eignung") bilden. Dazu gehören meist auch gemSpec_Krypt- und produktspezifische Afos.
3. Beim Anbieter das Security Governance Level bestimmen (gemTI_SEC_Standard Anhang A1) und die geltenden
   Controls auswählen.
4. Formale Prüfung nach F-01 bis F-23.
5. Inhaltliche Prüfung nach Teil A bzw. B, danach Teil C (Gutachtertauglichkeit).
6. Bericht nach `references/gemeinsam.md` Abschnitt 7.

## Teil A: Hersteller (gemSpec_DS_Hersteller)

| ID | Afo | Prüfkriterium |
|---|---|---|
| SK-A01 | A_19148 | Beschreibung des Produkts bezüglich allgemeiner Informationssicherheitsaspekte: Architektur, Komponenten, Schnittstellen, Datenflüsse, Vertrauensgrenzen, Betriebsumgebung. |
| SK-A02 | A_19148 | Sicherheitsanforderungen der gematik sind aufgeführt (Soll-Liste aus dem Steckbrief) und je Anforderung ist die Umsetzung beschrieben. |
| SK-A03 | A_19148 | Schutzbedarfsfeststellung für die verarbeiteten Informationen und die Komponenten, mit Begründung. |
| SK-A04 | A_19148, A_19154 | Bedrohungsanalyse ist durchgeführt und dokumentiert; zu jeder identifizierten Bedrohung gibt es umgesetzte Maßnahmen. |
| SK-A05 | A_19148 | Sicherheitsanalyse: Verifikation, dass die Maßnahmen wirksam sind. |
| SK-A06 | A_19148 | Restrisikoabschätzung mit Bewertung und Akzeptanz durch eine benannte Rolle. |
| SK-A07 | A_19151 | Implementierungsspezifische Sicherheitsanforderungen sind dokumentiert und umgesetzt. |
| SK-A08 | A_19147, A_19150 | Sicherheitstestplan: Sicherheitstests aller Entwicklungsphasen, regelmäßige Pentests durch Unabhängige, Detailgrad vergleichbar OWASP MSTG/MASVS, Testvorgehen zu den gematik-Vorgaben. Sicherheitstestbericht je veröffentlichter Produktversion. |
| SK-A09 | A_19152, A_19159 | Sicherer Produktlebenszyklus mit den Mindestaktivitäten, u. a. Quality Gates gegen Release mit „Mittel"/„Hoch" bewerteten Sicherheitsfehlern, Schwachstellenmanagement. |
| SK-A10 | A_19153, A_19155, A_19156 | Architektur-Review, Quellcode-Reviews/-Scans, automatisierte Sicherheitstests. |
| SK-A11 | A_19157, A_19158 | Schulungsplan und durchgeführte Schulungen. |
| SK-A12 | A_19160 | Änderungs- und Konfigurationsmanagement: Zusammensetzung des Produkts inkl. Dritt-Software jederzeit eindeutig. |
| SK-A13 | A_22984, A_22986, A_23029, A_23445 | Schwachstellen: CVSS-Bewertung in der geforderten Frist, Meldung ab CVSS 7, Behebungsfristen, CVD-Programm. |
| SK-A14 | A_17178, A_17179 | OWASP Top 10 behandelt; Nichtanwendbarkeit einzeln begründet. |
| SK-A15 | A_27429–A_27433 | Nur wo im Steckbrief gelistet (z. B. ePA, PoPP): Zulieferer-SDLC, Supply Chain, SBOM nach BSI TR-03183-2. |

## Teil B: Anbieter (gemSpec_DS_Anbieter ab V2.x, gemTI_SEC_Standard)

Seit gemSpec_DS_Anbieter V2.0.0 stehen die Detailvorgaben nicht mehr als Afos im Steckbrief, sondern als Controls
im TI Security Standard (verbindlich über A_27098-01). Die alten IDs GS-A_3737-01, GS-A_2328-01, GS-A_5563 usw.
kommen in aktuellen Steckbriefen nicht mehr vor; sie nur verwenden, wenn der Antragssteckbrief sie noch nennt.

| ID | Control / Afo | Prüfkriterium |
|---|---|---|
| SK-B01 | TI-Sec_0020 | **Systembeschreibung** ist vorhanden und produktspezifisch. |
| SK-B02 | TI-Sec_0020 | **Asseterfassung**; Aufteilung des Produkttyps in mehrere Assets, wo sinnvoll. |
| SK-B03 | TI-Sec_0020 | **Schutzbedarf** je Asset dokumentiert. |
| SK-B04 | TI-Sec_0020 | **Business Impact (BIA)** dokumentiert; konsistent zum Notfallkonzept. |
| SK-B05 | TI-Sec_0020 | **Sicherheitsanalyse:** Verifikation, dass die Maßnahmen im Hinblick auf den Schutzbedarf angemessen und ausreichend sind. |
| SK-B06 | TI-Sec_0020 | **(Rest-)Risikoabschätzung** mit Akzeptanz. |
| SK-B07 | GS-A_4980-02, GS-A_4981-01, TI-Sec_0010 | ISMS nach ISO/IEC 27001 für die Umgebungen, in denen TI-Dienste betrieben werden; Statement of Applicability; Zertifikat deckt alle Systeme und Prozesse des TI-Produkts ab (ISO 27001 auf Basis IT-Grundschutz gleichwertig; für Cloud-Dienste C5-Testat). |
| SK-B08 | GS-A_4982-01, GS-A_4983-01 | SOLL: ISO/IEC 27002 und BSI-Grundschutz; Abweichungen begründet. |
| SK-B09 | TI-Sec_0060 | Rollen- und Rechtekonzept: nicht gleichzeitig wahrnehmbare Rollen gekennzeichnet; kein missbräuchlicher Zugriff Einzelner auf medizinische Daten; Vier-Augen-Prinzip und Überwachung beschrieben. Im Konzept enthalten oder referenziert. |
| SK-B10 | TI-Sec_0090, GS-A_5551-01 | Schutzzonenkonzept mit allen betriebsrelevanten Standorten; Betriebsumgebung in EU/EWR/Schweiz. |
| SK-B11 | TI-Sec_0240 | Netzwerkkonzept: Netzwerkplan, Absicherung der Netzgrenzen und Segmentierung, administrative Zugriffe, Netzwerkmanagement, Sicherheitssysteme, Überwachung. |
| SK-B12 | TI-Sec_0230 | Kryptographie-Konzept: Verfahren mit Schlüssellängen und Modus, eingesetzte Systeme (HSM), Schlüssel-Lifecycle, Schutz privater Schlüssel; konform zu den gemSpec_Krypt-Afos des Steckbriefs. |
| SK-B13 | TI-Sec_0160 | Security-Monitoring-Konzept: überwachte Systeme, zu detektierende Ereignisse, Vorhaltefristen; vor Inbetriebnahme mit der gematik abgestimmt. |
| SK-B14 | TI-Sec_0310 | Maßnahmenumsetzung: Bewertung von Feststellungen binnen 10 Werktagen; Fristen nach CVSS (kritisch unverzüglich, schwer 1 Monat, mittel 1 Quartal). |
| SK-B15 | TI-Sec_0320 | Dienstleisterübersicht, vertragliche Regelung, Steuerungsnachweise. |
| SK-B16 | TI-Sec_0330 | Meldung von Sicherheitsvorfällen und Datenschutzverstößen binnen 72 Stunden; Nachweise 3 Jahre; RCA bei hoher Kritikalität. |
| SK-B17 | A_27099 | Audits und Sicherheitsanalysen durch die gematik sind organisatorisch möglich. |
| SK-B18 | TI-Sec_0340 | Verweis auf das Notfallkonzept (kann zusammen mit der Sicherheitskonzeption geliefert werden). |
| SK-B19 | produktspezifisch | Produkttypspezifische Sicherheits-Afos aus der Tabelle „Sicherheitsgutachten" sind einzeln behandelt. |

## Teil C: Tauglichkeit für das Sicherheitsgutachten

| ID | Prüfkriterium |
|---|---|
| SK-C01 | Zu jeder Afo der Soll-Liste gibt es eine Fundstelle, die auf **alle Teilanforderungen** eingeht. Generische Aussagen reichen dem Gutachter nicht (gemRL_PruefSichEig_DS A3). |
| SK-C02 | Die vier Prüfkriterien des Gutachters sind bedient: Aktualität (Stand der Technik), Angemessenheit (Risiko, Restrisiko, Akzeptanz, Verhältnismäßigkeit), Vollständigkeit, Umsetzung. |
| SK-C03 | „Nicht anwendbar" ist begründet und nennt die stattdessen verantwortliche Instanz. SOLL-Afos sind umgesetzt oder begründet abgelehnt. |
| SK-C04 | Prüfgegenstand ist eindeutig: Produkt- bzw. Dienstversion, Standorte, Dienstleister. Das Konzept beschreibt den Stand, der in die PU geht. |
| SK-C05 | Herleitungskette ist geschlossen: Asset → Schutzbedarf → Bedrohung → Maßnahme → Wirksamkeitsnachweis → Restrisiko. Keine Bedrohung ohne Maßnahme, keine Maßnahme ohne Bezug. |
| SK-C06 | Abbildungen (Architektur, Netz, Datenfluss) sind aktuell, beschriftet und stimmen mit Betriebshandbuch und Produktdokumentation überein. |
| SK-C07 | Verweise auf mitgeltende Dokumente (SIEM-/Monitoring-Konzept, Krypto-Konzept, Rollenkonzept, Notfallkonzept) nennen Titel und Version; die Dokumente liegen dem Gutachter vor. |
| SK-C08 | Gültigkeit: Gutachten 3 Jahre; bei wesentlichen technischen, organisatorischen oder baulichen Änderungen neu. Das Konzept hat einen Review-Zyklus (jährlich wegen TI-Sec_0020). |

## Hinweise aus der Praxis

- Die gematik hat beim Start einer Produktzulassung ausdrücklich darauf hingewiesen: Bei Fehlerkorrekturen wird die Version hochgezählt, und der Sicherheitsgutachter muss die letzte Version geprüft haben.
- Das Gutachten stützt sich in der Anbieterzulassung maßgeblich auf Sicherheitskonzept und SIEM-/Monitoring-Konzept; beide gemeinsam prüfen.
- Die Methodik gemMeth_SiKonz richtet sich nicht an Hersteller und Anbieter, kann aber freiwillig als Gliederungshilfe dienen (Bedrohungsanalyse auf Anwendungsfallebene, Datenklassen, Gefährdungskatalog).
