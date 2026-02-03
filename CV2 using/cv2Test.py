import cv2

import cv2Test

# Conecta com a webcam (0 é a câmera padrão)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Redimensiona para o formato que a IA geralmente espera (ex: 224x224)
    ia_input = cv2.resize(frame, (224, 224))

    cv2.imshow('Sua Câmera - Entrada para IA', ia_input)

    # Aperte 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()