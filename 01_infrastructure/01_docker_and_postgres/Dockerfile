# Image docker dasar
FROM python:3.11.7

RUN python3 -m venv /opt/venv

# menjalankan instalasi library pandas di image ini
RUN /opt/venv/bin/pip install pandas

# mengatur direktori kerja di dalam container
WORKDIR /app

# menyalin skrip ke container. Nama pertama adalah file sumber, nama kedua adalah tujuan
COPY pipeline.py pipeline.py

# mendefinisikan apa yang akan dilakukan pertama kali ketika conntainer dijalankan
# dalam contoh ini, akan dijalankan skrip pipeline.py
ENTRYPOINT ("python", "pipeline.py")

# Image docker dasar
FROM python:3.9.1

# menjalankan instalasi library pandas di image ini
RUN pip install pandas

# mengatur direktori kerja di dalam container
WORKDIR /app

# menyalin skrip ke container. Nama pertama adalah file sumber, nama kedua adalah tujuan
COPY pipeline.py pipeline.py

# mendefinisikan apa yang akan dilakukan pertama kali ketika container dijalankan
# dalam contoh ini, kita akan menjalankan skrip pipeline.py
ENTRYPOINT ["python", "pipeline.py"]
