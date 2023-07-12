import os

folder_path = '/extensions/sd-webui-controlnet'

# Memastikan bahwa folder ada sebelum menghapusnya
if os.path.exists(folder_path):
    # Menghapus folder menggunakan perintah rm
    os.system(f'rm -rf {folder_path}')
    print(f"Folder {folder_path} berhasil dihapus.")
else:
    print(f"Tidak dapat menemukan folder {folder_path}.")
