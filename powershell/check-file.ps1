# This script is used to find out files which have a pattern 112332-123344.txt and send out a slack message as part of monitoring
# PS drive is used to connect to remote windows systems

Install-PackageProvider -Name NuGet -RequiredVersion 2.8.5.201 -Force
Install-Module -Name PSSlack

#$webhook = provide slack webhook API key here
#$Cred = Supply admin credentials here

#$serverlist = "enter list of servers comma seperated"

# $file_location = "enter the target location"



Write-Host "Starting Scan..." -ForegroundColor Yellow

$found_files = @()

foreach($svn in $serverlist){
$batchfiles_found = $null

    try{
        
        New-PSDrive -Name bic -PSProvider FileSystem -Root \\$svn\c$ -Credential $Cred | Out-Null -ErrorAction Stop

    }catch{

    $error = "Could not read from $svn"

    $error | Out-File -FilePath -Append "connect-error.txt"
    continue;
    }

    $batchfiles_found = Get-ChildItem "bic:\$file_location" | Where-Object { $_.Name -match '^\d*-\d*\.txt\.?\w?\w?\w?$'-and $_.CreationTime -lt (date).addminutes(-5) } | Select-Object FullName

    if($batchfiles_found){
    Write-Host "$svn"
    Write-Host "$batchfiles_found"
    #$Message = @{ServerName=$svn;BatchFiles=$batchfiles_found;Status="Stuck Batch"}

        #foreach($batchitem in $batchfiles_found){

        #    if($batchitem -notin $found_files){
        
            
            $Message = "ServerName: $svn`nBatchFiles: $batchfiles_found`nStatus: something"
            Send-SlackMessage -Uri $webhook -Text $Message

    
    }

# for logging purposes
    foreach($item in $batchfiles_found){
    $timestamp = Get-Date -UFormat "%A %m/%d/%Y %R"
    $line = "$timestamp - $svn - $item"
    $line | Out-File -Append stuckfiles.txt

    }

    Remove-PSDrive -Name bic

}


Write-Host "Scan Complete..." -ForegroundColor Yellow