
# https://www.twilio.com/docs/voice/twiml
from twilio.rest import Client

account_sid = "ACa84f56264bcebe74c4930b0a4ac28703"
auth_token = "c85ba4d6bda3948826e150522a5c1eaa"
meu_numero = "+5571996034613"
numero_twilio = "+19547108319"

cliente = Client(account_sid, auth_token)

mensagem = """
<Response>
<Say language="pt-BR">
Ei, Garb, tudo bem? Parece que não trabalha mais, até ligaão está automatizado.+
</Say>
</Response>
"""

ligacao = cliente.calls.create(
    to=meu_numero,
    from_=numero_twilio,
    twiml=mensagem
)
