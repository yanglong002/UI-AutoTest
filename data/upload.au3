$CmdLine[0]
$CmdLine[1]

ControlFocus("打开","","Edit1")
ControlSetText("打开","","Edit1",$CmdLine[1])
Sleep(2000)
ControlClick("打开","","Button1")