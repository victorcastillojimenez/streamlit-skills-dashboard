# streamlit-skills-dashboard

Plantilla de arquitectura Streamlit multipágina con dashboard analítico, exportación
a Excel e informes PDF. Los datos son completamente simulados (`numpy.random`, semilla
fija); no requiere base de datos ni credenciales externas.

Desarrollado durante el Curso de Especialización en IA y Big Data — Instituto Nebrija (2026).

## El problema que resuelve

Demuestra cómo estructurar una aplicación Streamlit multipágina con separación clara
de responsabilidades: componentes reutilizables, capa de datos simulados, exportación
a formatos ofimáticos y tests con el framework nativo de Streamlit.
Es una plantilla de referencia; no está conectada a servicios externos ni opera con
datos reales.

## Stack

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.9–3.12 (probado con 3.12.8) |
| Framework web | Streamlit 1.35 |
| Datos y manipulación | pandas 2.2, numpy 1.26 |
| Visualización | Plotly 5.22 |
| Exportación Excel | openpyxl 3.1.5 |
| Exportación PDF | reportlab 4.5.1 |
| Compatibilidad | pyarrow==24.0.0 (pinado para numpy 1.26; lo instala streamlit automáticamente) |
| Tests | pytest >= 7.0, Streamlit AppTest |

## Arquitectura

```
app.py                              → Home (punto de entrada multipágina)
pages/
  1_📊_Dashboard.py                 → KPIs, gráficos de tendencia y tabla filtrable
  2_⚙️_Settings.py                  → Formulario de preferencias de usuario
components/
  login_form.py                     → Componente de formulario de login (demo)
  sidebar.py                        → Barra lateral reutilizable
  filtered_table.py                 → Tabla con búsqueda integrada
utils/
  data_loader.py                    → Generador de datos simulados (4 categorías × 30 días)
  helpers.py                        → Utilidades de formato numérico
generate_excel.py                   → Exporta datos a dashboard_datos.xlsx (openpyxl)
generate_report.py                  → Genera informe_dashboard.pdf (reportlab)
tests/
  test_calcular_media.py            → Tests de lógica pura (pytest)
  test_dashboard.py                 → Tests de UI con Streamlit AppTest
  test_protected_page.py            → Tests del componente login
```

## Cómo ejecutarlo

```bash
# 1. Crear y activar entorno virtual (requiere Python 3.9–3.12)
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS / Linux

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Lanzar la aplicación
streamlit run app.py

# 4. (Opcional) Exportar datos a Excel
python generate_excel.py

# 5. (Opcional) Generar informe PDF
python generate_report.py

# 6. Ejecutar tests (desde la raíz del proyecto)
pytest tests/
# Resultado: 9 passed, 1 xfailed (test_acceso_denegado_sin_login)
# El xfail documenta que Settings no implementa guardia de autenticación
```

La aplicación abre en http://localhost:8501 con tema oscuro configurado
en `.streamlit/config.toml`.

## Qué demuestra este proyecto

- Arquitectura multipágina de Streamlit con componentes reutilizables
- Separación entre capa de datos (simulados), lógica y presentación
- Exportación a Excel con openpyxl y generación de PDFs con reportlab
- Tests de interfaz con el framework nativo `streamlit.testing.v1.AppTest`

## Sobre el código

La estructura de este proyecto fue generada mediante agentes de IA con skills
especializadas (streamlit-bootstrap, streamlit-architect, streamlit-component-builder,
xlsx y pdf). Mi aportación fue definir los requisitos, dirigir el proceso de generación
y revisar el resultado.

## Autor

Victor Castillo Jiménez
