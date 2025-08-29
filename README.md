# Proyecto Web Scraping con Python

**Autor:** Christian Santacruz  
**Materia:** Herramientas Computacionales  

---

## Descripción del proyecto

Este proyecto implementa un script en **Python** utilizando la librería **Selenium** para automatizar la descarga de un archivo Excel desde el portal oficial de [datos.gov.co](https://www.datos.gov.co/).  

El programa abre un navegador de manera controlada, navega hacia el dataset **"Inventario de activos de información de la Subred Sur Occidente 2025"**, y descarga automáticamente el archivo Excel en la carpeta `datasets`.  

De esta forma, se demuestra el uso de Selenium para la interacción con sitios web que requieren clics, navegación y renderizado dinámico de elementos HTML.

---

## Tecnologías utilizadas

- **Python 3.11**  
- **Selenium** (para la automatización del navegador)  
- **Chrome WebDriver** (para controlar Google Chrome)  

---

## Comparativa entre Scrapy y Selenium

A continuación, se presenta un cuadro comparativo entre **Scrapy** y **Selenium**, mencionando al menos 3 ventajas y 3 desventajas de cada herramienta, pero ampliado con más características relevantes:

| Criterio | Scrapy | Selenium |
|----------|--------|----------|
| **Velocidad de scraping** | Muy alta, diseñado para scraping masivo y concurrente. | Baja, depende de abrir un navegador real o simulado. |
| **Manejo de JavaScript** | Limitado; necesita librerías externas como Splash o Playwright. | Excelente, renderiza páginas dinámicas como un usuario real. |
| **Interacción con la página** | Solo extrae datos; no interactúa con botones o formularios. | Puede interactuar con formularios, botones, scroll y eventos. |
| **Escalabilidad** | Muy escalable, soporta crawling de miles de páginas en poco tiempo. | Poco escalable, se vuelve lento y consume muchos recursos con grandes volúmenes. |
| **Consumo de recursos** | Muy bajo, no necesita navegador gráfico. | Alto, requiere levantar navegador (aunque existe el modo headless). |
| **Curva de aprendizaje** | Media a alta; requiere aprender spiders, pipelines y middlewares. | Baja a media; más intuitivo para tareas simples de automatización. |
| **Extracción de datos estructurados** | Muy eficiente; permite exportar directamente a CSV, JSON, XML. | Posible, pero se debe programar manualmente la exportación. |
| **Uso en pruebas de software** | No está diseñado para testing de interfaces. | Muy usado para pruebas funcionales de aplicaciones web. |
| **Manejo de bloqueos** | Fácil de detectar por servidores, requiere proxys y rotación de agentes. | Menos detectable porque simula un usuario real, aunque también puede ser bloqueado. |
| **Instalación y configuración** | Requiere instalación de Scrapy y conocimientos de su arquitectura. | Requiere instalación del WebDriver correspondiente al navegador. |
| **Casos de uso ideales** | Scraping masivo de sitios estáticos o con datos estructurados. | Scraping de sitios dinámicos, descargas automatizadas, pruebas de interfaz. |
| **Limitaciones principales** | No maneja bien páginas con mucho JavaScript. | Lentitud y consumo excesivo de recursos en scraping a gran escala. |

