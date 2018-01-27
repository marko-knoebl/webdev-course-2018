HTML Syntax
===========

## Elemente mit Inhalt
Haben ein Start-Tag (z.B. ```<div>```) und ein End-Tag (z.B. ```</div>```)  
Beispiel:
```html
<h1>This is a heading</h1>
```

## Elemente ohne Inhalt
Beispiel: br-Tag - diese Elemente haben kein End-Tag
```html
Hello<br>
World
```

## Attribute
Können im Anfangstag angegeben werden   
z.B.:
```html
<img src="portrait.png">
<a href="https://google.com">Google</a>
```
Die Werte werden *üblicherweise* in Anführungszeichen gesetzt (obwohl diese in vielen Fällen theoretisch wegfallen können)

## Kommentare
Alles zwischen ```<!--``` und ```-->``` ist ein Kommentar.



Allgemeine Dokumentstruktur (HTML5)
===================================

```html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
  </body>
</html>
```



HTML head Referenz
==================

Siehe auch: https://github.com/joshbuchea/HEAD

## title
Dokumenttitel (erscheint in der Fensterleiste)
```html
<title>My Website</title>
```

## meta

### charset
Heutzutage sollte immer utf-8 als encoding angegeben sein. Dadurch können einfach beliebige Unicode-Zeichen im dokument verwendet werden.
```html
<meta charset="utf-8">
```

### name="viewport"
Sollte auf allen Websites verwendet werden, um die Browserskalierung zurückzusetzen und dadurch eine gute Darstellung auf Mobilgeräten zu ermöglichen
```html
<meta name="viewport" width="device-width">
```

### name="description"
Dient als Titel für Browserlesezeichen, wird von Suchmaschinen genutzt.
```html
<meta name="description" content="Wikipedia is a free online encyclopedia, ...">
```

### name="keywords"
Kann von Suchmaschinen genutzt werden
```html
<meta name="keywords" content="HTML,javascript">
```

## favicon
Icon für den Browser-Tab / für Lesezeichen
```html
<link rel="icon" sizes="16x16" href="favicon_16.png" type="image/png">
<link rel="icon" sizes="32x32" href="favicon_32.png" type="image/png">
```



Stylessheets & Scripts
======================
Können entweder im head oder im body eingebunden werden

## stylesheets

```html
<link rel="stylesheet" href="style.css">
<!-- oder -->
<style>
  [...]
</style>
```

## scripts

```html
<script>[...]</script>
<!-- oder -->
<script src="myscript.js"></script>
```



HTML Tags: Übersicht
====================

vollständige Listen:
* https://www.w3schools.com/tags/ref_byfunc.asp
* https://www.w3schools.com/TAgs/default.asp
* https://developer.mozilla.org/de/docs/Web/HTML/Element

## allgemeine Elemente
* div: allgemeines block-Element
* span: allgemeines inline-Element

## Strukturierung (semantisch)
* main
* nav
* aside
* section
* article
* footer

## Links
* a

## Gliederung
* h1-h6
* p
* hr

## Textformattierung
* br
* em
* strong
* b (veraltet)
* i (veraltet)

## Listen
* ul
* ol
* li

## Medien
* img
* picture
* video
* audio

## Formulare
* button
* input
* label
* select

## Tabellen
* table
* (tbody)
* (thead)
* tr
* td
* th



Links
=====
```html
<a href="https://google.com" target="_blank">Google</a>
```
```target="_blank"``` öffnet den Link in einem neuen Fenster / Tab.



Bilder
======
```html
<img src="portrait.png" alt="portrait of John Doe">
```



Tabellen
========
Beispiel:
```html
<table>
  <caption>opening hours</caption>
  <tr>
    <th>Day</th>
    <th>Hours</th>
  </tr>
  <tr>
    <td>Monday</td>
    <td>9:00-17:00</td>
  </tr>
  <tr>
    <td>Tuesday</td>
    <td rowspan="2">10:00-17:00</td>
  <tr>
  <tr>
    <td>Wednesday</td>
  <tr>
</table>
```


general HTML attributes
=======================

lang="de" (usually on <HTML> elements)



lists
=====

```html
<ul>
  <li>shopping</li>
  <li>taxes</li>
</ul>
<ol>
  <li>learn HTML</li>
  <li>learn CSS</li>
  <li>learn JavaScript</li>
</ol>
```



media
=====

## img

attributes:
* src: location of the image
* alt: alternative text if the image cannot be displayed
* srcset?
```html
<img src="foo.png">
```

## picture
```html
<picture>
  <source srcset="portrait-lg.png" media="(min-width: 600px)">
  <source srcset="portrait-md.png" media="(min-width: 400px)">
  <img src="portrait-sm.png">
</picture>
```

## video
```html
<video src="myvideo.mk" autoplay controls>
</video>
```

## audio
```html
<audio src="myaudio.mk" loop volume="0.5"></audio>
```

## tables
```html
<table>
  <caption>opening hours</caption>
  <tr>
    <th>Day</th>
    <th>Hours</th>
  </tr>
  <tr>
    <td>Monday</td>
    <td>9:00-17:00</td>
  </tr>
  <tr>
    <td>Tuesday</td>
    <td rowspan="2">10:00-17:00</td>
  <tr>
  <tr>
    <td>Wednesday</td>
  <tr>
</table>
```

### table styling
```css
table {
  border-collapse: collapse;
}
tr:hover:nth-child(n) {
  background-color: lightgrey;
}
tr:nth-child(2n) {
  background-color: skyblue;
}
```

## forms



