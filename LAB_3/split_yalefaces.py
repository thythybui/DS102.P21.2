
import os
import shutil
from collections import defaultdict

# Đường dẫn thư mục ảnh gốc
data_dir = "yalefaces"
train_dir = "yalefaces_train"
test_dir = "yalefaces_test"

# Tạo thư mục nếu chưa có
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Gom ảnh theo người (subject)
person_images = defaultdict(list)
for fname in os.listdir(data_dir):
    if fname.endswith(".pgm"):
        person_id = fname.split(".")[0]  # ví dụ: subject01
        person_images[person_id].append(fname)

# Chia mỗi người: 5 ảnh đầu cho train, còn lại cho test
for person, files in person_images.items():
    files.sort()  # đảm bảo thứ tự cố định
    for i, fname in enumerate(files):
        src = os.path.join(data_dir, fname)
        dst_dir = train_dir if i < 5 else test_dir
        shutil.copy(src, os.path.join(dst_dir, fname))

print("✅ Đã chia xong tập train/test!")
