OCR et restructuration éditoriale (production des XML)
===

Restructuration des *Documents inédits sur l’histoire de France*.  
Description des motifs attendus.

L’objectif est de conserver la mise en forme et de la (re)sémantiser autant que possible.


# Structure du volume

|motif|TEI P5|HTML5|
|-----|------|-----|
|page de titre|[`titlePage`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-titlePage.html)||
|paratexte introductif : préface… (numérotation romaine)|[`front`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-front.html)|`section`|
|texte édité|[`body`]()|`section`|
|annexes : index…|[`back`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-back.html)|`section`|

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:id="file-id">
  <teiHeader/> <!-- métadonnées -->
  <text>
    <front/>   <!-- page de titre et paratexte introductif -->
    <body/>    <!-- texte édité -->
    <back/>    <!-- annexes (index, etc. et 4e de couverture) -->
  </text>
</TEI>
```


# Hiérarchie (divisions et titres)

|motif|TEI P5|HTML5|
|-----|------|-----|
|partie, chapitre, section, sous-section|[`div`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-div.html)|`section`|
|titres de niveau|[`head`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-head.html)|`h1`, `h2`…|

NB: l’objectif est de pouvoir générer automatiquement la table des matières.

```xml
<body>
  <div>
    <head>Titre de niveau 1</head>
    <div>
      <head>Titre de niveau 2</head>
      <p>paragraphe</p>
    </div>
  </div>
  <div>
    <head>Titre de niveau 1</head>
  </div>
</body>
```


# Blocs

|motif|TEI P5|HTML5|
|-----|------|-----|
|paragraphe|[`p`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-p.html) [`@rend="center"` si centré]||
|citation|[`quote`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-quote.html)|`blockquote`|
|vers|[`l`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-l.html)|`p`|
|strophe|`<l/>`|`<br/>`|
|tableau|[`table`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-table.html), `row`, `cell`|`table`, `tr`, `td`|
|liste|[`list`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-list.html), `item`|`ul`, `li`|
|référence bibliographique|[`bibl`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-bibl.html)|`cite`|
|titre non hiérarchique (liste, tableau, illustration)|[`head`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-head.html)|`caption`, `figcaption`|
|image|[`figure`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-figure.html), `graphic`|`figure`, `img`|

* NB1. On ne conserve ni les en-têtes ni les pieds de page.
* NB2. Pour marquer les strophes, inscrire un vers vide, `<l/>`.
* NB3. **Notes de bas de page** : traitement *inline* des blocs de notes (voir plus bas).


```xml
<div>
  <head>Titre de section</head>
  <p>Un paragraphe.</p>
  <!-- LISTE -->
  <list>
    <head>Titre de la liste</head>
    <item>Premier item</item>
    <item>Deuxième item</item>
  </list>
  <!-- TABLEAU -->
  <table>
    <head>Titre du tableau</head>
    <row>
      <cell>Première ligne, première cellule</cell>
      <cell>Première ligne, deuxième cellule</cell>
    </row>
    <row>
      <cell>Deuxième ligne, première cellule</cell>
      <cell>Deuxième ligne, deuxième cellule</cell>
    </row>
  </table>
  <!-- VERS, STROPHE -->
  <l>Première strophe, premier vers</l>
  <l>Première strophe, deuxième vers</l>
  <l/>
  <l>Deuxième strophe, premier vers</l>
  <l>Deuxième strophe, deuxième vers</l>
</div>
```

# Typographie


|motif|TEI P5|HTML5|
|-----|------|-----|
|italique|[`hi[@rend="i"]`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-hi.html)|`i`|
|gras|`hi[@rend="b"]`|`b`|
|small-caps|`hi[@rend="sc"]`||
|exposant|`hi[@rend="sup"]`|`sup`|

NB. Saisir les majuscules en MAJUSCULES.

# Milestones

## Notes de bas de page
[`note`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-note.html). Rattacher la note à son point d’appel, en recomposant éventuellement la note si elle court sur plusieurs pages.

```xml
<p>......suite du texte<note>Texte de la note de bas de page, éventuellement structurée en paragraphes</note> suite du texte......</p>
```

## Saut de page
[`pb`](http://www.tei-c.org/release/doc/tei-p5-doc/fr/html/ref-pb.html). Il convient d’enregistrer à chaque saut de page, la pagination imprimée et lien vers l’image.

```xml
<p>… M. de La Salle ; de <pb n="93" facs="http://gallica.bnf.fr/iiif/ark:/12148/bpt6k6561127c/f103/full/full/0/native.jpg"/>belles tapisseries de Flandre…</p>
```
