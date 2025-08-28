# utils.py

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

def smiles_to_3d_viewer(smiles_string: str, width: int = 400, height: int = 400):
    """
    Chuyển đổi một chuỗi SMILES thành một đối tượng py3Dmol viewer để hiển thị 3D.

    Args:
        smiles_string (str): Chuỗi SMILES của phân tử.
        width (int): Chiều rộng của khung hiển thị.
        height (int): Chiều cao của khung hiển thị.

    Returns:
        py3Dmol.view: Một đối tượng viewer có chứa mô hình 3D của phân tử.
                      Trả về None nếu chuỗi SMILES không hợp lệ.
    """
    try:
        # --- Giai đoạn 2: Xây dựng Lõi Xử lý ---
        
        # 1. Đọc chuỗi SMILES và chuyển thành đối tượng phân tử của RDKit
        mol = Chem.MolFromSmiles(smiles_string)
        if mol is None:
            # Trả về None nếu SMILES không hợp lệ
            return None

        # 2. Thêm các nguyên tử Hydro (quan trọng cho cấu trúc 3D chính xác)
        mol = Chem.AddHs(mol)

        # 3. Tạo ra tọa độ 3D cho các nguyên tử
        AllChem.EmbedMolecule(mol, AllChem.ETKDG())

        # 4. Tối ưu hóa cấu trúc 3D (giúp hình dạng trông "tự nhiên" hơn)
        AllChem.MMFFOptimizeMolecule(mol)

        # 5. Chuyển thông tin phân tử sang định dạng .mol block
        mblock = Chem.MolToMolBlock(mol)
        
        # --- Tạo đối tượng hiển thị ---

        # Khởi tạo viewer của py3Dmol
        viewer = py3Dmol.view(width=width, height=height)

        # Thêm mô hình phân tử từ .mol block vào viewer
        viewer.addModel(mblock, 'mol')

        # Định dạng kiểu hiển thị (ví dụ: 'stick')
        viewer.setStyle({'stick': {}})
        
        # Phóng to để vừa với khung nhìn
        viewer.zoomTo()

        # Trả về đối tượng viewer đã hoàn thiện
        return viewer

    except Exception as e:
        # Bắt các lỗi khác có thể xảy ra và trả về None
        print(f"An error occurred: {e}")
        return None