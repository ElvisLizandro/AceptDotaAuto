import pyautogui
import time
import winsound

print("🔍 Modo escucha activo... Buscando partida")

ultimo_estado = ""

while True:
    try:
        button = pyautogui.locateOnScreen(
            'accept.png',
            confidence=0.7
        )

        if button:
            if ultimo_estado != "detectado":
                print("🎯 Botón detectado... verificando")
                ultimo_estado = "detectado"

            # Doble verificación
            time.sleep(0.5)
            button2 = pyautogui.locateOnScreen('accept.png', confidence=0.7)

            if button2:
                print("✅ ¡PARTIDA ENCONTRADA! ACEPTANDO...")
                winsound.Beep(1000, 300)
                pyautogui.click(button2)

                time.sleep(5)  # evita múltiples clics
                ultimo_estado = "esperando"

        else:
            if ultimo_estado != "esperando":
                print("👀 Esperando...")
                ultimo_estado = "esperando"

    except pyautogui.ImageNotFoundException:
        if ultimo_estado != "esperando":
            print("👀 Esperando...")
            ultimo_estado = "esperando"

    except Exception as e:
        print("⚠️ Error real:", e)

    time.sleep(1)