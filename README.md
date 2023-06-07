![Logo](https://imgur.com/YL4RHxX.png)

# Web Scraping Hiper Libertad

## Índice

1) <a href="https://github.com/vivascarlosandres/crawler_hiperlibertad/tree/main#objetivo">Objetivo</a>
2) <a href="https://github.com/vivascarlosandres/crawler_hiperlibertad/tree/main#requerimientos-funcionales">Requerimientos funcionales</a>
3) <a href="https://github.com/vivascarlosandres/crawler_hiperlibertad/tree/main#instalación">Instalación</a>
4) <a href="https://github.com/vivascarlosandres/crawler_hiperlibertad/tree/main#sucursales">Sucursales</a>
5) <a href="https://github.com/vivascarlosandres/crawler_hiperlibertad/tree/main#ejecución-del-crawler">Ejecución del crawler</a>
6) <a href="https://github.com/vivascarlosandres/crawler_hiperlibertad/tree/main#modificación-de-la-categoría-y-subcategoría">Modificación de la categoría y subcategoría</a>
7) <a href="https://github.com/vivascarlosandres/crawler_hiperlibertad/tree/main#configuración-de-proxies">Configuración de proxies</a>
8) <a href="https://github.com/vivascarlosandres/crawler_hiperlibertad/tree/main#implementación-de-paralelismo-y-recursividad">Implementación de paralelismo y recursividad</a>
9) <a href="https://github.com/vivascarlosandres/crawler_hiperlibertad/tree/main#manejo-de-excepciones">Manejo de excepciones</a>
10) <a href="https://github.com/vivascarlosandres/crawler_hiperlibertad/tree/main#política-de-reintentos">Política de reintentos</a>

## Objetivo

Desarrollar un crawler para el sitio www.hiperlibertad.com.ar

## Requerimientos funcionales

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

## Sucursales

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

## Ejecución del crawler

El código ya viene configurado con una "base_url" de la categoría Hogar > Muebles de Interior a modo de ejemplo.

Para ejecutar el crawler utilizar el siguiente comando

```bash
scrapy crawl hiper -a sc_value=1 -o nombre_sucursal.csv
```
- "sc_value" corresponde al ID de la sucursal. En base a la tabla anterior de "Sucursales" se puede insertar el ID que se desee.
- "nombre_sucursal" es el nombre del archivo csv de salida. Se puede modificar como se desee.

Luego de ejecutado el código, se obtendrá como resultado un archivo csv de los productos de dicha sucursal, para la categoría > subcategoría que se indicó.

## Modificación de la categoría y subcategoría

Para poder utilizar el crawler y extraer los productos de una sucursal en específico para otra Categoría > Subcategoría se deben seguir los siguientes pasos:

1) Ingresar al sitio https://www.hiperlibertad.com.ar/ y elegir una sucursal.
2) En base a la tabla anterior de "Sucursales", se debe copiar el ID correspondiente de acuerdo a la sucursal elegida.
3) Elegir una Categoría > Subcategoría en específico. Por ejemplo: https://www.hiperlibertad.com.ar/hogar/muebles-de-interior
4) Ubicados en dicha página, hacemos click derecho > Inspeccionar. Dentro del inspector nos dirigimos a "Network" > Fetch/XHR > Buscamos la siguiente URL:

![RequestURL](https://i.imgur.com/eVFVTrc.png)

5) Una vez obtenida la URL que necesitamos, podemos modificar la "base_url" de nuestro código.

```Python
class HiperSpider(scrapy.Spider):
    name = "hiper"
    base_url = 'https://www.hiperlibertad.com.ar/api/catalog_system/pub/products/search/almacen/aceitunas-y-encurtidos'
    start_urls = [f'{base_url}?O=OrderByTopSaleDESC&_from=0&_to=23']
    sc_value = '1' # Default value
```

6) Procedemos a ejecutar el código

```bash
scrapy crawl hiper -a sc_value=1 -o nombre_sucursal.csv
```

## Configuración de proxies

Scrapy tiene soporte incorporado para el uso de proxies.
Se puede configurar el uso de los mismos desde el archivo de configuración "settings.py"

```bash
# settings.py

# Agrega los proxies que deseas utilizar en una lista
PROXIES = [
    'http://proxy1.example.com:1234',
    'https://proxy2.example.com:5678',
    # Agrega más proxies si es necesario
]

# Activa el middleware de Scrapy para usar proxies
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
}

# Configura el middleware para seleccionar un proxy aleatorio de la lista en cada solicitud
PROXY_LIST = PROXIES
PROXY_MODE = 0

```

## Implementación de paralelismo y recursividad

Scrapy cuenta con configuraciones que permiten controlar la velocidad y la cantidad de solicitudes que el bot realiza a un sitio web. El objetivo es evitar sobrecargar el servidor web y respetar las políticas de acceso del sitio web.

Se puede configurar el uso de las mismas desde el archivo de configuración "settings.py"

```bash
# settings.py

# Configurar el número máximo de solicitudes simultáneas que se pueden realizar.(default: 16)
CONCURRENT_REQUESTS = 32

# Configurar un retraso en segundos entre las solicitudes al mismo sitio. (default: 0)
DOWNLOAD_DELAY = 3

# Esta opción establece el número máximo de solicitudes simultáneas permitidas por DOMINIO o IP. La configuración "DOWNLOAD_DELAY" solo se aplicará a una sola:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

```

## Manejo de excepciones

En Scrapy, se puede utilizar el método "handle_httpstatus_list" para manejar códigos de estado HTTP específicos y realizar acciones personalizadas en caso de que ocurran. Por ejemplo:

```bash
def handle_httpstatus_list(self, response):
    if response.status == 404:
        self.logger.error(f'URL not found: {response.url}')

```

Se puede utilizar el método "errback" en las solicitudes para capturar y manejar excepciones específicas que ocurran durante la solicitud. Por ejemplo:

```bash
def start_requests(self):
    yield scrapy.Request(url='http://example.com', errback=self.handle_error)

def handle_error(self, failure):
    self.logger.error(f'An error occurred: {repr(failure)}')

```

También, se puede utilizar el middleware "RetryMiddleware" de Scrapy para volver a intentar solicitudes en caso de fallos. Este middleware maneja automáticamente los errores y reintentos según su configuración. Se puede personalizar su comportamiento configurando opciones como RETRY_TIMES y RETRY_HTTP_CODES en el archivo de configuración. Por ejemplo:

```bash
# Archivo settings.py
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]

```

## Política de reintentos

Se puede personalizar la política de reintentos utilizando el middleware "RetryMiddleware" mencionado anteriormente. Se puede ajustar la configuración según las necesidades, como el número máximo de reintentos permitidos (RETRY_TIMES) y los códigos de estado HTTP que deben considerarse para los reintentos (RETRY_HTTP_CODES).

Además, se puede implementar una lógica personalizada en el método "retry" de la spider para decidir si se debe reintentar una solicitud específica en función de la respuesta recibida. Por ejemplo:

```bash
def parse(self, response):
    if response.status == 500:
        # Lógica personalizada para decidir si se debe reintentar o no
        if self.should_retry(response):
            yield response.request.replace(dont_filter=True)
        else:
            self.logger.error('Max retries reached. Skipping request.')
    else:
        # Procesar la respuesta normalmente
        pass

def should_retry(self, response):
    # Lógica personalizada para decidir si se debe reintentar o no
    # Puedes considerar condiciones como el contenido de la respuesta, número de reintentos, etc.
    return True  # O False, dependiendo de tu lógica

```

Implementar el manejo de excepciones y una política de reintentos adecuados en la spider de Scrapy ayudará a mejorar la robustez y tolerancia a fallos de tu bot de web scraping.
