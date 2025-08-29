# Proyecto Web Scraping con Python

**Autor:** Christian Santacruz  
**Materia:** Herramientas Computacionales  

---

## 📌 Descripción del proyecto

Este proyecto implementa un script en **Python** con **Selenium** para automatizar la descarga de un archivo Excel desde el portal oficial de [datos.gov.co](https://www.datos.gov.co/).  

El script abre el navegador, navega hasta el dataset **"Inventario de activos de información de la Subred Sur Occidente 2025"**, y descarga automáticamente el archivo **Excel** en la carpeta `datasets`.

---

## 🚀 Tecnologías utilizadas
- Python 3.11  
- Selenium  
- Chrome WebDriver  

---

## 📑 Comparativa: Scrapy vs Selenium

A continuación se presenta un cuadro comparativo entre **Scrapy** y **Selenium**, destacando al menos **3 ventajas y 3 desventajas de cada herramienta**:

| Herramienta | Ventajas | Desventajas |
|-------------|----------|-------------|
| **Scrapy** | ⚡ **Alta velocidad**: muy eficiente para scraping masivo de múltiples páginas.<br>📂 **Gestión de datos estructurados**: maneja bien HTML, JSON, XML y exporta a CSV/JSON fácilmente.<br>🕷️ **Ideal para crawling a gran escala**: permite recorrer sitios completos con facilidad. | ❌ **Difícil manejo de JavaScript**: no interactúa fácilmente con páginas dinámicas.<br>❌ **Curva de aprendizaje**: requiere configurar spiders, pipelines y middlewares.<br>❌ **Bloqueos frecuentes**: algunos sitios lo detectan y bloquean. |
| **Selenium** | 🖱️ **Interacción real**: permite hacer clic en botones, llenar formularios y desplazarse en la página.<br>🌐 **Soporte para JavaScript**: renderiza el DOM igual que un usuario humano.<br>📥 **Automatización flexible**: útil para descargar archivos, probar interfaces y scraping dinámico. | 🐢 **Lentitud relativa**: mucho más lento que Scrapy al navegar múltiples páginas.<br>💻 **Alto consumo de recursos**: requiere abrir navegador real o en modo headless.<br>🔗 **No óptimo para scraping masivo**: menos eficiente para recorrer sitios muy grandes. |

---

## 📂 Estructura del proyecto

