# BƯỚC 2: IMPORT THƯ VIỆN VÀ CHẠY CODE TRỰC QUAN HÓA

import py3Dmol
from rdkit import Chem
from rdkit.Chem import AllChem
import streamlit as st

# In ra thông báo thành công để xác nhận
st.write("Tất cả thư viện đã được cài đặt và import thành công!")
st.write("---")

# --- Đoạn code trực quan hóa phân tử của em ---
# Bước 1: Tạo đối tượng phân tử từ chuỗi SMILES (ví dụ: Caffeine)
smiles_string = 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C'
mol = Chem.MolFromSmiles(smiles_string)

# Bước 2: Thêm Hydrogens và tạo tọa độ 3D
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol)
AllChem.UFFOptimizeMolecule(mol)

# Bước 3: Chuyển đổi sang định dạng mà py3Dmol có thể đọc
mblock = Chem.MolToMolBlock(mol)

# Bước 4: Tạo viewer và hiển thị phân tử
view = py3Dmol.view(width=600, height=400)
view.addModel(mblock, 'mol')
view.setStyle({'stick':{}})
view.zoomTo()

# Generate the HTML representation of the molecule
html = view._make_html()

# Display the molecule in Streamlit
st.components.v1.html(html, width=600, height=400)

# In ra thông báo thành công
st.write("Phân tử đã được hiển thị thành công ngay bên dưới!")