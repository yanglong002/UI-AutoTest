$CmdLine[0]
$CmdLine[1]

ControlFocus("��","","Edit1")
ControlSetText("��","","Edit1",$CmdLine[1])
Sleep(2000)
ControlClick("��","","Button1")