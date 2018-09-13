from cx_Freeze import setup, Executable

base = None    

executables = [Executable("erp.py", base=base)]

packages = ["idna", "requests", "re", "BeautifulSoup", "ctypes"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Claim Status",
    options = options,
    version = "1.0",
    description = 'A python tool to extract Claim amounts and status from Merce erp site',
    executables = executables
)