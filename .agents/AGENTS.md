# Instrucciones para Agentes de IA (.agents/AGENTS.md)

Este repositorio contiene un juego cognitivo simple desarrollado en Python. 

> ⚠️ **REGLA FUNDAMENTAL**: El desarrollador está **aprendiendo Python**. La prioridad absoluta es mantener el código simple, directo, legible y fácil de entender. **NO sobrecomplicar**.

---

## 🎯 Visión y Filosofía del Proyecto
- Minijuegos de agilidad mental y entrenamiento cognitivo en consola.
- Código en nivel básico/principiante (estructuras de control directas: `if`, `while`, `for`, funciones simples).
- Evitar sobreingeniería: NO usar patrones complejos, POO excesiva, programación asíncrona (`asyncio`), hilos (`threading`) ni librerías externas salvo que se pida expresamente.
- Usar funciones de la biblioteca estándar de Python (e.g. `random`, `time`, `msvcrt` en Windows).

## 📁 Estructura del Proyecto
```text
Cognitive-game/
├── .agents/
│   └── AGENTS.md          # Reglas y contexto para modelos de IA
├── src/
│   └── main.py            # Punto de entrada principal y lógica de los juegos
├── requirements.txt       # Dependencias de Python (si aplica)
├── .gitignore             # Archivos y carpetas a ignorar por git
└── README.md              # Documentación general del proyecto
```

## 🛠️ Directrices de Desarrollo
1. **Simplicidad al máximo**: Escribir la solución más corta y clara posible.
2. **Código didáctico y comentado**:
   - Variables y mensajes en español con nombres descriptivos.
   - Comentarios breves y claros explicando conceptos nuevos.
3. **Manejo sencillo de entradas**:
   - Para capturas de teclas directas sin `Enter` en Windows, usar `msvcrt.getwch()`.
4. **Respuestas claras**:
   - Explicar los cambios de manera sencilla, sin tecnicismos innecesarios.

## 🚀 Cómo ejecutar
```bash
python src/main.py
```
