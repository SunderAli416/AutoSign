
# PDF to Image Viewer and Formatter

This repository offers a comprehensive solution for converting PDFs into images, annotating these images with bounding boxes, saving the annotations, and finally applying formatting based on the annotations. The solution is provided through two main components: a GUI application (`label_gui.ipynb`) and a command-line script (`script.py`).

### Table of Contents

1. [Dependencies](#dependencies)
2. [`label_gui.ipynb`](#label_guiipynb)
    - [Purpose](#purpose)
    - [Code Structure](#code-structure)
    - [Usage Instructions](#usage-instructions)
3. [`script.py`](#scriptpy)
    - [Purpose](#purpose-1)
    - [Code Structure](#code-structure-1)
    - [Usage Instructions](#usage-instructions-1)
    - [Parameter Guide](#parameter-guide)

---

### Dependencies

1. `tkinter` - For the GUI interface.
2. `pdf2image` - To convert PDFs to images.
3. `PIL` (from `Pillow` package) - To handle image operations.
4. `json` - To handle JSON files.
5. `os` - For operating system dependent functionality.

Make sure to install these dependencies using pip:

```
pip install tkinter pdf2image Pillow
```

---

### `label_gui.ipynb`

#### Purpose:

- Convert a selected PDF into a sequence of images.
- Draw bounding boxes over these images interactively.
- Label and save these bounding boxes.
- Optionally, apply formatting to these bounding boxes and save the result as separate PDFs.

#### Code Structure:

The notebook primarily defines a `PDFImageApp` class that handles the GUI interactions:

1. `__init__`: Initializes the GUI components.
2. Event handlers like `start_draw_bbox`, `dragging`, and `end_draw_bbox` to handle bounding box drawing.
3. `save_data`: Save images and bounding boxes.
4. `apply_formatting`: Apply the formatting based on a JSON file.
5. Navigation functions like `prev_image` and `next_image`.
6. `upload_pdf`: To upload and display a PDF.
7. `display_image`: To display a particular image from the list.

#### Usage Instructions:

1. Run the `label_gui.ipynb` notebook.
2. Use the "Upload PDF" button to select and display a PDF.
3. Navigate through the images using the provided navigation buttons.
4. Draw bounding boxes using the mouse and label them.
5. Save the annotated images and their metadata using the "Save" button.
6. Optionally, apply formatting with the "Apply Formatting" button after uploading a formatting JSON.

---

### `script.py`

#### Purpose:

- Format a series of images based on bounding box annotations and style instructions provided in separate JSON files.
- Save the formatted images as PDFs.

#### Code Structure:

The script consists of a main function `apply_formatting_to_images` that handles the formatting:

1. Loading bounding box and style data.
2. Iterating over images and applying the styles based on bounding boxes.
3. Saving the modified images as PDFs.

#### Usage Instructions:

Execute the script from your command line or terminal:

```
python script.py <image_dir> <bbox_json_path> <style_json_path> <output_dir>
```

#### Parameter Guide:

- `image_dir`: Path to the directory containing images to be formatted.
- `bbox_json_path`: Path to the JSON file containing bounding box annotations.
- `style_json_path`: Path to the JSON file detailing the styles to be applied.
- `output_dir`: Directory where the resulting formatted PDFs will be stored.

---

