"""Plantillas de prompting parametrizables (few-shot y chain-of-thought).

`main.py` no arma prompts a mano: llama a una de estas funciones con la
consulta del usuario y obtiene el prompt final ya armado con la técnica
correspondiente. Reemplazá los ejemplos por los de tu propio caso de uso
(consigna 1) antes de entregar.
"""

# --- Ejemplos few-shot de referencia (reemplazar por los del caso de uso propio) ---
EJEMPLOS_FEW_SHOT = [
    {
        "consulta": "¿Qué tipo de vehículo necesito para transportar 6 pallets?",
        "respuesta": "Para una carga de 6 pallets puede utilizarse un vehículo tipo chasis, dependiendo también del peso y volumen de la mercadería.",
    },
    {
        "consulta": "¿Realizan envíos al interior del país?",
        "respuesta": "Sí, la empresa realiza servicios de transporte al interior. Para cotizar el viaje se deben considerar el destino, la distancia, el tipo de vehículo y las características de la carga.",
    },
    {
        "consulta": "¿Qué información necesito para solicitar una cotización?",
        "respuesta": "Para solicitar una cotización se recomienda indicar origen, destino, tipo de mercadería, peso aproximado, volumen, cantidad de pallets y fecha estimada del servicio.",
    },
]

INSTRUCCION_CHAIN_OF_THOUGHT = (
    "Antes de responder, pensá el problema paso a paso en voz alta. "
    "Al final, escribí la respuesta definitiva precedida por 'Respuesta:'."
)

def construir_prompt_few_shot(consulta: str, ejemplos: list[dict] = EJEMPLOS_FEW_SHOT) -> str:
    """Arma un prompt few-shot: muestra pares consulta/respuesta de ejemplo y
    al final agrega la consulta real del usuario sin responder."""
    
    bloques_ejemplo = [
        f"Consulta: {ejemplo['consulta']}\nRespuesta: {ejemplo['respuesta']}"
        for ejemplo in ejemplos
    ]
    
    ejemplos_formateados = "\n\n".join(bloques_ejemplo)

    return (
        "Sos un asistente de atención al cliente de una empresa de logística. "
        "Respondé únicamente con información que pueda deducirse de los ejemplos proporcionados. "
        "Si no contás con información suficiente, indicá que se necesita consultar con la empresa.\n\n"
        f"{ejemplos_formateados}\n\n"
        f"Consulta: {consulta}\n"
        "Respuesta:"
    )


def construir_prompt_chain_of_thought(consulta: str) -> str:
    """Arma un prompt chain-of-thought: le pide al modelo razonar paso a paso
    antes de dar la respuesta final."""
    return f"{INSTRUCCION_CHAIN_OF_THOUGHT}\n\nConsulta: {consulta}"
