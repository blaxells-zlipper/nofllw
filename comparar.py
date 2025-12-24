import json

def obtener_seguidores():
    nombres = set()
    try:
        with open('followers_1.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                lista_datos = item.get('string_list_data', [])
                if lista_datos:
                    valor = lista_datos[0].get('value')
                    if valor:
                        nombres.add(valor)
    except FileNotFoundError:
        print("Error: No se encontró followers_1.json")
    return nombres

def obtener_seguidos():
    nombres = set()
    try:
        with open('following.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            items = data.get('relationships_following', [])
            for item in items:
                valor = item.get('title')
                if valor:
                    nombres.add(valor)
    except FileNotFoundError:
        print("Error: No se encontró following.json")
    return nombres

seguidores = obtener_seguidores()
seguidos = obtener_seguidos()

no_me_siguen = seguidos - seguidores

with open('lista_unfollow.txt', 'w', encoding='utf-8') as f:
    for user in sorted(no_me_siguen):
        f.write(f"{user}\n")

print(f"--- Resultados ---")
print(f"Te siguen: {len(seguidores)}")
print(f"Tú sigues a: {len(seguidos)}")
print(f"No te devuelven el follow: {len(no_me_siguen)}")
print(f"Lista generada en 'lista_unfollow.txt'")

if no_me_siguen:
    print(f"\nEjemplos de gente que no te sigue: {list(no_me_siguen)[:5]}")