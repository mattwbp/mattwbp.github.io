import json
import sys
import os

json_output = os.path.join(os.path.dirname(__file__), 'breakdown_2020_002_data.json') 
from pprint import pprint


shot_breakdowns = {
    '01_omens_eden':{
        'image': 'img/cropped/half/omens_eden.jpg',
        'project': 'Good Omens',
        'shot_name': 'Garden of Eden',
        'year': '2018',
        'studio': 'Milk VFX',
        'location': 'London, UK',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Several elements of DMP rendered projected onto geometry',
            'Rain Stock elements'
            ],
        'description': 'Overall grading of several DMP elements to suit direction, heavy tweaking of background dmp elements and adding details. \
            Layers of Rain Stock camera pulls backwards through and a Comp flock of doves.'
        
    },

    '02_omens_hellhound':{
        'image': 'img/cropped/half/omens_hellhound.jpg',
        'project': 'Good Omens',
        'shot_name': 'Hell Hound',
        'year': '2018',
        'studio': 'Milk VFX',
        'location': 'London, UK',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Plate of dog walking with bluescreen background', 
            'Plate of moving forest background at HellHound Height', 
            'Roto of Dogs body',
            'Prep/Paint of Plate Dog Head Removal & Jowl/Lip cleanup over dogs neck', 
            'Lighting Render of HellHound head & FX Saliva'
            ],
        'description': 'Composited all elements. Added the CG Head to the Dogs body and matching musculature movement on the neck using animated STMaps based off trackers + vertices on the Geo. \
        Grading the CG to match the original dog plate, with some artistic license. Distorted the dogs body to suggest different size and to match better into moving background plate. \
            I was the sole compositor on all (7) of the Hell Hound head replacement shots.'
        
    },

    '03_pokemon_crowd':{
        'image': 'img/cropped/half/pokemon_crowd.jpg',
        'project': 'Pokemon : Detective Pikachu',
        'shot_name': 'The Crowd cheers',
        'year': '2019',
        'studio': 'Framestore',
        'location': 'London, UK',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Plate', 
            'Lighting Renders of Pokemon Characters (10 Pokemon) seperated into passes + Fences (deep)', 
            'Roto of Set',

            ],
        'description': 'Composited all elements. Several layers of (10)Pokemon characters.'
        
    },

       '04_pokemon_pikachu':{
        'image': 'img/cropped/half/pokemon_pikachu.jpg',
        'project': 'Pokemon : Detective Pikachu',
        'shot_name': 'Pikachu leaps up',
        'year': '2019',
        'studio': 'Framestore',
        'location': 'London, UK',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Plate', 
            'Lighting Renders of Pokemon Characters (Pikachu, Gengar, Blastoise) + Fences (deep)', 
            'Roto Characters and FG',

            ],
        'description': 'Composited all elements. several layers of Pokemon characters and dealing with Plate elements (FG, Characters and Light beams or edges changing due to light behind them) that behave differently now there is a character \
            between the light source and them. This includes Animated Grades etc to sit the characters into the environment which has constantly changing light'
        
    },

    '05_pokemon_charizard':{
        'image': 'img/cropped/half/pokemon_charizard.jpg',
        'project': 'Pokemon : Detective Pikachu',
        'shot_name': 'They ruined my jacket!',
        'year': '2019',
        'studio': 'Framestore',
        'location': 'London, UK',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Plate', 
            'Lighting Renders of Pokemon Characters (Charizard) seperated into passes + Fences (deep)', 
            'Roto for Characters',
            ],
        'description': 'Composited all elements. Similar to previous shot in terms of animated grades to help character integration, but this time the edges being babysit through light changes are fine detail hair and clothing.\
             For example, there is a light source behind the focus character which has been removed. Loads of edge work.',
        
    },

    '06_pokemon_growlithe':{
        'image': 'img/cropped/half/pokemon_growlithe.jpg',
        'project': 'Pokemon : Detective Pikachu',
        'shot_name': '-_-',
        'year': '2019',
        'studio': 'Framestore',
        'location': 'London, UK',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Plate', 
            'Lighting Renders of Pokemon Characters (Charizard, Pikachu, Growlithe) seperated into passes (deep)', 
            'Roto for Characters'

            ],
        'description': 'Composited all elements. Similar to previous shot in terms of animated grades to help character integration, but this time the edges being babysit through light changes are fine detail hair and clothing.\
             For example, there is a light source behind the focus character which has been removed. Loads of edge work.',
        
    },

    '07_tomjerry_keyboard':{
        'image': 'img/cropped/half/tomjerry_keyboard.jpg',
        'project': 'Tom and Jerry',
        'shot_name': 'Tom is down and out',
        'year': '2020',
        'studio': 'Framestore',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Plate',
            'Lighting Renders of Props & Characters',
            'Lighting Renders for Toon Lines',
            'Motion Graphic Elements for bonks and slaps',
            'FX for rain drips on characters & splashes on ground'
            ],
        'description': 'Composited all elements. Comp Lightning flash and careful attention to reflection in puddles and the wet look caused by rainfall.'
    },

    '08_tomjerry_champagne':{
        'image': 'img/cropped/half/tomjerry_champagne.jpg',
        'project': 'Tom and Jerry',
        'shot_name': 'Jerry gets a bubble bath',
        'year': '2020',
        'studio': 'Framestore',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Plate',
            'Lighting Renders of Props & Characters',
            'Lighting Renders for Toon Lines',
            'Motion Graphic Elements for bonks and slaps',
            ],
        'description': 'Composited all elements. Slight conundrum as a cartoon character is inside a real (stylistically) but cg object, so motion blur tweaked to help its integration. Loads of toonline artefacting fixes.',
    },
    
    '09_tomjerry_window':{
        'image': 'img/cropped/half/tomjerry_window.jpg',
        'project': 'Tom and Jerry',
        'shot_name': 'Out the window',
        'year': '2020',
        'studio': 'Framestore',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Plate',
            'Lighting Renders of Props & Characters',
            'Lighting Renders of exterior wall & Window',
            'Lighting Renders for Toon Lines',
            'Motion Graphic Elements for bonks and slaps',
            ],
        'description': 'Composited all elements. Load of shadow and reflection tweaking with the set and window distortion/reflections.',
    },

    '10_gijoe_satellite':{
        'image': 'img/cropped/half/gijoe_satellite.jpg',
        'project': 'GI Joe : Retaliation',
        'shot_name': 'The Zeus satellite',
        'year': '2012',
        'studio': 'Digital Domain/Reliance',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'DMP Earth reprojected onto 3D Sphere',
            'DMP Star Background',
            'Lighting passes of satellites'
            ],
        'description': 'Composited all elements. Assembling and Grading Lighting passes of the satellites + tweak grades using cryptomattes. Integration of Earth and Comp driven atmosphere into starfield, which required some tweaking to reduce twinkling of \
            pixel sized stars',
        
    },

    '11_gijoe_cobrachopper':{
        'image': 'img/cropped/half/gijoe_chopper.jpg',
        'project': 'GI Joe : Retaliation',
        'shot_name': 'Cobra Attack Helicoptor',
        'year': '2012',
        'studio': 'Digital Domain/Reliance',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Plate',
            'Lighting Render of Attack Helicoptor',
            'FX for engine haze & Water vapor kickup'
            ],
        'description': 'Composited all elements. Removal of Plate helicoptor, integration of CG Attack Helicoptor and then bringing the Plate guy on the side of the helicoptor back onto the CG Helicoptor. \
            Also details like water kickup fx + haze caused by the jet engines.',
        
    },

    '12_hercules_crowd':{
        'image': 'img/cropped/half/hercules_crowd.jpg',
        'project': 'Hercules',
        'shot_name': 'Battle standoff',
        'year': '2014',
        'studio': 'Prime Focus World',
        'role': 'Nuke Compositor',
        'supplied elements': [
            '4 Plates of Soldiers in different positions of the shield wall',
            'Roto Soldiers for each plate',
            'CG Environment',
            'Lighting Renders for Barbarian Crowd',
            'FX Passes for Smoke plumes'
            ],
        'description': 'Composited all elements. Several plates of soldiers used to crowd-dupe into a single shield formation, which is then comped into a CG environment. \
            A fair bit of culling problematic/intersecting crowd cg warriors and seating in the smoke plumes.',
        
    },

    '13_hercules_crowd_cg':{
        'image': 'img/cropped/half/hercules_crowd_cg.jpg',
        'project': 'Hercules',
        'shot_name': 'Battle standoff aerial view',
        'year': '2014',
        'studio': 'Prime Focus World',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Lighting Renders for CG Characters & Crowd',
            'Lighting Renders of CG Environment',
            'FX Smoke'
            ],
        'description': 'Composited all elements. A fully CG shot to match into the sequence and previous shot',
        
    },

    '14_kingsmen_westminster':{
        'image': 'img/cropped/half/kingsmen_westminster.jpg',
        'project': 'Kingsmen : Secret Service',
        'shot_name': 'chaos in London',
        'year': '2014',
        'studio': 'Prime Focus World',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Plate',
            'Prep crowd and vehicle removal',
            'Lighting Renders for crowds and vehicles',
            'Roto for Some FG Elements'
            ],
        'description': 'Composited all elements. CG Crowd + Vehicles into a prepped plate. Careful management of shadows and edges in detailed areas and a little bit of tracking fixing here and there',
        
    },

    '15_hisdarkmaterials_airship':{
        'image': 'img/cropped/half/hisdarkmaterials_airship.jpg',
        'project': 'His Dark Materials Season 2',
        'shot_name': 'Lee and Hester on the airship',
        'year': '2020',
        'studio': 'Framestore',
        'role': 'Nuke Compositor',
        'supplied elements': [
            'Plate',
            'Lighting Renders for CG Character (Hester)',
            'DMP for Sky BG',
            ],
        'description': 'Composited all elements. Plate keying and integration of CG Character',
        
    },

}

# pprint(shot_breakdowns)

with open(json_output, 'w') as fp:
    json.dump(shot_breakdowns, fp, indent=4)