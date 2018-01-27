CSS Syntax
==========

```css
selector {
  property1: value1;
  property2: value2;
}
/* this is a comment */
```

Beispiel:
```css
h1 {
  font-size: 20px;
  text-decoration: underline;
}
```



CSS-Selektoren: Grundlagen
==========================

## Universalselektor
Bezieht sich auf alle Elemente
```css
* {
  box-sizing: border-box;
}
```

## Tag-Selektoren
zB: alle *h1* Elemente
```css
h1 {
  font-size: 20px;
}
```

## Klassenselektoren
```css
.important {
  color: red;
}
```

## ID-Selektoren
```css
#main {
  max-width: 600px;
}
```



Priorität von CSS-Regeln
========================

Es gibt bestimmte Regeln, die bestimmen, welche Regel "gewinnt", wenn sich zwei CSS-Regeln widersprechen

## Arten von Selektoren
Unterschiedliche Selektorarten haben eine unterschiedliche Priorität (Spezifizität). In aufsteigender Reihenfolge:
* Universalselektor
* Tag-selektor
* Klassenselektor
* ID-Selektor
* inline-Stile (HTML elemente mit ```style="..."```)

Regeln mit hoher Spezifizität gewinnen gegen Regeln mit niedrigerer.

## Reihenfolge
Wenn selektoren der gleichen Spezifizität vorliegen, "gewinnt" die letzte Deklaration:
```css
h1 {
  color: red;
}
h1 {
  color: blue; /* dieser Selektor "gewinnt" */
}
```

## !important
Regeln können eine höhere Priorität erhalten, indem man ```!important``` vor dem Strichpunkt einfügt:
```css
h1 {
  color: red !important;
}
```
Im allgemeinen sollte das Verwenden von ```!important``` aber vermieden werden.



CSS Properties
==============

## Farbe
* color: Textfarbe
* background-color

### Werte
* standard-Farben, zB: blue, white, dark-grey
* rgb-Definition, zB: ```rgb(255, 255, 127)```
* hex-Wert, zB: ```#FFAA00```

## Schrift
* font-size: zB 20px, 150%
* text-decoration: zB underline, line-through, none
* font-family: zB ```Arial, sans-serif```
* text-align: zB right, left

## Größe und das Box-Modell
mögliche Properties:
* height (zB 100px)
* width
* padding (zB 8px)
* border (zB 8px solid black)
* margin (zB 8px)

## Tabellen
```css
table {
  border-collapse: collapse;
}