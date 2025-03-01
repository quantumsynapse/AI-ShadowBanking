import argparse
import torch
import random
import json
import os

# Configuração do CLI
def parse_args():
    parser = argparse.ArgumentParser(description="AI Shadow Banking CLI - Simulador de Fraudes Bancárias")

    parser.add_argument("--train", action="store_true", help="Treina a IA para aprender fraudes bancárias")
    parser.add_argument("--simulate", action="store_true", help="Simula uma fraude bancária")
    parser.add_argument("--evaluate", action="store_true", help="Avalia a precisão do modelo")

    return parser.parse_args()


# Simulador de Fraudes (Gerador de Transações Falsas)
def generate_fraudulent_transaction():
    transaction = {
        "id": random.randint(100000, 999999),
        "amount": round(random.uniform(1000, 100000), 2),
        "account_from": random.randint(1000000, 9999999),
        "account_to": random.randint(1000000, 9999999),
        "timestamp": random.randint(1609459200, 1640995200),  # Data aleatória entre 2021-2022
        "flagged_fraud": 1  # 1 indica fraude, 0 seria transação legítima
    }
    return transaction

def train_model():
    print("[INFO] Treinando modelo de IA para simular fraudes...")
    print("[INFO] Utilizando PyTorch com CUDA:", torch.cuda.is_available())


#Função para avaliar a IA (Placeholder)
def evaluate_model():
    print("[INFO] Avaliando modelo de IA...")
    print("[INFO] Precisão simulada: 95.2%")

# Executando CLI
if __name__ == "__main__":
    args = parse_args()

    if args.train:
        train_model()
    elif args.simulate:
        fraud = generate_fraudulent_transaction()
        print("[SIMULAÇÃO DE FRAUDE DETECTADA]")
        print(json.dumps(fraud, indent=4))
    elif args.evaluate:
        evaluate_model()
    else:
        print("Use --train, --simulate ou --evaluate para rodar o programa.")

