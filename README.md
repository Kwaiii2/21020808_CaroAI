# 21020808_CaroAI
# Caro AI - Chương trình cờ Caro giữa người và máy

## Giới thiệu

Đây là chương trình cờ Caro do em tự cài đặt cho bài tập giữa kỳ môn Trí tuệ nhân tạo. Chương trình cho phép người chơi đấu với máy tính trên bàn cờ 10x10, trong đó máy tính sử dụng thuật toán Minimax và Alpha-Beta pruning để lựa chọn nước đi. Chương trình chạy trên giao diện console, hiển thị bàn cờ bằng ký tự ASCII.

## Tính năng

- Bàn cờ kích thước 10x10
- Luật chơi Caro chuẩn: 4 quân liên tiếp theo hàng ngang, dọc hoặc chéo là thắng
- Người chơi là X, máy tính là O
- Hai chế độ AI: Minimax và Alpha-Beta pruning
- Hiển thị đầy đủ thông tin sau mỗi nước đi của máy (nước chọn, giá trị đánh giá, độ sâu, số trạng thái đã xét, thời gian chạy)
- Chức năng benchmark so sánh hiệu quả hai thuật toán trên 5 trạng thái bàn cờ khác nhau
- Hàm đánh giá heuristic ưu tiên chặn nước của người chơi
- Các kỹ thuật nâng cao: move ordering, iterative deepening, time budget


## Cách chạy chương trình

### 1. Chạy game (người đấu với máy)

```bash
cd source_code
python main.py
Sau đó chọn chế độ AI:
Nhấn 1 để chơi với Minimax
Nhấn 2 để chơi với Alpha-Beta
Người chơi nhập tọa độ hàng và cột (từ 0 đến 9) để đánh quân X. Máy tính sẽ tự động đánh quân O và hiển thị thông tin chi tiết.
