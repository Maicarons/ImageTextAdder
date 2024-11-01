# ImageTextAdder 批量添加文本到图片工具

## 简介

ImageTextAdder 是一个用于批量在图像上添加文本的简单工具。用户可以选择图像和文本文件，然后将文本添加到图像的指定位置。此工具使用 Python 的 Tkinter 库创建图形用户界面，并使用 Pillow 库处理图像。

## 功能

- 选择要添加文本的图片
- 选择文本文件（每行一个文本）
- 设置文本位置（x, y 坐标）
- 选择字体
- 批量生成新的图片并保存

## 安装

确保您已经安装了 Python 以及以下库：

```bash
pip install Pillow
```

## 使用

1. 启动应用程序。
2. 点击“浏览”按钮选择要添加文本的图片文件。
3. 点击“浏览”按钮选择含有文本的文件（txt 格式）。
4. 点击画布以获取文本的位置（x, y 坐标）。
5. 在下拉菜单中选择您喜欢的字体。
6. 点击“生成图片”按钮以创建新的图像。
7. 在 `output_images` 目录中查看生成的图像。

## 示例

```text
hello
world
ImageTextAdder
```

以上内容将分别添加到图片的指定位置，生成的图像文件将命名为 `output_image_1_hello.png`, `output_image_2_world.png`, 等等。

## 注意事项

- 请确认字体文件存在于您的系统中。
- 文本位置应以逗号分隔的形式输入，例如 `100, 200`。
- 默认保存目录为与程序同级的 `output_images` 文件夹。

---

# ImageTextAdder - A Tool for Batch Adding Text to Images

## Introduction

ImageTextAdder is a simple tool for batch adding text to images. Users can select an image and a text file, and then add the text to specified locations on the image. This tool uses Python's Tkinter library to create a graphical user interface and the Pillow library for image processing.

## Features

- Select an image to add text to
- Select a text file (one line of text per entry)
- Specify text position (x, y coordinates)
- Choose a font
- Batch generate new images and save them

## Installation

Make sure you have Python installed along with the following library:

```bash
pip install Pillow
```

## Usage

1. Launch the application.
2. Click the "Browse" button to select the image file to which you want to add text.
3. Click the "Browse" button to select the text file (in txt format).
4. Click on the canvas to get the position for the text (x, y coordinates).
5. Select your preferred font from the dropdown menu.
6. Click the "Generate Images" button to create the new images.
7. Check for the generated images in the `output_images` directory.

## Example

```text
hello
world
ImageTextAdder
```

The above content will be added to the image at the specified locations, and the generated image files will be named `output_image_1_hello.png`, `output_image_2_world.png`, and so on.

## Notes

- Please make sure the font files exist on your system.
- The text position should be entered in a comma-separated format, such as `100, 200`.
- The default save directory is the `output_images` folder at the same level as the program.
