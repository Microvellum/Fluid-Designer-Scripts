import bpy
import math
from mv import fd_types, unit, utils

class PANEL_Basic_Cabinet_Options(bpy.types.Panel):
    """Panel to Store all of the Cabinet Options"""
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Basic Cabinet Options"
    bl_category = "Fluid Designer"

    props = None

    def draw_header(self, context):
        layout = self.layout
        layout.label('',icon='BLANK1')

    def draw_column_style_options(self,layout):
        columns_panel_box = layout.box()
        columns_panel_box.label("Columns Options:")
        
        row = columns_panel_box.row(align=True)    
        row.prop(self.props,'expand_column',text="",icon='TRIA_DOWN' if self.props.expand_column else 'TRIA_RIGHT',emboss=False)
        row.label('Columns:')
        row.prop(self.props,'column_category',text="",icon='FILE_FOLDER')
        row.prop(self.props,'column_style',text="")
        row.operator('lm_cabinets.update_column_selection',text="",icon='MAN_TRANS')
        if self.props.expand_column:
            row = columns_panel_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self.props,"column_style",show_labels=True)
        
    def draw_exterior_defaults(self,layout):
        col = layout.column(align=True)
        
        box = col.box()
        box.label("Door & Drawer Defaults:")
        
        row = box.row(align=True)
        row.prop(self.props.exterior_defaults,"inset_door")
        row.prop(self.props.exterior_defaults,"no_pulls")
        
        if not self.props.exterior_defaults.no_pulls:
            box = col.box()
            box.label("Pull Placement:")
            
            row = box.row(align=True)
            row.label("Base Doors:")
            row.prop(self.props.exterior_defaults,"base_pull_location",text="From Top of Door")
            
            row = box.row(align=True)
            row.label("Tall Doors:")
            row.prop(self.props.exterior_defaults,"tall_pull_location",text="From Bottom of Door")
            
            row = box.row(align=True)
            row.label("Upper Doors:")
            row.prop(self.props.exterior_defaults,"upper_pull_location",text="From Bottom of Door")
            
            row = box.row(align=True)
            row.label("Distance From Edge:")
            row.prop(self.props.exterior_defaults,"pull_from_edge",text="")
            
            row = box.row(align=True)
            row.prop(self.props.exterior_defaults,"center_pulls_on_drawers")
    
            if not self.props.exterior_defaults.center_pulls_on_drawers:
                row.prop(self.props.exterior_defaults,"drawer_pull_from_top",text="Distance From Top")
        
        box = col.box()
        box.label("Door & Drawer Reveals:")
        
        if self.props.exterior_defaults.inset_door:
            row = box.row(align=True)
            row.label("Inset Reveals:")
            row.prop(self.props.exterior_defaults,"inset_reveal",text="")
        else:
            row = box.row(align=True)
            row.label("Standard Reveals:")
            row.prop(self.props.exterior_defaults,"left_reveal",text="Left")
            row.prop(self.props.exterior_defaults,"right_reveal",text="Right")
            
            row = box.row(align=True)
            row.label("Base Door Reveals:")
            row.prop(self.props.exterior_defaults,"base_top_reveal",text="Top")
            row.prop(self.props.exterior_defaults,"base_bottom_reveal",text="Bottom")
            
            row = box.row(align=True)
            row.label("Tall Door Reveals:")
            row.prop(self.props.exterior_defaults,"tall_top_reveal",text="Top")
            row.prop(self.props.exterior_defaults,"tall_bottom_reveal",text="Bottom")
            
            row = box.row(align=True)
            row.label("Upper Door Reveals:")
            row.prop(self.props.exterior_defaults,"upper_top_reveal",text="Top")
            row.prop(self.props.exterior_defaults,"upper_bottom_reveal",text="Bottom")
            
        row = box.row(align=True)
        row.label("Vertical Gap:")
        row.prop(self.props.exterior_defaults,"vertical_gap",text="")
    
        row = box.row(align=True)
        row.label("Door To Cabinet Gap:")
        row.prop(self.props.exterior_defaults,"door_to_cabinet_gap",text="")
    
    def draw_cabinet_sizes(self,layout):

        col = layout.column(align=True)

        box = col.box()
        box.label("Standard Frameless Cabinet Sizes:")
        
        row = box.row(align=True)
        row.label("Base:")
        row.prop(self.props.size_defaults,"base_cabinet_height",text="Height")
        row.prop(self.props.size_defaults,"base_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Tall:")
        row.prop(self.props.size_defaults,"tall_cabinet_height",text="Height")
        row.prop(self.props.size_defaults,"tall_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Upper:")
        row.prop(self.props.size_defaults,"upper_cabinet_height",text="Height")
        row.prop(self.props.size_defaults,"upper_cabinet_depth",text="Depth")

        row = box.row(align=True)
        row.label("Sink:")
        row.prop(self.props.size_defaults,"sink_cabinet_height",text="Height")
        row.prop(self.props.size_defaults,"sink_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Suspended:")
        row.prop(self.props.size_defaults,"suspended_cabinet_height",text="Height")
        row.prop(self.props.size_defaults,"suspended_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("1 Door Wide:")
        row.prop(self.props.size_defaults,"width_1_door",text="Width")
        
        row = box.row(align=True)
        row.label("2 Door Wide:")
        row.prop(self.props.size_defaults,"width_2_door",text="Width")
        
        row = box.row(align=True)
        row.label("Drawer Stack Width:")
        row.prop(self.props.size_defaults,"width_drawer",text="Width")
        
        box = col.box()
        box.label("Blind Cabinet Widths:")
        
        row = box.row(align=True)
        row.label('Base:')
        row.prop(self.props.size_defaults,"base_width_blind",text="Width")
        
        row = box.row(align=True)
        row.label('Tall:')
        row.prop(self.props.size_defaults,"tall_width_blind",text="Width")
        
        row = box.row(align=True)
        row.label('Upper:')
        row.prop(self.props.size_defaults,"upper_width_blind",text="Width")
        
        box = col.box()
        box.label("Inside Corner Cabinet Sizes:")
        row = box.row(align=True)
        row.label("Base:")
        row.prop(self.props.size_defaults,"base_inside_corner_size",text="")
        
        row = box.row(align=True)
        row.label("Upper:")
        row.prop(self.props.size_defaults,"upper_inside_corner_size",text="")
        
        box = col.box()
        box.label("Placement:")
        row = box.row(align=True)
        row.label("Height Above Floor:")
        row.prop(self.props.size_defaults,"height_above_floor",text="")
        
        box = col.box()
        box.label("Drawer Heights:")
        row = box.row(align=True)
        row.prop(self.props.size_defaults,"equal_drawer_stack_heights")
        if not self.props.size_defaults.equal_drawer_stack_heights:
            row.prop(self.props.size_defaults,"top_drawer_front_height")
    
    def draw(self, context):
        self.props = context.scene.lm_basic_cabinets
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.prop(self.props,'defaults_tabs',expand=True)
        
        if self.props.defaults_tabs == 'SIZES':
            self.draw_cabinet_sizes(box)
        
        if self.props.defaults_tabs == 'EXTERIOR':
            self.draw_exterior_defaults(box)

#---------PRODUCT: EXTERIOR PROMPTS

class PROMPTS_Door_Prompts(bpy.types.Operator):
    bl_idname = "exteriors.door_prompts"
    bl_label = "Door Prompts" 
    bl_description = "This shows all of the available door options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    door_rotation = bpy.props.FloatProperty(name="Door Rotation",subtype='ANGLE',min=0,max=math.radians(120))
    
    door_swing = bpy.props.EnumProperty(name="Door Swing",items=[('Left Swing',"Left Swing","Left Swing"),
                                                                 ('Right Swing',"Right Swing","Right Swing"),
                                                                 ('Double Door',"Double Door","Double Door")])
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        swing = self.assembly.get_prompt('Swing')
        door_rotation = self.assembly.get_prompt('Door Rotation')
        if swing:
            swing.set_value(self.door_swing)
        if door_rotation:
            door_rotation.set_value(self.door_rotation)
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        return True
        
    def execute(self, context):
        return {'FINISHED'}
        
    def set_default_properties(self):
        swing = self.assembly.get_prompt("Swing")
        door_pull = self.assembly.get_prompt("Door Pull")
        door_rotation = self.assembly.get_prompt("Door Rotation")
        if swing:
            self.door_swing = swing.value()
        if door_rotation:
            self.door_rotation = door_rotation.value()
            
    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = utils.get_bp(obj,'INSERT')
        self.assembly = fd_types.Assembly(obj_insert_bp)
        self.set_default_properties()
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=utils.get_prop_dialog_width(330))
        
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                box = layout.box()
                row = box.row()
                row.label("Open Door")
                row.prop(self,'door_rotation',slider=True,text="")
                row = box.row()
                row.label("Door Swing")
                row.prop(self,'door_swing',text="")

                inset_front = self.assembly.get_prompt('Inset Front')
                
                half_overlay_top = self.assembly.get_prompt('Half Overlay Top')
                half_overlay_bottom = self.assembly.get_prompt('Half Overlay Bottom')
                half_overlay_left = self.assembly.get_prompt('Half Overlay Left')
                half_overlay_right = self.assembly.get_prompt('Half Overlay Right')
                
                inset_reveal = self.assembly.get_prompt('Inset Reveal')
                top_reveal = self.assembly.get_prompt('Top Reveal')
                bottom_reveal = self.assembly.get_prompt('Bottom Reveal')
                left_reveal = self.assembly.get_prompt('Left Reveal')
                right_reveal = self.assembly.get_prompt('Right Reveal')
                
                vertical_gap = self.assembly.get_prompt('Vertical Gap')
                door_gap = self.assembly.get_prompt('Door to Cabinet Gap')
                
                row = box.row()
                row.label("Inset Front")
                row.prop(inset_front,'CheckBoxValue',text="")
                
                if not inset_front.value():
                    box = layout.box()
                    box.label("Half Overlays:")
                    row = box.row()
                    if half_overlay_top:
                        row.prop(half_overlay_top,'CheckBoxValue',text="Top")
                    if half_overlay_bottom:
                        row.prop(half_overlay_bottom,'CheckBoxValue',text="Bottom")
                    if half_overlay_left:
                        row.prop(half_overlay_left,'CheckBoxValue',text="Left")
                    if half_overlay_right:
                        row.prop(half_overlay_right,'CheckBoxValue',text="Right")
                    
                box = layout.box()
                box.label("Reveal and Gaps")
                
                if inset_front.value():
                    box.prop(inset_reveal,'DistanceValue',text="Inset Reveal")
                else:
                    col = box.column(align=True)
                    if top_reveal:
                        col.prop(top_reveal,'DistanceValue',text="Top Reveal")
                    if bottom_reveal:
                        col.prop(bottom_reveal,'DistanceValue',text="Bottom Reveal")
                    if left_reveal:
                        col.prop(left_reveal,'DistanceValue',text="Left Reveal")
                    if right_reveal:
                        col.prop(right_reveal,'DistanceValue',text="Right Reveal")
                 
                if vertical_gap:
                    box.prop(vertical_gap,'DistanceValue',text="Horizontal Gap")
                if door_gap:
                    box.prop(door_gap,'DistanceValue',text="Door To Cabinet Gap")


class PROMPTS_Drawer_Prompts(bpy.types.Operator):
    bl_idname = "exteriors.drawer_prompts"
    bl_label = "Drawer Prompts" 
    bl_description = "This shows all of the available drawer options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    drawer_tabs = bpy.props.EnumProperty(name="Main Tabs",
                                         items=[('DRAWER_FRONTS',"Drawer Fronts",'Set the Drawer Front Heights'),
                                                ('DRAWER_OPTIONS',"Drawer Options",'Set the Drawer Options')],
                                         default = 'DRAWER_FRONTS')
    
    open = bpy.props.FloatProperty(name="Open",min=0,max=100,subtype='PERCENTAGE')
    
    door_swing = bpy.props.EnumProperty(name="Door Swing",items=[('Left Swing',"Left Swing","Left Swing"),
                                                                 ('Right Swing',"Right Swing","Right Swing"),
                                                                 ('Double Door',"Double Door","Double Door")])
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        utils.run_calculators(self.assembly.obj_bp)
        swing = self.assembly.get_prompt('Swing')
        if swing:
            swing.set_value(self.door_swing)
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        return True
        
    def execute(self, context):
        return {'FINISHED'}
        
    def set_default_properties(self):
        pass

    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = utils.get_bp(obj,'INSERT')
        self.assembly = fd_types.Assembly(obj_insert_bp)
        self.set_default_properties()
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=utils.get_prop_dialog_width(330))
    
    def draw_drawer_heights(self,layout):
        top = self.assembly.get_prompt("Top Drawer Height")
        second = self.assembly.get_prompt("Second Drawer Height")
        third = self.assembly.get_prompt("Third Drawer Height")
        bottom = self.assembly.get_prompt("Bottom Drawer Height")
        
        if top:
            row = layout.row()
            row.label("Top Drawer Height:")
            if top.equal:
                row.label(str(unit.meter_to_active_unit(top.DistanceValue)))
                row.prop(top,'equal',text="")
            else:
                row.prop(top,'DistanceValue',text="")
                row.prop(top,'equal',text="")
        
        if second:
            row = layout.row()
            row.label("Second Drawer Height:")
            if second.equal:
                row.label(str(unit.meter_to_active_unit(second.DistanceValue)))
                row.prop(second,'equal',text="")
            else:
                row.prop(second,'DistanceValue',text="")
                row.prop(second,'equal',text="")
        
        if third:
            row = layout.row()
            row.label("Third Drawer Height:")
            if third.equal:
                row.label(str(unit.meter_to_active_unit(third.DistanceValue)))
                row.prop(third,'equal',text="")
            else:
                row.prop(third,'DistanceValue',text="")
                row.prop(third,'equal',text="")
        
        if bottom:
            row = layout.row()
            row.label("Bottom Drawer Height:")
            if bottom.equal:
                row.label(str(unit.meter_to_active_unit(bottom.DistanceValue)))
                row.prop(bottom,'equal',text="")
            else:
                row.prop(bottom,'DistanceValue',text="")
                row.prop(bottom,'equal',text="")
        
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                box = layout.box()
                row = box.row()
                row.prop(self,'drawer_tabs',expand=True)
                if self.drawer_tabs == 'DRAWER_FRONTS':
                    self.draw_drawer_heights(box)
                if self.drawer_tabs == 'DRAWER_OPTIONS':
                    inset_front = self.assembly.get_prompt('Inset Front')
                    open = self.assembly.get_prompt('Open')
                    
                    half_overlay_top = self.assembly.get_prompt('Half Overlay Top')
                    half_overlay_bottom = self.assembly.get_prompt('Half Overlay Bottom')
                    half_overlay_left = self.assembly.get_prompt('Half Overlay Left')
                    half_overlay_right = self.assembly.get_prompt('Half Overlay Right')
                    
                    inset_reveal = self.assembly.get_prompt('Inset Reveal')
                    top_reveal = self.assembly.get_prompt('Top Reveal')
                    bottom_reveal = self.assembly.get_prompt('Bottom Reveal')
                    left_reveal = self.assembly.get_prompt('Left Reveal')
                    right_reveal = self.assembly.get_prompt('Right Reveal')
                    
                    horizontal_gap  = self.assembly.get_prompt('Horizontal Gap')
                    door_gap = self.assembly.get_prompt('Door to Cabinet Gap')
                    
                    row = box.row()
                    row.label("Inset Door")
                    row.prop(inset_front,'CheckBoxValue',text="")
                    
                    row = box.row()
                    row.label("Open")
                    row.prop(open,'PercentageValue',text="")
                    
                    if not inset_front.value():
                        box = layout.box()
                        box.label("Half Overlays:")
                        row = box.row()
                        row.prop(half_overlay_top,'CheckBoxValue',text="Top")
                        row.prop(half_overlay_bottom,'CheckBoxValue',text="Bottom")
                        row.prop(half_overlay_left,'CheckBoxValue',text="Left")
                        row.prop(half_overlay_right,'CheckBoxValue',text="Right")
                        
                    box = layout.box()
                    box.label("Reveal and Gaps")
                    
                    if inset_front.value():
                        box.prop(inset_reveal,'DistanceValue',text="Inset Reveal")
                    else:
                        col = box.column(align=True)
                        col.prop(top_reveal,'DistanceValue',text="Top Reveal")
                        col.prop(bottom_reveal,'DistanceValue',text="Bottom Reveal")
                        col.prop(left_reveal,'DistanceValue',text="Left Reveal")
                        col.prop(right_reveal,'DistanceValue',text="Right Reveal")
                     
                    box.prop(horizontal_gap,'DistanceValue',text="Vertical Gap")
                    box.prop(door_gap,'DistanceValue',text="Door To Cabinet Gap")


class PROMPTS_Hamper_Prompts(bpy.types.Operator):
    bl_idname = "exteriors.hamper_prompts"
    bl_label = "Hamper Prompts" 
    bl_description = "This shows all of the available hamper options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        return {'FINISHED'}
        
    def check(self, context):
        utils.run_calculators(self.assembly.obj_bp)
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        return True

    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = utils.get_bp(obj,'INSERT')
        self.assembly = fd_types.Assembly(obj_insert_bp)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=330)
    
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                open_hamper = self.assembly.get_prompt('Open')
                box = layout.box()
                row = box.row()
                row.prop(open_hamper,'PercentageValue',text="Open")

#---------PRODUCT: INTERIOR PROMPTS

class PROMPTS_Hanging_Rod_Prompts(bpy.types.Operator):
    bl_idname = "interiors.hanging_rod_prompts"
    bl_label = "Hanging Rod Prompts" 
    bl_description = "This shows all of the available hanging rod options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    hanging_rod_type = bpy.props.EnumProperty(name="Hanging Rod Type",items=[('Round',"Round","Round"),
                                                                             ('Oval',"Oval","Oval")])
    
    assembly = None
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        hanging_rod_type = self.assembly.get_prompt("Hanging Rod Type")
        hanging_rod_type.set_value(self.hanging_rod_type) 
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        return True
        
    def execute(self, context):
        return {'FINISHED'}
            
    def set_default_properties(self):
        hanging_rod_type = self.assembly.get_prompt("Hanging Rod Type")
        if hanging_rod_type:
            self.hanging_rod_type = hanging_rod_type.COL_EnumItem[hanging_rod_type.EnumIndex].name
            
    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = utils.get_bp(obj,'INSERT')
        self.assembly = fd_types.Assembly(obj_insert_bp)
        self.set_default_properties()
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=utils.get_prop_dialog_width(330))
        
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                
                hanging_rod_quantity = self.assembly.get_prompt("Hanging Rod Quantity")
                hanging_rod_offset = self.assembly.get_prompt("Hanging Rod Offset")
                
                box = layout.box()
                row = box.row()
                row.label("Hanging Rod Type")
                row.prop(self,'hanging_rod_type',text="")
                row = box.row()
                row.label("Quantity")
                row.prop(hanging_rod_quantity,'QuantityValue',text="")
                row = box.row()
                row.label("Offset")
                row.prop(hanging_rod_offset,'DistanceValue',text="")
        
        
class PROMPTS_Shelf_Prompts(bpy.types.Operator):
    bl_idname = "interiors.shelf_prompt"
    bl_label = "Shelf Prompts" 
    bl_description = "This shows all of the available vertical splitter options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    adj_shelf_qty = bpy.props.IntProperty(name="Adjustable Shelf Quantity",min=0,max=5)
    fix_shelf_qty = bpy.props.IntProperty(name="Fixed Shelf Quantity",min=0,max=5)
    
    adj_shelf_qty_prompt = None
    fix_shelf_qty_prompt = None
    
    assembly = None
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        utils.run_calculators(self.assembly.obj_bp)
        
        if self.adj_shelf_qty_prompt:
            self.adj_shelf_qty_prompt.set_value(self.adj_shelf_qty)
        
        if self.fix_shelf_qty_prompt:
            self.fix_shelf_qty_prompt.set_value(self.fix_shelf_qty)
            
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        
        return True
        
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = utils.get_bp(obj,'INSERT')
        self.assembly = fd_types.Assembly(obj_insert_bp)
        
        self.adj_shelf_qty_prompt = self.assembly.get_prompt("Adj Shelf Qty")
        self.fix_shelf_qty_prompt = self.assembly.get_prompt("Fixed Shelf Qty")

        if self.adj_shelf_qty_prompt:
            self.adj_shelf_qty = self.adj_shelf_qty_prompt.value()
        
        if self.fix_shelf_qty_prompt:
            self.fix_shelf_qty = self.fix_shelf_qty_prompt.value()
        
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=utils.get_prop_dialog_width(330))
        
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                
                if self.adj_shelf_qty_prompt:
                    adj_shelf_setback = self.assembly.get_prompt("Adj Shelf Setback")
                    shelf_angle = self.assembly.get_prompt("Shelf Angle")
                    box = layout.box()
                    row = box.row()
                    row.label("Adjustable Shelf Options:")
                    row = box.row()
                    row.prop(self,'adj_shelf_qty')
                    if self.adj_shelf_qty > 0:
                        row = box.row()
                        row.prop(adj_shelf_setback,'DistanceValue',text="Adj Shelf Setback")
                        row = box.row()
                    if shelf_angle:
                        row = box.row()
                        row.prop(shelf_angle,'AngleValue',text="Shelf Angle")
                        
                if self.fix_shelf_qty_prompt:
                    fix_shelf_setback = self.assembly.get_prompt("Fixed Shelf Setback")
                    box = layout.box()
                    row = box.row()
                    row.label("Fixed Shelf Options:")
                    row = box.row()
                    row.prop(self,'fix_shelf_qty')
                    if self.fix_shelf_qty > 0:
                        row = box.row()
                        row.prop(fix_shelf_setback,'DistanceValue',text="Fix Shelf Setback")
                        row = box.row()
                        
                        
class PROMPTS_Wire_Baskets(bpy.types.Operator):
    bl_idname = "interiors.wire_baskets"
    bl_label = "Wire Basket Prompts" 
    bl_description = "This shows all of the available wire basket options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        return True
        
    def execute(self, context):
        return {'FINISHED'}
    
    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = utils.get_bp(obj,'INSERT')
        self.assembly = fd_types.Assembly(obj_insert_bp)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=utils.get_prop_dialog_width(330))
        
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                
                open_var = self.assembly.get_prompt("Open")
                qty = self.assembly.get_prompt("Basket Quantity")
                b1_z_dim = self.assembly.get_prompt("Basket 1 Z Dim")
                b2_z_dim = self.assembly.get_prompt("Basket 2 Z Dim")
                b3_z_dim = self.assembly.get_prompt("Basket 3 Z Dim")
                b4_z_dim = self.assembly.get_prompt("Basket 4 Z Dim")
                dist_between_baskets = self.assembly.get_prompt("Distance Between Baskets")
                bottom_gap = self.assembly.get_prompt("Bottom Gap")
                
                box = layout.box()
                row = box.row()
                row.label("Open")
                row.prop(open_var,'PercentageValue',text="")
                row = box.row()
                row.label("Quantity")
                row.prop(qty,'QuantityValue',text="")
                if qty.QuantityValue > 3:
                    row = box.row()
                    row.label("Basket 4 Height")
                    row.prop(b4_z_dim,'DistanceValue',text="")
                if qty.QuantityValue > 2:
                    row = box.row()
                    row.label("Basket 3 Height")
                    row.prop(b3_z_dim,'DistanceValue',text="")
                if qty.QuantityValue > 1:
                    row = box.row()
                    row.label("Basket 2 Height")
                    row.prop(b2_z_dim,'DistanceValue',text="")
                row = box.row()
                row.label("Basket 1 Height")
                row.prop(b1_z_dim,'DistanceValue',text="")
                row = box.row()
                row.label("Distance Between Baskets")
                row.prop(dist_between_baskets,'DistanceValue',text="")
                row = box.row()
                row.label("Bottom Gap")
                row.prop(bottom_gap,'DistanceValue',text="")
                
                
class PROMPTS_Shoe_Cubbies(bpy.types.Operator):
    bl_idname = "interiors.shoe_cubbies"
    bl_label = "Shoe Cubbies Prompts" 
    bl_description = "This shows all of the available shoe cubby options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    vertical_opening_space = 0
    horizontal_opening_space = 0
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        
        return True
        
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = utils.get_bp(obj,'INSERT')
        self.assembly = fd_types.Assembly(obj_insert_bp)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=330)
        
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                vert_qty = self.assembly.get_prompt("Vertical Quantity")
                horz_qty = self.assembly.get_prompt("Horizontal Quantity")
                setback = self.assembly.get_prompt("Cubby Setback")
                panel_thickness = self.assembly.get_prompt("Panel Thickness")
                
                layout.prop(vert_qty,'QuantityValue',text="Vertical Quantity")
                layout.prop(horz_qty,'QuantityValue',text="Horizontal Quantity")
                layout.prop(setback,'DistanceValue',text="Setback Amount")
                
                height = self.assembly.obj_z.location.z
                width = self.assembly.obj_x.location.x
                v_qty = vert_qty.QuantityValue
                h_qty = horz_qty.QuantityValue
                
                vertical_opening = (height - (panel_thickness.DistanceValue*h_qty))/(h_qty+1)
                horizontal_opening = (width - (panel_thickness.DistanceValue*v_qty))/(v_qty+1)
                
                layout.label("Shoe Cubby Vertical Opening Space: " + str(unit.meter_to_active_unit(vertical_opening)) + '"')
                layout.label("Shoe Cubby Horizontal Opening Space: " + str(unit.meter_to_active_unit(horizontal_opening)) + '"')

#---------PRODUCT: SPLITTER PROMPTS

class PROMPTS_Splitter_Prompts(bpy.types.Operator):
    bl_idname = "interiors.splitter_prompts"
    bl_label = "Vertical Splitter Prompts" 
    bl_description = "This shows all of the available vertical splitter options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        utils.run_calculators(self.assembly.obj_bp)
        return True
        
    def execute(self, context):
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                utils.run_calculators(self.assembly.obj_bp)
        return {'FINISHED'}
        
    def get_splitter(self,obj_bp):
        assembly = fd_types.Assembly(obj_bp)
        if assembly.get_prompt("Opening 1 Height") or assembly.get_prompt("Opening 1 Width"):
            return assembly
        if obj_bp.parent:
            assembly = fd_types.Assembly(obj_bp.parent)
            if assembly.get_prompt("Opening 1 Height") or assembly.get_prompt("Opening 1 Width"):
                return assembly
            if assembly.obj_bp.parent:
                assembly = fd_types.Assembly(assembly.obj_bp.parent)
                if assembly.get_prompt("Opening 1 Height") or assembly.get_prompt("Opening 1 Width"):
                    return assembly
        
    def select_all(self,obj_bp):
        obj_bp.select = True
        for child in obj_bp.children:
            self.select_all(child)
        
    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = utils.get_bp(obj,'INSERT')
        self.assembly = self.get_splitter(obj_insert_bp)
        self.select_all(obj_insert_bp)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=utils.get_prop_dialog_width(330))
        
    def draw_selected_insert_prompts(self,layout):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = utils.get_bp(obj,'INSERT')
        if "Drawer Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("exteriors.drawer_prompts",text="Drawer Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Door Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("exteriors.door_prompts",text="Door Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Shoe Cubby Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("interiors.shoe_cubbies",text="Shoe Cubby Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Hanging Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("interiors.hanging_rod_prompts",text="Hanging Rod Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Slanted Shoe Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("interiors.shelf_prompt",text="Slanted Shoe Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Wire Basket Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("interiors.wire_baskets",text="Wire Basket Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Hamper Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("exteriors.hamper_prompts",text="Hamper Options",icon='SETTINGS').object_name = obj_insert_bp.name
            
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.get_prompt("Opening 1 Height"):
                name = "Height"
            else:
                name = "Width"
            if self.assembly.obj_bp.name in context.scene.objects:
                box = layout.box()
                opening_1 = self.assembly.get_prompt("Opening 1 " + name)
                opening_2 = self.assembly.get_prompt("Opening 2 " + name)
                opening_3 = self.assembly.get_prompt("Opening 3 " + name)
                opening_4 = self.assembly.get_prompt("Opening 4 " + name)
                
                if opening_1:
                    row = box.row()
                    row.label("Opening 1 " + name + ":")
                    if opening_1.equal:
                        row.label(str(unit.meter_to_active_unit(opening_1.DistanceValue)))
                        row.prop(opening_1,'equal',text="")
                    else:
                        row.prop(opening_1,'DistanceValue',text="")
                        row.prop(opening_1,'equal',text="")
                if opening_2:
                    row = box.row()
                    row.label("Opening 2 " + name + ":")
                    if opening_2.equal:
                        row.label(str(unit.meter_to_active_unit(opening_2.DistanceValue)))
                        row.prop(opening_2,'equal',text="")
                    else:
                        row.prop(opening_2,'DistanceValue',text="")
                        row.prop(opening_2,'equal',text="")
                if opening_3:
                    row = box.row()
                    row.label("Opening 3 " + name + ":")
                    if opening_3.equal:
                        row.label(str(unit.meter_to_active_unit(opening_3.DistanceValue)))
                        row.prop(opening_3,'equal',text="")
                    else:
                        row.prop(opening_3,'DistanceValue',text="")
                        row.prop(opening_3,'equal',text="")
                if opening_4:
                    row = box.row()
                    row.label("Opening 4 " + name + ":")
                    if opening_4.equal:
                        row.label(str(unit.meter_to_active_unit(opening_4.DistanceValue)))
                        row.prop(opening_4,'equal',text="")
                    else:
                        row.prop(opening_4,'DistanceValue',text="")
                        row.prop(opening_4,'equal',text="")
                        
                self.draw_selected_insert_prompts(box)

#---------PRODUCT: COLUMN PROMPTS

class PROMPTS_Column_Prompts(bpy.types.Operator):
    bl_idname = "cabinet.column_prompts"
    bl_label = "Column Prompts"
    bl_options = {'UNDO'}
    object_name = bpy.props.StringProperty(name="Object Name")

    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = bpy.props.FloatProperty(name="Depth",unit='LENGTH',precision=4)

    product = None
    Left_End_Assembly = None
    Right_End_Assembly = None
    Standalone_Assembly = None
    Column_Detail_prompt = None
    
    def check(self, context):
        self.product.obj_x.location.x = self.width

        if self.product.obj_bp.mv.mirror_y:
            self.product.obj_y.location.y = -self.depth
        else:
            self.product.obj_y.location.y = self.depth

        if self.product.obj_bp.mv.mirror_z:
            self.product.obj_z.location.z = -self.height
        else:
            self.product.obj_z.location.z = self.height

        self.product.obj_bp.location = self.product.obj_bp.location #refreshes drawing
        return True

    def execute(self, context):
        # This gets called when the OK button is clicked
        return {'FINISHED'}

    def invoke(self,context,event):
        # This gets called first and is used as an init call
        obj = context.scene.objects[self.object_name]
        obj_product_bp = utils.get_bp(obj,'PRODUCT')
        self.product = fd_types.Assembly(obj_product_bp)
        if self.product.obj_bp:
            self.depth = math.fabs(self.product.obj_y.location.y)
            self.height = math.fabs(self.product.obj_z.location.z)
            self.width = math.fabs(self.product.obj_x.location.x)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=utils.get_prop_dialog_width(480))
    
    def draw_product_size(self,layout):
        box = layout.box()
        
        row = box.row()
        
        col = row.column(align=True)
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_x):
            row1.label('Width: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_x.location.x))))
        else:
            row1.label('Width:')
            row1.prop(self,'width',text="")
            row1.prop(self.product.obj_x,'hide',text="")
        
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_z):
            row1.label('Height: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_z.location.z))))
        else:
            row1.label('Height:')
            row1.prop(self,'height',text="")
            row1.prop(self.product.obj_z,'hide',text="")
        
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_y):
            row1.label('Depth: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_y.location.y))))
        else:
            row1.label('Depth:')
            row1.prop(self,'depth',text="")
            row1.prop(self.product.obj_y,'hide',text="")
            
        col = row.column(align=True)
        col.label("Location X:")
        col.label("Location Y:")
        col.label("Location Z:")
            
        col = row.column(align=True)
        col.prop(self.product.obj_bp,'location',text="")
        
        row = box.row()
        row.label('Rotation Z:')
        row.prop(self.product.obj_bp,'rotation_euler',index=2,text="")
            
    def object_has_driver(self,obj):
        if obj.animation_data:
            if len(obj.animation_data.drivers) > 0:
                return True

    def draw(self, context):
        layout = self.layout
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                box = layout.box()

                split = box.split(percentage=.8)
                split.label(self.product.obj_bp.mv.name_object + " | " + self.product.obj_bp.cabinetlib.spec_group_name,icon='LATTICE_DATA')
                split.menu('MENU_Current_Cabinet_Menu',text="Menu",icon='DOWNARROW_HLT')

                Extend_Left_End = self.product.get_prompt("Extend Left End")
                Extend_Right_End = self.product.get_prompt("Extend Right End")
                Panel_Depth = self.product.get_prompt("Panel Depth")

                self.draw_product_size(box)
                col = box.column(align=True)
                col.label("Basic Column Options:")
                row = col.row()
                row.prop(Extend_Left_End,'CheckBoxValue',text="Extend Left End")
                row.prop(Extend_Right_End,'CheckBoxValue',text="Extend Right End")
                row = col.row()
                row.prop(Panel_Depth,'DistanceValue',text="Panel Depth")

class PROMPTS_Angled_Column_Prompts(bpy.types.Operator):
    bl_idname = "cabinet.angled_column_prompts"
    bl_label = "Angled Column Prompts"
    bl_options = {'UNDO'}
    object_name = bpy.props.StringProperty(name="Object Name")

    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = bpy.props.FloatProperty(name="Depth",unit='LENGTH',precision=4)

    product = None
    Left_End_Assembly = None
    Right_End_Assembly = None
    Standalone_Assembly = None
    Column_Detail_prompt = None
    
    def check(self, context):
        self.product.obj_x.location.x = self.width

        if self.product.obj_bp.mv.mirror_y:
            self.product.obj_y.location.y = -self.depth
        else:
            self.product.obj_y.location.y = self.depth

        if self.product.obj_bp.mv.mirror_z:
            self.product.obj_z.location.z = -self.height
        else:
            self.product.obj_z.location.z = self.height

        self.product.obj_bp.location = self.product.obj_bp.location #refreshes drawing
        return True

    def execute(self, context):
        # This gets called when the OK button is clicked
        return {'FINISHED'}

    def invoke(self,context,event):
        # This gets called first and is used as an init call
        obj = context.scene.objects[self.object_name]
        obj_product_bp = utils.get_bp(obj,'PRODUCT')
        self.product = fd_types.Assembly(obj_product_bp)
        if self.product.obj_bp:
            self.depth = math.fabs(self.product.obj_y.location.y)
            self.height = math.fabs(self.product.obj_z.location.z)
            self.width = math.fabs(self.product.obj_x.location.x)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=utils.get_prop_dialog_width(480))
    
    def draw_product_size(self,layout):
        box = layout.box()
        
        row = box.row()
        
        col = row.column(align=True)
#         row1 = col.row(align=True)
#         if self.object_has_driver(self.product.obj_x):
#             row1.label('Width: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_x.location.x))))
#         else:
#             row1.label('Width:')
#             row1.prop(self,'width',text="")
#             row1.prop(self.product.obj_x,'hide',text="")
        
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_z):
            row1.label('Height: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_z.location.z))))
        else:
            row1.label('Height:')
            row1.prop(self,'height',text="")
            row1.prop(self.product.obj_z,'hide',text="")
        
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_y):
            row1.label('Depth: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_y.location.y))))
        else:
            row1.label('Depth:')
            row1.prop(self,'depth',text="")
            row1.prop(self.product.obj_y,'hide',text="")
            
        col = row.column(align=True)
        col.label("Location X:")
        col.label("Location Y:")
        col.label("Location Z:")
            
        col = row.column(align=True)
        col.prop(self.product.obj_bp,'location',text="")
        
        row = box.row()
        row.label('Rotation Z:')
        row.prop(self.product.obj_bp,'rotation_euler',index=2,text="")
            
    def object_has_driver(self,obj):
        if obj.animation_data:
            if len(obj.animation_data.drivers) > 0:
                return True

    def draw(self, context):
        layout = self.layout
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                box = layout.box()

                split = box.split(percentage=.8)
                split.label(self.product.obj_bp.mv.name_object + " | " + self.product.obj_bp.cabinetlib.spec_group_name,icon='LATTICE_DATA')
                split.menu('MENU_Current_Cabinet_Menu',text="Menu",icon='DOWNARROW_HLT')

                self.draw_product_size(box)


#---------PRODUCT: CABINET PROMPTS

class PROMPTS_Frameless_Cabinet_Prompts(bpy.types.Operator):
    bl_idname = "cabinetlib.frameless_cabinet_prompts"
    bl_label = "Frameless Cabinet Prompts" 
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = bpy.props.FloatProperty(name="Depth",unit='LENGTH',precision=4)

    product_tabs = bpy.props.EnumProperty(name="Door Swing",items=[('CARCASS',"Carcass","Carcass Options"),
                                                         ('EXTERIOR',"Exterior","Exterior Options"),
                                                         ('INTERIOR',"Interior","Interior Options"),
                                                         ('SPLITTER',"Openings","Openings Options")])

    door_rotation = bpy.props.FloatProperty(name="Door Rotation",subtype='ANGLE',min=0,max=math.radians(120))
    
    door_swing = bpy.props.EnumProperty(name="Door Swing",items=[('Left Swing',"Left Swing","Left Swing"),
                                                                 ('Right Swing',"Right Swing","Right Swing")])
    
    product = None
    
    open_door_prompts = []
    
    show_exterior_options = False
    show_interior_options = False
    show_splitter_options = False
    
    inserts = []
    
    @classmethod
    def poll(cls, context):
        return True

    def check(self, context):
        self.product.obj_x.location.x = self.width
        
        if self.product.obj_bp.mv.mirror_y:
            self.product.obj_y.location.y = -self.depth
        else:
            self.product.obj_y.location.y = self.depth
        
        if self.product.obj_bp.mv.mirror_z:
            self.product.obj_z.location.z = -self.height
        else:
            self.product.obj_z.location.z = self.height
            
        for open_door_prompt in self.open_door_prompts:
            open_door_prompt.set_value(self.door_rotation)
            
        utils.run_calculators(self.product.obj_bp)
        return True

    def execute(self, context):
        utils.run_calculators(self.product.obj_bp)
        return {'FINISHED'}

    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_product_bp = utils.get_bp(obj,'PRODUCT')
        self.product = fd_types.Assembly(obj_product_bp)
        if self.product.obj_bp:
            self.depth = math.fabs(self.product.obj_y.location.y)
            self.height = math.fabs(self.product.obj_z.location.z)
            self.width = math.fabs(self.product.obj_x.location.x)
            new_list = []
            self.inserts = utils.get_insert_bp_list(self.product.obj_bp,new_list)
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                door = fd_types.Assembly(insert)
                door_rotation = door.get_prompt("Door Rotation")
                if door_rotation:
                    self.open_door_prompts.append(door_rotation)
                    self.door_rotation = door_rotation.value()
                self.show_exterior_options = True
            if "Drawer Options" in insert.mv.PromptPage.COL_MainTab:
                self.show_exterior_options = True
            if "Interior Options" in insert.mv.PromptPage.COL_MainTab:
                self.show_interior_options = True
            if "Opening Heights" in insert.mv.PromptPage.COL_MainTab:
                self.show_splitter_options = True
            if "Opening Widths" in insert.mv.PromptPage.COL_MainTab:
                self.show_splitter_options = True
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=utils.get_prop_dialog_width(500))

    def draw_product_size(self,layout):
        box = layout.box()
        
        row = box.row()
        
        col = row.column(align=True)
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_x):
            row1.label('Width: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_x.location.x))))
        else:
            row1.label('Width:')
            row1.prop(self,'width',text="")
            row1.prop(self.product.obj_x,'hide',text="")
        
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_z):
            row1.label('Height: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_z.location.z))))
        else:
            row1.label('Height:')
            row1.prop(self,'height',text="")
            row1.prop(self.product.obj_z,'hide',text="")
        
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_y):
            row1.label('Depth: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_y.location.y))))
        else:
            row1.label('Depth:')
            row1.prop(self,'depth',text="")
            row1.prop(self.product.obj_y,'hide',text="")
            
        col = row.column(align=True)
        col.label("Location X:")
        col.label("Location Y:")
        col.label("Location Z:")
        
        col = row.column(align=True)
        col.prop(self.product.obj_bp,'location',text="")
        
        row = box.row()
        row.label('Rotation Z:')
        row.prop(self.product.obj_bp,'rotation_euler',index=2,text="")
        
    def object_has_driver(self,obj):
        if obj.animation_data:
            if len(obj.animation_data.drivers) > 0:
                return True
            
    def draw_carcass_prompts(self,layout):
        for insert in self.inserts:
            if "Carcass Options" in insert.mv.PromptPage.COL_MainTab:
                carcass = fd_types.Assembly(insert)
                left_fin_end = carcass.get_prompt("Left Fin End")
                right_fin_end = carcass.get_prompt("Right Fin End")
                left_wall_filler = carcass.get_prompt("Left Side Wall Filler")
                right_wall_filler = carcass.get_prompt("Right Side Wall Filler")
                
                valance_height_top = carcass.get_prompt("Valance Height Top")
                toe_kick_height = carcass.get_prompt("Toe Kick Height")
                remove_bottom = carcass.get_prompt("Remove Bottom")
                remove_back = carcass.get_prompt("Remove Back")
                use_thick_back = carcass.get_prompt("Use Thick Back")
                use_nailers = carcass.get_prompt("Use Nailers")
                cabinet_depth_left = carcass.get_prompt("Cabinet Depth Left")
                cabinet_depth_right = carcass.get_prompt("Cabinet Depth Right")
                
                sub_front_height = carcass.get_prompt("Sub Front Height")
                
                # SIDE OPTIONS:
                if left_wall_filler and right_wall_filler:
                    col = layout.column(align=True)
                    col.label("Side Options:")
                    
                    row = col.row()
                    row.prop(left_wall_filler,'DistanceValue',text="Left Filler Amount")
                    row.prop(left_fin_end,'CheckBoxValue',text="Left Fin End")
                    
                    row = col.row()
                    row.prop(right_wall_filler,'DistanceValue',text="Right Filler Amount")
                    row.prop(right_fin_end,'CheckBoxValue',text="Right Fin End")
                
                # CARCASS OPTIONS:
                col = layout.column(align=True)
                col.label("Carcass Options:")
                row = col.row()
                if use_thick_back:
                    row.prop(use_thick_back,'CheckBoxValue',text="Use Thick Back")
                if use_nailers:
                    row.prop(use_nailers,'CheckBoxValue',text="Use Nailers")
                if remove_bottom:
                    row.prop(remove_bottom,'CheckBoxValue',text="Remove Bottom")
                if remove_back:
                    row.prop(remove_back,'CheckBoxValue',text="Remove Back")
                if cabinet_depth_left:
                    row = col.row()
                    row.prop(cabinet_depth_left,'DistanceValue',text="Cabinet Depth Left")
                    row.prop(cabinet_depth_right,'DistanceValue',text="Cabinet Depth Right")
                
                # TOE KICK OPTIONS
                if toe_kick_height:
                    col = layout.column(align=True)
                    toe_kick_setback = carcass.get_prompt("Toe Kick Setback")
                    col.label("Toe Kick Options:")
                    row = col.row()
                    row.prop(toe_kick_height,'DistanceValue',text="Toe Kick Height")
                    row.prop(toe_kick_setback,'DistanceValue',text="Toe Kick Setback")
                    
                # VALANCE OPTIONS
                if valance_height_top:
                    r_full_height = carcass.get_prompt("Right Side Full Height")
                    l_full_height = carcass.get_prompt("Left Side Full Height")
                    valance_each_unit = carcass.get_prompt("Valance Each Unit")
                    
                    col = layout.column(align=True)
                    col.label("Valance Options:")
                    door_valance_top = carcass.get_prompt("Door Valance Top")
                    row = col.row()
                    row.prop(valance_height_top,'DistanceValue',text="Valance Height Top")
                    row.prop(door_valance_top,'CheckBoxValue',text="Door Valance Top")

                    valance_height_bottom = carcass.get_prompt("Valance Height Bottom")
                    
                    if valance_height_bottom:
                        door_valance_bottom = carcass.get_prompt("Door Valance Bottom")
                        row = col.row()
                        row.prop(valance_height_bottom,'DistanceValue',text="Valance Height Bottom")
                        row.prop(door_valance_bottom,'CheckBoxValue',text="Door Valance Bottom")
                    
                    row = col.row()
                    row.prop(l_full_height,'CheckBoxValue',text="Left Side Full Height")
                    row.prop(r_full_height,'CheckBoxValue',text="Right Side Full Height")
                    
                    row = col.row()
                    row.prop(valance_each_unit,'CheckBoxValue',text="Add Valance For Each Unit")
                    
                if sub_front_height:
                    pass
                
            if "Countertop Options" in insert.mv.PromptPage.COL_MainTab:
                ctop = fd_types.Assembly(insert)
                Add_Backsplash = ctop.get_prompt("Add Backsplash")
                Add_Left_Backsplash = ctop.get_prompt("Add Left Backsplash")
                Add_Right_Backsplash = ctop.get_prompt("Add Right Backsplash")
                Countertop_Overhang_Front = self.product.get_prompt("Countertop Overhang Front")
                Countertop_Overhang_Back = self.product.get_prompt("Countertop Overhang Back")
                Countertop_Overhang_Left = self.product.get_prompt("Countertop Overhang Left")
                Countertop_Overhang_Right = self.product.get_prompt("Countertop Overhang Right")
                col = layout.column(align=True)
                col.label("Countertop Options:")
                
                if Add_Backsplash and Add_Left_Backsplash and Add_Right_Backsplash:
                    row = col.row()
                    row.label("Add Splash:")
                    row.prop(Add_Backsplash,'CheckBoxValue',text="Back")
                    row.prop(Add_Left_Backsplash,'CheckBoxValue',text="Left")
                    row.prop(Add_Right_Backsplash,'CheckBoxValue',text="Right")
                
                if Countertop_Overhang_Front:
                    row = col.row(align=True)
                    row.label("Overhang:")
                    row.prop(Countertop_Overhang_Front,'DistanceValue',text="Front")
                    row.prop(Countertop_Overhang_Back,'DistanceValue',text="Back")
                    row.prop(Countertop_Overhang_Left,'DistanceValue',text="Left")
                    row.prop(Countertop_Overhang_Right,'DistanceValue',text="Right")
                
    def draw_opening_prompt(self):
        pass
        
    def draw_door_prompts(self,layout):
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                row = layout.row()
                row.label("Open Door")
                row.prop(self,'door_rotation',text="",slider=True)
                break
            
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                row = col.row()
                row.label(insert.mv.name_object + " Options:")
                door = fd_types.Assembly(insert)
                left_swing = door.get_prompt("Left Swing")
                inset_front = door.get_prompt("Inset Front")
                hot = door.get_prompt("Half Overlay Top")
                hob = door.get_prompt("Half Overlay Bottom")
                hol = door.get_prompt("Half Overlay Left")
                hor = door.get_prompt("Half Overlay Right")
                
                row.prop(inset_front,'CheckBoxValue',text="Inset Door")
                
                if left_swing:
                    row.prop(left_swing,'CheckBoxValue',text="Left Swing Door")
                    
                if hot:
                    row = col.row()
                    row.label("Half Overlays:")
                    row.prop(hot,'CheckBoxValue',text="Top")
                    row.prop(hob,'CheckBoxValue',text="Bottom")
                    row.prop(hol,'CheckBoxValue',text="Left")
                    row.prop(hor,'CheckBoxValue',text="Right")
        
    def draw_drawer_prompts(self,layout):
        for insert_bp in self.inserts:
            if "Drawer Options" in insert_bp.mv.PromptPage.COL_MainTab:
                insert = fd_types.Assembly(insert_bp)
                open_prompt = insert.get_prompt("Open")
                
                if open_prompt:
                    row = layout.row()
                    row.label("Open Drawer")
                    row.prop(open_prompt,"PercentageValue",text="")
                
                box = layout.box()
                col = box.column(align=True)
                row = col.row()
                row.label(insert_bp.mv.name_object + " Options:")
                
                inset_front = insert.get_prompt("Inset Front")
                half_overlay_top = insert.get_prompt("Half Overlay Top")
                
                if inset_front:
                    row.prop(inset_front,'CheckBoxValue',text="Inset Front")
                    
                if half_overlay_top:
                    half_overlay_bottom = insert.get_prompt("Half Overlay Bottom")
                    half_overlay_left = insert.get_prompt("Half Overlay Left")
                    half_overlay_right = insert.get_prompt("Half Overlay Right")
                    row = col.row()
                    row.label("Half Overlays:")
                    row.prop(half_overlay_top,'CheckBoxValue',text="Top")
                    row.prop(half_overlay_bottom,'CheckBoxValue',text="Bottom")
                    row.prop(half_overlay_left,'CheckBoxValue',text="Left")
                    row.prop(half_overlay_right,'CheckBoxValue',text="Right")
                
            if "Drawer Heights" in insert_bp.mv.PromptPage.COL_MainTab:
                insert = fd_types.Assembly(insert_bp)
                drawer_height_1 = insert.get_prompt("Top Drawer Height")
                drawer_height_2 = insert.get_prompt("Second Drawer Height")
                drawer_height_3 = insert.get_prompt("Third Drawer Height")
                drawer_height_4 = insert.get_prompt("Bottom Drawer Height")
                
                if drawer_height_1:
                    row = box.row()
                    row.label("Drawer 1 Height:")
                    if drawer_height_1.equal:
                        row.label(str(unit.meter_to_active_unit(drawer_height_1.DistanceValue)))
                        row.prop(drawer_height_1,'equal',text="")
                    else:
                        row.prop(drawer_height_1,'DistanceValue',text="")
                        row.prop(drawer_height_1,'equal',text="")
                
                if drawer_height_2:
                    row = box.row()
                    row.label("Drawer 2 Height:")
                    if drawer_height_2.equal:
                        row.label(str(unit.meter_to_active_unit(drawer_height_2.DistanceValue)))
                        row.prop(drawer_height_2,'equal',text="")
                    else:
                        row.prop(drawer_height_2,'DistanceValue',text="")
                        row.prop(drawer_height_2,'equal',text="")
                
                if drawer_height_3:
                    row = box.row()
                    row.label("Drawer 3 Height:")
                    if drawer_height_3.equal:
                        row.label(str(unit.meter_to_active_unit(drawer_height_3.DistanceValue)))
                        row.prop(drawer_height_3,'equal',text="")
                    else:
                        row.prop(drawer_height_3,'DistanceValue',text="")
                        row.prop(drawer_height_3,'equal',text="")
                
                if drawer_height_4:
                    row = box.row()
                    row.label("Drawer 4 Height:")
                    if drawer_height_4.equal:
                        row.label(str(unit.meter_to_active_unit(drawer_height_4.DistanceValue)))
                        row.prop(drawer_height_4,'equal',text="")
                    else:
                        row.prop(drawer_height_4,'DistanceValue',text="")
                        row.prop(drawer_height_4,'equal',text="")
        
    def draw_interior_prompts(self,layout):
        for insert in self.inserts:
            if "Interior Options" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                col.label("Interior Options:")
                carcass = fd_types.Assembly(insert)
                adj_shelf_qty = carcass.get_prompt("Adj Shelf Qty")
                fix_shelf_qty = carcass.get_prompt("Fixed Shelf Qty")
                div_qty_per_row = carcass.get_prompt("Divider Qty Per Row")
                division_qty = carcass.get_prompt("Division Qty")
                adj_shelf_rows = carcass.get_prompt("Adj Shelf Rows")
                fixed_shelf_rows = carcass.get_prompt("Fixed Shelf Rows")
                
                if adj_shelf_qty:
                    row = col.row()
                    row.label("Adjustable Shelf Qty")
                    row.prop(adj_shelf_qty,'QuantityValue',text="")
        
                    row.label("Fixed Shelf Qty")
                    row.prop(fix_shelf_qty,'QuantityValue',text="")
                    
                if div_qty_per_row:
                    row = col.row()
                    row.label("Divider Qty Per Row")
                    row.prop(div_qty_per_row,'QuantityValue',text="")
                
                if division_qty:
                    row = col.row()
                    row.label("Division Qty")
                    row.prop(division_qty,'QuantityValue',text="")
                
                if adj_shelf_rows:
                    row = col.row()
                    row.label("Adjustable Shelf Rows")
                    row.prop(adj_shelf_rows,'QuantityValue',text="")
                    
                    row.label("Fixed Shelf Rows")
                    row.prop(fixed_shelf_rows,'QuantityValue',text="")
        
    def draw_splitter_prompts(self,layout):
        for insert in self.inserts:
            if "Opening Heights" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                col.label("Splitter Options:")
                splitter = fd_types.Assembly(insert)
                opening_1 = splitter.get_prompt("Opening 1 Height")
                opening_2 = splitter.get_prompt("Opening 2 Height")
                opening_3 = splitter.get_prompt("Opening 3 Height")
                opening_4 = splitter.get_prompt("Opening 4 Height")
                
                if opening_1:
                    row = box.row()
                    row.label("Opening 1 Height:")
                    if opening_1.equal:
                        row.label(str(unit.meter_to_active_unit(opening_1.DistanceValue)))
                        row.prop(opening_1,'equal',text="")
                    else:
                        row.prop(opening_1,'DistanceValue',text="")
                        row.prop(opening_1,'equal',text="")
                if opening_2:
                    row = box.row()
                    row.label("Opening 2 Height:")
                    if opening_2.equal:
                        row.label(str(unit.meter_to_active_unit(opening_2.DistanceValue)))
                        row.prop(opening_2,'equal',text="")
                    else:
                        row.prop(opening_2,'DistanceValue',text="")
                        row.prop(opening_2,'equal',text="")
                if opening_3:
                    row = box.row()
                    row.label("Opening 3 Height:")
                    if opening_3.equal:
                        row.label(str(unit.meter_to_active_unit(opening_3.DistanceValue)))
                        row.prop(opening_3,'equal',text="")
                    else:
                        row.prop(opening_3,'DistanceValue',text="")
                        row.prop(opening_3,'equal',text="")
                if opening_4:
                    row = box.row()
                    row.label("Opening 4 Height:")
                    if opening_4.equal:
                        row.label(str(unit.meter_to_active_unit(opening_4.DistanceValue)))
                        row.prop(opening_4,'equal',text="")
                    else:
                        row.prop(opening_4,'DistanceValue',text="")
                        row.prop(opening_4,'equal',text="")
        
    def draw(self, context):
        layout = self.layout
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                box = layout.box()
                
                split = box.split(percentage=.8)
                split.label(self.product.obj_bp.mv.name_object + " | " + self.product.obj_bp.cabinetlib.spec_group_name,icon='LATTICE_DATA')
                split.menu('MENU_Current_Cabinet_Menu',text="Menu",icon='DOWNARROW_HLT')
                
                self.draw_product_size(box)
                
                prompt_box = box.box()
                row = prompt_box.row(align=True)
                row.prop_enum(self, "product_tabs", 'CARCASS') 
                if self.show_exterior_options:
                    row.prop_enum(self, "product_tabs", 'EXTERIOR') 
                if self.show_interior_options:
                    row.prop_enum(self, "product_tabs", 'INTERIOR') 
                if self.show_splitter_options:
                    row.prop_enum(self, "product_tabs", 'SPLITTER') 

                if self.product_tabs == 'CARCASS':
                    self.draw_carcass_prompts(prompt_box)
                if self.product_tabs == 'EXTERIOR':
                    self.draw_door_prompts(prompt_box)
                    self.draw_drawer_prompts(prompt_box)
                if self.product_tabs == 'INTERIOR':
                    self.draw_interior_prompts(prompt_box)
                if self.product_tabs == 'SPLITTER':
                    self.draw_splitter_prompts(prompt_box)     
      
      
class PROMPTS_Face_Frame_Cabinet_Prompts(bpy.types.Operator):
    bl_idname = "face_frame_cabients.cabinet_prompts"
    bl_label = "Face Frame Cabinet Prompts" 
    bl_options = {'UNDO'}
         
    object_name = bpy.props.StringProperty(name="Object Name")
     
    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = bpy.props.FloatProperty(name="Depth",unit='LENGTH',precision=4)
 
    product_tabs = bpy.props.EnumProperty(name="Door Swing",items=[('CARCASS',"Carcass","Carcass Options"),
                                                         ('EXTERIOR',"Exterior","Exterior Options"),
                                                         ('INTERIOR',"Interior","Interior Options"),
                                                         ('SPLITTER',"Openings","Openings Options"),
                                                         ('FACEFRAME',"Face Frame","Face Frame Options")])
 
    door_rotation = bpy.props.FloatProperty(name="Door Rotation",subtype='ANGLE',min=0,max=math.radians(120))
     
    door_swing = bpy.props.EnumProperty(name="Door Swing",items=[('Left Swing',"Left Swing","Left Swing"),
                                                       ('Right Swing',"Right Swing","Right Swing")])
     
    product = None
     
    open_door_prompt = None
     
    open_door_prompts = []
     
    inserts = []
     
    show_exterior_options = False
    show_interior_options = False
    show_splitter_options = False
     
    @classmethod
    def poll(cls, context):
        return True
 
    def check(self, context):
        self.product.obj_x.location.x = self.width
         
        if self.product.obj_bp.mv.mirror_y:
            self.product.obj_y.location.y = -self.depth
        else:
            self.product.obj_y.location.y = self.depth
         
        if self.product.obj_bp.mv.mirror_z:
            self.product.obj_z.location.z = -self.height
        else:
            self.product.obj_z.location.z = self.height
             
        for prompt in self.open_door_prompts:
            prompt.set_value(self.door_rotation)
             
        utils.run_calculators(self.product.obj_bp)
        self.product.obj_bp.location = self.product.obj_bp.location
        return True
 
    def execute(self, context):
        utils.run_calculators(self.product.obj_bp)
        
        return {'FINISHED'}
 
    def invoke(self,context,event):
        self.open_door_prompts = []
        obj = bpy.data.objects[self.object_name]
        obj_product_bp = utils.get_bp(obj,'PRODUCT')
        self.product = fd_types.Assembly(obj_product_bp)
        if self.product.obj_bp:
            self.depth = math.fabs(self.product.obj_y.location.y)
            self.height = math.fabs(self.product.obj_z.location.z)
            self.width = math.fabs(self.product.obj_x.location.x)
            new_list = []
            self.inserts = utils.get_insert_bp_list(self.product.obj_bp,new_list)
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                door = fd_types.Assembly(insert)
                door_rotation = door.get_prompt("Door Rotation")
                if door_rotation:
                    self.open_door_prompts.append(door_rotation)
                    self.door_rotation = door_rotation.value()
                self.show_exterior_options = True
            if "Drawer Options" in insert.mv.PromptPage.COL_MainTab:
                self.show_exterior_options = True
            if "Interior Options" in insert.mv.PromptPage.COL_MainTab:
                self.show_interior_options = True
            if "Opening Heights" in insert.mv.PromptPage.COL_MainTab:
                self.show_splitter_options = True
            if "Opening Widths" in insert.mv.PromptPage.COL_MainTab:
                self.show_splitter_options = True
 
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=utils.get_prop_dialog_width(500))
 
    def draw_product_size(self,layout):
        box = layout.box()
         
        row = box.row()
         
        col = row.column(align=True)
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_x):
            row1.label('Width: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_x.location.x))))
        else:
            row1.label('Width:')
            row1.prop(self,'width',text="")
            row1.prop(self.product.obj_x,'hide',text="")
         
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_z):
            row1.label('Height: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_z.location.z))))
        else:
            row1.label('Height:')
            row1.prop(self,'height',text="")
            row1.prop(self.product.obj_z,'hide',text="")
         
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_y):
            row1.label('Depth: ' + str(unit.meter_to_active_unit(math.fabs(self.product.obj_y.location.y))))
        else:
            row1.label('Depth:')
            row1.prop(self,'depth',text="")
            row1.prop(self.product.obj_y,'hide',text="")
             
        col = row.column(align=True)
        col.label("Location X:")
        col.label("Location Y:")
        col.label("Location Z:")
             
        col = row.column(align=True)
        col.prop(self.product.obj_bp,'location',text="")
         
        row = box.row()
        row.label('Rotation Z:')
        row.prop(self.product.obj_bp,'rotation_euler',index=2,text="")
             
    def object_has_driver(self,obj):
        if obj.animation_data:
            if len(obj.animation_data.drivers) > 0:
                return True
             
    def draw_carcass_prompts(self,layout):
        for insert in self.inserts:
            if "Carcass Options" in insert.mv.PromptPage.COL_MainTab:
                carcass = fd_types.Assembly(insert)
                left_fin_end = carcass.get_prompt("Left Fin End")
                right_fin_end = carcass.get_prompt("Right Fin End")
#                 left_wall_filler = carcass.get_prompt("Left Side Wall Filler")
#                 right_wall_filler = carcass.get_prompt("Right Side Wall Filler")
                 
                toe_kick_height = carcass.get_prompt("Toe Kick Height")
                remove_bottom = carcass.get_prompt("Remove Bottom")
                remove_back = carcass.get_prompt("Remove Back")
                use_thick_back = carcass.get_prompt("Use Thick Back")
                use_nailers = carcass.get_prompt("Use Nailers")
                cabinet_depth_left = carcass.get_prompt("Cabinet Depth Left")
                cabinet_depth_right = carcass.get_prompt("Cabinet Depth Right")
                 
                # SIDE OPTIONS:
                col = layout.column(align=True)
                col.label("Side Options:")
                row = col.row()
                row.prop(left_fin_end,'CheckBoxValue',text="Left Fin End")
                row.prop(right_fin_end,'CheckBoxValue',text="Right Fin End")
                 
                # CARCASS OPTIONS:
                col = layout.column(align=True)
                col.label("Carcass Options:")
                row = col.row()
                if use_thick_back:
                    row.prop(use_thick_back,'CheckBoxValue',text="Use Thick Back")
                if use_nailers:
                    row.prop(use_nailers,'CheckBoxValue',text="Use Nailers")
                if remove_bottom:
                    row.prop(remove_bottom,'CheckBoxValue',text="Remove Bottom")
                if remove_back:
                    row.prop(remove_back,'CheckBoxValue',text="Remove Back")
                if cabinet_depth_left:
                    row = col.row()
                    row.prop(cabinet_depth_left,'DistanceValue',text="Cabinet Depth Left")
                    row.prop(cabinet_depth_right,'DistanceValue',text="Cabinet Depth Right")
                 
                # TOE KICK OPTIONS
                if toe_kick_height:
                    col = layout.column(align=True)
                    toe_kick_setback = carcass.get_prompt("Toe Kick Setback")
                    col.label("Toe Kick Options:")
                    row = col.row()
                    row.prop(toe_kick_height,'DistanceValue',text="Toe Kick Height")
                    row.prop(toe_kick_setback,'DistanceValue',text="Toe Kick Setback")
                     
            if "Countertop Options" in insert.mv.PromptPage.COL_MainTab:
                ctop = fd_types.Assembly(insert)
                Add_Backsplash = ctop.get_prompt("Add Backsplash")
                Add_Left_Backsplash = ctop.get_prompt("Add Left Backsplash")
                Add_Right_Backsplash = ctop.get_prompt("Add Right Backsplash")
                Countertop_Overhang_Front = self.product.get_prompt("Countertop Overhang Front")
                Countertop_Overhang_Back = self.product.get_prompt("Countertop Overhang Back")
                Countertop_Overhang_Left = self.product.get_prompt("Countertop Overhang Left")
                Countertop_Overhang_Right = self.product.get_prompt("Countertop Overhang Right")
                col = layout.column(align=True)
                col.label("Countertop Options:")
                
                if Add_Backsplash and Add_Left_Backsplash and Add_Right_Backsplash:
                    row = col.row()
                    row.label("Add Splash:")
                    row.prop(Add_Backsplash,'CheckBoxValue',text="Back")
                    row.prop(Add_Left_Backsplash,'CheckBoxValue',text="Left")
                    row.prop(Add_Right_Backsplash,'CheckBoxValue',text="Right")
                
                if Countertop_Overhang_Front:
                    row = col.row(align=True)
                    row.label("Overhang:")
                    row.prop(Countertop_Overhang_Front,'DistanceValue',text="Front")
                    row.prop(Countertop_Overhang_Back,'DistanceValue',text="Back")
                    row.prop(Countertop_Overhang_Left,'DistanceValue',text="Left")
                    row.prop(Countertop_Overhang_Right,'DistanceValue',text="Right")
                     
    def draw_door_prompts(self,layout):
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                 
                #TODO make pie cut door insert rot z for door open
                if "Pie Cut" not in insert.mv.name_object:
                    row = layout.row()
                    row.label("Open")
                    row.prop(self,'door_rotation',text="",slider=True)
                    break
             
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                col.label(insert.mv.name_object + " Options:")
                door = fd_types.Assembly(insert)
                left_swing = door.get_prompt("Left Swing")
                inset_front = door.get_prompt("Inset Front")
                 
                row = col.row()
                row.label("Inset Door")
                row.prop(inset_front,'CheckBoxValue',text="")
 
                if left_swing:
                    row = col.row()
                    row.label("Left Door Swing")
                    row.prop(left_swing,'CheckBoxValue',text="")
         
    def draw_drawer_prompts(self,layout):
        for insert_bp in self.inserts:
            if "Drawer Options" in insert_bp.mv.PromptPage.COL_MainTab:
                insert = fd_types.Assembly(insert_bp)
                open_prompt = insert.get_prompt("Open")
                 
                if open_prompt:
                    row = layout.row()
                    row.label("Open Drawer")
                    row.prop(open_prompt,"PercentageValue",text="")
                 
                box = layout.box()
                col = box.column(align=True)
                row = col.row()
                row.label(insert_bp.mv.name_object + " Options:")
                 
                inset_front = insert.get_prompt("Inset Front")
                half_overlay_top = insert.get_prompt("Half Overlay Top")
                 
                if inset_front:
                    row.prop(inset_front,'CheckBoxValue',text="Inset Front")
                     
                if half_overlay_top:
                    half_overlay_bottom = insert.get_prompt("Half Overlay Bottom")
                    half_overlay_left = insert.get_prompt("Half Overlay Left")
                    half_overlay_right = insert.get_prompt("Half Overlay Right")
                    row = col.row()
                    row.label("Half Overlays:")
                    row.prop(half_overlay_top,'CheckBoxValue',text="Top")
                    row.prop(half_overlay_bottom,'CheckBoxValue',text="Bottom")
                    row.prop(half_overlay_left,'CheckBoxValue',text="Left")
                    row.prop(half_overlay_right,'CheckBoxValue',text="Right")
                 
            if "Drawer Heights" in insert_bp.mv.PromptPage.COL_MainTab:
                insert = fd_types.Assembly(insert_bp)
                drawer_height_1 = insert.get_prompt("Top Drawer Height")
                drawer_height_2 = insert.get_prompt("Second Drawer Height")
                drawer_height_3 = insert.get_prompt("Third Drawer Height")
                drawer_height_4 = insert.get_prompt("Bottom Drawer Height")
                 
                if drawer_height_1:
                    row = box.row()
                    row.label("Drawer 1 Height:")
                    if drawer_height_1.equal:
                        row.label(str(unit.meter_to_active_unit(drawer_height_1.DistanceValue)))
                        row.prop(drawer_height_1,'equal',text="")
                    else:
                        row.prop(drawer_height_1,'DistanceValue',text="")
                        row.prop(drawer_height_1,'equal',text="")
                 
                if drawer_height_2:
                    row = box.row()
                    row.label("Drawer 2 Height:")
                    if drawer_height_2.equal:
                        row.label(str(unit.meter_to_active_unit(drawer_height_2.DistanceValue)))
                        row.prop(drawer_height_2,'equal',text="")
                    else:
                        row.prop(drawer_height_2,'DistanceValue',text="")
                        row.prop(drawer_height_2,'equal',text="")
                 
                if drawer_height_3:
                    row = box.row()
                    row.label("Drawer 3 Height:")
                    if drawer_height_3.equal:
                        row.label(str(unit.meter_to_active_unit(drawer_height_3.DistanceValue)))
                        row.prop(drawer_height_3,'equal',text="")
                    else:
                        row.prop(drawer_height_3,'DistanceValue',text="")
                        row.prop(drawer_height_3,'equal',text="")
                 
                if drawer_height_4:
                    row = box.row()
                    row.label("Drawer 4 Height:")
                    if drawer_height_4.equal:
                        row.label(str(unit.meter_to_active_unit(drawer_height_4.DistanceValue)))
                        row.prop(drawer_height_4,'equal',text="")
                    else:
                        row.prop(drawer_height_4,'DistanceValue',text="")
                        row.prop(drawer_height_4,'equal',text="")
         
    def draw_face_frame_options(self,layout):
        top_rail_width = self.product.get_prompt("Top Rail Width")
        bottom_rail_width = self.product.get_prompt("Bottom Rail Width")
        left_stile_width = self.product.get_prompt("Left Stile Width")
        right_stile_width = self.product.get_prompt("Right Stile Width")
         
        if top_rail_width:
            box = layout.box()
            box.label("Face Frame Options:")
            row = box.row()
            row.prop(top_rail_width,"DistanceValue",text="Top Rail Width") 
            row.prop(bottom_rail_width,"DistanceValue",text="Bottom Rail Width") 
            row = box.row()
            row.prop(left_stile_width,"DistanceValue",text="Left Stile Width") 
            row.prop(right_stile_width,"DistanceValue",text="Right Stile Width") 
             
    def draw_interior_prompts(self,layout):
        for insert in self.inserts:
            if "Interior Options" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                col.label("Interior Options:")
                carcass = fd_types.Assembly(insert)
                adj_shelf_qty = carcass.get_prompt("Adj Shelf Qty")
                fix_shelf_qty = carcass.get_prompt("Fixed Shelf Qty")
                div_qty_per_row = carcass.get_prompt("Divider Qty Per Row")
                division_qty = carcass.get_prompt("Division Qty")
                adj_shelf_rows = carcass.get_prompt("Adj Shelf Rows")
                fixed_shelf_rows = carcass.get_prompt("Fixed Shelf Rows")
                 
                if adj_shelf_qty:
                    row = col.row()
                    row.label("Adjustable Shelf Qty")
                    row.prop(adj_shelf_qty,'QuantityValue',text="")
         
                    row.label("Fixed Shelf Qty")
                    row.prop(fix_shelf_qty,'QuantityValue',text="")
                     
                if div_qty_per_row:
                    row = col.row()
                    row.label("Divider Qty Per Row")
                    row.prop(div_qty_per_row,'QuantityValue',text="")
                 
                if division_qty:
                    row = col.row()
                    row.label("Division Qty")
                    row.prop(division_qty,'QuantityValue',text="")
                 
                if adj_shelf_rows:
                    row = col.row()
                    row.label("Adjustable Shelf Rows")
                    row.prop(adj_shelf_rows,'QuantityValue',text="")
                     
                    row.label("Fixed Shelf Rows")
                    row.prop(fixed_shelf_rows,'QuantityValue',text="")
         
    def draw_splitter_prompts(self,layout):
        for insert in self.inserts:
            if "Opening Heights" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                col.label("Splitter Options:")
                splitter = fd_types.Assembly(insert)
                opening_1 = splitter.get_prompt("Opening 1 Height")
                opening_2 = splitter.get_prompt("Opening 2 Height")
                opening_3 = splitter.get_prompt("Opening 3 Height")
                opening_4 = splitter.get_prompt("Opening 4 Height")
                 
                if opening_1:
                    row = col.row()
                    row.label("Opening 1 Height:")
                    if opening_1.equal:
                        row.label(str(unit.meter_to_active_unit(opening_1.DistanceValue)))
                        row.prop(opening_1,'equal',text="")
                    else:
                        row.prop(opening_1,'DistanceValue',text="")
                        row.prop(opening_1,'equal',text="")
                if opening_2:
                    row = col.row()
                    row.label("Opening 2 Height:")
                    if opening_2.equal:
                        row.label(str(unit.meter_to_active_unit(opening_2.DistanceValue)))
                        row.prop(opening_2,'equal',text="")
                    else:
                        row.prop(opening_2,'DistanceValue',text="")
                        row.prop(opening_2,'equal',text="")
                if opening_3:
                    row = col.row()
                    row.label("Opening 3 Height:")
                    if opening_3.equal:
                        row.label(str(unit.meter_to_active_unit(opening_3.DistanceValue)))
                        row.prop(opening_3,'equal',text="")
                    else:
                        row.prop(opening_3,'DistanceValue',text="")
                        row.prop(opening_3,'equal',text="")
                if opening_4:
                    row = col.row()
                    row.label("Opening 4 Height:")
                    if opening_4.equal:
                        row.label(str(unit.meter_to_active_unit(opening_4.DistanceValue)))
                        row.prop(opening_4,'equal',text="")
                    else:
                        row.prop(opening_4,'DistanceValue',text="")
                        row.prop(opening_4,'equal',text="")
         
    def draw_product_placment(self,layout):
        box = layout.box()
        row = box.row()
        row.label('Location:')
        row.prop(self.product.obj_bp,'location',text="")
        row.label('Rotation:')
        row.prop(self.product.obj_bp,'rotation_euler',index=2,text="")
         
    def draw(self, context):
        layout = self.layout
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                box = layout.box()
                  
                split = box.split(percentage=.8)
                split.label(self.product.obj_bp.mv.name_object + " | " + self.product.obj_bp.cabinetlib.spec_group_name,icon='LATTICE_DATA')
                split.menu('MENU_Current_Cabinet_Menu',text="Menu",icon='DOWNARROW_HLT')
                
                self.draw_product_size(box)
                
                prompt_box = box.box()
                row = prompt_box.row(align=True)
                row.prop_enum(self, "product_tabs", 'CARCASS') 
                if self.show_exterior_options:
                    row.prop_enum(self, "product_tabs", 'EXTERIOR') 
                if self.show_interior_options:
                    row.prop_enum(self, "product_tabs", 'INTERIOR') 
                if self.show_splitter_options:
                    row.prop_enum(self, "product_tabs", 'SPLITTER') 
                row.prop_enum(self, "product_tabs", 'FACEFRAME') 
                if self.product_tabs == 'CARCASS':
                    self.draw_carcass_prompts(prompt_box)
                if self.product_tabs == 'FACEFRAME':
                    self.draw_face_frame_options(prompt_box)
                if self.product_tabs == 'EXTERIOR':
                    self.draw_door_prompts(prompt_box)
                    self.draw_drawer_prompts(prompt_box)
                if self.product_tabs == 'INTERIOR':
                    self.draw_interior_prompts(prompt_box)
                if self.product_tabs == 'SPLITTER':
                    self.draw_splitter_prompts(prompt_box)      

bpy.utils.register_class(PANEL_Basic_Cabinet_Options)
bpy.utils.register_class(PROMPTS_Door_Prompts)
bpy.utils.register_class(PROMPTS_Drawer_Prompts)
bpy.utils.register_class(PROMPTS_Hamper_Prompts)
bpy.utils.register_class(PROMPTS_Hanging_Rod_Prompts)
bpy.utils.register_class(PROMPTS_Shelf_Prompts)
bpy.utils.register_class(PROMPTS_Wire_Baskets)
bpy.utils.register_class(PROMPTS_Shoe_Cubbies)
bpy.utils.register_class(PROMPTS_Splitter_Prompts)
bpy.utils.register_class(PROMPTS_Column_Prompts)
bpy.utils.register_class(PROMPTS_Angled_Column_Prompts)
bpy.utils.register_class(PROMPTS_Frameless_Cabinet_Prompts)
bpy.utils.register_class(PROMPTS_Face_Frame_Cabinet_Prompts)
    