import os


folder_structure = {}
folder_structure['.'] = ['00_LIB', '01_SHOT', '02_PUBLISH']
folder_structure['.\\00_LIB'] = ['00_CHARA', '01_ENVIRO']
folder_structure['.\\00_LIB\\00_CHARA'] = ['00_SPHERE', '01_CUBE', '02_CYLINDER']
folder_structure['.\\00_LIB\\00_CHARA\\00_SPHERE'] = ['00_MODE', '01_RIG', '02_TEXTURING', '03_GROOM']
folder_structure['.\\00_LIB\\00_CHARA\\01_CUBE'] = ['00_MODE', '01_RIG', '02_TEXTURING', '03_GROOM']
folder_structure['.\\00_LIB\\00_CHARA\\02_CYLINDER'] = ['00_MODE', '01_RIG', '02_TEXTURING', '03_GROOM']
folder_structure['.\\01_SHOT'] = ['S110']
folder_structure['.\\01_SHOT\\S110'] = ['S110P110', 'S110P120', 'S110P130']
folder_structure['.\\01_SHOT\\S110\\S110P110'] = ['ANIM', 'LIGHTING_RENDERING']
folder_structure['.\\01_SHOT\\S110\\S110P120'] = ['ANIM', 'LIGHTING_RENDERING']
folder_structure['.\\01_SHOT\\S110\\S110P130'] = ['ANIM', 'LIGHTING_RENDERING']
folder_structure['.\\02_PUBLISH'] = ['00_CHARA', 'S110']
folder_structure['.\\02_PUBLISH\\00_CHARA'] = ['00_SPHERE', '01_CUBE', '02_CYLINDER']
folder_structure['.\\02_PUBLISH\\00_CHARA\\00_SPHERE'] = ['00_MODE', '01_RIG', '02_TEXTURING', '03_GROOM', '04_LOOKDEV']
folder_structure['.\\02_PUBLISH\\00_CHARA\\00_SPHERE\\00_MODE'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\00_SPHERE\\01_RIG'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\00_SPHERE\\02_TEXTURING'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\00_SPHERE\\03_GROOM'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\00_SPHERE\\04_LOOKDEV'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\01_CUBE'] = ['00_MODE', '01_RIG', '02_TEXTURING', '03_GROOM', '04_LOOKDEV']
folder_structure['.\\02_PUBLISH\\00_CHARA\\01_CUBE\\00_MODE'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\01_CUBE\\01_RIG'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\01_CUBE\\02_TEXTURING'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\01_CUBE\\03_GROOM'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\01_CUBE\\04_LOOKDEV'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\02_CYLINDER'] = ['00_MODE', '01_RIG', '02_TEXTURING', '03_GROOM', '04_LOOKDEV']
folder_structure['.\\02_PUBLISH\\00_CHARA\\02_CYLINDER\\00_MODE'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\02_CYLINDER\\01_RIG'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\02_CYLINDER\\02_TEXTURING'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\02_CYLINDER\\03_GROOM'] = ['old']
folder_structure['.\\02_PUBLISH\\00_CHARA\\02_CYLINDER\\04_LOOKDEV'] = ['old']
folder_structure['.\\02_PUBLISH\\S110'] = ['S110P110', 'S110P120', 'S110P130']
folder_structure['.\\02_PUBLISH\\S110\\S110P110'] = ['ANIM', 'LIGHTING_RENDERING']
folder_structure['.\\02_PUBLISH\\S110\\S110P120'] = ['ANIM', 'LIGHTING_RENDERING']
folder_structure['.\\02_PUBLISH\\S110\\S110P130'] = ['ANIM', 'LIGHTING_RENDERING']

def create_folder_structure(folder_map):
 for parent, subfolders in folder_map.items():
  for subfolder in subfolders:
   path = os.path.join(parent, subfolder)
   os.makedirs(path, exist_ok=True)

create_folder_structure(folder_structure)