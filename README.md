![Logo](https://imgur.com/YL4RHxX.png)

# Web Scraping Hiper Libertad

## Objetivo

Desarrollar un crawler para el sitio www.hiperlibertad.com.ar

## Requerimientos Funcionales

El crawler deberá extraer todos los productos disponibles en el sitio mencionado,
específicamente para cada una de las sucursales, para posteriormente almacenarlos en
archivos CSV individuales (uno por sucursal).

Datos a recolectar incluyen, pero no se limitan a:
- Nombre
- Precio regular (es decir, precio de lista o tachado)
- Precio publicado (esto es, precio online o precio promocional)
- Categoría
- SKU (si está disponible)
- URL del producto
- Stock (si está disponible)
- Descripción del producto

Nota importante: Algunos productos pueden no tener dos precios listados. En tales
casos, el único precio existente se debe considerar como el precio publicado.

## Instalación

Pre-requisitos:
- Python: https://www.python.org/downloads/
- Pip (packet manager para Python): https://pip.pypa.io/en/stable/installation/
- Virtualenv:
```bash
  Windows: pip install virtualenv
  Linux: pip3 install virtualenv
```


1) Clonar el proyecto
```bash
  git clone https://github.com/vivascarlosandres/crawler_hiperlibertad.git
```
2) Crear un nuevo Virtual Enviroment "venv" para el proyecto

```bash
  python -m venv venv
```

3) Activar el Virtual Enviroment

```bash
  Windows: .\venv\Scripts\Activate.ps1
  Linux: source venv/bin/activate
```

4) Instalar Scrapy utilizando Pip:

```bash
  pip install scrapy
```

<h3>Sucursales</h3>

CÓRDOBA - Hipermercado Lugones = 1<br>
CÓRDOBA - Hipermercado Rivera = 2<br>
CÓRDOBA - Hipermercado Jacinto Rios = 3<br>
CÓRDOBA - Hipermercado Ruta 9 = 4<br>
MENDOZA - Hipermercado Godoy Cruz = 6<br>
MISIONES - Hipermercado Posadas = 7<br>
TUCUMÁN - Hipermercado Tucumán 1 = 8<br>
TUCUMÁN - Hipermercado Tucumán 2 = 9<br>
CHACO - Hipermercado Chaco = 10<br>
SANTA FÉ - Hipermercado Rosario = 11<br>
SGO DEL ESTERO - Hipermercado Sgo del Estero = 12<br>
SAN JUAN - Hipermercado San Juan = 13<br>
SALTA - Hipermercado Salta = 14<br>
SANTA FÉ - Hipermercado Rafaela = 15<br>
MENDOZA - Tienda Digital Mza Capital = 16
