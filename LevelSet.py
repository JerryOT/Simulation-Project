import LevelClass
import Classes
import Slingshot
import Enums

Levels = {
    1 : {
        # required n amount of velocity in order to start taking damage
        'velocity_damage_minimum' : 3,

        # percentage of damage being scaled when bird taking damage
        # damage = velocity * velocity_damage_bird_reduce
        'velocity_damage_bird_reduce' : 0.8,

        'Slingshot' : {
            'Position': {'X': 100, 'Y': 250, },
        },
        'Pig_Set' : {
            0: {'Pig_Type' : Enums.Pig['Small'],
                'Position' : {'X' : 500,'Y' : 180,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
            },
            8: {'Pig_Type' : Enums.Pig['Small'],
                'Position' : {'X' : 480+640,'Y' : 530,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
            },
            7: {'Pig_Type' : Enums.Pig['Small'],
                'Position': {'X': 0+640, 'Y': 530, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                },
            1: {'Pig_Type' : Enums.Pig['Big'],
                'Position': {'X': 160+640, 'Y': 190, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                },
            2: {'Pig_Type' : Enums.Pig['Big'],
                'Position': {'X': 240+640, 'Y': 190, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                },
            3: {'Pig_Type' : Enums.Pig['Big'],
                'Position': {'X': 320+640, 'Y': 190, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                },
            4: {'Pig_Type' : Enums.Pig['Small'],
                'Position': {'X': 200+640, 'Y': 270, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                },
            5: {'Pig_Type' : Enums.Pig['Small'],
                'Position': {'X': 280+640, 'Y': 270, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                },
            6: {'Pig_Type' : Enums.Pig['Small'],
                'Position': {'X': 240+640, 'Y': 360, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                },
        },
        'Bird_Set' : {
            1 : {
                'Bird_Type' : Enums.Bird['Red'],
                'Position': {'X': 20, 'Y': 200, },
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
            },
        },
        'Building_Box_Set' : {
            1 : {
                'Material' : Enums.Material['Glass'],
                'Size' : {'Width' : 10,'Height' : 80,},
                'Position' : {'X' : 200+640,'Y' : 200,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            2 : {
                'Material' : Enums.Material['Glass'],
                'Size' : {'Width' : 10,'Height' : 80,},
                'Position' : {'X' : 120+640,'Y' : 200,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            3 : {
                'Material' : Enums.Material['Glass'],
                'Size' : {'Width' : 10,'Height' : 80,},
                'Position' : {'X' : 280+640,'Y' : 200,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            4 : {
                'Material' : Enums.Material['Glass'],
                'Size' : {'Width' : 10,'Height' : 80,},
                'Position' : {'X' : 360+640,'Y' : 200,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            5 : {
                'Material' : Enums.Material['Glass'],
                'Size' : {'Width' : 80,'Height' : 10,},
                'Position' : {'X' : 240+640,'Y' : 245,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            6 : {
                'Material' : Enums.Material['Glass'],
                'Size' : {'Width' : 80,'Height' : 10,},
                'Position' : {'X' : 160+640,'Y' : 245,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            7 : {
                'Material' : Enums.Material['Glass'],
                'Size' : {'Width' : 80,'Height' : 10,},
                'Position' : {'X' : 320+640,'Y' : 245,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            8 : {
                'Material' : Enums.Material['Wood'],
                'Size' : {'Width' : 10,'Height' : 80,},
                'Position' : {'X' : 160+640,'Y' : 290,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            9 : {
                'Material' : Enums.Material['Wood'],
                'Size' : {'Width' : 10,'Height' : 80,},
                'Position' : {'X' : 240+640,'Y' : 290,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            10 : {
                'Material' : Enums.Material['Wood'],
                'Size' : {'Width' : 10,'Height' : 80,},
                'Position' : {'X' : 320+640,'Y' : 290,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            11 : {
                'Material' : Enums.Material['Wood'],
                'Size' : {'Width' : 80,'Height' : 10,},
                'Position' : {'X' : 200+640,'Y' : 335,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            12 : {
                'Material' : Enums.Material['Wood'],
                'Size' : {'Width' : 80,'Height' : 10,},
                'Position' : {'X' : 280+640,'Y' : 335,},
                'Velocity' : {'X' : 0,'Y' : 0,},
                'Rotation' : 0,
                'Anchored' : False,},
            13: {
                'Material': Enums.Material['Stone'],
                'Size': {'Width': 10, 'Height': 80, },
                'Position': {'X': 200+640, 'Y': 380, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                'Anchored' : False,},
            14: {
                'Material': Enums.Material['Stone'],
                'Size': {'Width': 10, 'Height': 80, },
                'Position': {'X': 280+640, 'Y': 380, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                'Anchored' : False,},
            16: {
                'Material': Enums.Material['Earth'],
                'Size': {'Width': 1280, 'Height': 160, },
                'Position': {'X': 0+640, 'Y': 80, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                'Anchored' : True,},
            17: {
                'Material': Enums.Material['Earth'],
                'Size': {'Width': 100, 'Height': 20, },
                'Position': {'X': 0+640, 'Y': 500, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                'Anchored' : True,},
            18: {
                'Material': Enums.Material['Earth'],
                'Size': {'Width': 100, 'Height': 20, },
                'Position': {'X': 480+640, 'Y': 500, },
                'Velocity': {'X': 0, 'Y': 0, },
                'Rotation': 0,
                'Anchored' : True,},
            },
        'Building_Circle_Set' : {
            1 : {
                'Material' : Enums.Material['Stone'],
                'Size' : {'Radius' : 20,},
                'Position' : {'X' : 500,'Y' : 200,},
                'Velocity' : {'X' : 20,'Y' : 15,},
                'Rotation' : 0,
                'Anchored' : False,
            },
        },
    },
}


def Get_Level(level_index):
    level_data = Levels[level_index]
    slingshot = Slingshot.Slingshot(level_data['Slingshot']['Position']['X'], level_data['Slingshot']['Position']['Y'])
    level_obj = LevelClass.Level(slingshot)

    for _, data in level_data['Building_Box_Set'].items():
        obj = Classes.Building__Box(data['Material'], data['Size']['Width'], data['Size']['Height'])
        obj.physics_state.Set_Position(data['Position']['X'], data['Position']['Y'])
        obj.physics_state.Set_Velocity(data['Velocity']['X'], data['Velocity']['Y'])
        obj.physics_state.Set_Rotation(data['Rotation'])
        obj.physics_state.Set_Anchor(data['Anchored'])
        level_obj.Add_Object( obj )

    for _, data in level_data['Pig_Set'].items():
        obj = Classes.Pig(data['Pig_Type'], data['Pig_Type']['Value']['Radius'])
        obj.physics_state.Set_Position(data['Position']['X'], data['Position']['Y'])
        obj.physics_state.Set_Velocity(data['Velocity']['X'], data['Velocity']['Y'])
        obj.physics_state.Set_Rotation(data['Rotation'])
        level_obj.Add_Object( obj )

    for _, data in level_data['Bird_Set'].items():
        obj = Classes.Bird(data['Bird_Type'], data['Bird_Type']['Value']['Radius'])
        obj.physics_state.Set_Position(data['Position']['X'], data['Position']['Y'])
        obj.physics_state.Set_Velocity(data['Velocity']['X'], data['Velocity']['Y'])
        obj.physics_state.Set_Rotation(data['Rotation'])
        level_obj.Add_Object( obj )
    
    #
    # for _, data in level_data['Building_Circle_Set'].items():
    #     obj = Classes.Building__Circle(data['Material'], data['Size']['Radius'])
    #     obj.physics_state.Set_Position(data['Position']['X'], data['Position']['Y'])
    #     obj.physics_state.Set_Velocity(data['Velocity']['X'], data['Velocity']['Y'])
    #     obj.physics_state.Set_Rotation(data['Rotation'])
    #     obj.physics_state.Set_Anchor(data['Anchored'])
    #     print(obj.object_type, obj.health)
    #     level_obj.Add_Object( obj )

    level_obj.velocity_damage_minimum = level_data['velocity_damage_minimum']
    level_obj.velocity_damage_bird_reduce = level_data['velocity_damage_bird_reduce']

    return level_obj