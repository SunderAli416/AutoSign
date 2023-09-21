import os
import json
from PIL import Image, ImageDraw, ImageFont
from typing import List, Dict
import argparse

def apply_formatting_to_images(image_dir: str, bbox_json_path: str, style_json_path: str, output_dir: str):

    # Load bounding boxes and styles
    with open(bbox_json_path, 'r') as bbox_file, open(style_json_path, 'r') as style_file:
        bounding_boxes = json.load(bbox_file)
        styles = json.load(style_file)
    
    # List all image files from directory
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort()  # Ensure the images are processed in order
    images = [Image.open(os.path.join(image_dir, img_file)) for img_file in image_files]
    
    # Apply formatting to each image based on bounding boxes and styles
    max_texts = max([len(style['texts']) for style in styles.values()])
    for text_idx in range(max_texts):
        modified_images = [img.copy() for img in images]
        
        for name, bbox_data_list in bounding_boxes["bounding_boxes"].items():
            formatting = styles.get(name, {})
            texts = formatting.get("texts", [])
            if text_idx >= len(texts):
                continue
            text = texts[text_idx]
            
            for bbox_data in bbox_data_list:
                img = modified_images[bbox_data["image_index"]]
                draw = ImageDraw.Draw(img)
                
                # Background Color
                bg_color = formatting.get("background_color")
                draw.rectangle(bbox_data['coords'], fill=bg_color)

                # Font Details
                font_size = formatting["font"]["size"]
                font_color = formatting["font"]["color"]
                font_style = formatting["font"]["style"]

                if font_style == "bold":
                    font = ImageFont.truetype("d:/times new roman bold.ttf", font_size)
                elif font_style == "italic":
                    font = ImageFont.truetype("d:/times new roman italic.ttf", font_size)
                else:  # assuming normal style
                    font = ImageFont.truetype("d:/times new roman.ttf", font_size)
                
                text_x = bbox_data['coords'][0]
                text_y = bbox_data['coords'][1]
                draw.text((text_x, text_y), text, fill=font_color, font=font)

        # Save the modified images to PDF
        pdf_filename = f"modified_{text_idx + 1}.pdf"
        pdf_path = os.path.join(output_dir, pdf_filename)
        modified_images[0].save(pdf_path, save_all=True, append_images=modified_images[1:])






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Apply formatting to images and save as PDFs.')
    
    parser.add_argument('image_dir', type=str, help='Directory containing images.')
    parser.add_argument('bbox_json_path', type=str, help='Path to bounding boxes JSON.')
    parser.add_argument('style_json_path', type=str, help='Path to style JSON.')
    parser.add_argument('output_dir', type=str, help='Output directory to store modified PDFs.')
    
    args = parser.parse_args()
    
    apply_formatting_to_images(args.image_dir, args.bbox_json_path, args.style_json_path, args.output_dir)