# This script can be used to check your active directory users and send a password expiry notification to users whose passwords would expire in the next 10 days.
#edit domain and mailserver values
import-module ActiveDirectory

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Install-PackageProvider -Name NuGet -RequiredVersion 2.8.5.201 -Force
Install-Module -Name PSSlack

$Channel = "enter #slack-channel here"
$SlackUri = "enter slack webhook here"


$all_admin_users =  Get-ADUser -filter {  Enabled -eq $True -and PasswordNeverExpires -eq $False } -Properties "SamAccountName","GivenName","EmailAddress","pwdLastSet","msDS-UserPasswordExpiryTimeComputed" | Select-Object -Property "SamAccountName","GivenName","EmailAddress",@{Name="Last_Password_Change";Expression={[datetime]::FromFileTime($_."pwdLastSet")}},@{Name="Next_Password_Change";Expression={[datetime]::FromFileTime($_."msDS-UserPasswordExpiryTimeComputed")}}


$today = Get-Date

foreach ($item in $all_admin_users){
    
    if(!$($item.Next_Password_Change)){
        continue;
    }
    # If the password expiration date is after today and less than 10 days 
    if(((New-TimeSpan -Start $today -End $($item.Next_Password_Change)).Days -gt 0) -and ((New-TimeSpan -Start $today -End $($item.Next_Password_Change)).Days -le 10)){
        # $val is the number of days left before password expires
        $val =  (New-TimeSpan -Start $today -End $($item.Next_Password_Change)).Days
        
        #write-host("Username: $($item.SamAccountName),$($item.GivenName), LastPass Change: $($item.Last_Password_Change), NextPass Change: $($item.Next_Password_Change), Diff: $val, $($item.EmailAddress)")
        if($($item.EmailAddress)){
            # send email if an email address is found for the account in AD
            Send-MailMessage -SmtpServer mailserver.yourcompany.com -From "admin@yourcompany.com" -To $($item.EmailAddress) -Subject "Your account AD\$($item.SamAccountName) expires in $val days" -Body "Hello, `nYour domain account $($item.SamAccountName) expires in $val days.`nPlease reset your password to avoid getting locked out. `n`nThank you,`nYou Admin"
            # for logging
            write-host "Email was sent to $($item.EmailAddress) for account $($item.SamAccountName) with Diff value $val"
        }
        else{

            # if email address is not found, it is likely that this is a service account so send a slack message

            Send-SlackMessage -Text "The AD service account $($item.SamAccountName) expires in $val days. Please reset the password immediately" -Channel $Channel -Uri $SlackUri
            # for logging
            write-host "Slack message was posted for $($item.SamAccountName) with Diff $val"
        
        }

    }
}