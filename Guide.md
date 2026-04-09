# Hướng dẫn chạy dự án N-Puzzle

Dự án này sử dụng ngôn ngữ lập trình **Python** và thư viện đồ họa **Pygame**. Dưới đây là các bước để cài đặt và khởi chạy dự án.

## 1. Yêu cầu hệ thống
- Đã cài đặt **Python 3.10** trở lên (Khuyên dùng 3.13).

## 2. Các bước cài đặt

### Bước 1: Tạo môi trường ảo (Khuyên dùng)
Việc sử dụng môi trường ảo giúp quản lý thư viện tốt hơn và tránh xung đột hệ thống.
```bash
# Tạo môi trường ảo có tên là .venv
python -m venv .venv

# Kích hoạt trên Windows:
.venv\Scripts\activate

# Kích hoạt trên macOS/Linux:
source .venv/bin/activate
```

### Bước 2: Cài đặt các thư viện cần thiết
Sử dụng file `requirements.txt` để cài đặt thư viện Pygame và các phụ trợ khác:
```bash
pip install -r requirements.txt
```

## 3. Chạy dự án
Sau khi đã hoàn tất cài đặt, bạn có thể khởi chạy ứng dụng bằng lệnh:
```bash
python main.py
```

## 4. Cấu trúc dự án sơ bộ
- `main.py`: Entry point, quản lý vòng lặp chính của trò chơi.
- `requirements.txt`: Chứa danh sách các thư viện phụ thuộc.
- `README.md`: Bản đặc tả yêu cầu và kế hoạch dự án.
- `mockup.png` & `wireframe-ui.png`: Tài liệu tham khảo về giao diện.
