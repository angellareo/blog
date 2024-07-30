Title: Principales indicadores y métricas en ciencia
Slug: indicadores-ciencia
Date: 2024-07-07 10:52
Category: Ciencia
Tags: Investigación, Ciencia, STEM, métricas, Factor de impacto
Author: Angel Lareo
Cover: images/metricas.png
Summary: Un repaso a los principales indicadores utilizados para valorar el trabajo de quienes investigamos.

Vivimos en un mundo con cierta obsesión por la cuantificación objetiva, especialmente cuando hablamos de productividad. Dentro de esa búsqueda utópica (algunos dirían, distópica) no son pocos los **indicadores para valorar la calidad la cantidad de la producción científica** de una persona investigadora¹. No obstante, es relevante para quienes investigamos entender qué miden estos indicadores y cómo lo miden. Así pues, revisémoslos.

## Bases de datos

Para empezar, todo indicador está ligado a una **base de datos** subyacente de publicaciones o de actividad científica. Las más importantes son **Scopus**, que origina el *Scimago Journal & Country Rank (SJR)*; **Web of Science**, vinculada a los *Journal Citation Reports* (JCR); **Medline** y **Scholar** de Google. También veremos que otros indicadores, como [altmetrics, utilizan datos de diferentes fuentes](https://www.altmetric.com/about-us/our-data/our-sources/) como documentos de políticas públicas, redes sociales, Wikipedia, blogs, etc.

[**Scopus**](https://www.scopus.com/home.uri) es la base de datos de pago de *Elsevier*. Cubre una gran variedad de áreas (ciencias, arte, humanidades...) y artículos de revistas científicas. Es, de hecho, la base de datos que indexa más referencias. Además contiene libros, artículos de conferencias y patentes. Calcula índices de impacto como *SJR (Scimago Journal Rank)*, *SNIP (Source Normalized Impact per Paper)* y bibliométricos como el ***índice h***.

[**Web of Science (WoS)**](https://clarivate.com/products/scientific-and-academic-research/research-discovery-and-workflow-solutions/webofscience-platform/) es la versión electrónica del *Science Citation Index* originado en 1955 por el *Institute for Scientific Information (ISI)* y, desde 2016, pertenece a la empresa *Clarivate Analytics*. La licencia española de WoS es gestionada por la *Fundación Española para la Ciencia y la Tecnología (FECYT)*. Como Scopus, cubre una amplia variedad de áreas con publicaciones desde principios del siglo XX. Realiza el cálculo del **factor de impacto** (*Journal Impact Factor (JIF)*, solo para las revistas de ciencias y ciencias sociales) y el JCI (*Journal Citation Indicator*) de las revistas científicas, además de otros índices específicos para disciplinas como ciencias naturales aplicadas y clínicas (SCIE), ciencias sociales (SSCI) o artes y humanidades (SSCI); también tienen índices específicos de libros (BKCI) o de actas de conferencia (CPCI).

[**Medline**](https://www.nlm.nih.gov/bsd/medline.html) es una base de datos creada por la Biblioteca Nacional de Medicina de los Estados Unidos de América. Contiene referencias de unos 26 millones de artículos publicados desde 1946, fundamentalmente en áreas relacionadas con ciencias de la vida. Medline también se conoce como **PubMed**, que es [la interfaz pública](https://www.nlm.nih.gov/bsd/difference.html) que incluye, además de las referencias de *Medline*, artículos de otros campos de estudio. Por último, [**PubMed Central**](https://www.ncbi.nlm.nih.gov/pmc/about/intro/) es un archivo de *Medline* que contiene documentos de texto completo de revistas biomédicas y de ciencias de la vida que se ofrecen de forma gratuita.

[**Scholar**](https://scholar.google.com) es la base de datos de referencias académicas de *Google*. En este caso se trata de una base de datos gratuita y con referencias en una gran variedad de idiomas. Incluye todo tipo de publicaciones, muchas de las cuales no pasan por un proceso de revisión por pares. Además del índice h y el h5*, Scholar calcula el índice i10. 

## Journal Impact Factor (JIF)

El *Journal Impact Factor (JIF)* o factor de impacto es una métrica a nivel de revista. Refleja el número promedio de citas que reciben los artículos de una revista publicados en los últimos dos años. Este indicador se crea en 1975[²] a partir del *Science Citation Index* (SCI) de [Eugene Garfield](https://es.wikipedia.org/wiki/Eugene_Garfield).

El JIF de una revista para un año N se calcula de acuerdo a la siguiente fórmula:
$$ JIF = \frac{\text{Citas en N a N-1 + Citas en N a N-2}}{\#\text{N-1} + \#\text{N-2}},$$
donde:

 - N es la colección de publicaciones en el año actual

 - N-1 y N-2 son las colecciones de publicaciones en el año anterior y el previo respectivamente
 
 - \# es la cardinalidad del conjunto (cantidad de items citables)

A partir de este valor se elabora el ranking JCR. Los **cuartiles** y **percentiles** son medidas estadísticas utilizadas para comparar el impacto de diferentes revistas en un mismo campo. Para calcular los cuartiles de una revista:

 1. Se recopilan los datos de factor de impacto de la revista en cuestión y de las demás revistas de su campo.

 2. Se ordenan las revistas del campo según su factor de impacto, de mayor a menor.

 3. Se divide la lista en cuatro grupos iguales (cuartiles) de acuerdo con el número de revistas en la lista.

Es importante mencionar que el cuartil aplicable es el del año en el que se publica el artículo o el último cuartil disponible si su publicación es reciente.

Desde 2018, WoS calcula también:

 - Versión del JIF que **excluye las autocitas**. Útil, aunque no es la utilizada para elaborar los rankings. Hay que tener en cuenta que las autocitas pueden ser pertinentes. Además, para el caso de malas praxis con autocitas, WoS ya penaliza en el cálculo del JIF a unas pocas decenas de publicaciones por exceso de autocitas.

 - **JIF a cinco años**, calculado con la fórmula adaptada a cinco años en lugar de a dos.

 - ***Inmediacy index***, adaptación de la fórmula del JIF que toma en cuenta únicamente las **citas en el mismo año** de publicación del artículo (en lugar de los dos años anteriores).
 
 - ***Cited half live***, el cálculo de la **media de "edad" de las citas** recibidas, entendiendo por edad la distancia en años entre el año de publicación del artículo y la cita.
 
 - ***Eigenfactor***, que es un cálculo derivado del **JIF a cinco años, sin autocitas y con diferente peso** de cada cita según nivel de la revista citante.

Estas variantes permiten una visión más completa del factor de impacto de una publicación.

## Scimago Journal Rank (SJR)

El SJR también es una métrica de revista. Se calcula utilizando un algoritmo similar al [PageRank de Google](https://es.wikipedia.org/wiki/PageRank) en el que **cada revista se interpreta como un nodo en un grafo**, y el flujo de "prestigio" se distribuye entre estos nodos. De modo iterativo, el algoritmo considera tanto la cantidad de citas recibidas por una revista como el prestigio de las revistas que citan a la revista en cuestión.

En una **primera fase**, se calcula el **prestigio (PSJR2)** de cada revista. Todas parten del mismo valor de prestigio inicial 1/N (donde N es el número de revistas de la base de datos) y se aplica un **algoritmo iterativo**. Cada iteración modifica los valores de prestigio de cada revista de acuerdo con tres criterios: (1) un valor mínimo de prestigio por el simple hecho de estar incluida en la base de datos; (2) un prestigio de la revista dado por el número de documentos incluidos en la base de datos; y (3) un prestigio de citación dado por el número, la «importancia» y la «cercanía» de las citas recibidas de otras revistas.

El PSJR2 calculado en la primera fase es dependiente del tamaño (a mayor tamaño, valores de prestigio más elevados) por lo que no es adecuado para comparaciones entre revistas. En una **segunda fase**, el PSJR2 se divide por la proporción de documentos citables que tiene cada revista en relación con el total para obtener SJR2.

$$ \text{SJR2}_{i} = \frac{\text{PSJR2}_{i}}{(\frac{\text{Art}_{i}}{\sum_{j=1}^{N}{\text{Art}_j}})} $$ 

Donde $\text{Art}_{i}$ es el número de documentos primarios (artículos, reseñas, estudios breves y ponencias) de la revista $i$. Como las proporciones de documentos citables suman 1, este procedimiento compara la "porción del pastel" de prestigio que alcanza una revista, lo que implica una ventaja a la hora de interpretar los valores. Un valor SJR2 = 1 significa que el prestigio por documento es la media. Un valor de 0,8 se interpreta como que se ha alcanzado un 20% menos de prestigio que la media, y un valor de 1,3 corresponde a un 30% más de prestigio que la media.

Este algoritmo se aplica a todas las revistas en la base de datos Scopus en una ventana de citas de tres años y el proceso iterativo se repite hasta que los valores convergen.

Para más información sobre cómo se calcula SJR y una caracterización estadística del mismo, puedes consultar el [artículo de Guerrero-Bote y Moya-Anegón's (2012)](https://www.scimagojr.com/files/SJR2.pdf).

## Índices: *h* y *g*

JIF y SJR2 eran métricas a nivel de revista, sin embargo los índices **h** y **g** son métricas referidas a la **producción e impacto de un investigador** basándose en sus publicaciones y citas.

El [índice **h**](https://es.wikipedia.org/wiki/%C3%8Dndice_h) fue [propuesto por el físico Jorge E. Hirsch en 2005](https://www.pnas.org/doi/full/10.1073/pnas.0507655102). Su valor viene dado por el número máximo $h$ tal que el investigador tiene al menos $h$ publicaciones que han sido citadas al menos $h$ veces.

El [índice **g**](https://en.wikipedia.org/wiki/G-index) fue [propuesto por Leo Egghe en 2006](https://link.springer.com/article/10.1007/s11192-006-0144-7) como una **alternativa al índice h**. Su valor es el mayor número $g$ tal que las $g$ publicaciones más citadas han recibido, conjuntamente, al menos $g^2$ citas. De este modo, considera el número acumulado de citas, dándole más peso a las publicaciones altamente citadas.

Por ejemplo, un investigador que tiene las siguientes publicaciones: Publicación A (19 citas);  Publicación B (8 citas); Publicación C (7 citas); Publicación D (2 citas); Publicación E (1 citas); Publicación F (0 citas). Su **índice h sería 3** (A, B y C han sido publicadas al menos 3 veces), mientras que su **índice g sería 6** (tomando sus 6 publicaciones, acumulan 37 citas y $37\geq6^{2}$).


## Referencias
 - [Citation indexes for science: a new dimension in documentation through association of ideas.](https://academic.oup.com/ije/article/35/5/1123/762383)

 - [A further step forward in measuring journals’ scientific prestige: The SJR2 indicator](https://www.scimagojr.com/files/SJR2.pdf)

 - [An index to quantify an individual's scientific research output](https://www.pnas.org/doi/full/10.1073/pnas.0507655102)

 - [Theory and practise of the g-index](https://link.springer.com/article/10.1007/s11192-006-0144-7)

---
**NOTAS**

1. Si esto empieza a sonarte a cadena de montaje, no eres el primero ni el único.
2. Sobre la evolución del indicador es interesante [este artículo](https://garfield.library.upenn.edu/papers/barcelona2007a.pdf)
