using UnityEngine;

public class Status : MonoBehaviour
{
    [Header("Walk, Run speed")]
    [SerializeField]
    private float    walkSpeed;
    [SerializeField]
    private float    runSpeed;

    public  float    WalkSpeed => walkSpeed;
    public  float    RunSpeed  => runSpeed;
}
