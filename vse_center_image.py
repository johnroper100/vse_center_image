# Copyright 2017 John Roper
#
# ##### BEGIN GPL LICENSE BLOCK ######
#
# VSE Center Image is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# VSE Center Image is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with VSE Center Image.  If not, see <http://www.gnu.org/licenses/>.
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "VSE Center Image",
    "author": "John Roper",
    "version": (1, 0, 0),
    "blender": (2, 78, 0),
    "location": "Sequencer > Center Image",
    "description": "Center the image of any VSE clip",
    "warning": "",
    "wiki_url": "http://jmroper.com/",
    "tracker_url": "mailto:johnroper100@gmail.com",
    "category": "Sequencer"
}

import bpy
from bpy.types import Operator


class VCICenterImage(Operator):
    """Center the strip image"""
    bl_idname = "scene.vci_center_image"
    bl_label = "Center Image"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        seq = bpy.context.selected_editable_sequences[0]

        if seq.use_translation:
            seq.transform.offset_x = bpy.context.scene.render.resolution_x/2 - seq.strip_elem_from_frame(bpy.context.scene.frame_current).orig_width/2
            seq.transform.offset_y = bpy.context.scene.render.resolution_y/2 - seq.strip_elem_from_frame(bpy.context.scene.frame_current).orig_height/2

        return {'FINISHED'}


def VCI_panel(self, context):
    layout = self.layout
    seq = bpy.context.selected_editable_sequences[0]

    if seq.use_translation:
        layout.operator("scene.vci_center_image", icon="FULLSCREEN_EXIT")


def register():
    bpy.utils.register_class(VCICenterImage)
    bpy.types.SEQUENCER_PT_input.append(VCI_panel)


def unregister():
    bpy.utils.unregister_class(VCICenterImage)
    bpy.types.SEQUENCER_PT_input.remove(VCI_panel)

if __name__ == "__main__":
    register()
