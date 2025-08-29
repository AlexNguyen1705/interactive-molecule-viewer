# app.py

import streamlit as st
import streamlit.components.v1 as components
from utils import smiles_to_3d_viewer # Import hàm cốt lõi của chúng ta

# --- Thiết lập giao diện trang ---
st.set_page_config(layout="wide")
st.title("🧪 Trình Tương tác, Trực quan hóa Phân tử")

# --- Giao diện người dùng ---

# 1. Ô nhập liệu SMILES
smiles_input = st.text_input(
    label="Nhập chuỗi SMILES:",
    # [ ] Yêu cầu 3: Hiển thị Caffeine làm giá trị mặc định
    value="CN1C=NC2=C1C(=O)N(C(=O)N2C)C" 
)

# 2. Nút bấm để kích hoạt logic
clicked = st.button("Hiển thị Phân tử", type="primary")

# --- Logic kết nối & Xử lý ---

# Chúng ta muốn hiển thị phân tử mặc định ngay khi mở app
# và cũng muốn cập nhật khi người dùng bấm nút.
# Điều kiện `if clicked:` chỉ xử lý khi nút được bấm. 
# Để xử lý cả trường hợp mặc định, chúng ta cần một logic tinh tế hơn.
# Ta sẽ sử dụng Session State của Streamlit để lưu trữ SMILES cuối cùng cần hiển thị.

# Khởi tạo session state nếu chưa có
if 'smiles_to_display' not in st.session_state:
    st.session_state.smiles_to_display = "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"

# Khi người dùng bấm nút, cập nhật SMILES cần hiển thị
if clicked:
    st.session_state.smiles_to_display = smiles_input

# Luôn luôn hiển thị phân tử dựa trên session state
if st.session_state.smiles_to_display:
    st.write(f"Đang hiển thị mô hình 3D cho: `{st.session_state.smiles_to_display}`")
    
    # [ ] Yêu cầu 4: Gọi hàm xử lý cốt lõi
    viewer = smiles_to_3d_viewer(smiles_string=st.session_state.smiles_to_display, width=800, height=600)

    # [ ] Yêu cầu 5: Xử lý lỗi
    if viewer:
        viewer_html = viewer._make_html()
        components.html(viewer_html, height=600, width=800, scrolling=True)
    else:
        # Nếu hàm trả về None, tức là SMILES không hợp lệ
        st.error("Lỗi: Chuỗi SMILES bạn nhập không hợp lệ hoặc không thể tạo mô hình 3D. Vui lòng kiểm tra lại.")