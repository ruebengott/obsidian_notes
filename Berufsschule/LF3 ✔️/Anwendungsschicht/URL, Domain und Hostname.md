---
tags: [berufsschule, lf3, dns, url]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=52]]"
datum:
status: zu-lernen
---
# URL, Domain und Hostname

> [!summary] Kurz & knapp
> Eine **URL** (Uniform Resource Locator, „Internet-/Webadresse“) setzt sich aus **Protokoll, Hostname (Subdomain + Domain + TLD), Pfad und Parametern** zusammen. Meist ist damit ein konkreter Pfad zu einer Datei oder einem Verzeichnis einer Website gemeint.

## Aufbau einer URL
Beispiel: `http://www.youtube.com/watch?v=QhcwLyyEjOA`

| Nr. | Bestandteil | Im Beispiel | Erklärung |
|---|---|---|---|
| 1 | Protokoll | `http://` | Hypertext Transfer Protocol. Andere: HTTPS, FTP … |
| 2 | Host / Hostname | `www.youtube.com` | vollständiger Name des Servers |
| 3 | Subdomain | `www.` | Unterbereich der Domain |
| 4 | Domain(name) | `youtube.com` | registrierter Name |
| 5 | Top-Level-Domain (TLD) | `.com` | Endung der Webadresse |
| 6 | Pfad | `/watch` | verweist meist auf eine Datei oder einen Ordner auf dem Webserver, z. B. `/ordner/datei.html` |
| 7 | Parameter und Wert | `?v=QhcwLyyEjOA` | Parameter werden mit `?` eingeleitet und stehen immer im Schema `Parametername=Parameterwert` (hier Name `v`, Wert `QhcwLyyEjOA`) |

```text
http://  www.  youtube  .com  /watch  ?v=QhcwLyyEjOA
  (1)    (3)  └─(4) Domain──┘(5)  (6)       (7)
         └──── (2) Hostname ────┘
```

## Sprachgebrauch
- Mit **URL** meint man meist den konkreten Pfad zu einem Verzeichnis (`http://www.domain.de/ein-verzeichnis/`) oder einer Datei (`http://www.domain.de/dokumente/studie.pdf`).
- Es ist nicht ganz falsch, nur den Host- oder Domainnamen „URL“ zu nennen. Man sollte aber auf die korrekten Begriffe achten.
- Der **Hostname** wird per [[DNS]] in eine IP-Adresse aufgelöst.

> [!tip] Merke
> - URL = Protokoll + Hostname + Pfad + Parameter
> - Hostname = Subdomain + Domain + TLD
> - Parameter beginnen mit `?`, Format `name=wert` (mehrere werden mit `&` verbunden)

## Lernfragen
> [!question]- Zerlege `https://shop.example.de/produkte/index.html?id=42`.
> Protokoll `https`, Hostname `shop.example.de`, Subdomain `shop`, Domain `example.de`, TLD `.de`, Pfad `/produkte/index.html`, Parameter `id`, Wert `42`.

> [!question]- Was ist der Unterschied zwischen Domain und Hostname?
> Die Domain ist der registrierte Name inkl. TLD (z. B. youtube.com). Der Hostname bezeichnet einen konkreten Rechner innerhalb der Domain inkl. Subdomain (z. B. www.youtube.com).

> [!question]- Wofür steht URL?
> Uniform Resource Locator.

> [!question]- Mit welchem Zeichen werden Parameter in einer URL eingeleitet?
> Mit dem Fragezeichen `?`.

## Siehe auch
- [[DNS]]
