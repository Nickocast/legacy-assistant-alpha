# Proyecto Aurora v0.6.16 alpha (Legacy)

Este repositorio contiene una versión temprana del asistente virtual **A.U.R.O.R.A.**, diseñada como prototipo funcional para pruebas de comandos por voz, interacción contextual y respuestas habladas en español.

> ⚠️ Este proyecto se considera **obsoleto** y ha sido archivado como referencia histórica. Actualmente se encuentra en desarrollo una versión completamente nueva, optimizada y modular del sistema.

---

## 📌 Descripción General

El sistema se basa en el uso de reconocimiento de voz con **VOSK** y generación de voz con **pyttsx3**, junto con módulos personalizados para la obtención de información contextual (hora, fecha, clima, etc.). Su arquitectura fue pensada para correr en segundo plano con bajo consumo de recursos, permitiendo su integración con otros entornos de trabajo o juego.

---

## 🎯 Características Principales

- Activación por nombre ("Aurora") en lenguaje natural.
- Soporte para saludos y agradecimientos con reconocimiento contextual.
- Comandos básicos:
  - Fecha, hora, mes y año actuales.
  - Clima del día y recomendaciones de abrigo.
- Lectura de voz natural con síntesis TTS.
- Soporte modular para futuras expansiones de comandos.
- Monitoreo de uso de memoria RAM durante ejecución.

---

## ⚙️ Tecnologías Utilizadas

- `Python 3.10+`
- [`VOSK`](https://alphacephei.com/vosk/) (Reconocimiento de voz offline)
- `pyttsx3` (Síntesis de voz offline)
- `pyaudio` (Captura de audio del micrófono)
- `psutil` (Monitoreo de recursos)
- API externa de clima (requiere clave API y ciudad configurada)
- Estructura modular personalizada (`modules/`, `commands/`)
