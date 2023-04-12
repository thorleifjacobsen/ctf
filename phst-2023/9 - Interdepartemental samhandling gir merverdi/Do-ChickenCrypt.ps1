
function Do-ChickenCrypt {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        $Data,
        [int]$times = 9000,
        [byte]$key,
        [switch]$Base64 = $false,
        [switch]$Returnbytes = $False,
        [switch]$InputisBytes = $False
        )

    if (!$InputisBytes) {
        $enc = [System.Text.Encoding]::UTF8
        $String = $Data
        $bytes = $enc.GetBytes($String)
        }

        else {
        $bytes = $Data
        }
    
    #2001: Svakhet i algoritme, monochicken. Oppgraderer til duoChicken for ekstra trygghet
    #2014: Sjefen sier det fortsatt er svakt. Oppgradert til quadrochicken
    #2019: Oppgradert til valgfri antall chickens etter klage fra internsikkerhet. 

$banner = @"
    ______   __        __            __                             ______                                  __     
    /      \ |  \      |  \          |  \                           /      \                                |  \                              
|  ££££££\| ££____   \££  _______ | ££   __   ______   _______  |  ££££££\  ______   __    __   ______  _| ££_                          //  
| ££   \££| ££    \ |  \ /       \| ££  /  \ /      \ |       \ | ££   \££ /      \ |  \  |  \ /      \|   ££ \      ww_          ___.///  
| ££      | £££££££\| ££|  £££££££| ££_/  ££|  ££££££\| £££££££\| ££      |  ££££££\| ££  | ££|  ££££££\\££££££    /o__ '._.-'''''    //  
| ££   __ | ££  | ££| ££| ££      | ££   ££ | ££    ££| ££  | ££| ££   __ | ££   \££| ££  | ££| ££  | ££ | ££ __   |/  \   ,     /   //   
| ££__/  \| ££  | ££| ££| ££_____ | ££££££\ | ££££££££| ££  | ££| ££__/  \| ££      | ££__/ ££| ££__/ ££ | ££|  \  /     \  '',,,' _//     
    \££    ££| ££  | ££| ££ \££     \| ££  \££\ \££     \| ££  | ££ \££    ££| ££       \££    ££| ££    ££  \££  ££         '-.  \--'   .''. 
    \££££££  \££   \££ \££  \£££££££ \££   \££  \£££££££ \££   \££  \££££££  \££       _\£££££££| £££££££    \££££              \_/_/   '.,' 
                                                                                    |  \__| ££| ££                              \\\\     
                                                                                        \££    ££| ££                             ,,',''   
                                                                                        \££££££  \££               
"@
$Banner_2 = """. --. --.{----- ..--.- -.-. .-.. ..- -.-. -.- ... ..--.- --. .. ...- . -.}"""

    Write-Host $banner

    function Print-Disclaimer {
        Write-host "Proprietær kode, RFC8140, 7.1 Compliant" -ForegroundColor Blue 
        Write-Host "Easter chicken encryption software inc. ltd. AS. Com"
        Write-host "All rights reversed" 
        }

    $EncryptionCounter = 0
    while ($EncryptionCounter -lt $times) {
    
        for($i=0; $i -lt $bytes.count ; $i++)
        {
            $bytes[$i] = $bytes[$i] -bxor $key
        }
        write-host "Cluck" -ForegroundColor Yellow
        $EncryptionCounter += 1

        }

    if (!$Returnbytes) {
        $enc = [System.Text.Encoding]::UTF8
        $Result = $enc.GetString($bytes)
        }
    else {
        $Result = $bytes
        }

    return $Result
    
}
