# Scrapy settings for population_project

BOT_NAME = "population_project"

SPIDER_MODULES = ["population_project.spiders"]
NEWSPIDER_MODULE = "population_project.spiders"

# Ignorar robots.txt (para que no bloquee la descarga)
ROBOTSTXT_OBEY = False

# User-Agent y headers realistas
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/127.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
    "Accept-Encoding": "gzip, deflate",  # ⚠️ quitamos "br"
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

# Concurrencia y delay para no parecer bot
CONCURRENT_REQUESTS = 4
DOWNLOAD_DELAY = 1

# No usar cookies
COOKIES_ENABLED = False

# Exportación CSV/JSON en UTF-8
FEED_EXPORT_ENCODING = "utf-8"

# Activar rotación de User-Agent (scrapy-user-agents)
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": None,
}

# Opcionales para mejorar scraping
#AUTOTHROTTLE_ENABLED = True
#HTTPCACHE_ENABLED = True
