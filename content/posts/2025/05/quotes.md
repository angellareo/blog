Title: CLI-quotes
Slug: CLI-quotes
Date: 2025-05-04 16:32
Category: General
Tags: Citas, Cultura, FLOSS
Author: Angel Lareo
Cover: images/CLI-quotes.png
Summary: Crea tu colección de citas y visualízalas en tu terminal.

Hace tiempo que no subo nada por aquí, así que aprovecho para actualizar con un pequeño proyecto personal. Se trata de [CLI-quotes](https://github.com/angellareo/CLI-quotes?tab=readme-ov-file), una aplicación muy simple para gestionar colecciones de citas que se muestren de manera aleatoria. Yo la he incluido en `.bashrc`, de modo que se muestre una cada vez que lanzo una terminal.

El proyecto está basado en [esta aplicación](https://github.com/pouyakary/bret-victor-quotes) que escrapeaba la [base de datos de citas de Bret Victor](https://worrydream.com/quotes/). El objetivo es utilizar el script de go destinado a mostrarlas, pero sin la funcionalidad de scrapear. El formato de la base de datos sigue siendo JSON como en el proyecto original, pero con algunos campos añadidos.

Viene por defecto con algunas citas (en inglés y español) que pretendo ir ampliando. En algún momento puede que separe la aplicación de la base de datos, pero de momento se distribuyen conjuntamente. 

