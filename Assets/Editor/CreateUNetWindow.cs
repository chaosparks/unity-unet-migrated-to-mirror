using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using UnityEngine.Networking;

public class CreateUNetWindow : EditorWindow
{
        // Add menu named "My Window" to the Window menu
    [MenuItem("Window/CreateUNet Window")]
    static void Init()
    {
        // Get existing open window or if none, make a new one:
        CreateUNetWindow window = (CreateUNetWindow)EditorWindow.GetWindow(typeof(CreateUNetWindow));
        window.Show();
    }

    void OnGUI()
    {
        if ( GUILayout.Button("Create UNet Object") ) {
            new GameObject("NetworkManager").AddComponent<NetworkManager>();
            new GameObject("NetworkIdentity").AddComponent<NetworkIdentity>();
            new GameObject("NetworkLobbyManager").AddComponent<NetworkLobbyManager>();
            new GameObject("NetworkMigrationManager").AddComponent<NetworkMigrationManager>();
            new GameObject("NetworkStartPosition").AddComponent<NetworkStartPosition>();
            new GameObject("NetworkDiscovery").AddComponent<NetworkDiscovery>();
            new GameObject("NetworkProximityChecker").AddComponent<NetworkProximityChecker>();
            new GameObject("NetworkLobbyPlayer").AddComponent<NetworkLobbyPlayer>();
            new GameObject("NetworkManagerHUD").AddComponent<NetworkManagerHUD>();
            new GameObject("NetworkTransformChild").AddComponent<NetworkTransformChild>();
            new GameObject("NetworkTransform").AddComponent<NetworkTransform>();
            new GameObject("NetworkBehaviour").AddComponent<NetworkBehaviour>();
            new GameObject("NetworkTransformVisualizer").AddComponent<NetworkTransformVisualizer>();
        }
    }
}
