Title: CLI-quotes
Slug: CLI-quotes
Date: 2025-05-04 16:32
Category: General
Tags: Citas, Cultura, FLOSS
Author: Angel Lareo
Cover: images/CLI-quotes.png
Summary: Crea tu colección de citas y visualízalas en tu terminal.

Hace tiempo que no subo nada por aquí, así que aprovecho para actualizar con un pequeño proyecto personal. Se trata de [CLI-quotes](https://github.com/angellareo/CLI-quotes?tab=readme-ov-file), una aplicación muy simple para gestionar colecciones de citas que se muestren de manera aleatoria. Yo la he incluido en `.bashrc`, de modo que se muestra una cita de manera aleatoria cada vez que lanzo una terminal.

El proyecto está basado en [esta aplicación](https://github.com/pouyakary/bret-victor-quotes) que escrapeaba la [base de datos de citas de Bret Victor](https://worrydream.com/quotes/). El objetivo es reutilizar y ampliar la funcionalidad del script de go dedicado a mostrarlas, obviando la funcionalidad de scrapear. El formato de la base de datos sigue siendo un JSON, como en el proyecto original, pero con varios campos extra.

Aunque proyecto del repositorio viene por defecto con algunas citas (en inglés y español) que pretendo ir ampliando, puedes utilizarlo para generar tu propia colección. La base de datos está en la carpeta `quotes-data/$LANG_CODE`.

Un ejemplo de cita es:
```json
{
    "author":      "Cathy O'Neil",
    "authorlink":  "https://es.wikipedia.org/wiki/Cathy_O%27Neil",
    "link":        "https://lab.cccb.org/es/la-autoridad-de-lo-inescrutable-cathy-oneil/",
    "quote":       "Los algoritmos son opiniones incrustadas en lenguaje matemático\n\n",
    "source":      "Weapons of Math Destruction"
}
```

Puede que, en algún momento, separe la aplicación de la base de datos, pero de momento se distribuyen conjuntamente. Está liberado bajo licencia AGPLv3.0. Avisadme si hacéis uso del proyecto ;)

