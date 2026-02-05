import os
import subprocess
import sys

def check_compilation():
    root_dir = os.getcwd()
    modules = ["modulo 1", "modulo 2", "modulo 3"]
    
    print("=========================================")
    print("  VERIFICADOR DE COMPILACIÓN LATEX  ")
    print("=========================================")
    
    has_errors = False
    
    for module in modules:
        print(f"\n[INFO] Verificando: {module}...")
        module_path = os.path.join(root_dir, module)
        
        if not os.path.exists(module_path):
            print(f"[ERROR] La carpeta {module} no existe.")
            has_errors = True
            continue
            
        # Detectar archivo principal .tex
        tex_files = [f for f in os.listdir(module_path) if f.startswith("modulo_") and f.endswith(".tex")]
        if not tex_files:
            print(f"[ERROR] No se encontró archivo modulo_X.tex en {module}")
            has_errors = True
            continue
            
        main_file = tex_files[0]
        print(f"       Archivo principal: {main_file}")
        
        # Ejecutar pdflatex
        # -interaction=nonstopmode: No detenerse en errores para poder capturarlos
        # -halt-on-error: Detenerse fatalmente si hay errores graves (aunque nonstopmode trata de seguir)
        cmd = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", main_file]
        
        try:
            # Limpiar archivos auxiliares antes de compilar para una prueba limpia
            subprocess.run("rm -f *.aux *.log *.out *.toc", shell=True, cwd=module_path, stderr=subprocess.DEVNULL)
            
            # Primera pasada
            subprocess.run(
                cmd,
                cwd=module_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding='utf-8',
                errors='replace',
                text=True
            )
            
            # Segunda pasada para TOC y referencias
            print(f"       Compilando segunda pasada para índices...")
            result = subprocess.run(
                cmd,
                cwd=module_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding='utf-8',
                errors='replace',
                text=True
            )
            
            if result.returncode == 0:
                print(f"[OK] {module} compiló exitosamente.")
            else:
                has_errors = True
                print(f"[FALLO] {module} tuvo errores de compilación (código {result.returncode}).")
                
                # Analizar logs para extraer errores
                print("       --- DETALLES DEL ERROR ---")
                captured_errors = []
                lines = result.stdout.splitlines()
                for i, line in enumerate(lines):
                    if line.startswith("!"):
                        # Capturar la línea del error y un poco de contexto
                        context = lines[i:i+3]
                        captured_errors.extend(context)
                        print(f"       {line}")
                
                if not captured_errors:
                    print("       No se pudieron parsear errores específicos. Revisa el archivo .log.")

        except Exception as e:
            print(f"[FATAL] Error ejecutando pdflatex en {module}: {e}")
            has_errors = True

    print("\n=========================================")
    if has_errors:
        print(" RESUMEN: SE ENCONTRARON ERRORES")
        sys.exit(1)
    else:
        print(" RESUMEN: TODOS LOS MÓDULOS OK")
        sys.exit(0)

if __name__ == "__main__":
    check_compilation()
