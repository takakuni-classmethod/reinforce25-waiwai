function nonCompliant(){
    // Noncompliant: Does not ensures the request is being sent to the expected destination
    $file = file_get_contents($_POST['r']);
}

$username = $_COOKIE['username'];
// Noncompliant: Incorporating variable into command strings
exec("wto -n \"$username\" -g", $ret);


$fs = new Filesystem();
// Noncompliant: `0777` as it gives full read, write, and execute permissions to all users, which can be a security risk.
$fs->chmod("foo", 0777);


// Noncompliant: Used insecure FTP functions that transmit credentials in plain text, such as ftp_login.
$login_result = ftp_login($conn_id, $ftp_user_name, $ftp_user_pass);
