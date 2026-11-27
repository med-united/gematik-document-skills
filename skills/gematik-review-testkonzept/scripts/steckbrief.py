#!/usr/bin/env python3
"""Hilfswerkzeug für gematik-Steckbriefe (xlsx-Export von gemspec.gematik.de).

  steckbrief.py verfahren  <steckbrief.xlsx>
      Prüfverfahren des Steckbriefs mit Anzahl der Anforderungen.

  steckbrief.py liste      <steckbrief.xlsx> [--verfahren TEXT] [--quelle TEXT] [--mit-text]
      Anforderungen, gefiltert nach Teilstring des Prüfverfahrens (z. B. "Produkttest",
      "Betriebshandbuch", "Sicherheitsgutachten") und/oder des Quelldokuments (z. B. "gemKPT_Test").

  steckbrief.py abgleich   <steckbrief.xlsx> <dokument> [--verfahren TEXT]
      Vergleicht die Anforderungen des Prüfverfahrens mit den Afo-IDs, die in einem Dokument
      vorkommen (xlsx, csv, txt, md; für docx/pdf vorher Text extrahieren). Meldet fehlende IDs,
      unbekannte IDs und IDs, bei denen nur das Versionssuffix abweicht.

Quelle (Muster): https://gemspec.gematik.de/downloads/gemProdT/<Name>/<Name>_PTV_<x.y.z-n>_V<a.b.c>.xlsx
"""
import argparse
import re
import sys

import openpyxl

AFO = re.compile(r'\b[A-Za-z][A-Za-z0-9-]*_\d{3,}(?:-\d+)?\b')
SHEET = 'Festlegungen'


def festlegungen(path):
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    if SHEET not in wb.sheetnames:
        sys.exit(f'Blatt "{SHEET}" fehlt in {path}; vorhanden: {wb.sheetnames}')
    rows = wb[SHEET].iter_rows(values_only=True)
    head = [str(c or '').strip() for c in next(rows)]

    def col(prefix):
        for i, h in enumerate(head):
            if h.lower().startswith(prefix.lower()):
                return i
        sys.exit(f'Spalte "{prefix}…" fehlt; vorhanden: {head}')

    c_id, c_titel, c_text = col('ID'), col('Titel'), col('Beschreibung')
    c_verb, c_quelle, c_verf = col('Verbindlichkeit'), col('Quelle'), col('Pruefverfahren')
    for r in rows:
        if not r or not r[c_id]:
            continue
        yield {
            'id': str(r[c_id]).strip(),
            'titel': str(r[c_titel] or '').strip(),
            'text': ' '.join(str(r[c_text] or '').split()),
            'verbindlichkeit': str(r[c_verb] or '').strip(),
            'quelle': str(r[c_quelle] or '').strip(),
            'verfahren': ' '.join(str(r[c_verf] or '').split()),
        }


def gefiltert(path, verfahren=None, quelle=None):
    for f in festlegungen(path):
        if verfahren and verfahren.lower() not in f['verfahren'].lower():
            continue
        if quelle and quelle.lower() not in f['quelle'].lower():
            continue
        yield f


def ids_im_dokument(path):
    if path.lower().endswith(('.xlsx', '.xlsm')):
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        text = '\n'.join(str(c) for ws in wb for row in ws.iter_rows(values_only=True) for c in row if c is not None)
    else:
        text = open(path, encoding='utf-8', errors='replace').read()
    return set(AFO.findall(text))


def basis(afo):
    return re.sub(r'-\d+$', '', afo)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('verfahren'); s.add_argument('steckbrief')
    s = sub.add_parser('liste'); s.add_argument('steckbrief')
    s.add_argument('--verfahren'); s.add_argument('--quelle'); s.add_argument('--mit-text', action='store_true')
    s = sub.add_parser('abgleich'); s.add_argument('steckbrief'); s.add_argument('dokument'); s.add_argument('--verfahren')
    a = p.parse_args()

    if a.cmd == 'verfahren':
        zaehler = {}
        for f in festlegungen(a.steckbrief):
            zaehler[f['verfahren']] = zaehler.get(f['verfahren'], 0) + 1
        for v, n in sorted(zaehler.items()):
            print(f'{n:4d}  {v}')
    elif a.cmd == 'liste':
        for f in gefiltert(a.steckbrief, a.verfahren, a.quelle):
            zeile = f"{f['id']}\t{f['verbindlichkeit']}\t{f['quelle']}\t{f['titel']}\t{f['verfahren']}"
            print(zeile + ('\t' + f['text'] if a.mit_text else ''))
    elif a.cmd == 'abgleich':
        soll = {f['id'] for f in gefiltert(a.steckbrief, a.verfahren)}
        alle = {f['id'] for f in festlegungen(a.steckbrief)}
        ist = ids_im_dokument(a.dokument)
        fehlen = soll - ist
        nur_suffix = {s for s in fehlen if basis(s) in {basis(i) for i in ist}}
        unbekannt = {i for i in ist - alle if basis(i) not in {basis(x) for x in alle}}
        print(f'Soll (Steckbrief, Verfahren "{a.verfahren or "alle"}"): {len(soll)}')
        print(f'Im Dokument gefunden: {len(soll & ist)}')
        print(f'Fehlen im Dokument ({len(fehlen - nur_suffix)}): {sorted(fehlen - nur_suffix)}')
        print(f'Nur Versionssuffix abweichend ({len(nur_suffix)}): '
              f'{sorted((s, sorted(i for i in ist if basis(i) == basis(s))) for s in nur_suffix)}')
        print(f'Im Dokument, aber nicht im Steckbrief ({len(unbekannt)}): {sorted(unbekannt)}')
        sys.exit(1 if fehlen else 0)


if __name__ == '__main__':
    main()
