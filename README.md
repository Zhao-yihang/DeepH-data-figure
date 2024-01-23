Hello! Here are the results of a training set based on the DeepH method, along with plotting operations. The Excel spreadsheet contains fundamental data for all generated graphene, including Hamiltonian, electrical conductivity, density of states, etc.

The training dataset is automatically obtained through the included Python script. You can refer to get_dataset.py for more details.

---
You can train DeepH models using the existing dataset to reproduce the results of the reference paper.

Firstly, `python get_dataset.py` to get the dataset.

Secondly, edit corresponding config files. It should be set to the path of the downloaded `dataset.graph_dir` and `save_dir` should be set to the path to save your graph file and results file during the training. For grahene, twisted bilayer graphene and twisted bilayer bismuthene, a single MPNN model is used for each dataset. For MoS2, four MPNN models are used. Run

`deeph-train --config ${config_path}`
with '''${config_path}''' replaced by the path of config file for training.

After completing the training, you can find the trained model in save_dir, which can be used to make prediction on new structures by run

`deeph-inference --config ${inference_config_path}`
with `${inference_config_path}` replaced by the path of config file for inference. Please note that the DFT results in this dataset were calculated using OpenMX. This means that if you want to use a model trained on this dataset to calculate properties, you need to use the overlap calculated using OpenMX. The orbital information required for overlap calculations can be found in the paper.

---
This project is a derivative of the DeepH method. If you wish to explore the original method and understand the current status of the original research group, please visit the following website: 
http://deeph-pack.deepmodeling.com/en/latest/
or
https://github.com/mzjb/DeepH-pack

>References:
>H. Li, Z. Wang, N. Zou, M. Ye, R. Xu, X. Gong, W. Duan, Y. Xu. Deep-learning density functional theory Hamiltonian for efficient ab initio electronic-structure calculation. Nat. Comput. Sci. 2, 367–377 (2022).
