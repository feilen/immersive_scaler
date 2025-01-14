# (global-set-key (kbd "C-c b") (lambda () (interactive) (shell-command "zip -r ../immersive_scaler.zip ../immersive_scaler")))
#
#

import importlib
importlib.invalidate_caches()

# import immersive_scaler.operations as imops
# import immersive_scaler.ui as imui

from . import operations as imops
from . import ui as imui

# from .operations import ops_register
# from .operations import ops_unregister
# from .ui import ui_register
# from .ui import ui_unregister


bl_info = {
    "name": "Immersive Scaler",
    "category": "3D View",
    'author': 'triazo',
    'version': (0, 2, 7),
    'blender': (2, 81, 0),
    'location': 'View3D',
}

def register():
    print(__name__)
    importlib.reload(imops)
    importlib.reload(imui)
    imui.ui_register()
    imops.ops_register()

def unregister():
    imui.ui_unregister()
    imops.ops_unregister()
