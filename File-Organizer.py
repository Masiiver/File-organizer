import os
import shutil
from datetime import datetime

def organize_files(directory, by_year=False):
    if not os.path.exists(directory):
        print("El directorio no existe.")
        return
    
    file_types = {
        'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Audios': ['.mp3', '.wav', '.flac'],
        'Otros': []
    }
    
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                moved = False
                file_year = datetime.fromtimestamp(os.path.getmtime(file_path)).year
                for folder, extensions in file_types.items():
                    if any(file.lower().endswith(ext) for ext in extensions):
                        dest_folder = os.path.join(directory, folder)
                        if by_year:
                            dest_folder = os.path.join(dest_folder, str(file_year))
                        if not os.path.exists(dest_folder):
                            os.makedirs(dest_folder)
                        try:
                            shutil.move(file_path, os.path.join(dest_folder, file))
                            moved = True
                            break
                        except PermissionError:
                            print(f"No se pudo mover {file} por falta de permisos.")
                        except Exception as e:
                            print(f"Error al mover {file}: {e}")
                if not moved:
                    dest_folder = os.path.join(directory, 'Otros')
                    if by_year:
                        dest_folder = os.path.join(dest_folder, str(file_year))
                    if not os.path.exists(dest_folder):
                        os.makedirs(dest_folder)
                    try:
                        shutil.move(file_path, os.path.join(dest_folder, file))
                    except PermissionError:
                        print(f"No se pudo mover {file} por falta de permisos.")
                    except Exception as e:
                        print(f"Error al mover {file}: {e}")
    
    print("Organización completada.")

# Ejemplo de uso
directory = input("Ingrese la ruta del directorio a organizar: ")
by_year = input("¿Desea organizar por año? (s/n): ").strip().lower() == 's'
organize_files(directory, by_year)
