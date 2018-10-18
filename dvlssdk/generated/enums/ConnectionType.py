from enum import Enum


class ConnectionType(Enum):
    Undefined = 0
    RDPConfigured = 1
    RDPFilename = 2
    CommandLine = 3
    VNC = 4
    WebBrowser = 5
    LogMeIn = 6
    TeamViewer = 7
    Putty = 8
    Ftp = 9
    VirtualPC = 10
    Radmin = 11
    Dameware = 12
    VMWare = 13
    PCAnywhere = 14
    ICA = 15
    XWindow = 16
    HyperV = 17
    AddOn = 18
    RemoteAssistance = 19
    VPN = 20
    VirtualBox = 21
    VMRC = 22
    XenServer = 23
    WindowsVirtualPC = 24
    Group = 25
    Credential = 26
    HpRgs = 27
    Desktone = 28
    ApplicationTool = 29
    SessionTool = 30
    Contact = 31
    DataEntry = 32
    DataReport = 33
    Agent = 34
    Computer = 35
    DropBox = 36
    S3 = 37
    AzureStorage = 38
    CitrixWeb = 39
    PowerShell = 40
    HostSessionTool = 41
    Shortcut = 42
    IntelAMT = 43
    Azure = 44
    Document = 45
    VMWareConsole = 46
    InventoryReport = 47
    SkyDrive = 48
    ScreenConnect = 49
    AzureTableStorage = 50
    AzureQueueStorage = 51
    TemplateGroup = 52
    Host = 53
    Database = 54
    Customer = 55
    ADConsole = 56
    Aws = 57
    SNMPReport = 58
    Sync = 59
    Gateway = 60
    PlayList = 61
    TerminalConsole = 62
    PSExec = 63
    AppleRemoteDesktop = 64
    Spiceworks = 65
    DeskRoll = 66
    SecureCRT = 67
    Iterm = 68
    Sheet = 69
    Splunk = 70
    PortForward = 71
    TeamViewerConsole = 72
    ScreenHero = 73
    Telnet = 74
    Serial = 75
    SSHTunnel = 76
    SSHShell = 77
    ResetPassword = 78
    Wayk = 79
    ControlUp = 80
    DataSource = 81
    ChromeRemoteDesktop = 82
    RDCommander = 83
    IDrac = 84
    Ilo = 85
    WebDav = 86
    BeyondTrustPasswordSafeConsole = 87
    DevolutionsProxy = 88
    FtpNative = 89
    PowerShellRemoteConsole = 90
    ProxyTunnel = 91
    Root = 92
    BeyondTrustPasswordSafe = 93
    FileExplorer = 94
    Scp = 95
    Sftp = 96
    AzureBlobStorage = 97
    TFtp = 98
    GoToAssist = 99
    IPTable = 100
    Hub = 101
    GoogleDrive = 102
    GoogleCloud = 103
    NoVNC = 104
    Splashtop = 105
    JumpDesktop = 106
    BoxNet = 107
    MSPAnywhere = 108
    Repository = 109

    @staticmethod
    def value_from_name(typename):
        for name, member in ConnectionType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ConnectionType]
        return int_value in values
