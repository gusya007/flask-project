from flask import Flask, request, render_template, send_file
from PIL import Image, ImageEnhance
import io
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получение файла и интенсивности
        file = request.files["image"]
        intensity = float(request.form.get("intensity", 1.0))
        
        # Открытие изображения и изменение интенсивности
        image = Image.open(file)
        enhancer = ImageEnhance.Color(image)
        enhanced_image = enhancer.enhance(intensity)

        # Построение графиков распределения цветов
        original_plot = "static/original_plot.png"
        enhanced_plot = "static/enhanced_plot.png"
        plot_color_distribution(image, original_plot)
        plot_color_distribution(enhanced_image, enhanced_plot)

        # Сохранение нового изображения в буфер
        output = io.BytesIO()
        enhanced_image.save(output, format="JPEG")
        output.seek(0)

        return render_template("result.html", enhanced_image=output, original_plot=original_plot, enhanced_plot=enhanced_plot)
    return render_template("index.html")

def plot_color_distribution(image, filename):
    arr = np.array(image)
    colors = ["Red", "Green", "Blue"]
    for i, color in enumerate(colors):
        plt.hist(arr[:, :, i].flatten(), bins=256, color=color.lower(), alpha=0.6, label=color)
    plt.legend()
    plt.savefig(filename)
    plt.close()
