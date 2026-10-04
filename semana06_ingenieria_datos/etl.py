import os
import sys
import pandas as pd
import sqlite3

# Asegurar codificación utf-8 en consola para compatibilidad universal en Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_etl():
    """
    Pipeline ETL para la Semana 6: Fundamentos de Ingenieria de Datos.
    Lee ventas.csv, calcula metricas, modela un esquema estrella
    (dim_categoria y fact_ventas) y carga los datos en SQLite (almacen.db).
    """
    # Determinacion de rutas relativas al directorio del script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "ventas.csv")
    db_path = os.path.join(base_dir, "almacen.db")

    print("=" * 65)
    print(">>> INICIANDO PIPELINE ETL - SEMANA 6: INGENIERIA DE DATOS <<<")
    print("=" * 65)

    # ===== 1. EXTRACT: Extraer los datos de la fuente =====
    print("\n[1/3] FASE EXTRACT (Extraccion)")
    df = pd.read_csv(csv_path)
    print(f"-> Datos extraidos exitosamente desde '{csv_path}'")
    print(f"-> Total de filas extraidas: {len(df)}")
    print("\nMuestra de datos crudos (primeras 3 filas):")
    print(df.head(3).to_string(index=False))

    # ===== 2. TRANSFORM: Limpiar y crear una feature nueva =====
    print("\n[2/3] FASE TRANSFORM (Transformacion y Modelado Dimensional)")
    # Nueva feature: ingreso total por venta
    df["total"] = df["precio"] * df["cantidad"]
    print("-> Feature creada: 'total' = precio * cantidad")

    # Modelado dimensional: Esquema Estrella
    # 2.1 Tabla de Dimension: dim_categoria
    categorias_unicas = sorted(df["categoria"].unique())
    dim_categoria = pd.DataFrame({"categoria": categorias_unicas})
    dim_categoria["cat_id"] = range(1, len(dim_categoria) + 1)
    dim_categoria = dim_categoria[["cat_id", "categoria"]]

    # 2.2 Tabla de Hechos: fact_ventas
    fact = df.merge(dim_categoria, on="categoria")
    fact["venta_id"] = range(1, len(fact) + 1)
    fact_ventas = fact[["venta_id", "producto", "cat_id", "precio", "cantidad", "total"]]

    print(f"-> Dimension generada: 'dim_categoria' ({len(dim_categoria)} categorias)")
    print(dim_categoria.to_string(index=False))
    print(f"\n-> Tabla de hechos generada: 'fact_ventas' ({len(fact_ventas)} registros)")
    print(fact_ventas.head(5).to_string(index=False))

    # ===== 3. LOAD: Cargar a SQLite =====
    print("\n[3/3] FASE LOAD (Carga)")
    conn = sqlite3.connect(db_path)
    dim_categoria.to_sql("dim_categoria", conn, if_exists="replace", index=False)
    fact_ventas.to_sql("fact_ventas", conn, if_exists="replace", index=False)
    print(f"-> Tablas 'dim_categoria' y 'fact_ventas' persistidas exitosamente en '{db_path}'")

    # ===== 4. QUERY ANALITICA: Esquema estrella en accion =====
    print("\n" + "=" * 65)
    print("CONSULTA ANALITICA SQL (JOIN DE HECHOS Y DIMENSION)")
    print("=" * 65)
    query = """
    SELECT 
        d.categoria, 
        COUNT(f.venta_id) AS num_ventas,
        SUM(f.cantidad) AS unidades_vendidas,
        ROUND(AVG(f.precio), 2) AS precio_promedio,
        ROUND(SUM(f.total), 2) AS ingresos_totales
    FROM fact_ventas f 
    JOIN dim_categoria d ON f.cat_id = d.cat_id 
    GROUP BY d.categoria 
    ORDER BY ingresos_totales DESC;
    """
    res_df = pd.read_sql(query, conn)
    print(res_df.to_string(index=False))
    print("=" * 65)

    conn.close()
    print(">>> Pipeline ETL completado con exito. <<<\n")
    return res_df

if __name__ == "__main__":
    run_etl()
