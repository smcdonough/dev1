from cx_Freeze import setup, Executable #This is once you have cx_Freeze installed

#This fills out some of the specs for the exe, like the actual name of the exe, version, escription, then the executables part calls the Executable module to run on that file.
setup(name='BattleSim', 
      version='1.0', 
      description='Simulates Space Battles', 
      executables = [Executable("BattleSim1.py")])