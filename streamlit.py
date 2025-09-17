import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors
import shap
import matplotlib.pyplot as plt

# 创建SHAP解释器
explainer = shap.TreeExplainer(model)
# 计算SHAP值（使用训练数据）
shap_values = explainer.shap_values(X_train)

st.title("鲜味肽强度预测器")
seq = st.text_input("输入肽序列（如EE）", "EE")
vina_energy = st.number_input("Vina结合能 (kcal/mol)", value=-7.0)
if st.button("预测"):
    mol = Chem.MolFromSequence(seq)
    features = [[Descriptors.MolLogP(mol), Descriptors.TPSA(mol), Chem.rdmolops.GetFormalCharge(mol),vina_energy]]
    score = model.predict(features)[0]
    st.success(f"预测鲜味强度: {score:.1f}/5.0")

if st.checkbox("显示SHAP解释"):
    fig = plt.figure()
    shap.summary_plot(shap_values, X_train, feature_names=['logP','TPSA','charge','vina_energy'], show=False)
    plt.tight_layout()
    st.pyplot(fig)

from stmol import showmol
import py3Dmol
from rdkit.Chem import AllChem

# 在显示3D结构的部分修改为：
xyzview = py3Dmol.view()
mol = Chem.MolFromSequence(seq)
if mol is not None:
    # 添加构象生成
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.UFFOptimizeMolecule(mol)
    xyzview.addModel(Chem.MolToXYZBlock(mol), 'xyz')
    xyzview.setStyle({'stick':{}})
    showmol(xyzview, height=300, width=400)
else:
    st.error("无法生成肽序列的3D结构")