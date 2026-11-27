---
name: gematik-review-testkonzept
description: Prüft ein Testkonzept eines Herstellers oder Anbieters für die Eigenverantwortlichen Tests (EvT) bzw. Zulassungstests eines gematik-Produkts gegen gemKPT_Test (Tab_Test_013, TIP1-A_6524-01). Verwenden bei "Testkonzept reviewen", "Testkonzept für die gematik prüfen", "EvT vorbereiten", "Testkonzept Produktzulassung".
---

# Review Testkonzept

Das Testkonzept ist Eingangskriterium für EvT und Zulassungstest. Der Testansprechpartner der gematik prüft
„die Testkonzeption sowie die Afo-Testmatrix auf Einhaltung der Vorgaben" (gemKPT_Test Tab_Test_005_01). Bei
Erstzulassung ist es immer zu liefern, bei Folgezulassung nur bei wesentlichen Änderungen im Testvorgehen.

Zuerst `references/gemeinsam.md` lesen.

## Vorgehen

1. Produkttypsteckbrief laden. Die Tabelle „Produkttest/Produktübergreifender Test" ist die Testbasis; die
   gemKPT_Test-Afos unter „Herstellererklärung funktionale Eignung" regeln das Testvorgehen.
2. Feststellen, welches Regime gilt: **neues Vorgehen** (EvT → PüT → GIT-TI; zuerst u. a. VSDM 2.0, ZETA, PoPP)
   oder **bisheriges Vorgehen** (EvT in der RU, Zulassungstest in der TU). Der Steckbrief zeigt es über die
   gelisteten Afo-Fassungen (z. B. TIP1-A_6517-02/TIP1-A_6519-01 gegenüber TIP1-A_6519).
3. Prüfen, ob die gematik-Vorlage verwendet wurde (A_20065; Bezug über den Testansprechpartner, Vorlagen aus
   dem letzten Verfahren dürfen weiterverwendet werden; Abweichungen sind mit dem Testmanager abzustimmen).
4. Formale Prüfung nach F-01 bis F-23.
5. Pflichtinhalte (TK-01 bis TK-16), dann Qualität (TK-20 ff.).
6. Bericht nach `references/gemeinsam.md` Abschnitt 7.

## Pflichtinhalte nach Tab_Test_013

| ID | Geforderter Inhalt | Worauf achten |
|---|---|---|
| TK-01 | Testbasis | Steckbrief mit PTV, Spezifikationsversionen, Liste der Anwendungsfälle (vom Zulassungsnehmer zu erstellen), Normen. Versionen exakt, nicht „latest". |
| TK-02 | Zu testende Objekte | Produkt mit Version nach gemSpec_OM, Komponenten, Ausprägungen (z. B. Client je Betriebssystem). |
| TK-03 | Zu testende Leistungsmerkmale | Aus Afos und Anwendungsfällen abgeleitet, nicht frei formuliert. |
| TK-04 | Nicht zu testende Leistungsmerkmale | Mit Begründung; Afos anderer Prüfverfahren (Herstellererklärung, Gutachten) ausdrücklich abgegrenzt. |
| TK-05 | Testvorgehensweise | Teststufen, Testarten (funktional, nicht-funktional, Interoperabilität, Regression, Sicherheit, Performance), manuelle und automatisierte Anteile, Testentwurfsverfahren. |
| TK-06 | Testabdeckungsgrad und Testumfang | Zielwert und Messung. Mindestens ein Testfall pro Anforderung und pro Anwendungsfall, vollständige Abdeckung der Interoperabilität (Tab_Test_021); Verfahrensbeschreibungen verlangen 100 % Abdeckung gemäß Steckbrief. |
| TK-07 | Übersicht aller Testspezifikationen | Vollständige Liste mit Version. |
| TK-08 | Eingangs- und Testausgangskriterien | Für den EvT vom Hersteller zu definieren (gemKPT_Test 4.3), messbar. Die gematik-Kriterien für die Folgestufe sind als Mindestanforderung übernommen. |
| TK-09 | Testabbruch- und Wiederaufnahmekriterien | Konkrete Auslöser und Bedingungen. |
| TK-10 | Aufgaben | Was ist wann zu tun, einschließlich Lieferung der Testdokumentation. |
| TK-11 | Testumgebung | RU (ggf. RU DEV), TU; eigene Infrastruktur; Simulatoren und Referenzobjekte; Testkarten, Testidentitäten, Zertifikate. |
| TK-12 | Verantwortlichkeiten | Namen oder Rollen, Testmanager, Ansprechpartner für die gematik, Unterauftragnehmer. |
| TK-13 | Ressourcen | Personal, Werkzeuge, Testmanagementsystem. |
| TK-14 | Zeitplan | Mit Meilensteinen und Lieferzeitpunkten der Dokumente. |
| TK-15 | Testrisiken und Notfallpläne | Risiken bewertet, Gegenmaßnahmen benannt. |
| TK-16 | Verweis auf die ausgefüllte, separat bereitzustellende Afo_Testmatrix | Dateiname und Version (A_25392-01). |

## Qualität und Sonderthemen

| ID | Afo / Quelle | Prüfkriterium |
|---|---|---|
| TK-20 | Tab_Test_013 | Das Konzept stellt dar, **wie die Testfälle den Nachweis über Anforderungen und Anwendungsfälle führen** und welche Anforderungen mit welchen Testfällen im Testbericht nachgewiesen werden. |
| TK-21 | Tab_Test_013 | Struktur nach „Master Test Plan" bzw. „Level Test Plan" (ISO/IEC/IEEE 29119), Begriffe nach ISTQB; je Testphase ein Testkonzept pro Produkttyp; Beiträge von Unterauftragnehmern konsolidiert. |
| TK-22 | TIP1-A_4191, GS-A_2162 | Keine Echtdaten und kein produktives Kryptomaterial in RU und TU; Herkunft der Testdaten beschrieben. |
| TK-23 | TIP1-A_6772, TIP1-A_6529, TIP1-A_7334 | Interoperabilitätstests gegen Referenzobjekte im Mindestumfang (Tab_Test_033), mit Risikoabschätzung. |
| TK-24 | TIP1-A_6526 (Fassung laut Steckbrief), TIP1-A_5052, TIP1-A_7333 | Bereitstellung der Testobjekte je Version in RU/TU, dauerhafte Verfügbarkeit in der RU, Parallelbetrieb mehrerer Versionen. |
| TK-25 | TIP1-A_2773 | Einsatz von Simulatoren begründet; was dadurch nicht abgedeckt ist, steht in den Risiken. |
| TK-26 | Tab_Test_022 | Bei geändertem Produkt: Regressionstest auf Basis der Auswirkungsanalyse aus den Release Notes. |
| TK-27 | A_26241 | Performancetests gegen gemSpec_Perf geplant; separater Performance-Testbericht vorgesehen. |
| TK-28 | A_19147 | Abgrenzung oder Verweis auf den Sicherheitstestplan. |
| TK-29 | Fehlermanagement | Fehlerschweregrade nach gemKPT_Test 4.2.4.1 („Sehr schwer", „Schwer", „Mittel", „Leicht") verwendet; Erfolgreich-/Fehlgeschlagen-Kriterium je Testfall vorgesehen; im neuen Vorgehen Fehlerbehebungsplan (A_27475). |
| TK-30 | produktspezifisch | Produktspezifische Testvorgaben aus gemKPT_Test berücksichtigt, z. B. TI-M (Testtreiberschnittstelle A_24933, Referenz- und Testinstanzen, Tests mit der Referenzimplementierung), KIM (A_18892, A_25831; PKI-Testsuite), im neuen Vorgehen BDD-Szenarien (A_26675). |
| TK-31 | Altstand | Nur wenn der Steckbrief auf eine ältere gemKPT_Test-Fassung verweist: separate, sortierbare Liste umzusetzender SOLL-/SOLL-NICHT-Anforderungen mit Begründung bei Nichtumsetzung und Liste geplanter KANN-Anforderungen (so in gemKPT_Test 2.9.0 gefordert). |
| TK-32 | Konsistenz | Versionen, Umgebungen und Abdeckungsziele stimmen mit Testspezifikation, Afo_Testmatrix und Produktdokumentation überein. |

## Hinweise aus der Praxis

- Die gematik prüft die EvT-Dokumentation stichprobenartig; Abweichungen zwischen dokumentierten EvT-Ergebnissen und Zulassungstest sind ein Abbruchgrund für den Zulassungstest (gemKPT_Test 4.3.3). Ein Konzept, das Abdeckung nur behauptet, fällt dort auf.
- Wo Testfälle aus mehreren Quellen stammen (manuelle Tests im Testmanagementsystem, automatisierte Unit-/Integrationstests, Testsuite der gematik), muss das Konzept sagen, welche Quelle welche Afos abdeckt und wie daraus ein gemeinsames Protokoll entsteht.
- Für von der gematik-Testsuite abgedeckte Anwendungsfälle genügen bei TI-M die Testergebnisse; alles darüber hinaus muss Anforderungen zugeordnet und dokumentiert sein.
