
import os
import Helper.FileUtil
import Helper.UnityScene


file = "path to unet sence with unset gameobject only"
lines = Helper.FileUtil.read_lines_from_file(file)
parser = Helper.UnityScene.UnitySceneParser()
parser.parse_unity_scene(lines)
parser.get_MonoBehaviour_Info()