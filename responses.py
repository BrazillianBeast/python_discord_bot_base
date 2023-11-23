import random

def handle_response(message) -> str:
    processed_message = message.lower()

    if processed_message == 'oi':
        return 'Oi, tudo bem!'
    
    if processed_message == 'role os dados':
        return str(random.randint(1, 6))
    
    if processed_message == '!ajuda':
        return "`Essa é uma mensagem de resposta que você pode modificar.`"
    