---
name: gematik-review-produktdokumentation
description: Prüft die Produktdokumentation eines gematik-Produkts (Architekturmodell, Produktzerlegung, Produkthandbücher, Benutzer- und Administrationsdokumentation) gegen gemKPT_Test Tab_Test_016, GS-A_5033 und produktspezifische Dokumentations-Afos. Verwenden bei "Produktdokumentation reviewen", "Produktdoku für die gematik prüfen", "Benutzerhandbuch/Admin-Handbuch Zulassung", "Produktzerlegung prüfen".
---

# Review Produktdokumentation

Die Produktdokumentation ist vor Beginn der Zulassungstests zu liefern, bei Erstzulassung immer, bei
Folgezulassung nur bei wesentlichen Änderungen. Eine (Vorab-)Version begleitet auf Anfrage das Produktmuster.

Abgrenzung: Die Produktdokumentation beschreibt das **Produkt** (Hersteller). Der Betrieb durch einen Anbieter
gehört ins Betriebshandbuch. Die gematik hat ein Betriebshandbuch, das sich „wie ein Produkthandbuch eines
Herstellers" las, mit Fehlerklasse 1 bewertet; die Trennung also in beide Richtungen prüfen.

Zuerst `references/gemeinsam.md` lesen.

## Vorgehen

1. Steckbrief laden und alle Afos heraussuchen, die Dokumentation, Anleitung, Handbuch, Hinweis oder Instruktion
   fordern (über alle Tabellen; meist unter „Herstellererklärung"). Das ist die produktspezifische Soll-Liste.
2. Formale Prüfung nach F-01 bis F-23.
3. Pflichtinhalte PD-01 bis PD-06, Nutzerdokumentation PD-10 ff., Konsistenz PD-20 ff.
4. Bericht nach `references/gemeinsam.md` Abschnitt 7.

## Pflichtinhalte nach Tab_Test_016

| ID | Geforderter Inhalt | Prüfkriterium |
|---|---|---|
| PD-01 | Architekturmodell | Komponenten, Schnittstellen (insbesondere die Außenschnittstellen des Produkttyps), Datenflüsse, Verteilung; aktuell für die eingereichte Version. |
| PD-02 | Architekturmodell | Zuordnung der Komponenten zu den Vorgaben des Produkttyps ist erkennbar; Abweichungen und Herstellererweiterungen sind benannt. |
| PD-03 | Produktzerlegung: Fremdproduktanteile | Jede Fremdkomponente mit Version, **Lizenzart** und **Verbreitungsgrad**. |
| PD-04 | Produktzerlegung: selbst erzeugte Produktanteile | Eigene Komponenten sind aufgeführt und von den Fremdanteilen abgegrenzt. |
| PD-05 | Produkthandbücher für dezentrale Produkte | Für Produkte, die beim Nutzer installiert oder bedient werden (Clients, Apps, Module): Installations-, Bedienungs- und Administrationshandbuch. Für rein zentrale Dienste ausdrücklich „nicht anwendbar" mit Begründung. |
| PD-06 | Identifikation | Produktname, Produktversion nach gemSpec_OM, Produkttypversion; identisch zu Antrag und Release Notes. |

## Nutzer-, Betriebs- und Administrationsdokumentation

| ID | Afo | Prüfkriterium |
|---|---|---|
| PD-10 | GS-A_5033 (SOLL) | Dokumentation für Nutzer (Betreiber, Anbieter, Anwender), die Nutzung, operativen Betrieb und Administration aus Nutzersicht beschreibt. Fehlt sie, ist eine Begründung nötig. |
| PD-11 | A_24941 (TI-M-Client, Beispiel) | Installationsanleitung und Bedienungsanleitung je unterstützter Betriebssystemversion. |
| PD-12 | A_29022, A_25312, A_24741 (TI-M, Beispiele) | Produktspezifische Pflichtinhalte: z. B. Benutzerhandbuch für Org-Admins, Instruktion zu Passwortvorgaben, Dokumentation für Whitelabel-Ausprägungen. Nur prüfen, was der Steckbrief listet. |
| PD-13 | TIP1-A_3361 | Dokumentation für den Betrieb in RU und TU, wo gefordert. |
| PD-14 | Sicherheit | Sicherheitshinweise für Installation und Betrieb: Systemvoraussetzungen, Härtung, Rechte, Updates, Umgang mit Schlüsseln und Zertifikaten, sichere Konfiguration als Vorgabe. |
| PD-15 | GS-A_3804 ff., GS-A_3813, GS-A_4864 | Fehlermeldungen und Logging sind beschrieben: Fehlercodes mit Bedeutung und Abhilfe; keine personenbezogenen oder medizinischen Daten in Fehlermeldungen; erweitertes Test-Logging ist in der PU gesperrt. |
| PD-16 | Verständlichkeit | Handbücher sind für die Zielgruppe geschrieben (medizinisches Personal, Administratoren), mit Schritten in der Reihenfolge der Ausführung und aktuellen Abbildungen der eingereichten Version. |
| PD-17 | Support | Kontaktwege, Supportzeiten und Vorgehen bei Störungen sind genannt und stimmen mit dem Betriebshandbuch des Anbieters überein. |

## Konsistenz und Nachweisfähigkeit

| ID | Prüfkriterium |
|---|---|
| PD-20 | Die Fremdanteile der Produktzerlegung stimmen mit der Zusammensetzung aus dem Konfigurationsmanagement (A_19160) und, wo gefordert, der SBOM (A_27432, BSI TR-03183-2) überein. |
| PD-21 | Architektur und Komponentenliste stimmen mit Sicherheitskonzept, Testbericht (Kurzbeschreibung des Testobjekts) und Betriebshandbuch (Systemüberblick) überein. |
| PD-22 | Für jede Afo der Tabelle „Herstellererklärung", die eine Produkteigenschaft betrifft, gibt es eine Fundstelle in der Dokumentation oder einen internen Umsetzungsnachweis. Die Erklärung erfolgt mit der Unterschrift auf dem Antrag; die gematik darf sie auditieren (A_19165). |
| PD-23 | Funktionen des Produktmusters, die nicht im EvT getestet wurden, sind dokumentiert (TIP1-A_7358). |
| PD-24 | Die Dokumentation beschreibt, was das Produkt tut, nicht was es können soll. Zitate aus der Spezifikation ohne Bezug zur Implementierung sind Befunde. |
| PD-25 | Verweise auf Repositories, Wikis oder Portale sind für die gematik aufrufbar oder die Inhalte liegen bei; Zugriffsbeschränkungen sind vermerkt. |
| PD-26 | Bei Whitelabel- oder Mehrfachausprägungen: Unterschiede je Ausprägung sind dokumentiert, und jede Ausprägung ist eindeutig identifizierbar. |
