# RiverRadar – csak Python stdlib, nincs pip függőség
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    HOST=0.0.0.0 \
    PORT=8080 \
    RIVERRADAR_DB_PATH=/data/riverradar_history.sqlite

RUN useradd --system --uid 10001 --home /app riverradar \
    && mkdir -p /data && chown riverradar /data

WORKDIR /app
COPY --chown=riverradar server.py storage.py ./
COPY --chown=riverradar countries ./countries
COPY --chown=riverradar static ./static
COPY --chown=riverradar certs ./certs

USER riverradar
VOLUME ["/data"]
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
  CMD python -c "import urllib.request,os;urllib.request.urlopen('http://127.0.0.1:%s/api/history/stats' % os.environ.get('PORT','8080'), timeout=4)" || exit 1

CMD ["python", "server.py"]
