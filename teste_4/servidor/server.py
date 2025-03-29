from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

csv_file = "../../teste_3/data/Relatorio_cadop.csv"
df = pd.read_csv(csv_file, encoding="utf-8", dtype=str, sep=";")


@app.get("/buscar-operadoras/")
async def buscar_operadoras(termo: str = Query(..., description="Termo de busca")):
    """
    Busca operadoras de saúde pelo termo informado.
    A busca considera Razão Social, Nome Fantasia e Modalidade.
    """
    termo = termo.lower()

    resultados = df[
        df[['Razao_Social', 'Nome_Fantasia', 'Modalidade']]
        .apply(lambda x: x.str.lower().str.contains(termo, na=False, regex=False))
        .any(axis=1)
    ]

    resultados = resultados.fillna('')

    # Converter para JSON e retornar os primeiros 10 registros mais relevantes
    return resultados.head(10).to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
