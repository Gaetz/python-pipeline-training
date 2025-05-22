import sys, os
import subprocess

def convert_exr_to_tga(exr_file, tga_file):
    """
    Convertit un fichier EXR en TGA en utilisant oiiotool (OpenImageIO)
    """
    if not os.path.isfile(exr_file):
        print(f"Erreur: Le fichier {exr_file} n'existe pas.")
        return False

    filename, extension = os.path.splitext(exr_file)
    if not extension.lower().endswith('.exr'):
        print(f"Erreur: {exr_file} n'est pas un fichier EXR.")
        return False

    try:
        # Construction de la commande oiiotool
        # La commande convertit l'image EXR en TGA avec une conversion de couleur de linéaire à sRGB
        cmd = ['.\\OpenImageIO\\oiiotool.exe', exr_file, '-d', 'uint8', '--colorconvert', 'linear', 'sRGB', '-o', tga_file]
        print(f"Exécution de la commande: {' '.join(cmd)}")
        
        # Exécution de la commande
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
        
        # Vérification du résultat
        if process.returncode == 0:
            print(f"Fichier TGA sauvegardé: {tga_file}")
            return True
        else:
            print(f"Erreur lors de la conversion: {process.stderr}")
            return False
    
    except Exception as e:
        print(f"Erreur lors de la conversion: {e}")
        return False


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python convert_exr_to_tga.py <dossier>")
        sys.exit(1)

    exr_folder = sys.argv[1]
    if not os.path.isdir(exr_folder):
        print(f"Le dossier '{exr_folder}' n'existe pas.")
        sys.exit(1)

    # Vérification que oiiotool est installé
    try:
        subprocess.run(['.\\OpenImageIO\\oiiotool.exe', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    except FileNotFoundError:
        print("Erreur: oiiotool (OpenImageIO) n'est pas installé ou n'est pas dans le PATH.")
        print("Veuillez l'installer: https://openimageio.readthedocs.io/en/latest/oiiotool.html")
        sys.exit(1)

    for filename in os.listdir(exr_folder):
        if filename.lower().endswith('.exr'):
            exr_path = os.path.join(exr_folder, filename)
            basename = os.path.splitext(filename)[0]
            tga_path = os.path.join(exr_folder, basename + '.tga')
            print(f"Conversion de {exr_path} -> {tga_path}")
            convert_exr_to_tga(exr_path, tga_path)
