# anti-slop Delivery Gate: startseite.html (02.11.2026)

Grundlage: antislop.md (github.com/miqdadbadjuber/anti-slop), Modus „during“.
Richtung: `DESIGN.md` (abgeleitet, vom Owner zu bestätigen).

Design Read: persönliche Angebotsseite eines Einzelunternehmers für kleine
Betriebe und Vereine in Graz, in Papier-und-Tusche-Buchtypografie,
Dial ENERGY 2 / RHYTHM 2 / MOTION 1.

Prüfweg: lokaler HTTP-Server, System-Chromium über Playwright, Breiten
1440 / 900 / 390 / 320 px, Skript `/tmp/hp-tools/check.py`.

## Block 1: Hard Gate

| Regel | Ergebnis | Beleg |
|---|---|---|
| R-02 Gedankenstrich | PASS | kein U+2014 im HTML, kein U+2013 im sichtbaren Text |
| R-03 Mobil | PASS | 0 px Überlauf bei 390 und 320, keine Elemente außerhalb |
| R-17 Zahlen | PASS | keine Statistiken; Preise sind Angebote (Owner-Bestätigung offen) |
| R-18 Testimonials | PASS | keine |
| R-23 Assets | PASS | Stempel „BS“ vom Owner vorläufig bestätigt (02.11.), Logo-Entscheidung später; kein Foto erfunden; Favicon bewusst leer |
| R-24 Navigation | PASS | Arbeiten, Angebot, Preise, Kontakt zeigen auf vorhandene Abschnitte |
| R-25 Kontrast | PASS | 78 Textknoten gemessen, Minimum 5,06:1 |
| R-26 Bedienelemente | PASS | 5 Ankerlinks + 1 mailto, keine toten Elemente |
| R-27 Zustände | n. a. | statische Seite ohne Daten |
| R-28 FAQ | PASS | keine FAQ |
| R-32 Tastatur | PASS | Tab-Reihenfolge Name, 4 Nav-Links, E-Mail; Fokusrahmen 2 px rot |
| R-33 Patch-Skripte | PASS | alles direkt im Quelltext |
| R-34 Themes | PASS | nur hell, mit Markengrund (R-21) |
| R-35 Durchklicken | PASS | Arbeiten → #arbeiten, Angebot → #angebot, Preise → #preise, Kontakt → #kontakt (Seitenende), Name → #start; 0 Konsolenfehler |
| R-36 Behauptungen | PASS | nur überprüfbare App-Fakten |
| R-37 Richtung | PASS | DESIGN.md vorhanden, als abgeleitet gekennzeichnet |
| R-38 Platzhalter | OFFEN | Kurzbiografie vom Owner geliefert (02.11.); `hallo@nbsystems.dev` muss vor Livegang angelegt werden |
| R-39 Semantik | PASS | lang=de, title, header/nav/main/footer, ein h1, keine übersprungenen Ebenen, alt-Texte, cursor: pointer, Hover mit Unterstreichung, kein Zoomverbot |
| R-40 Performance | PASS | alle Bilder mit width/height und lazy (kein Bild im Einstieg), keine Fremdskripte, Schriften selbst gehostet; Ladezeiten nicht gemessen |

## Block 2: Purpose-Gate (Gründe)

- R-01 Farbe: kein Verlauf; Siegelrot als einziger Akzent (Hanko).
- R-04 Icons: keine.
- R-06 Schrift: Newsreader wegen Papier/Buch-Charakter; Kennzeichnungen kursiv statt gesperrter Versalien. Ausnahme: Stempelring in Versalien, weil ein Stempel so aussieht.
- R-07 Hintergrund: Papierkorn trägt die Papier-Metapher, sehr schwach.
- R-08 Pfeile: keine.
- R-09 Badges: keine; Status steht als Kursivtext in der Metazeile.
- R-10, R-13 Glas, Glow: keine.
- R-12 Schatten: keiner; die versetzte Papierfläche hinter den Screens ersetzt ihn.
- R-14 Karten: keine gleichförmigen Karten; Leitprojekt groß, zwei kleinere.
- R-19 Animation: keine (MOTION 1).
- R-22 Illustration: keine, nur echte App-Screens.

## Block 3: Lebendigkeit

- Regler gesetzt: ENERGY 2 / RHYTHM 2 / MOTION 1 (DESIGN.md).
- Fokuspunkt je Bildschirm: Überschrift + Stempel, Sudoku-Screen, Streichliste, Preisliste, E-Mail.
- Weißraum trennt Abschnitte, Randspalte als feste Achse.
- Ein Akzent: Siegelrot (Stempel, Streichungen, Fokus, Hover).
- Motiv: Stempel + rote Durchstreichung + Buch-Randspalte.

## Block 4: Handwerk

Kein Vorlagenaufbau (kein Hero mit zwei Buttons, keine Logoleiste, keine
3-Spalten-Preise, keine 4-Spalten-Fußzeile), keine Floskel-Buttons, keine
Werbewörter, Palette 2 + 1, kein Klon eines bekannten Produkts.

## Vor dem Livegang offen

1. Postfach `hallo@nbsystems.dev` anlegen oder eine andere Adresse nennen.
2. Preise bestätigen (seit 02.11. marktbasierte Empfehlung: App ab 6.500 €,
   Betreuung ab 29 €/Monat inkl. 30 Min. Änderungen).
3. Impressum (nach Gewerbeanmeldung) und kurze Datenschutzinfo zur Seite selbst.
