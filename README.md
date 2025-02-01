# YAIMG (Yet Another Image Compressor) 📷

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pillow](https://img.shields.io/badge/Pillow-8.0.1%2B-green?style=for-the-badge&logo=python&logoColor=white)](https://pillow.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

**YAIMG** es una herramienta de compresión de imágenes desde la terminal, diseñada para optimizar y redimensionar imágenes de manera eficiente. Soporta formatos comunes como JPEG y PNG, y permite ajustar la calidad, el tamaño y la optimización de las imágenes.

## 🚀 Características principales
- Compresión de imágenes con ajuste de calidad.
- Redimensionamiento de imágenes manteniendo la relación de aspecto.
- Soporte para formatos JPEG y PNG.
- Optimización automática de imágenes.
- Informe detallado del tamaño original y comprimido, junto con la tasa de compresión.

## 🛠 Tecnologías utilizadas
- **Lenguaje:** Python 3.8+
- **Dependencias principales:**
  - Pillow (PIL Fork) para el manejo de imágenes.
  - argparse para el manejo de argumentos de la terminal.

## 📦 Instalación

### Requisitos previos
- Python 3.8 o superior.
- pip (gestor de paquetes de Python).

### Pasos para la instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/ErickinSegura/YAIMG.git
   cd yaimg
   ```

2. **Crear un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Instalar el paquete YAIMG:**
   ```bash
   pip install .
   ```

   Esto instalará YAIMG como un comando global en tu sistema, permitiéndote usarlo desde cualquier lugar en la terminal.


## 🛠 Uso básico

Una vez instalado, puedes usar YAIMG desde la terminal con el siguiente comando:

```bash
yaimg input_image.jpg -o output_image.jpg -q 85 --width 800
```

### Opciones disponibles:
- `input`: Ruta de la imagen de entrada (requerido).
- `-o, --output`: Ruta de la imagen de salida (opcional, por defecto se añade `_compressed` al nombre del archivo).
- `-q, --quality`: Calidad de la imagen (1-100, por defecto 75).
- `-W, --width`: Ancho de la imagen redimensionada (opcional).
- `-H, --height`: Alto de la imagen redimensionada (opcional).
- `--no-optimize`: Deshabilita la optimización de la imagen (opcional).
- `-V, --version`: Muestra la versión de YAIMG.

### Ejemplos de uso:

1. **Comprimir una imagen con calidad personalizada:**
   ```bash
   yaimg foto.jpg -o foto_compressed.jpg -q 90
   ```

2. **Redimensionar una imagen a un ancho específico (manteniendo la relación de aspecto):**
   ```bash
   yaimg foto.jpg --width 1024
   ```

3. **Comprimir una imagen deshabilitando la optimización:**
   ```bash
   yaimg foto.jpg --no-optimize
   ```

4. **Redimensionar una imagen a un alto específico:**
   ```bash
   yaimg foto.jpg --height 768
   ```

## 🤝 Cómo contribuir

¡Las contribuciones son bienvenidas! Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y commitea (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## 🐛 Reportar un problema

Si encuentras algún error o tienes una sugerencia para mejorar YAIMG, sigue estos pasos:

1. **Verifica si ya existe el problema:**  
   Busca en los [issues existentes](https://github.com/ErickinSegura/YAIMG//issues) para evitar duplicados.

2. **Crea un nuevo issue:**  
   Usa la plantilla adecuada:
   - [Reporte de error](https://github.com/ErickinSegura/YAIMG/issues/new?template=bug_report.md)
   - [Solicitud de función](https://github.com/ErickinSegura/YAIMG/issues/new?template=feature_request.md)

3. **Proporciona detalles completos:**
   - Descripción clara del problema.
   - Pasos para reproducirlo.
   - Comportamiento esperado vs actual.
   - Capturas de pantalla (si aplica).
   - Entorno (SO, versión de Python, versión de YAIMG).

**Ejemplo de buen reporte:**
```markdown
## Descripción
Error al redimensionar imágenes PNG.

## Pasos para reproducir
1. Ejecutar `yaimg imagen.png --width 800`
2. Ver error en la consola.

## Comportamiento esperado
La imagen debería redimensionarse correctamente.

## Ambiente
- SO: Ubuntu 20.04
- Python: 3.9.7
- Versión de YAIMG: 1.0.0
```

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](https://github.com/ErickinSegura/YAIMG?tab=MIT-1-ov-file) para más detalles.
