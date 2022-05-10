.PHONY: env
env: 
	conda env create -f environment.yml 
	conda activate /home/jovyan/envs/home/jovyan/hw07-hw07-group12/dev_env;python -m ipykernel install --user --name=dev_env

.PHONY: html
html:
	jupyter-book build .

.PHONY: html-hub
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	cd _build/html
	python -m http.server

.PHONY : clean
clean :
	rm -f figures/*.png

.PHONY : all
all :
	jupyter execute fig1_analysis.ipynb
	jupyter execute fig2_analysis.ipynb
	jupyter execute fig3pt1_analysis.ipynb
	jupyter execute fig3pt2_analysis.ipynb