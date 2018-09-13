from cx_Freeze import setup, Executable

base = None    

executables = [Executable("erp.py", base=base)]

packages = ["idna", "requests", "bs4"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "erp",
    options = options,
    version = "1.0",
    description = 'Scrape amounts and status of claimes',
    executables = executables
)