### 🔧 Sobre `command_level`

Actualmente, el sistema maneja un único nivel de comandos (`normal`), pero la variable `command_level` está diseñada como punto de extensión futura.

Esta arquitectura anticipa posibles modos como:
- Comandos administrativos.
- Modo de depuración o mantenimiento.
- Control remoto seguro.

Aunque por ahora solo se usa "Aurora" como nombre de activación, el sistema está preparado para escalar sin refactorización profunda.
