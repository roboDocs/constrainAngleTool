import os
from mojo.extensions import ExtensionBundle

basePath      = os.path.dirname(__file__)
sourcePath    = os.path.join(basePath,   'source')
libPath       = os.path.join(sourcePath, 'code')
htmlPath      = os.path.join(sourcePath, 'docs')
resourcesPath = os.path.join(sourcePath, 'resources')
licensePath   = os.path.join(basePath,   'LICENSE')

extensionFile = 'ConstrainAngleTool.roboFontExt'
extensionPath = os.path.join(basePath, extensionFile)

B = ExtensionBundle()
B.name = "ConstrainAngleTool"
B.developer = 'RoboDocs'
B.developerURL = 'http://gitlab.com/robodocs'
B.icon = None # os.path.join(basePath, 'ConstrainAngleToolMechanicIcon.png')
B.version = '0.1'
B.launchAtStartUp = True
B.mainScript = 'constrainAngleTool.py'
B.html = False
B.requiresVersionMajor = '3'
B.requiresVersionMinor = '3'
B.addToMenu = []

with open(licensePath) as license:
    B.license = license.read()

print('building extension...', end=' ')
B.save(extensionPath, libPath=libPath, htmlPath=htmlPath, resourcesPath=resourcesPath)
print('done!')

print()
print(B.validationErrors())