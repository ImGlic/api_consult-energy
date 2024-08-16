from fastapi.testclient import TestClient
from main import app  
import pytest

client = TestClient(app)

def test_get_fornecedores():
    response = client.get("/fornecedores")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    fornecedor = response.json()[0]
    assert "nome" in fornecedor
    assert "logo" in fornecedor
    assert "estado" in fornecedor
    assert "custo_por_kwh" in fornecedor
    assert "limite_minimo_kwh" in fornecedor
    assert "numero_total_clientes" in fornecedor
    assert "avaliacao_media" in fornecedor

def test_escolher_fornecedor():
    response = client.post("/escolha", json={"consumo": 15000})
    assert response.status_code == 200
    fornecedores = response.json()
    assert isinstance(fornecedores, list)
    assert len(fornecedores) > 0
    for fornecedor in fornecedores:
        assert fornecedor["limite_minimo_kwh"] < 15000

    response = client.post("/escolha", json={"consumo": 5000})
    assert response.status_code == 200
    fornecedores = response.json()
    assert isinstance(fornecedores, list)
    assert len(fornecedores) == 0
