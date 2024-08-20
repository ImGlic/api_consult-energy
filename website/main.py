from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class Fornecedor(BaseModel):
    nome: str
    logo: str
    estado: str
    custo_por_kwh: float
    limite_minimo_kwh: int
    numero_total_clientes: int
    avaliacao_media: float

fornecedores = [
    Fornecedor(nome="Energia Alfa", logo="logo_energia_alfa.png", estado="SP", custo_por_kwh=0.45, limite_minimo_kwh=10000, numero_total_clientes=1200, avaliacao_media=4.6),
    Fornecedor(nome="Beta Power", logo="logo_beta_power.png", estado="RJ", custo_por_kwh=0.42, limite_minimo_kwh=15000, numero_total_clientes=900, avaliacao_media=4.3),
    Fornecedor(nome="Gama Energia", logo="logo_gama_energia.png", estado="MG", custo_por_kwh=0.50, limite_minimo_kwh=20000, numero_total_clientes=600, avaliacao_media=4.0),
    Fornecedor(nome="Delta Power", logo="logo_delta_power.png", estado="RS", custo_por_kwh=0.48, limite_minimo_kwh=25000, numero_total_clientes=800, avaliacao_media=4.5),
    Fornecedor(nome="Epsilon Energia", logo="logo_epsilon_energia.png", estado="PR", custo_por_kwh=0.40, limite_minimo_kwh=12000, numero_total_clientes=1100, avaliacao_media=4.7),
    Fornecedor(nome="Zeta Power", logo="logo_zeta_power.png", estado="SC", custo_por_kwh=0.52, limite_minimo_kwh=30000, numero_total_clientes=500, avaliacao_media=4.2),
    Fornecedor(nome="Theta Energia", logo="logo_theta_energia.png", estado="BA", custo_por_kwh=0.44, limite_minimo_kwh=18000, numero_total_clientes=700, avaliacao_media=4.1),
    Fornecedor(nome="Iota Power", logo="logo_iota_power.png", estado="PE", custo_por_kwh=0.47, limite_minimo_kwh=22000, numero_total_clientes=650, avaliacao_media=4.4),
    Fornecedor(nome="Kappa Energia", logo="logo_kappa_energia.png", estado="CE", custo_por_kwh=0.43, limite_minimo_kwh=14000, numero_total_clientes=1000, avaliacao_media=4.6),
    Fornecedor(nome="Lambda Power", logo="logo_lambda_power.png", estado="GO", custo_por_kwh=0.41, limite_minimo_kwh=13000, numero_total_clientes=850, avaliacao_media=4.8)
]

@app.get("/fornecedores", response_model=List[Fornecedor])
def get_fornecedores(): 
    return fornecedores

@app.post("/fornecedores/consultar")
def escolher_fornecedor(consumo: int):
    return [f for f in fornecedores if consumo >= f.limite_minimo_kwh]


@app.post("/fornecedores/adicionar", response_model=Fornecedor)
def adicionar_fornecedor(fornecedor: Fornecedor):
    for f in fornecedores:
        if f.nome == fornecedor.nome:
            raise HTTPException(status_code=400, detail="Fornecedor já existe")
    
    fornecedores.append(fornecedor)
    return fornecedor

UPLOAD_DIR = os.path.join(os.getcwd(), "assets")
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.post("/upload-logo/")
async def upload_logo(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to save file")

    return {"filename": file.filename}