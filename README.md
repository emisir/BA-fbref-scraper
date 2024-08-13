# FBref Scraper für Bachelorarbeit

Dieses Repository enthält einen Web-Scraper, der Daten von der FBref-Website extrahiert. Der Scraper wurde im Rahmen meiner Bachelorarbeit entwickelt und dient zur Sammlung und Analyse von Fußballstatistiken. Zusätzlich enthält das Repository ein Beispielskript, das zeigt, warum BeautifulSoup allein nicht ausreicht, um Daten von FBref zu scrapen.

## Inhalt

- [Überblick](#überblick)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [bs.py: BeautifulSoup Limitierungen](#bspy-beautifulsoup-limitierungen)

## Überblick

Dieser Scraper extrahiert relevante Daten von der FBref-Website und speichert sie in einem strukturierten Format zur weiteren Analyse.

## Installation
Um den Scraper lokal auf Ihrem Rechner zu installieren, gehen Sie bitte wie folgt vor:

1. Klonen Sie das Repository:

```bash
git clone https://github.com/emisir/BA-fbref-scraper.git
```

2. Navigieren Sie in das Projektverzeichnis:

```bash
cd BA-fbref-scraper
```

3. Erstellen und aktivieren Sie eine virtuelle Umgebung:

```bash
python3 -m venv env
source env/bin/activate  # Für Windows: env\Scripts\activate
```

4. Installieren Sie die benötigten Abhängigkeiten:

```bash
pip install -r requirements.txt
```

## Verwendung

Nach der Installation können Sie den Scraper wie folgt ausführen:

```bash
python scraper.py
```

Dieser Befehl startet den Scraper und beginnt mit dem Extrahieren der Daten von der FBref-Website. Die extrahierten Daten werden im `output`-Verzeichnis gespeichert.

## bs.py: BeautifulSoup Limitierungen

Die Datei `bs.py` ist ein Beispielskript, das aufzeigt, warum der Einsatz von **BeautifulSoup** allein nicht ausreicht, um Daten von FBref zu scrapen. FBref verwendet JavaScript, um Tabelleninhalte dynamisch zu laden, was dazu führt, dass diese Inhalte nicht im statischen HTML der Seite vorhanden sind.

### So führen Sie `bs.py` aus:

```bash
python bs.py
```

### Was zeigt `bs.py`?

- **Keine Datenextraktion:** Wenn Sie `bs.py` ausführen, werden Sie feststellen, dass die Tabelle, welche für die Tabellenextraktion unausweichlich ist, nicht in der Konsolenausgabe erscheint.
- **JavaScript-Rendering:** Das Skript verdeutlicht, dass BeautifulSoup nur statisches HTML verarbeiten kann und nicht in der Lage ist, JavaScript-geladene Inhalte zu scrapen. Dies ist der Hauptgrund, warum ein anderer Ansatz erforderlich ist, um die vollständigen Daten von FBref zu extrahieren.

