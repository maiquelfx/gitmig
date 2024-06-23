import os
import zipfile

# Obtém o diretório onde o script está localizado
script_dir = os.path.dirname(os.path.abspath(__file__))
# Obtém o nome do diretório (pasta)
folder_name = os.path.basename(script_dir)
# Define o nome do arquivo ZIP
zip_filename = f"{folder_name}.zip"

# Cria um arquivo ZIP
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    # Itera por todos os arquivos no diretório
    for root, _, files in os.walk(script_dir):
        for file in files:
            # Evita adicionar o próprio script ou o arquivo ZIP ao ZIP
            if file != os.path.basename(__file__) and file != zip_filename:
                # Adiciona cada arquivo ao ZIP
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file), script_dir))

print(f"Arquivo ZIP '{zip_filename}' criado com sucesso!")
