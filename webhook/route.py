from fastapi import APIRouter, Request, Response, Header, HTTPException
from config import VERIFY_TOKEN, logger
from webhook.security import verify_signature
from request.dispatcher import dispatch_message

router = APIRouter()


# GET verification endpoint
@router.get("/webhook")
async def verify(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        logger.info("✅ WEBHOOK_VERIFIED")
        return Response(content=str(challenge), status_code=200)

    return Response(content="❌ verify token mismatch", status_code=403)


# POST webhook endpoint
@router.post("/webhook")
async def receive_data(request: Request, x_hub_signature_256: str = Header(None)):
    body = await request.body()

    # Validar firma
    if not x_hub_signature_256:
        raise HTTPException(status_code=400, detail="Missing signature header")
    verify_signature(body, x_hub_signature_256)

    # Parsear JSON completo
    try:
        raw_data = await request.json()
    except Exception as e:
        logger.error(f"❌ Error parsing JSON: {e}")
        raise HTTPException(status_code=400, detail="Invalid JSON")

    logger.info(f"📨 Webhook received (RAW): {raw_data}")

    # Pasar todo raw_data al dispatcher
    parsed_data = dispatch_message(raw_data)

    return {"raw": raw_data, "parsed": parsed_data}
