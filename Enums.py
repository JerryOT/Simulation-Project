import pygame, sys


Color = {
    'BLACK' : (0, 0, 0),
    'WHITE' : (255, 255, 255),
    'GREY' : (150, 150, 150),
    'RED' : (255, 0, 0),
    'GREEN' : (0, 255, 0),
    'DEEPGREEN' : (0, 150, 0),
    'BLUE' : (0, 0, 255),
    'BROWN' : (150, 75, 0)
}

ObjectType = {
    'Circle' : 'Circle',
    'Box' : 'Box',
    'Bird' : 'Bird',
    'Pig' : 'Pig',
}
CollisionType = {
    'Circle' : 'Circle',
    'Box' : 'Box',
}


Bird = {
    'Red' : {
        'Name' : 'Red',
        'Value' : {
            'Color' : Color['RED'],
            'Density' : 10,

            'Radius' : 20,
            'Health' : 80,
            'Max_Slingshot_Velocity' : 50,
        },
    },
}
Pig = {
    'Small' : {
        'Name' : 'Small',
        'Value' : {
            'Color' : Color['GREEN'],
            'Density' : 10,

            'Radius' : 15,
            'Health' : 15,
        },
    },

    'Big': {
        'Name': 'Big',
        'Value': {
            'Color': Color['GREEN'],
            'Density': 10,

            'Radius': 30,
            'Health': 25,
        },
    },
}


Material = {
    'Wood' : {
        'Name' : 'Wood',
        'Value' : {
            'Color' : Color['BROWN'],
            'Density' : 3,

            'Health_Density' : 0.5,
        },
    },
    'Stone' : {
        'Name' : 'Stone',
        'Value' : {
            'Color' : Color['GREY'],
            'Density' : 7,

            'Health_Density' : 2,
        },
    },
    'Glass': {
        'Name': 'Glass',
        'Value': {
            'Color': Color['WHITE'],
            'Density': 1,

            'Health_Density' : 0.01,
        },
    },
    'Earth': {
        'Name': 'Earth',
        'Value': {
            'Color': Color['DEEPGREEN'],
            'Density': 100,

            'Health_Density' : 9999,
        },
    },
}