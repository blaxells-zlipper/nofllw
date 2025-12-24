from instagrapi import Client
import time
import random
import os

# --- CONFIGURACIÓN ---
USERNAME = 'lcnrossini'
PASSWORD = '1998supre'
SESSION_FILE = "session.json"

cl = Client()

# Intentar cargar sesión previa para evitar bloqueos por login
if os.path.exists(SESSION_FILE):
    cl.load_settings(SESSION_FILE)
    print("Sesión cargada desde archivo.")
else:
    print("Iniciando sesión nueva...")
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)

# Cargar la lista
try:
    with open('lista_unfollow.txt', 'r', encoding='utf-8') as f:
        users_to_unfollow = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    print("Error: No se encontró lista_unfollow.txt")
    exit()

print(f"Total de personas a dejar de seguir: {len(users_to_unfollow)}")

# Contador para control
contador = 0

for user in users_to_unfollow:
    try:
        print(f"Procesando a: {user}...")
        
        user_id = cl.user_id_from_username(user)
        
        cl.user_unfollow(user_id)
        
        contador += 1
        print(f"[{contador}] Éxito: Ya no sigues a {user}")
        
        # PAUSA MUY IMPORTANTE
        espera = random.randint(400, 900) # Entre 6 y 15 minutos
        print(f"Esperando {espera} segundos para evitar sospechas...")
        time.sleep(espera)

    except Exception as e:
        print(f"Error con {user}: {e}")
        # Si el error es de "Challenge" o "Login required", mejor parar
        if "login_required" in str(e).lower() or "feedback_required" in str(e).lower():
            print("Instagram detectó actividad sospechosa. Deteniendo el script por seguridad.")
            break
        continue

print("Proceso finalizado o detenido.")