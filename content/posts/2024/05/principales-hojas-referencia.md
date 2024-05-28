Title: Hojas de referencia
Slug: principales-hojas-referencia
Date: 2024-05-11 20:02
Category: General
Tags: cheatsheet, referencia
Author: Angel Lareo
Summary: Algunas hojas de referencia que pueden ayudarte en tu día a día.

Como ya dije, tengo intención de usar el blog como referencia (aunque con la esperanza de que a alguien más le resulte útil).

Existen muchísimas hojas de referencia, la mayoría probablemente más completas de lo que yo pueda crear aquí. No obstante, puesto que cada uno tenemos nuestras necesidades y preferencias, aquí está es mi selección personalizada de comandos útiles para el día a día (que, probablemente, se irá actualizando).

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

# git

Configuración inicial
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Clonación de repositorios
```
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
```
git commit -m "Commit message"
```

Push / pull
```bash
git push origin <branch_name>    # Push changes to a remote repository
git pull origin <branch_name>    # Pull changes from a remote repository
```

Deshacer últimos commits (no *pusheados*). El ejemplo se muestra para *1* commit, pero podría hacerse para un número *n*.
```
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
 

