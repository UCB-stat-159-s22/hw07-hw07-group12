.PHONY: env
env: 
	conda env create -f environment.yml 
	conda activate /home/jovyan/envs/home/jovyan/hw07-hw07-group12/dev_env;python -m ipykernel install --user --name=dev_env

.PHONY : clean
clean :
	rm -f figures/*.png

.PHONY : all
all :
	jupyter execute main.ipynb
	jupyter execute dentate_vignette.ipynb
	jupyter execute dentategyrus_JQ.ipynb