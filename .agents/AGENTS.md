# Instrucciones para Agentes de IA (.agents/AGENTS.md)

Este repositorio contiene un juego cognitivo simple desarrollado en Python. La prioridad es mantener el código limpio, fácil de entender y sin complejidad innecesaria.

## 🎯 Visión del Proyecto
- Desarrollar minijuegos de agilidad mental y entrenamiento cognitivo (tiempo de reacción, memoria, cálculo rápido, etc.).
- Mantener la arquitectura simple y directa para facilitar el aprendizaje y la iteración rápida.

## 📁 Estructura del Proyecto
```text
Cognitive-game/
├── .agents/
│   └── AGENTS.md          # Reglas y contexto para modelos de IA
├── src/
│   └── main.py            # Punto de entrada principal y lógica de los juegos
├── .gitignore             # Archivos y carpetas a ignorar por git
└── README.md              # Documentación general del proyecto
```

## 🛠️ Directrices de Desarrollo
1. **Simplicidad**: Evitar sobreingeniería o patrones de diseño innecesariamente complejos.
2. **Código legible**:
   - Nombres de variables y funciones descriptivos en español.
   - Comentarios breves donde la lógica lo requiera.
   - Modularizar los diferentes tipos de juegos o retos dentro de funciones o módulos en `src/`.
3. **Dependencias**: Priorizar el uso de la biblioteca estándar de Python (`time`, `random`, etc.) salvo que se justifique una librería externa.
4. **Manejo de entrada/errores**: Asegurar que las entradas por consola no rompan la ejecución si el usuario ingresa un valor no esperado (e.g. `try-except ValueError` al convertir con `int()`).

## 🚀 Cómo ejecutar
```bash
python src/main.py
```
