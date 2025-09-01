# WhatsApp Cloud API Webhook + Respuestas Automáticas

Este proyecto implementa un **servidor webhook** para recibir mensajes de WhatsApp mediante la **Cloud API** y responder automáticamente con mensajes de texto (y otros tipos en el futuro).

Está desarrollado en **Python**, utilizando:

- **FastAPI** → para exponer el endpoint webhook donde WhatsApp enviará los mensajes entrantes.
- **aiohttp** → para realizar llamadas asincrónicas a la API de WhatsApp y enviar respuestas.
- **uv** → como gestor de entorno, dependencias y ejecución.

---

## 🚀 Características

- Recepción de mensajes entrantes vía **webhook**.
- Respuesta en **tiempo real** a los usuarios.
- Envío de mensajes de texto simples, con vista previa de enlaces o como respuesta contextual.
- Arquitectura **asíncrona** y escalable con `async`/`await`.
- Preparado para extender con **botones, listas, media y plantillas**.

---

## 📦 Instalación

Clona el repositorio:

```bash
git clone https://github.com/fordez/whatsapp-cloud-api-webhook.git
cd whatsapp-cloud-api-webhook
