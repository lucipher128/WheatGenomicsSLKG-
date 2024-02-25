## Wheat Genomics Literature KG SPARQL Queries


### Prefixes of Used Ontologies and Vocabularies


```sparql
prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> 
prefix xsd:     <http://www.w3.org/2001/XMLSchema#> 
prefix schema:  <http://schema.org/> 
prefix owl:     <http://www.w3.org/2002/07/owl#> 
prefix skos:    <http://www.w3.org/2004/02/skos/core#> 
prefix oa:      <http://www.w3.org/ns/oa#> 
prefix ncbi:    <http://identifiers.org/taxonomy/> 
prefix dct:     <http://purl.org/dc/terms/> 
prefix frbr:    <http://purl.org/vocab/frbr/core#> 
prefix fabio:   <http://purl.org/spar/fabio/> 
prefix obo:     <http://purl.obolibrary.org/obo/> 
prefix bibo:    <http://purl.org/ontology/bibo/> 
prefix d2kab:   <http://ns.inria.fr/d2kab/> 
prefix dc:      <http://purl.org/dc/terms/> 
```


## CQ 1.

The first SPARQL query allows scientists to retrieve genes that are mentioned proximal to the a given phenotype (resistance to leaf rust in this example). The query counts the number of times that a gene is cited in the PubMed corpus proximal to the phenotype. The results of this query confirms that Lr34 is one most frequent genes mentionned  proximal to the resistance to leaf rust phenotype. Lr10, Lr26 and Lr24 genes appear also in the top of the list. 


```sparql
SELECT ?GeneName (count(distinct ?paper) as ?NbOcc) WHERE {

   ?a1 a oa:Annotation; 
      oa:hasTarget [ oa:hasSource ?source1 ] ;  
      oa:hasBody [ a d2kab:Phenotype; skos:prefLabel "resistance to Leaf Rust"] .

   ?source1 frbr:partOf+ ?paper .
    
   ?a a oa:Annotation ; 
      oa:hasTarget [ oa:hasSource ?source ] ;
      oa:hasBody [ a d2kab:Gene; skos:prefLabel ?GeneName ].

   ?source frbr:partOf+ ?paper.

   ?paper a fabio:ResearchPaper.
}
GROUP BY ?GeneName 
HAVING (count(distinct ?paper) > 1)
ORDER BY DESC(?NbOcc)
```


<div class="krn-spql"><table><tr class=hdr><th>GeneName</th>
<th>NbOcc</th></tr><tr class=odd><td class=val>Lr34</td>
<td class=val>34</td></tr><tr class=even><td class=val>Lr10</td>
<td class=val>33</td></tr><tr class=odd><td class=val>Lr1</td>
<td class=val>33</td></tr><tr class=even><td class=val>Lr</td>
<td class=val>24</td></tr><tr class=odd><td class=val>Lr26</td>
<td class=val>22</td></tr><tr class=even><td class=val>Lr24</td>
<td class=val>20</td></tr><tr class=odd><td class=val>Lr9</td>
<td class=val>19</td></tr><tr class=even><td class=val>Lr28</td>
<td class=val>19</td></tr><tr class=odd><td class=val>Lr21</td>
<td class=val>19</td></tr><tr class=even><td class=val>Lr16</td>
<td class=val>18</td></tr><tr class=odd><td class=val>Lr18</td>
<td class=val>15</td></tr><tr class=even><td class=val>Lr13</td>
<td class=val>15</td></tr><tr class=odd><td class=val>Lr19</td>
<td class=val>14</td></tr><tr class=even><td class=val>Lr3</td>
<td class=val>12</td></tr><tr class=odd><td class=val>Lr46</td>
<td class=val>12</td></tr><tr class=even><td class=val>Lr37</td>
<td class=val>11</td></tr><tr class=odd><td class=val>Lr11</td>
<td class=val>10</td></tr><tr class=even><td class=val>Lr30</td>
<td class=val>10</td></tr><tr class=odd><td class=val>Lr35</td>
<td class=val>9</td></tr><tr class=even><td class=val>Lr17</td>
<td class=val>8</td></tr></table><div class="tinfo">Total: 56, Shown: 20</div></div>


## CQ2.

The SPARQL query allows to retrieve genetic markers mentioned proximal to a gene which is in turn mentioned proximal to a phenotype ("resistance to Stripe Rust" in this example) considering the same scientific publication. The results of this query returns 30 scientific publications that list several genetic markers related to different genes which are mentioned proximal to the <i> resistance to Stripe Rust</i> phenotype.


```sparql
SELECT distinct ?GeneName (GROUP_CONCAT(distinct ?marker; SEPARATOR="-") as ?markers) ?paper ?year 
WHERE {

   ?a1 a oa:Annotation ;
      oa:hasTarget [ oa:hasSource ?source1 ] ;
      oa:hasBody [ a d2kab:Gene ; skos:prefLabel ?GeneName] .

   ?source1 frbr:partOf+ ?paper .

   ?a2 a oa:Annotation ;
      oa:hasTarget [ oa:hasSource ?source2 ] ;
      oa:hasBody [ a d2kab:Marker ; skos:prefLabel ?marker ]. 

   ?source2 frbr:partOf+ ?paper .

   ?a3 a oa:Annotation ; 
      oa:hasTarget [ oa:hasSource ?source3 ] ;
      oa:hasBody [ skos:prefLabel "resistance to Stripe Rust"; a d2kab:Phenotype ] .

   ?source3 frbr:partOf+ ?paper . 

   ?paper a fabio:ResearchPaper ;  dct:title ?source3; dct:issued ?year .
   FILTER (?year >= "2010"^^xsd:gYear)
}
GROUP BY ?GeneName?paper ?year
```


<div class="krn-spql"><table><tr class=hdr><th>GeneName</th>
<th>markers</th>
<th>paper</th>
<th>year</th></tr><tr class=odd><td class=val>Lr52</td>
<td class=val>cfb309-gwm234</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/21344185" target="_other">https://pubmed.ncbi.nlm.nih.gov/21344185</a></td>
<td class=val>2011</td></tr><tr class=even><td class=val>Yr18</td>
<td class=val>Xbarc98-Xgwm165-Xgwm192</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/20848270" target="_other">https://pubmed.ncbi.nlm.nih.gov/20848270</a></td>
<td class=val>2011</td></tr><tr class=odd><td class=val>Gc</td>
<td class=val>gwm148</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/27795677" target="_other">https://pubmed.ncbi.nlm.nih.gov/27795677</a></td>
<td class=val>2016</td></tr><tr class=even><td class=val>Yr65</td>
<td class=val>Xgdm33-Xgwm11-Xgwm18-Xgwm413</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/25142874" target="_other">https://pubmed.ncbi.nlm.nih.gov/25142874</a></td>
<td class=val>2014</td></tr><tr class=odd><td class=val>LrW1</td>
<td class=val>cfb309-gwm234</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/21344185" target="_other">https://pubmed.ncbi.nlm.nih.gov/21344185</a></td>
<td class=val>2011</td></tr><tr class=even><td class=val>Yr</td>
<td class=val>Xbarc8-Xgwm493</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/27818611" target="_other">https://pubmed.ncbi.nlm.nih.gov/27818611</a></td>
<td class=val>2015</td></tr><tr class=odd><td class=val>Yr26</td>
<td class=val>Xbarc187-Xgwm11-Xgwm18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24487977" target="_other">https://pubmed.ncbi.nlm.nih.gov/24487977</a></td>
<td class=val>2014</td></tr><tr class=even><td class=val>Yr47</td>
<td class=val>cfb309-gwm234</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/21344185" target="_other">https://pubmed.ncbi.nlm.nih.gov/21344185</a></td>
<td class=val>2011</td></tr><tr class=odd><td class=val>Yr10</td>
<td class=val>Xgwm273</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/26649867" target="_other">https://pubmed.ncbi.nlm.nih.gov/26649867</a></td>
<td class=val>2016</td></tr><tr class=even><td class=val>Yr24</td>
<td class=val>Xbarc137-Xbarc187-Xbarc240-Xgwm11-Xgwm18-Xgwm273</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/22967144" target="_other">https://pubmed.ncbi.nlm.nih.gov/22967144</a></td>
<td class=val>2012</td></tr><tr class=odd><td class=val>Yr50</td>
<td class=val>Xbarc1096-Xgpw7272-Xgwm540-Xwmc310-Xwmc47</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/23052018" target="_other">https://pubmed.ncbi.nlm.nih.gov/23052018</a></td>
<td class=val>2013</td></tr><tr class=even><td class=val>Lr34</td>
<td class=val>Xbarc98-Xgwm165-Xgwm192</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/20848270" target="_other">https://pubmed.ncbi.nlm.nih.gov/20848270</a></td>
<td class=val>2011</td></tr><tr class=odd><td class=val>Yr80</td>
<td class=val>gwm108-gwm376</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/29560515" target="_other">https://pubmed.ncbi.nlm.nih.gov/29560515</a></td>
<td class=val>2018</td></tr><tr class=even><td class=val>RL6077</td>
<td class=val>Xbarc98-Xgwm165-Xgwm192</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/20848270" target="_other">https://pubmed.ncbi.nlm.nih.gov/20848270</a></td>
<td class=val>2011</td></tr><tr class=odd><td class=val>Yr15</td>
<td class=val>Xbarc8-Xgwm493</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/27818611" target="_other">https://pubmed.ncbi.nlm.nih.gov/27818611</a></td>
<td class=val>2015</td></tr><tr class=even><td class=val>Yr46</td>
<td class=val>Xbarc98-Xgwm165-Xgwm192</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/20848270" target="_other">https://pubmed.ncbi.nlm.nih.gov/20848270</a></td>
<td class=val>2011</td></tr><tr class=odd><td class=val>Yr</td>
<td class=val>Xgwm146</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/23396999" target="_other">https://pubmed.ncbi.nlm.nih.gov/23396999</a></td>
<td class=val>2013</td></tr><tr class=even><td class=val>Yr5</td>
<td class=val>Xwmc441</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/23090143" target="_other">https://pubmed.ncbi.nlm.nih.gov/23090143</a></td>
<td class=val>2013</td></tr><tr class=odd><td class=val>V26</td>
<td class=val>Xbarc187-Xgwm11-Xgwm18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24487977" target="_other">https://pubmed.ncbi.nlm.nih.gov/24487977</a></td>
<td class=val>2014</td></tr><tr class=even><td class=val>Lr67</td>
<td class=val>Xbarc98-Xgwm165-Xgwm192</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/20848270" target="_other">https://pubmed.ncbi.nlm.nih.gov/20848270</a></td>
<td class=val>2011</td></tr></table><div class="tinfo">Total: 30, Shown: 20</div></div>


## CQ2 bis.
The SPARQL query retrieves couples of scientific publications such as a first publication mentions a given phenotype and a gene and the second one mentions the same gene name with a genetic marker. To reduce the number of results, the following query retrieves only publications which mention the <i>resistance to Stripe Rust</i> phenotype in their title along with genetic markers and genes in their abstract.  


```sparql
SELECT distinct ?geneName ?paper1 ?marker ?paper2 WHERE {
   {
    SELECT distinct ?geneName ?gene ?paper1 WHERE {
       ?a1 a oa:Annotation ; 
          oa:hasTarget [ oa:hasSource ?source1 ] ;
          oa:hasBody [ skos:prefLabel "resistance to Stripe Rust" ] .

       ?a2 a oa:Annotation ;
          oa:hasTarget [ oa:hasSource ?source2 ] ;
          oa:hasBody ?gene .
          ?gene a d2kab:Gene ; skos:prefLabel ?geneName . 
          ?source1 frbr:partOf+ ?paper1 .
          ?source2 frbr:partOf+ ?paper1 .
          ?paper1 a fabio:ResearchPaper ; dct:title ?source1 .
    }
   }
   ?a3 a oa:Annotation ;
      oa:hasTarget [ oa:hasSource ?source3 ] ;
      oa:hasBody [a d2kab:Marker ; skos:prefLabel ?marker ] .
 
   ?a4 a oa:Annotation ;
      oa:hasTarget [ oa:hasSource ?source4 ] ;
      oa:hasBody ?gene .
 
   ?source3 frbr:partOf+ ?paper2 .
   ?source4 frbr:partOf+ ?paper2 .
   ?paper2 a fabio:ResearchPaper .
   FILTER (URI(?paper1) != URI(?paper2))
}
```


<div class="krn-spql"><table><tr class=hdr><th>geneName</th>
<th>paper1</th>
<th>marker</th>
<th>paper2</th></tr><tr class=odd><td class=val>R2</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15841362" target="_other">https://pubmed.ncbi.nlm.nih.gov/15841362</a></td>
<td class=val>mta9</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/12582867" target="_other">https://pubmed.ncbi.nlm.nih.gov/12582867</a></td></tr><tr class=even><td class=val>R2</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/17989954" target="_other">https://pubmed.ncbi.nlm.nih.gov/17989954</a></td>
<td class=val>mta9</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/12582867" target="_other">https://pubmed.ncbi.nlm.nih.gov/12582867</a></td></tr><tr class=odd><td class=val>Yr18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/23558982" target="_other">https://pubmed.ncbi.nlm.nih.gov/23558982</a></td>
<td class=val>Xgwm295</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15965649" target="_other">https://pubmed.ncbi.nlm.nih.gov/15965649</a></td></tr><tr class=even><td class=val>Yr18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/23177146" target="_other">https://pubmed.ncbi.nlm.nih.gov/23177146</a></td>
<td class=val>Xgwm295</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15965649" target="_other">https://pubmed.ncbi.nlm.nih.gov/15965649</a></td></tr><tr class=odd><td class=val>Yr18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/21104373" target="_other">https://pubmed.ncbi.nlm.nih.gov/21104373</a></td>
<td class=val>Xgwm295</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15965649" target="_other">https://pubmed.ncbi.nlm.nih.gov/15965649</a></td></tr><tr class=even><td class=val>Yr18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/20848270" target="_other">https://pubmed.ncbi.nlm.nih.gov/20848270</a></td>
<td class=val>Xgwm295</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15965649" target="_other">https://pubmed.ncbi.nlm.nih.gov/15965649</a></td></tr><tr class=odd><td class=val>Yr18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/19638674" target="_other">https://pubmed.ncbi.nlm.nih.gov/19638674</a></td>
<td class=val>Xgwm295</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15965649" target="_other">https://pubmed.ncbi.nlm.nih.gov/15965649</a></td></tr><tr class=even><td class=val>Yr18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/19638674" target="_other">https://pubmed.ncbi.nlm.nih.gov/19638674</a></td>
<td class=val>Xgwm1220</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15965649" target="_other">https://pubmed.ncbi.nlm.nih.gov/15965649</a></td></tr><tr class=odd><td class=val>Yr18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/23558982" target="_other">https://pubmed.ncbi.nlm.nih.gov/23558982</a></td>
<td class=val>Xgwm1220</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15965649" target="_other">https://pubmed.ncbi.nlm.nih.gov/15965649</a></td></tr><tr class=even><td class=val>Yr18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/21104373" target="_other">https://pubmed.ncbi.nlm.nih.gov/21104373</a></td>
<td class=val>Xgwm1220</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15965649" target="_other">https://pubmed.ncbi.nlm.nih.gov/15965649</a></td></tr><tr class=odd><td class=val>Yr18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/23177146" target="_other">https://pubmed.ncbi.nlm.nih.gov/23177146</a></td>
<td class=val>Xgwm1220</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15965649" target="_other">https://pubmed.ncbi.nlm.nih.gov/15965649</a></td></tr><tr class=even><td class=val>Yr18</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/20848270" target="_other">https://pubmed.ncbi.nlm.nih.gov/20848270</a></td>
<td class=val>Xgwm1220</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15965649" target="_other">https://pubmed.ncbi.nlm.nih.gov/15965649</a></td></tr><tr class=odd><td class=val>Sr2</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/23558982" target="_other">https://pubmed.ncbi.nlm.nih.gov/23558982</a></td>
<td class=val>Xgwm533</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15340687" target="_other">https://pubmed.ncbi.nlm.nih.gov/15340687</a></td></tr><tr class=even><td class=val>Rg1</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/12582703" target="_other">https://pubmed.ncbi.nlm.nih.gov/12582703</a></td>
<td class=val>Xgwm0136</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/16874490" target="_other">https://pubmed.ncbi.nlm.nih.gov/16874490</a></td></tr><tr class=odd><td class=val>Rg1</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/12582703" target="_other">https://pubmed.ncbi.nlm.nih.gov/12582703</a></td>
<td class=val>Xgwm1223</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/16874490" target="_other">https://pubmed.ncbi.nlm.nih.gov/16874490</a></td></tr><tr class=even><td class=val>Rg1</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/12582703" target="_other">https://pubmed.ncbi.nlm.nih.gov/12582703</a></td>
<td class=val>Xgwm0033</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/16874490" target="_other">https://pubmed.ncbi.nlm.nih.gov/16874490</a></td></tr><tr class=odd><td class=val>R2</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15841362" target="_other">https://pubmed.ncbi.nlm.nih.gov/15841362</a></td>
<td class=val>Xbarc151</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/17989954" target="_other">https://pubmed.ncbi.nlm.nih.gov/17989954</a></td></tr><tr class=even><td class=val>R2</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15841362" target="_other">https://pubmed.ncbi.nlm.nih.gov/15841362</a></td>
<td class=val>Xwmc170</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/17989954" target="_other">https://pubmed.ncbi.nlm.nih.gov/17989954</a></td></tr><tr class=odd><td class=val>R2</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/15841362" target="_other">https://pubmed.ncbi.nlm.nih.gov/15841362</a></td>
<td class=val>Xwmc407</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/17989954" target="_other">https://pubmed.ncbi.nlm.nih.gov/17989954</a></td></tr><tr class=even><td class=val>Sr2</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/23558982" target="_other">https://pubmed.ncbi.nlm.nih.gov/23558982</a></td>
<td class=val>gwm533</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/22278178" target="_other">https://pubmed.ncbi.nlm.nih.gov/22278178</a></td></tr></table><div class="tinfo">Total: 666, Shown: 20</div></div>


## CQ 3. 

This SPARQL query allows scientists to retrieve detected wheat varieties that have specific phenotypes.


```sparql
SELECT distinct ?variety ?label ?paper WHERE {

   ?rel1 d2kab:hasVariety ?a1 ; d2kab:hasPhenotype ?a2 .
  
   ?a1 a oa:Annotation ;
      oa:hasTarget [ oa:hasSource ?source1 ] ;  
      oa:hasBody [ a d2kab:Variety ; skos:prefLabel ?variety ] .

   ?a2 a oa:Annotation ;
      oa:hasTarget [ oa:hasSource ?source2 ] ;
      oa:hasBody [ a d2kab:Phenotype ; skos:prefLabel ?label ] .

   ?source1 frbr:partOf+ ?paper .
   ?source2 frbr:partOf+ ?paper . 
   ?paper a fabio:ResearchPaper .
}
ORDER BY ?variety
```


<div class="krn-spql"><table><tr class=hdr><th>variety</th>
<th>label</th>
<th>paper</th></tr><tr class=odd><td class=val>Apache</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/21655994" target="_other">https://pubmed.ncbi.nlm.nih.gov/21655994</a></td></tr><tr class=even><td class=val>Apache</td>
<td class=val>resistance to septoria</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/21655994" target="_other">https://pubmed.ncbi.nlm.nih.gov/21655994</a></td></tr><tr class=odd><td class=val>Apache</td>
<td class=val>plant height</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/31646363" target="_other">https://pubmed.ncbi.nlm.nih.gov/31646363</a></td></tr><tr class=even><td class=val>Apache</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/31646363" target="_other">https://pubmed.ncbi.nlm.nih.gov/31646363</a></td></tr><tr class=odd><td class=val>Apache</td>
<td class=val>heat resistance</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/31646363" target="_other">https://pubmed.ncbi.nlm.nih.gov/31646363</a></td></tr><tr class=even><td class=val>Arina</td>
<td class=val>resistance to rust</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24794977" target="_other">https://pubmed.ncbi.nlm.nih.gov/24794977</a></td></tr><tr class=odd><td class=val>Arina</td>
<td class=val>resistance to Stem Rust</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24794977" target="_other">https://pubmed.ncbi.nlm.nih.gov/24794977</a></td></tr><tr class=even><td class=val>Arina</td>
<td class=val>resistance to Leaf Rust</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24173052" target="_other">https://pubmed.ncbi.nlm.nih.gov/24173052</a></td></tr><tr class=odd><td class=val>Arina</td>
<td class=val>resistance to Leaf Rust</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/27659842" target="_other">https://pubmed.ncbi.nlm.nih.gov/27659842</a></td></tr><tr class=even><td class=val>Arina</td>
<td class=val>pathogen resistance</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/27659842" target="_other">https://pubmed.ncbi.nlm.nih.gov/27659842</a></td></tr><tr class=odd><td class=val>Arina</td>
<td class=val>resistance to Septoria Leaf Blotch</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/18943769" target="_other">https://pubmed.ncbi.nlm.nih.gov/18943769</a></td></tr><tr class=even><td class=val>Arina</td>
<td class=val>resistance to Leaf Rust</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/16896711" target="_other">https://pubmed.ncbi.nlm.nih.gov/16896711</a></td></tr><tr class=odd><td class=val>Arina</td>
<td class=val>resistance to Stripe Rust</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/25112204" target="_other">https://pubmed.ncbi.nlm.nih.gov/25112204</a></td></tr><tr class=even><td class=val>Arina</td>
<td class=val>pathogen resistance</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/25112204" target="_other">https://pubmed.ncbi.nlm.nih.gov/25112204</a></td></tr><tr class=odd><td class=val>Arina</td>
<td class=val>resistance to rust</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/25112204" target="_other">https://pubmed.ncbi.nlm.nih.gov/25112204</a></td></tr><tr class=even><td class=val>Biscay</td>
<td class=val>plant height</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/31646363" target="_other">https://pubmed.ncbi.nlm.nih.gov/31646363</a></td></tr><tr class=odd><td class=val>Biscay</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/31646363" target="_other">https://pubmed.ncbi.nlm.nih.gov/31646363</a></td></tr><tr class=even><td class=val>Biscay</td>
<td class=val>heat resistance</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/31646363" target="_other">https://pubmed.ncbi.nlm.nih.gov/31646363</a></td></tr><tr class=odd><td class=val>Cajeme 71</td>
<td class=val>grain protein content</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24202585" target="_other">https://pubmed.ncbi.nlm.nih.gov/24202585</a></td></tr><tr class=even><td class=val>Cajeme 71</td>
<td class=val>protein content of seed</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24202585" target="_other">https://pubmed.ncbi.nlm.nih.gov/24202585</a></td></tr></table><div class="tinfo">Total: 91, Shown: 20</div></div>


## CQ 4.

First we query all phenotypes defined in WTO as sub-classes of the "resistance to a fungal pathogen" Class.


```sparql
SELECT distinct ?phenotype ?phenotypeLabel WHERE {
?e skos:prefLabel "resistance to a fungal pathogen" ; 
   skos:narrower* ?phenotype .
?phenotype skos:prefLabel ?phenotypeLabel
}

```


<div class="krn-spql"><table><tr class=hdr><th>phenotype</th>
<th>phenotypeLabel</th></tr><tr class=odd><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000340" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000340</a></td>
<td class=val>resistance to a fungal pathogen</td></tr><tr class=even><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000465" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000465</a></td>
<td class=val>late blight resistance</td></tr><tr class=odd><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000471" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000471</a></td>
<td class=val>resistance to Alternaria Leaf Blight</td></tr><tr class=even><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000474" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000474</a></td>
<td class=val>resistance to Anthracnose</td></tr><tr class=odd><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000475" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000475</a></td>
<td class=val>resistance to Ascochyta Leaf Spot</td></tr><tr class=even><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000476" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000476</a></td>
<td class=val>resistance to Black Point</td></tr><tr class=odd><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000477" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000477</a></td>
<td class=val>resistance to Bunt</td></tr><tr class=even><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000478" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000478</a></td>
<td class=val>resistance to Cephalosporium Leaf Stripe</td></tr><tr class=odd><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000480" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000480</a></td>
<td class=val>resistance to Ergot</td></tr><tr class=even><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000482" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000482</a></td>
<td class=val>resistance to Eyespot</td></tr><tr class=odd><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000483" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000483</a></td>
<td class=val>resistance to Fusarium head blight</td></tr><tr class=even><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000484" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000484</a></td>
<td class=val>resistance to Helminthosporium Leaf Blight</td></tr><tr class=odd><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000487" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000487</a></td>
<td class=val>resistance to Mold</td></tr><tr class=even><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000488" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000488</a></td>
<td class=val>resistance to Sclerotium Wilt</td></tr><tr class=odd><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000489" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000489</a></td>
<td class=val>resistance to Sharp Eyespot</td></tr><tr class=even><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000490" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000490</a></td>
<td class=val>resistance to Take-All</td></tr><tr class=odd><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000501" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000501</a></td>
<td class=val>resistance to mildew</td></tr><tr class=even><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000504" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000504</a></td>
<td class=val>resistance to root rot</td></tr><tr class=odd><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000506" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000506</a></td>
<td class=val>resistance to rust</td></tr><tr class=even><td class=val><a href="http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000508" target="_other">http://opendata.inrae.fr/wto/v3.0/thesaurus/WTO_0000508</a></td>
<td class=val>resistance to septoria</td></tr></table><div class="tinfo">Total: 52, Shown: 20</div></div>


The following SPARQL query allows scientists to retrieve publications in which genes are mentioned proximal to phenotypes from a specific class (considering its sub-classes), e.g., all phenotypes related to fungal pathogen resistance. 


```sparql
SELECT ?GeneName ?LPhenotype ?paper WHERE {

   ?aa1 a oa:Annotation; 
      oa:hasTarget [ oa:hasSource ?source1 ];
      oa:hasBody [ a d2kab:Gene; skos:prefLabel ?GeneName ] .
  
   ?source1 frbr:partOf+ ?paper . 

   ?aa2 a oa:Annotation; 
      oa:hasTarget [ oa:hasSource ?source2 ] ; 
      oa:hasBody ?Phenotype .
   
   ?source2 frbr:partOf+ ?paper .
   
   ?Phenotype a d2kab:Phenotype ; skos:prefLabel ?LPhenotype .
   ?e2 skos:prefLabel "resistance to a fungal pathogen" ; skos:narrower* ?Phenotype .

   ?paper a fabio:ResearchPaper ; dct:title ?source2 .
}
GROUP BY ?paper ?Phenotype
ORDER BY ?Phenotype
```


<div class="krn-spql"><table><tr class=hdr><th>GeneName</th>
<th>LPhenotype</th>
<th>paper</th></tr><tr class=odd><td class=val>H26</td>
<td class=val>resistance to a fungal pathogen</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/20128702" target="_other">https://pubmed.ncbi.nlm.nih.gov/20128702</a></td></tr><tr class=even><td class=val>H6</td>
<td class=val>resistance to a fungal pathogen</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/20128702" target="_other">https://pubmed.ncbi.nlm.nih.gov/20128702</a></td></tr><tr class=odd><td class=val>H9</td>
<td class=val>resistance to a fungal pathogen</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/20128702" target="_other">https://pubmed.ncbi.nlm.nih.gov/20128702</a></td></tr><tr class=even><td class=val>H13</td>
<td class=val>resistance to a fungal pathogen</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/20128702" target="_other">https://pubmed.ncbi.nlm.nih.gov/20128702</a></td></tr><tr class=odd><td class=val>r2</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/17426773" target="_other">https://pubmed.ncbi.nlm.nih.gov/17426773</a></td></tr><tr class=even><td class=val>Fr</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/25726000" target="_other">https://pubmed.ncbi.nlm.nih.gov/25726000</a></td></tr><tr class=odd><td class=val>St</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/31881925" target="_other">https://pubmed.ncbi.nlm.nih.gov/31881925</a></td></tr><tr class=even><td class=val>B1</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/12671743" target="_other">https://pubmed.ncbi.nlm.nih.gov/12671743</a></td></tr><tr class=odd><td class=val>Vrn-1</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/32556394" target="_other">https://pubmed.ncbi.nlm.nih.gov/32556394</a></td></tr><tr class=even><td class=val>Kb</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/23071572" target="_other">https://pubmed.ncbi.nlm.nih.gov/23071572</a></td></tr><tr class=odd><td class=val>Rht-D1</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/23451238" target="_other">https://pubmed.ncbi.nlm.nih.gov/23451238</a></td></tr><tr class=even><td class=val>Rg-B1</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/28163582" target="_other">https://pubmed.ncbi.nlm.nih.gov/28163582</a></td></tr><tr class=odd><td class=val>Rht-B1</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/32556394" target="_other">https://pubmed.ncbi.nlm.nih.gov/32556394</a></td></tr><tr class=even><td class=val>D1</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/30821405" target="_other">https://pubmed.ncbi.nlm.nih.gov/30821405</a></td></tr><tr class=odd><td class=val>Vrn-A1</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/32556394" target="_other">https://pubmed.ncbi.nlm.nih.gov/32556394</a></td></tr><tr class=even><td class=val>H19</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/12671754" target="_other">https://pubmed.ncbi.nlm.nih.gov/12671754</a></td></tr><tr class=odd><td class=val>Vrn-B1</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/32556394" target="_other">https://pubmed.ncbi.nlm.nih.gov/32556394</a></td></tr><tr class=even><td class=val>Rht-1</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/32556394" target="_other">https://pubmed.ncbi.nlm.nih.gov/32556394</a></td></tr><tr class=odd><td class=val>B1</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/12671754" target="_other">https://pubmed.ncbi.nlm.nih.gov/12671754</a></td></tr><tr class=even><td class=val>Rht-B1</td>
<td class=val>resistance to Fusarium head blight</td>
<td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/19034409" target="_other">https://pubmed.ncbi.nlm.nih.gov/19034409</a></td></tr></table><div class="tinfo">Total: 694, Shown: 20</div></div>



## Federated Query.
 
This query allows scientists to jointly exploit both KGs to retrieve publications in PubMed and PHB bulletins mentioning the same taxon ("Triticum aestivum" in the example SPARQL query below).
As each corpus uses different semantic resources to annotate taxon entities (NCBI taxonomy in the WheatKG graph, and FCU thesaurus in PHB graph), the query exploits a third KG, TaxRef-LD\footnote{TaxRef-LD is a a Linked Data knowledge graph representing TAXREF, the French national taxonomical register for fauna, flora and fungus, that covers mainland France and overseas territories. 


```sparql
prefix d2kab_inrae:   <http://ontology.inrae.fr/bsv/ontology/>
prefix dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
prefix dct:     <http://purl.org/dc/terms/> 
prefix taxref: <http://taxref.mnhn.fr/lod/property/>
prefix fcu: <http://ontology.inrae.fr/frenchcropusage/>
```



```sparql
SELECT distinct ?paper ?title ?bsv WHERE {
  
    {
    # retrieve scientific papers 
    SELECT distinct ?paper ?title ?taxrefClass ?fcuCropName ?ncbiTaxon WHERE 
    {       
      ?annot a oa:Annotation; oa:hasTarget [ oa:hasSource ?source ] ; oa:hasBody ?ncbiTaxon .
      ?ncbiTaxon a d2kab:Taxon; skos:prefLabel ?label .
      ?source frbr:partOf+ ?paper .
      ?paper a fabio:ResearchPaper ; dct:title ?source .
      ?source rdf:value ?title .
      FILTER(CONTAINS(?label, "Triticum aestivum"))
      
      SERVICE <https://taxref.mnhn.fr/sparql> { 
        SELECT ?taxrefClass ?taxLabel ?ncbiTaxon WHERE {
          ?taxrefClass owl:equivalentClass ?ncbiTaxon ; rdfs:label ?taxLabel .  
        }
      }
    # retrieve alignments  
    ?fcuCropName taxref:candidateAlignment_geves ?taxrefClass .    
    }
   LIMIT 50
  }
    
    SERVICE <http://ontology.inrae.fr/bsv/sparql> { 
      ?bsv a d2kab_inrae:Bulletin ; dul:isRealizedBy ?s ; dct:spatial ?w  ; dct:date ?date_bsv .
     ?aa a oa:Annotation ; oa:hasTarget [ oa:hasSource ?s ]  ; oa:hasBody ?fcuCropName .
  }      
   
   
}
LIMIT 50
```


<div class="krn-spql"><table><tr class=hdr><th>paper</th>
<th>title</th>
<th>bsv</th></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no12_du_06-05-14_cle0cdc21" target="_other">http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no12_du_06-05-14_cle0cdc21</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/char_gdes_Cultures_no14_du_22-05-19_cle0b1586" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/char_gdes_Cultures_no14_du_22-05-19_cle0b1586</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190403_LOR_BSV_Grandes_Cultures_cle8ff1e5" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190403_LOR_BSV_Grandes_Cultures_cle8ff1e5</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190320_LOR_BSV_Grandes_Cultures_cle83816d" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190320_LOR_BSV_Grandes_Cultures_cle83816d</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2016/char_Grandes_Cultures_no42_2016-11-24_cle0385bf" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2016/char_Grandes_Cultures_no42_2016-11-24_cle0385bf</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18678082/2019/BSV_GC_NA_Limousin_13_20190521_cle0cb17e" target="_other">http://ontology.inrae.fr/bsv/resources/Q18678082/2019/BSV_GC_NA_Limousin_13_20190521_cle0cb17e</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190507_LOR_BSV_Grandes_Cultures_cle893371" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190507_LOR_BSV_Grandes_Cultures_cle893371</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q13947/2019/BSV_cereales_paille_15_du_16-04-19_cle81e145" target="_other">http://ontology.inrae.fr/bsv/resources/Q13947/2019/BSV_cereales_paille_15_du_16-04-19_cle81e145</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q13947/2019/BSV_cereales_paille_02_du_29-10-19_cle8cbcac" target="_other">http://ontology.inrae.fr/bsv/resources/Q13947/2019/BSV_cereales_paille_02_du_29-10-19_cle8cbcac</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q1179/2013/BSV_N_41-Grandes_Cultures-2013.11.07" target="_other">http://ontology.inrae.fr/bsv/resources/Q1179/2013/BSV_N_41-Grandes_Cultures-2013.11.07</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q13917/2019/BSV_GRANDES_CULTURES_2019_No7_cle8446d7" target="_other">http://ontology.inrae.fr/bsv/resources/Q13917/2019/BSV_GRANDES_CULTURES_2019_No7_cle8446d7</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2020/BSV05_GC_LOR_S13_2020_cle4419d7" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2020/BSV05_GC_LOR_S13_2020_cle4419d7</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q12130/2020/BSV_no7_du_31-03-20_cle835128" target="_other">http://ontology.inrae.fr/bsv/resources/Q12130/2020/BSV_no7_du_31-03-20_cle835128</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q12130/2018/BSV_no13_du_15-05-18_cle01162f" target="_other">http://ontology.inrae.fr/bsv/resources/Q12130/2018/BSV_no13_du_15-05-18_cle01162f</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677875/2019/BSV_19-19_cereales_Normandie_2019_cle8dba8a" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677875/2019/BSV_19-19_cereales_Normandie_2019_cle8dba8a</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q1190/2010/BSV_GC_13_LIM_27avril2010_cle088887-1" target="_other">http://ontology.inrae.fr/bsv/resources/Q1190/2010/BSV_GC_13_LIM_27avril2010_cle088887-1</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q16954/2014/BSV_11-3_cereales_Normandie_R2014_cle83cb2e" target="_other">http://ontology.inrae.fr/bsv/resources/Q16954/2014/BSV_11-3_cereales_Normandie_R2014_cle83cb2e</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q16994/2011/bsv_grandescultures_20110503_24__cle083e91" target="_other">http://ontology.inrae.fr/bsv/resources/Q16994/2011/bsv_grandescultures_20110503_24__cle083e91</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677875/2019/BSV_01-42_cereales_Normandie_2020_cle83b764" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677875/2019/BSV_01-42_cereales_Normandie_2020_cle83b764</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/alsace_gdes_cultures_no17_du_19-06-19_cle026e84" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/alsace_gdes_cultures_no17_du_19-06-19_cle026e84</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677875/2015/BSV_4-27_cereales_Normandie_R2016_cle84c13e-2" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677875/2015/BSV_4-27_cereales_Normandie_R2016_cle84c13e-2</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q16961/2010/BSV_13_cereales_Normandie_cle01ccd2" target="_other">http://ontology.inrae.fr/bsv/resources/Q16961/2010/BSV_13_cereales_Normandie_cle01ccd2</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190417_CHA_BSV_Grandes_Cultures_cle8333d7" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190417_CHA_BSV_Grandes_Cultures_cle8333d7</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677767/2019/BSV-GC-n__33-01102019_cle41f418" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677767/2019/BSV-GC-n__33-01102019_cle41f418</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q13947/2019/BSV_cereales_paille_06_du_26-11-19_cle81855b" target="_other">http://ontology.inrae.fr/bsv/resources/Q13947/2019/BSV_cereales_paille_06_du_26-11-19_cle81855b</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no9_du_15-04-14_cle81cb1c" target="_other">http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no9_du_15-04-14_cle81cb1c</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q1179/2013/BSV_N_9-Grandes_Cultures-2013.04.11" target="_other">http://ontology.inrae.fr/bsv/resources/Q1179/2013/BSV_N_9-Grandes_Cultures-2013.04.11</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677767/2019/bsv-gc-n__14-21-mai-2019_cle85ad4f" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677767/2019/bsv-gc-n__14-21-mai-2019_cle85ad4f</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677875/2015/BSV_bilan_cereales_Normandie_R2015_V2_cle0e2acd" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677875/2015/BSV_bilan_cereales_Normandie_R2015_V2_cle0e2acd</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q16994/2010/22_bsv_gc_04_05_2010_cle022e2c" target="_other">http://ontology.inrae.fr/bsv/resources/Q16994/2010/22_bsv_gc_04_05_2010_cle022e2c</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2015/BSVcampagnols3_cle8d3542" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2015/BSVcampagnols3_cle8d3542</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q12130/2019/BSV_no11_du_30-04-19_cle0bc1be" target="_other">http://ontology.inrae.fr/bsv/resources/Q12130/2019/BSV_no11_du_30-04-19_cle0bc1be</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q16994/2014/BSV_GC_du_11_fevrier_2014_2_cle01b924" target="_other">http://ontology.inrae.fr/bsv/resources/Q16994/2014/BSV_GC_du_11_fevrier_2014_2_cle01b924</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no15_du_27-05-14_cle0f3e54" target="_other">http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no15_du_27-05-14_cle0f3e54</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190522_LOR_BSV_Grandes_Cultures_cle8b3b61" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190522_LOR_BSV_Grandes_Cultures_cle8b3b61</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18678082/2019/BSV_NA_GC_AQUITAINE_N09_20190404_cle0279a3" target="_other">http://ontology.inrae.fr/bsv/resources/Q18678082/2019/BSV_NA_GC_AQUITAINE_N09_20190404_cle0279a3</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q16961/2010/BSV_9_cereales_Normandie_cle81b469" target="_other">http://ontology.inrae.fr/bsv/resources/Q16961/2010/BSV_9_cereales_Normandie_cle81b469</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677767/2019/BSV-GC-n__36-22102019_cle43a7f1" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677767/2019/BSV-GC-n__36-22102019_cle43a7f1</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q13947/2011/BSV_cereales_paille_07_003" target="_other">http://ontology.inrae.fr/bsv/resources/Q13947/2011/BSV_cereales_paille_07_003</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18678082/2019/BSV_NA_GC_Poitou_Charentes_04_20190306_cle854b15" target="_other">http://ontology.inrae.fr/bsv/resources/Q18678082/2019/BSV_NA_GC_Poitou_Charentes_04_20190306_cle854b15</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q12130/2019/BSV_no6_du_26-03-19_cle8da969" target="_other">http://ontology.inrae.fr/bsv/resources/Q12130/2019/BSV_no6_du_26-03-19_cle8da969</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677875/2019/BSV_07-48_cereales_Normandie_2020_cle8d6d3f" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677875/2019/BSV_07-48_cereales_Normandie_2020_cle8d6d3f</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/2997729" target="_other">https://pubmed.ncbi.nlm.nih.gov/2997729</a></td>
<td class=val>The nucleotide sequence of a HMW glutenin subunit gene located on chromosome 1A of wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/char_gdes_Cultures_no11_du_30-04-19_cle096f9c" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/char_gdes_Cultures_no11_du_30-04-19_cle096f9c</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24185819" target="_other">https://pubmed.ncbi.nlm.nih.gov/24185819</a></td>
<td class=val>Molecular mapping of stripe rust resistance gene Yr51 in chromosome 4AL of wheat.</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no12_du_06-05-14_cle0cdc21" target="_other">http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no12_du_06-05-14_cle0cdc21</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24185819" target="_other">https://pubmed.ncbi.nlm.nih.gov/24185819</a></td>
<td class=val>Molecular mapping of stripe rust resistance gene Yr51 in chromosome 4AL of wheat.</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/char_gdes_Cultures_no14_du_22-05-19_cle0b1586" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/char_gdes_Cultures_no14_du_22-05-19_cle0b1586</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24185819" target="_other">https://pubmed.ncbi.nlm.nih.gov/24185819</a></td>
<td class=val>Molecular mapping of stripe rust resistance gene Yr51 in chromosome 4AL of wheat.</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190403_LOR_BSV_Grandes_Cultures_cle8ff1e5" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190403_LOR_BSV_Grandes_Cultures_cle8ff1e5</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24185819" target="_other">https://pubmed.ncbi.nlm.nih.gov/24185819</a></td>
<td class=val>Molecular mapping of stripe rust resistance gene Yr51 in chromosome 4AL of wheat.</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190320_LOR_BSV_Grandes_Cultures_cle83816d" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190320_LOR_BSV_Grandes_Cultures_cle83816d</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24185819" target="_other">https://pubmed.ncbi.nlm.nih.gov/24185819</a></td>
<td class=val>Molecular mapping of stripe rust resistance gene Yr51 in chromosome 4AL of wheat.</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2016/char_Grandes_Cultures_no42_2016-11-24_cle0385bf" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2016/char_Grandes_Cultures_no42_2016-11-24_cle0385bf</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24185819" target="_other">https://pubmed.ncbi.nlm.nih.gov/24185819</a></td>
<td class=val>Molecular mapping of stripe rust resistance gene Yr51 in chromosome 4AL of wheat.</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18678082/2019/BSV_GC_NA_Limousin_13_20190521_cle0cb17e" target="_other">http://ontology.inrae.fr/bsv/resources/Q18678082/2019/BSV_GC_NA_Limousin_13_20190521_cle0cb17e</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/24185819" target="_other">https://pubmed.ncbi.nlm.nih.gov/24185819</a></td>
<td class=val>Molecular mapping of stripe rust resistance gene Yr51 in chromosome 4AL of wheat.</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190507_LOR_BSV_Grandes_Cultures_cle893371" target="_other">http://ontology.inrae.fr/bsv/resources/Q18677983/2019/20190507_LOR_BSV_Grandes_Cultures_cle893371</a></td></tr></table><div class="tinfo">Total: 50, Shown: 50</div></div>





```sparql
SELECT ?paper ?title 
       SAMPLE(?bsv) as ?bsv
WHERE
{
SELECT distinct ?paper ?title  ?bsv ?NCBItaxon ?fcuConcept ?taxrefClass ?taxrefLabel  WHERE {

  # Get scientific articles in PubMed with "Triticum aestivum" taxon annotations
  { SELECT distinct ?paper ?title ?NCBItaxon WHERE {       
      ?annot a oa:Annotation; oa:hasTarget [ oa:hasSource ?source ] ; oa:hasBody ?NCBItaxon .
      ?NCBItaxon a d2kab:Taxon; skos:prefLabel ?label .
      ?source frbr:partOf+ ?paper .
      ?paper a fabio:ResearchPaper ; dct:title ?source ; dct:issued ?year .
      ?source rdf:value ?title .
      FILTER(CONTAINS(?label, "Triticum aestivum"))
      FILTER (?year >= "2015"^^xsd:gYear)
    } LIMIT 100
  }

  # Retrieve the taxon mentioned in the article from TAXREF-LD
  SERVICE <https://taxref.mnhn.fr/sparql> {
    ?taxrefClass owl:equivalentClass ?NCBItaxon ; rdfs:label ?taxrefLabel . 
  }
  
  # Retrieve the alignment between the taxon from TAXREF-LD and FCU concepts
  ?fcuConcept taxref:candidateAlignment_geves ?taxrefClass .  

  # Get BSV annotations
  SERVICE <http://ontology.inrae.fr/bsv/sparql> { 
    ?bsv a d2kab_inrae:Bulletin ; dul:isRealizedBy ?s ; dct:spatial ?w  ; dct:date ?date_bsv .
    ?aa a oa:Annotation ; oa:hasTarget [ oa:hasSource ?s ]  ; oa:hasBody ?fcuConcept .
  }      
}
LIMIT 100
}
```


<div class="krn-spql"><table><tr class=hdr><th>paper</th>
<th>title</th>
<th>bsv</th></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/26934890" target="_other">https://pubmed.ncbi.nlm.nih.gov/26934890</a></td>
<td class=val>Identification and genetic mapping of PmAF7DS a powdery mildew resistance gene in bread wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no12_du_06-05-14_cle0cdc21" target="_other">http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no12_du_06-05-14_cle0cdc21</a></td></tr><tr class=even><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/25713931" target="_other">https://pubmed.ncbi.nlm.nih.gov/25713931</a></td>
<td class=val>Isolation and characterization of rubisco small subunit gene promoter from common wheat (Triticum aestivum L.).</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no12_du_06-05-14_cle0cdc21" target="_other">http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no12_du_06-05-14_cle0cdc21</a></td></tr><tr class=odd><td class=val><a href="https://pubmed.ncbi.nlm.nih.gov/27857194" target="_other">https://pubmed.ncbi.nlm.nih.gov/27857194</a></td>
<td class=val>Cloning and characterization of TaVIP2 gene from Triticum aestivum and functional analysis in Nicotiana tabacum.</td>
<td class=val><a href="http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no12_du_06-05-14_cle0cdc21" target="_other">http://ontology.inrae.fr/bsv/resources/Q12130/2014/BSV_no12_du_06-05-14_cle0cdc21</a></td></tr></table><div class="tinfo">Total: 3, Shown: 3</div></div>







