from fastapi import FastAPI
from webhook.route import router as webhook_router

app = FastAPI(title="WhatsApp Cloud API Webhook")

# Include routes
app.include_router(webhook_router)
