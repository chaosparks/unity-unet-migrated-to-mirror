# unity-unet-migrated-to-mirror
complete python code to help unity unet migrate to mirror: replace the old UNet object reference with Mirror ones

## How to use the python code
1. open `python/fix_UNet.py`,
2. fix `unet_ref_file` with **UNet_ref.txt** file full path on your computer
3. fix `asset_folder` with your real unity project asset folder
4. run `python fix_UNet.py` under command line

## create_UNet_ref.py
You will not run this file unless you find some UNet objects ref which list here are not completely cover yours. The following are UNet object guid refs found which exist in **UNet_ref.txt**:

- UnityEngine.Networking.NetworkManager
- UnityEngine.Networking.NetworkIdentity
- UnityEngine.Networking.NetworkLobbyManager
- UnityEngine.Networking.NetworkMigrationManager
- UnityEngine.Networking.NetworkStartPosition
- UnityEngine.Networking.NetworkDiscovery
- UnityEngine.Networking.NetworkAnimator
- UnityEngine.Networking.NetworkProximityChecker
- UnityEngine.Networking.NetworkLobbyPlayer
- UnityEngine.Networking.NetworkManagerHUD
- UnityEngine.Networking.NetworkTransformChild
- UnityEngine.Networking.NetworkTransform
- UnityEngine.Networking.NetworkBehaviour
- UnityEngine.Networking.NetworkTransformVisualizer

If you find those are not enough, you can add the missing ones into the unity scene, then run **create_UNet_ref.py** to get the whole list

## [Full Course for Unity UNet migrated to Mirror](https://www.chaosparks.com/tech/unity/unity-unet-migrated-to-mirror/)

This repo contains the complete source code or scripts used to migrate UNet to Mirror, to view other issued involved, you can check [My blog](https://www.chaosparks.com/tech/unity/unity-unet-migrated-to-mirror/).

In the blog, more details are covered, such as csharp code migrated and so on! And the whole precess works in real project, you can reference it.

Thanks a lots!
  
