import argparse
from PIL import Image
import os
import sys
from .__version__ import __version__

def compress_image(input_path, output_path, quality, optimize, width, height):
    try:
        with Image.open(input_path) as img:
            original_width, original_height = img.size

            if width or height:
                if width and height:
                    new_size = (width, height)
                elif width:
                    ratio = width / original_width
                    new_height = int(original_height * ratio)
                    new_size = (width, new_height)
                else:
                    ratio = height / original_height
                    new_width = int(original_width * ratio)
                    new_size = (new_width, height)
                img = img.resize(new_size, Image.Resampling.LANCZOS)

            file_ext = os.path.splitext(output_path)[1].lower()
            if file_ext in ('.png', '.jpg', '.jpeg'):
                format = 'JPEG' if file_ext in ('.jpg', '.jpeg') else 'PNG'
            else:
                format = 'JPEG' 

            if format == 'JPEG' and img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')

            save_kwargs = {
                'format': format,
                'quality': quality,
                'optimize': optimize,
            }
            if format == 'JPEG':
                save_kwargs['progressive'] = True  
            elif format == 'PNG':
                save_kwargs['compress_level'] = 9  

            img.save(output_path, **save_kwargs)

            original_size = os.path.getsize(input_path)
            compressed_size = os.path.getsize(output_path)
            print(f"Original size: {original_size/1024:.2f} KB")
            print(f"Compressed size: {compressed_size/1024:.2f} KB")
            print(f"Compression ratio: {compressed_size/original_size:.1%}")

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="YAIMG - Yet Another Image Compressor",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument('input', help='Input image file path')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-q', '--quality', type=int, 
                        help='Image quality (1-100)', default=75)
    parser.add_argument('-W', '--width', type=int, 
                        help='Resize width (mantiene relación de aspecto)')
    parser.add_argument('-H', '--height', type=int, 
                        help='Resize height')
    parser.add_argument('--no-optimize', action='store_false',
                        dest='optimize',
                        help='Deshabilitar optimización')
    parser.add_argument('-V', '--version', action='version',
                        version=f'%(prog)s {__version__}',
                        help='Muestra la versión de YAIMG')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Archivo de entrada '{args.input}' no encontrado", file=sys.stderr)
        sys.exit(1)
        
    if not 1 <= args.quality <= 100:
        print("Error: La calidad debe estar entre 1 y 100", file=sys.stderr)
        sys.exit(1)
    
    if not args.output:
        base_name, ext = os.path.splitext(args.input)
        args.output = f"{base_name}_compressed.jpg"  

    compress_image(
        input_path=args.input,
        output_path=args.output,
        quality=args.quality,
        optimize=args.optimize,
        width=args.width,
        height=args.height
    )

if __name__ == '__main__':
    main()