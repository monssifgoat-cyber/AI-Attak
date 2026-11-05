FROM python:3.11-slim

# أدوات الأمن
RUN apt-get update && apt-get install -y nmap curl wget git && rm -rf /var/lib/apt/lists/*

# nuclei + httpx
RUN wget -q https://github.com/projectdiscovery/nuclei/releases/download/v3.3.0/nuclei_3.3.0_linux_amd64.zip -O /tmp/n.zip \
 && unzip -o /tmp/n.zip -d /usr/local/bin && rm /tmp/n.zip && chmod +x /usr/local/bin/nuclei
RUN wget -q https://github.com/projectdiscovery/httpx/releases/download/v1.6.0/httpx_1.6.0_linux_amd64.zip -O /tmp/h.zip \
 && unzip -o /tmp/h.zip -d /usr/local/bin && rm /tmp/h.zip && chmod +x /usr/local/bin/httpx
RUN nuclei -update-templates

# sqlmap
RUN git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git /opt/sqlmap \
 && ln -s /opt/sqlmap/sqlmap.py /usr/local/bin/sqlmap && chmod +x /usr/local/bin/sqlmap

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "main.py"]
