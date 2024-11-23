Title: Hojas de referencia
Slug: hojas-referencia
Date: 2024-05-11 20:02
Modified: 2024-11-13 12:57
Category: General
Tags: cheatsheet, referencia
Author: Angel Lareo
Summary: Resumen de hojas de referencia que utilizo en mi día a día: Bash, Git, Conda.

Como ya dije, tengo intención de usar el blog como referencia (con la esperanza de que a alguien más le resulte útil).

Existen muchísimas hojas de referencia, la mayoría probablemente más completas de lo que yo pueda crear aquí. No obstante, puesto que cada uno tenemos nuestras necesidades y preferencias, aquí está es mi selección personalizada de comandos útiles para el día a día (que, probablemente, se irá actualizando).

# bash

## grep

Buscar texto en archivos:
```bash
grep "pattern" file.txt
```

Buscar con contexto (líneas antes y después):
```bash
grep -C 3 "pattern" file.txt
```

Excluir líneas que coinciden con el patrón:
```bash
grep -v "pattern" file.txt
```

Devolver sólo nombres de archivo que contienen el patrón:
```bash
grep -l "pattern" *.txt
```

## find

Buscar archivos por nombre:
```bash
find /path/to/search -name "filename"
```

Buscar archivos por tipo:
```bash
find /path/to/search -type f -name "*.txt"
```

Buscar archivos modificados en los últimos 7 días:
```bash
find /path/to/search -mtime -7
```

## cat

Mostrar el contenido de un archivo:
```bash
cat file.txt
```

Concatenar varios archivos:
```bash
cat file1.txt file2.txt > combined.txt
```

## awk

Añadir una columna a un CSV:
```bash
awk -F, '{print $0",new_column"}' file.csv
```

Eliminar una columna de un CSV:
```bash
awk -F, '{$2=""; print $0}' OFS=, file.csv
```

Sustituir un campo en un CSV:
```bash
awk -F, '{$2="new_value"; print $0}' OFS=, file.csv
```

## head/tail

Mostrar las primeras 10 líneas de un archivo:
```bash
head file.txt
```

Mostrar las últimas 10 líneas de un archivo:
```bash
tail file.txt
```

Mostrar las primeras 20 líneas de un archivo:
```bash
head -n 20 file.txt
```

Mostrar las últimas 20 líneas de un archivo:
```bash
tail -n 20 file.txt
```

## ls

Listar archivos con detalles:
```bash
ls -l
```

Listar archivos ordenados por fecha:
```bash
ls -lt
```

Listar archivos incluyendo archivos ocultos:
```bash
ls -a
```

## pipes

Redirigir la salida de un comando a otro:
```bash
command1 | command2
```

Redirigir la entrada de un archivo a un comando:
```bash
command < inputfile
```

Redirigir la salida de un comando a un archivo (sobrescribir):
```bash
command > outputfile
```

Redirigir la salida de un comando a un archivo (añadir):
```bash
command >> outputfile
```

Redirigir errores a un archivo:
```bash
command 2> errorfile
```

Redirigir salida estándar y errores a un archivo:
```bash
command > outputfile 2>&1
```

Descartar la salida:
```bash
command > /dev/null
```

## Ejemplos compuestos

Buscar archivos .log y contar las líneas que contienen "error":
```bash
find /path/to/search -name "*.log" | xargs grep -c "error"
```

Listar archivos modificados en los últimos 7 días y mostrar las primeras 10 líneas de cada uno:
```bash
find /path/to/search -mtime -7 -type f | xargs head -n 10
```

## Ejemplo de script bash usando IFS

```bash
#!/bin/bash

# Procesar un archivo línea por línea
input="file.txt"
while IFS= read -r line
do
  echo "Processing: $line"
done < "$input"
```


# git

Configuración inicial
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Clonación de repositorios
```bash
git clone <repository_url>
```

Añadir o eliminar del stage (cambios a confirmar)
```bash
git add <file_name>              # Stage a specific file
git add .                        # Stage all changes
git reset <file_name>            # Unstage a specific file
git reset                        # Unstage all changes
```

Mostrar remotos
```bash
git remote -v                    # List remote repositories
```

Confirmar cambios
```bash
git commit -m "Commit message"
```

Push / pull
```bash
git push origin <branch_name>    # Push changes to a remote repository
git pull origin <branch_name>    # Pull changes from a remote repository
```

Deshacer últimos commits (no *pusheados*). El ejemplo se muestra para *1* commit, pero podría hacerse para un número *n*.
```bash
git reset HEAD~1                 # Undo last commit and keep changes staged
git reset HEAD~1 --soft          # Undo last commit and keep changes unstaged
```

Manejo de ramas
```bash
git branch                       # List branches
git branch <branch_name>         # Create a new branch
git checkout <branch_name>       # Switch to a different branch
git merge <branch_name>          # Merge changes from another branch into the current branch
```

Manejo del stash
```bash
git stash                        # Stash changes
git stash pop                    # Apply stashed changes and remove them from the stash
git stash list                   # List stashed changes
git stash apply                  # Apply stashed changes without removing them from the stash
git stash drop                   # Remove a specific stash
git stash clear                  # Remove all stashes
```
 

# conda

Listar environments
```bash
conda info --envs
conda env list
```

Crear enviroments:
```bash
conda create --name <my-env>
conda create -n <my-env>
conda create -n myenv python=3.12
conda env create -f environment.yml
```

Exportar environment a fichero yml:
```bash
conda env export > environment.yml
```

Eliminar environment:
```bash
conda remove --name <my-env> --all
```