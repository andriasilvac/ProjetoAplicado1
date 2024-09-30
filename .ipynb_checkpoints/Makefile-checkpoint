# Nome do projeto
PROJECT_NAME = ProjetoAplicado1

# Caminhos dos diretórios
DATA_DIR = data
SRC_DIR = src
NOTEBOOK_DIR = notebooks
MODEL_DIR = models
REPORT_DIR = reports

# Comando para configurar o ambiente (caso você use um ambiente virtual)
VENV = .venv

# Variável para Python e Jupyter
PYTHON = $(VENV)/bin/python
JUPYTER = $(VENV)/bin/jupyter

# Regras principais
.PHONY: all data notebooks train report clean

# Preparar o ambiente (instalar pacotes necessários)
install:
	pip install -r requirements.txt

# Processar os dados
data:
	$(PYTHON) $(SRC_DIR)/data/make_dataset.py

# Rodar os notebooks
notebooks:
	$(JUPYTER) notebook $(NOTEBOOK_DIR)/01_analise-exploratoria_a1.ipynb

# Treinar o modelo
train:
	$(PYTHON) $(SRC_DIR)/models/train_model.py

# Gerar o relatório final
report:
	$(PYTHON) $(SRC_DIR)/visualization/visualize.py
	$(PYTHON) $(REPORT_DIR)/generate_report.py

# Limpar arquivos temporários
clean:
	rm -rf $(DATA_DIR)/interim $(DATA_DIR)/processed $(MODEL_DIR)/*.pkl $(REPORT_DIR)/figures/*.png
