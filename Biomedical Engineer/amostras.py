import math

# Número de amostras
N = 100
# Coeficiente do filtro passa-baixa
ALPHA = 0.1

# Simulação de um sinal de ECG com ruído
ecg_raw = []
ecg_filtered = []

# Gerando sinal simulado (ECG + ruído senoidal)
for i in range(N):
    sinal_base = math.sin(2 * math.pi * i / 20.0)   # batimento cardíaco
    ruido = 0.3 * math.sin(2 * math.pi * i / 5.0)   # ruído
    ecg_raw.append(sinal_base + ruido)

# Aplicando filtro passa-baixa simples (exponencial)
ecg_filtered.append(ecg_raw[0])
for i in range(1, N):
    valor_filtrado = ALPHA * ecg_raw[i] + (1 - ALPHA) * ecg_filtered[i-1]
    ecg_filtered.append(valor_filtrado)

# Exibindo resultados
print("Amostra\tECG bruto\tECG filtrado")
for i in range(N):
    print(f"{i}\t{ecg_raw[i]:.3f}\t\t{ecg_filtered[i]:.3f}")