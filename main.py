import re
import tkinter as tk
from tkinter import filedialog

from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os
import glob


class ImageTextAdder:
    def __init__(self, master):
        self.master = master
        master.title("批量添加文本到图片")

        # 选择图片
        self.label_image = tk.Label(master, text="选择图片文件:")
        self.label_image.pack()
        self.btn_image = tk.Button(master, text="浏览", command=self.load_image)
        self.btn_image.pack()

        # 显示图像
        self.canvas = tk.Canvas(master, width=500, height=500, bg='white')
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.get_coordinates)

        # 选择文本文件
        self.label_text = tk.Label(master, text="选择文本文件:")
        self.label_text.pack()
        self.btn_text = tk.Button(master, text="浏览", command=self.load_text_file)
        self.btn_text.pack()

        # 设置文本位置
        self.label_position = tk.Label(master, text="设置文本位置 (x, y):")
        self.label_position.pack()
        self.entry_position = tk.Entry(master)
        self.entry_position.pack()

        # 选择字体
        self.label_font = tk.Label(master, text="选择字体:")
        self.label_font.pack()

        # 获取系统字体
        self.font_family = tk.StringVar(master)
        self.font_family.set("Arial")
        self.font_menu = tk.OptionMenu(master, self.font_family, *self.get_system_fonts())
        self.font_menu.pack()

        # 生成图片的按钮
        self.btn_generate = tk.Button(master, text="生成图片", command=self.generate_images)
        self.btn_generate.pack()

        self.image_path = None
        self.text_file_path = None
        self.image_tk = None
        self.original_image = None
        self.scale_factor = 1.0

    def get_system_fonts(self):
        """从 C:\Windows\Fonts 目录获取字体文件"""
        font_files = glob.glob(r"C:\Windows\Fonts\*.ttf") + glob.glob(r"C:\Windows\Fonts\*.otf") + \
                     glob.glob(r"C:\Windows\Fonts\*.TFF") + glob.glob(r"C:\Windows\Fonts\*.OTF")
        font_names = [os.path.basename(font_file) for font_file in font_files]  # 获取文件名，不带扩展名

        def custom_sort(font_name):
            # 检查字体名称是否包含中文字符
            if re.search(r'[\u4e00-\u9fa5]', font_name):
                return (0, font_name)  # 中文名字排在前面
            else:
                return (1, font_name)  # 英文名字排在后面

        # 排序字体名称
        font_names = sorted(font_names, key=custom_sort)

        return font_names

    def load_image(self):
        self.image_path = filedialog.askopenfilename(title="选择图片",
                                                     filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:
            self.show_image()

    def show_image(self):
        """在画布上显示图像并缩放"""
        self.original_image = Image.open(self.image_path)
        self.scale_factor = min(500 / self.original_image.width, 500 / self.original_image.height)  # 计算缩放比例
        new_size = (
            int(self.original_image.width * self.scale_factor), int(self.original_image.height * self.scale_factor))
        image_resized = self.original_image.resize(new_size, Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(image_resized)
        self.canvas.config(width=self.image_tk.width(), height=self.image_tk.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)

    def get_coordinates(self, event):
        """获取鼠标点击的坐标并显示在输入框中"""
        # 计算原始图像坐标
        original_x = int(event.x / self.scale_factor)
        original_y = int(event.y / self.scale_factor)
        self.entry_position.delete(0, tk.END)
        self.entry_position.insert(0, f"{original_x}, {original_y}")

    def load_text_file(self):
        self.text_file_path = filedialog.askopenfilename(title="选择文本文件", filetypes=[("Text files", "*.txt")])

    def generate_images(self):
        if not self.image_path or not self.text_file_path:
            messagebox.showerror("错误", "请先选择图片和文本文件。")
            return

        position = self.entry_position.get()
        try:
            x, y = map(int, position.split(','))
        except ValueError:
            messagebox.showerror("错误", "请正确输入位置 (x, y)。")
            return

        font_name = self.font_family.get()  # 选择字体

        with open(self.text_file_path, 'r', encoding='utf-8') as txt_file:  # 确保读取文件时使用UTF-8编码
            lines = txt_file.readlines()

        output_directory = 'output_images'
        os.makedirs(output_directory, exist_ok=True)

        for i, line in enumerate(lines):
            text = line.strip()
            if text:
                img = self.original_image.copy()  # 仍然使用原始图像进行处理
                draw = ImageDraw.Draw(img)

                # 设置字体
                try:
                    # TODO: 这里可以设置您想要的中文字体文件路径
                    font_size = 60
                    font = ImageFont.truetype(font_name, font_size)
                except IOError:
                    messagebox.showwarning("字体错误", f"无法找到字体: {font_name}. 将使用默认字体.")
                    font = ImageFont.load_default()

                # 使用原始坐标
                draw.text((x, y), text, font=font, fill="black")

                output_path = os.path.join(output_directory, f"output_image_{i + 1}_{text}.png")
                img.save(output_path)

        messagebox.showinfo("完成", f"已生成{len(lines)}张图片，保存在 {output_directory} 文件夹内。")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageTextAdder(root)
    root.mainloop()
